import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = arcpy.GetParameterAsText(0)
target_spatial_ref = arcpy.Describe(arcpy.GetParameterAsText(1)).spatialReference
fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    if arcpy.Describe(fc).spatialReference.name != target_spatial_ref.name:
        arcpy.management.Project(fc, fc[:-4] + "_projected.shp" if fc.endswith(".shp") else fc + "_projected", target_spatial_ref)


