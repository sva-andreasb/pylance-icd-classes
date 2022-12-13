def ramBytesUsed():
    '''    public long ramBytesUsed()
    '''
def close():
    '''    public void close()
    '''
def getValues():
    '''    public PointValues getValues(final String fieldName)
    '''
def intersect():
    '''    public void intersect(final IntersectVisitor mergedVisitor)
    '''
def visit():
    '''    public void visit(final int docID)
    public void visit(final int docID, final byte[] packedValue)
    '''
def compare():
    '''    public Relation compare(final byte[] minPackedValue, final byte[] maxPackedValue)
    '''
def estimatePointCount():
    '''    public long estimatePointCount(final IntersectVisitor visitor)
    '''
def getMinPackedValue():
    '''    public byte[] getMinPackedValue()
    '''
def getMaxPackedValue():
    '''    public byte[] getMaxPackedValue()
    '''
def getNumDimensions():
    '''    public int getNumDimensions()
    '''
def getNumIndexDimensions():
    '''    public int getNumIndexDimensions()
    '''
def getBytesPerDimension():
    '''    public int getBytesPerDimension()
    '''
def size():
    '''    public long size()
    '''
def getDocCount():
    '''    public int getDocCount()
    '''
def checkIntegrity():
    '''    public void checkIntegrity()
    '''
def merge():
    '''    public void merge(final MergeState mergeState)
    '''
