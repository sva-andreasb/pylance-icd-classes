RECORD_ID = "short  -4090"
RECORD_DESCRIPTION = "String  MsofbtDgg""
def EscherDggRecord():
'''public EscherDggRecord()
'''
pass
def fillFields():
'''public int fillFields(final byte[] data, final int offset, final EscherRecordFactory recordFactory)
'''
pass
def serialize():
'''public int serialize(final int offset, final byte[] data, final EscherSerializationListener listener)
'''
pass
def getRecordSize():
'''public int getRecordSize()
'''
pass
def getRecordId():
'''public short getRecordId()
'''
pass
def getRecordName():
'''public String getRecordName()
'''
pass
def getShapeIdMax():
'''public int getShapeIdMax()
'''
pass
def setShapeIdMax():
'''public void setShapeIdMax(final int shapeIdMax)
'''
pass
def getNumIdClusters():
'''public int getNumIdClusters()
'''
pass
def getNumShapesSaved():
'''public int getNumShapesSaved()
'''
pass
def setNumShapesSaved():
'''public void setNumShapesSaved(final int numShapesSaved)
'''
pass
def getDrawingsSaved():
'''public int getDrawingsSaved()
'''
pass
def setDrawingsSaved():
'''public void setDrawingsSaved(final int drawingsSaved)
'''
pass
def getMaxDrawingGroupId():
'''public int getMaxDrawingGroupId()
'''
pass
def getFileIdClusters():
'''public FileIdCluster[] getFileIdClusters()
'''
pass
def setFileIdClusters():
'''public void setFileIdClusters(final FileIdCluster[] fileIdClusters)
'''
pass
def addCluster():
'''public FileIdCluster addCluster(final int dgId, final int numShapedUsed)
public FileIdCluster addCluster(final int dgId, final int numShapedUsed, final boolean sort)
'''
pass
def compare():
'''public int compare(final FileIdCluster f1, final FileIdCluster f2)
'''
pass
def findNewDrawingGroupId():
'''public short findNewDrawingGroupId()
'''
pass
def allocateShapeId():
'''public int allocateShapeId(final EscherDgRecord dg, final boolean sort)
'''
pass
def FileIdCluster():
'''public FileIdCluster(final int drawingGroupId, final int numShapeIdsUsed)
'''
pass
def getDrawingGroupId():
'''public int getDrawingGroupId()
'''
pass
def getNumShapeIdsUsed():
'''public int getNumShapeIdsUsed()
'''
pass
