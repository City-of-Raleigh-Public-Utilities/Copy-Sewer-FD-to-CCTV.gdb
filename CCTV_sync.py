## This script is for updating CCTV request. Changes will be synced to CCTV.gdb on shared drive. 
import arcpy

arcpy.env.workspace = "Database Connections/RPUD_TRANSDB.sde"

## set up variables
replica_gdb1 = "Database Connections/RPUD_TRANSDB.sde"
replica_gdb2 = "//corfile/common/Public Utilities/CCTV/CCTV.gdb"
replica_name = "RPUD.CCTV_gistprd_to_cctv_fgdb" ## this 
 
sync_direction = "FROM_GEODATABASE1_TO_2"
print ("Updates on CCTV will be synced from {0} to {1}".format(replica_gdb1, replica_gdb2))
arcpy.AddMessage("Updates on CCTV will be synced from {0} to {1}".format(replica_gdb1, replica_gdb2))
## sync changes
arcpy.SynchronizeChanges_management(replica_gdb1, replica_name, replica_gdb2, sync_direction)
print ("Sync complete")
arcpy.AddMessage("Sync complete")