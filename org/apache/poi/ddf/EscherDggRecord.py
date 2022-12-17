RECORD_ID = "short  -4090"
RECORD_DESCRIPTION = "String  \"MsofbtDgg\""
def ():
    '''returns FileIdCluster\n\n
    ()\n
    (final int drawingGroupId, final int numShapeIdsUsed)\n
    '''
def fillFields():
    '''returns int\n\n
    fillFields(final byte[] data, final int offset, final EscherRecordFactory recordFactory)\n
    '''
def serialize():
    '''returns int\n\n
    serialize(final int offset, final byte[] data, final EscherSerializationListener listener)\n
    '''
def getRecordSize():
    '''returns int\n\n
    getRecordSize()\n
    '''
def getRecordId():
    '''returns short\n\n
    getRecordId()\n
    '''
def getRecordName():
    '''returns String\n\n
    getRecordName()\n
    '''
def getShapeIdMax():
    '''returns int\n\n
    getShapeIdMax()\n
    '''
def setShapeIdMax():
    '''returns None\n\n
    setShapeIdMax(final int shapeIdMax)\n
    '''
def getNumIdClusters():
    '''returns int\n\n
    getNumIdClusters()\n
    '''
def getNumShapesSaved():
    '''returns int\n\n
    getNumShapesSaved()\n
    '''
def setNumShapesSaved():
    '''returns None\n\n
    setNumShapesSaved(final int numShapesSaved)\n
    '''
def getDrawingsSaved():
    '''returns int\n\n
    getDrawingsSaved()\n
    '''
def setDrawingsSaved():
    '''returns None\n\n
    setDrawingsSaved(final int drawingsSaved)\n
    '''
def getMaxDrawingGroupId():
    '''returns int\n\n
    getMaxDrawingGroupId()\n
    '''
def getFileIdClusters():
    '''returns FileIdCluster[]\n\n
    getFileIdClusters()\n
    '''
def setFileIdClusters():
    '''returns None\n\n
    setFileIdClusters(final FileIdCluster[] fileIdClusters)\n
    '''
def addCluster():
    '''returns FileIdCluster\n\n
    addCluster(final int dgId, final int numShapedUsed)\n
    addCluster(final int dgId, final int numShapedUsed, final boolean sort)\n
    '''
def compare():
    '''returns int\n\n
    compare(final FileIdCluster f1, final FileIdCluster f2)\n
    '''
def findNewDrawingGroupId():
    '''returns short\n\n
    findNewDrawingGroupId()\n
    '''
def allocateShapeId():
    '''returns int\n\n
    allocateShapeId(final EscherDgRecord dg, final boolean sort)\n
    '''
def getDrawingGroupId():
    '''returns int\n\n
    getDrawingGroupId()\n
    '''
def getNumShapeIdsUsed():
    '''returns int\n\n
    getNumShapeIdsUsed()\n
    '''
