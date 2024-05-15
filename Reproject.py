import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = arcpy.GetParameterAsText(0)
target_spatial_ref = arcpy.Describe(arcpy.GetParameterAsText(1)).spatialReference

