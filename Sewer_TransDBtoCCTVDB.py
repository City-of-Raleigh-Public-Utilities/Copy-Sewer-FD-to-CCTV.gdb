import arcpy

arcpy.env.overwriteOutput = True

# Set local variables
in_data =  "Database Connections/RPUD_TRANSDB.sde/RPUD.SewerCollectionNetwork"
print "IN data source is " + in_data
out_data = "//corfile/Public Utilities/CCTV/CCTV.gdb/SewerCollectionNetwork"
print "Data will be copied to " + out_data
data_type = "FeatureDataset"

# Clean up existing data first
delete_data = "//corfile/Public Utilities/CCTV/CCTV.gdb"
arcpy.Delete_management(delete_data)
print "Existing geodatabase deleted"

# Create new geodatabase
arcpy.CreateFileGDB_management("//corfile/Public Utilities/CCTV", "CCTV.gdb")

# Execute Copy
arcpy.Copy_management(in_data, out_data, data_type)
print "Data copied to " + out_data
print "Complete"



