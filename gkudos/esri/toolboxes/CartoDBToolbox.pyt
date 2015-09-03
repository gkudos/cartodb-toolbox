import arcpy
import os, tempfile
import gkudos

from gkudos.esri_scripts import create_zip
from gkudos.cartodb_utils import CartoDB

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "CartoDB"
        self.alias = "CartoDB"

        # List of tool classes associated with this toolbox
        self.tools = [CartoDBImportToolbox]


class CartoDBImportToolbox(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Upload data to CartoDB"
        self.description = "Upload data to CartoDB"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        # El parametro definido como respuesta siempre va en la primera posicion ("Estandar" Programacion SNC)
        results = arcpy.Parameter(
            displayName="Results",
            name="results",
            datatype="GPString",
            parameterType="Derived",
            direction="Output")
        
        param0 = arcpy.Parameter(
            displayName="Cartodb User Name",
            name="cdb_user_name",
            datatype="GPString",
            parameterType="Required",
            direction="Input")
			
        param1 = arcpy.Parameter(
            displayName="Api Key",
            name="cdb_key",
            datatype="GPString",
            parameterType="Required",
            direction="Input")
        
        param2 = arcpy.Parameter(
            displayName="Feature Class",
            name="feature_class",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input", 
			multiValue=True)
        
        params = [results, param0, param1, param2]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        cdb_user_name           = parameters[1].valueAsText.strip()
        cdb_key            		= parameters[2].valueAsText.strip()
        features           		= parameters[3].values
        
        temp_folder             = tempfile.mkdtemp()
        
        arcpy.SetProgressor("step", "Uploading data to CartoDB...",  0, len(features), 1)
        
        #messages.addMessage("cdb_user_name : " + cdb_user_name )
        #messages.addMessage("cdb_key : " + cdb_key )
        #messages.addMessage("temp_folder : " + temp_folder )
        new_tables = []
        feature_counter = 0
        for feature in features:
            desc = arcpy.Describe(feature)
            feature_name = None
            try:
                feature_name = desc.name
            except Exception as e:
                feature_name = "feature_"+str(feature_counter)
                        
            messages.addMessage("feature_name : " + feature_name )
            arcpy.SetProgressorLabel("Loading {0}...".format(feature_name))
            
            outputFolder = temp_folder+"\\"+feature_name
            os.makedirs(outputFolder)
            
            # Trim the '.shp' extension
            #fc = os.path.splitext(shp)[0]
            #feature_name = 
            # Update the progressor label for current shapefile
            
            arcpy.FeatureClassToShapefile_conversion([feature], outputFolder)
            
            output_file = temp_folder+"\\"+feature_name+".zip"
            create_zip(outputFolder, output_file )
            
            messages.addMessage("Zip File : " + output_file )
            
            options = {}
            options["f"] = output_file
            options["k"] = cdb_key
            options["u"] = cdb_user_name
            options["verbose"] = True
            
            
            cartodb = CartoDB(options)
            new_table = cartodb.upload()
            messages.addMessage("New Table : " + new_table )
            new_tables.append(new_table)
            
            # Update the progressor position
            arcpy.SetProgressorPosition()
            feature_counter += 1
            
        #os.removedirs(temp_folder)	
        arcpy.SetParameter(0, new_tables)
        messages.AddMessage("Data import completed.")
        return