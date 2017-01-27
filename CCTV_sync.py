## This script is for updating CCTV request. Changes will be synced from transactional to CCTV.gdb on shared drive. 
import arcpy, os
from arcpy import env

#create following path in C drive is not exists to store schema xml files
xmlPath = "C:/ReplicaSchema"
if not os.path.exists(xmlPath):
	os.makedirs(xmlPath)
env.workspace = xmlPath
env.overwriteOutput = True

# env.workspace = "Database Connections/RPUD_TRANSDB.sde"

## set up variables
replica_gdb1 = "Database Connections/RPUD_TRANSDB.sde" #parent 
replica_gdb2 = "//corfile/common/Public Utilities/CCTV/CCTV.gdb" #child
replica_name = "RPUD.CCTV_gistprd_to_cctv_fgdb"  #Replica pre-defined and registered on RPUD
sync_direction = "FROM_GEODATABASE1_TO_2"

## compare replica schema
print("Comparing replica schema...")
arcpy.AddMessage("Comparing replica schema...")
outputXML = "C:/data/replicaSchema.xml"
# overwriteXML(outputXML)
arcpy.ExportReplicaSchema_management(replica_gdb1, outputXML, replica_name)
schemaChangeXML = "C:/data/schemaChange.xml"
# overwriteXML(schemaChangeXML)
arcpy.CompareReplicaSchema_management(replica_gdb2, outputXML, schemaChangeXML)
arcpy.ImportReplicaSchema_management(replica_gdb2, schemaChangeXML)

## synchronize change
print ("Updating CCTV data from {0} to {1}...".format(replica_gdb1, replica_gdb2))
arcpy.AddMessage("Updating CCTV data from {0} to {1}...".format(replica_gdb1, replica_gdb2))

# sync changes
arcpy.SynchronizeChanges_management(replica_gdb1, replica_name, replica_gdb2, sync_direction)
print ("Sync complete.")
arcpy.AddMessage("Sync complete.")

