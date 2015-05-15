'''
Created on 14/05/2015

http://desktop.arcgis.com/en/desktop/latest/analyze/sharing-workflows/h-zip-python-script.htm

@author: arcgis
'''

import sys, zipfile, arcpy, os, traceback

# Function for zipping files.  If keep is true, the folder, along with 
#  all its contents, will be written to the zip file.  If false, only 
#  the contents of the input folder will be written to the zip file - 
#  the input folder name will not appear in the zip file.
#
def zipws(path, zip, keep):
    path = os.path.normpath(path)
    # os.walk visits every subdirectory, returning a 3-tuple
    #  of directory name, subdirectories in it, and file names
    #  in it.
    #
    for (dirpath, dirnames, filenames) in os.walk(path):
        # Iterate over every file name
        #
        for file in filenames:
            # Ignore .lock files
            #
            if not file.endswith('.lock'):
                #arcpy.AddMessage("Adding %s..." % os.path.join(path, dirpath, file))
                try:
                    if keep:
                        zip.write(os.path.join(dirpath, file),
                        os.path.join(os.path.basename(path), os.path.join(dirpath, file)[len(path)+len(os.sep):]))
                    else:
                        zip.write(os.path.join(dirpath, file),            
                        os.path.join(dirpath[len(path):], file)) 
                        
                except Exception, e:
                    arcpy.AddWarning("    Error adding %s: %s" % (file, e))

    return None

'''

'''
def create_zip(infolder, outfile):
    # Create the zip file for writing compressed data. In some rare
    #  instances, the ZIP_DEFLATED constant may be unavailable and
    #  the ZIP_STORED constant is used instead.  When ZIP_STORED is
    #  used, the zip file does not contain compressed data, resulting
    #  in large zip files. 
    try:
        arcpy.AddMessage("Creating Zip file...")
        zip = zipfile.ZipFile(outfile, 'w', zipfile.ZIP_DEFLATED)
        zipws(infolder, zip, True)
        zip.close()
    except RuntimeError:
        # Delete zip file if it exists
        #
        if os.path.exists(outfile):
                os.unlink(outfile)
        zip = zipfile.ZipFile(outfile, 'w', zipfile.ZIP_STORED)
        zipws(infolder, zip, True)
        zip.close()
        arcpy.AddWarning("    Unable to compress zip file contents.")
               
    arcpy.AddMessage("Zip file created successfully")
