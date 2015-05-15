# -*- coding: utf-8 -*-

# Import arcpy module
import arcpy

# Process: Import Data
arcpy.CartoDBImportToolbox_CartoDB( "your_user", "your_key", "F:\\data\\your_Data.gdb\\yourFeature")

