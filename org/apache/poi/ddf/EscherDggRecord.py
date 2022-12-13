RECORD_ID = "short  -4090"
RECORD_DESCRIPTION = "String  \"MsofbtDgg\""
def EscherDggRecord():
    '''    public EscherDggRecord()
    '''
def fillFields():
    '''    public int fillFields(final byte[] data, final int offset, final EscherRecordFactory recordFactory)
    '''
def serialize():
    '''    public int serialize(final int offset, final byte[] data, final EscherSerializationListener listener)
    '''
def getRecordSize():
    '''    public int getRecordSize()
    '''
def getRecordId():
    '''    public short getRecordId()
    '''
def getRecordName():
    '''    public String getRecordName()
    '''
def getShapeIdMax():
    '''    public int getShapeIdMax()
    '''
def setShapeIdMax():
    '''    public void setShapeIdMax(final int shapeIdMax)
    '''
def getNumIdClusters():
    '''    public int getNumIdClusters()
    '''
def getNumShapesSaved():
    '''    public int getNumShapesSaved()
    '''
def setNumShapesSaved():
    '''    public void setNumShapesSaved(final int numShapesSaved)
    '''
def getDrawingsSaved():
    '''    public int getDrawingsSaved()
    '''
def setDrawingsSaved():
    '''    public void setDrawingsSaved(final int drawingsSaved)
    '''
def getMaxDrawingGroupId():
    '''    public int getMaxDrawingGroupId()
    '''
def getFileIdClusters():
    '''    public FileIdCluster[] getFileIdClusters()
    '''
def setFileIdClusters():
    '''    public void setFileIdClusters(final FileIdCluster[] fileIdClusters)
    '''
def addCluster():
    '''    public FileIdCluster addCluster(final int dgId, final int numShapedUsed)
    public FileIdCluster addCluster(final int dgId, final int numShapedUsed, final boolean sort)
    '''
def compare():
    '''    public int compare(final FileIdCluster f1, final FileIdCluster f2)
    '''
def findNewDrawingGroupId():
    '''    public short findNewDrawingGroupId()
    '''
def allocateShapeId():
    '''    public int allocateShapeId(final EscherDgRecord dg, final boolean sort)
    '''
def FileIdCluster():
    '''    public FileIdCluster(final int drawingGroupId, final int numShapeIdsUsed)
    '''
def getDrawingGroupId():
    '''    public int getDrawingGroupId()
    '''
def getNumShapeIdsUsed():
    '''    public int getNumShapeIdsUsed()
    '''
