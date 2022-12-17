def ramBytesUsed():
    '''returns long\n\n
    ramBytesUsed()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getValues():
    '''returns PointValues\n\n
    getValues(final String fieldName)\n
    '''
def intersect():
    '''returns None\n\n
    intersect(final IntersectVisitor mergedVisitor)\n
    '''
def visit():
    '''returns None\n\n
    visit(final int docID)\n
    visit(final int docID, final byte[] packedValue)\n
    '''
def compare():
    '''returns Relation\n\n
    compare(final byte[] minPackedValue, final byte[] maxPackedValue)\n
    '''
def estimatePointCount():
    '''returns long\n\n
    estimatePointCount(final IntersectVisitor visitor)\n
    '''
def getMinPackedValue():
    '''returns byte[]\n\n
    getMinPackedValue()\n
    '''
def getMaxPackedValue():
    '''returns byte[]\n\n
    getMaxPackedValue()\n
    '''
def getNumDimensions():
    '''returns int\n\n
    getNumDimensions()\n
    '''
def getNumIndexDimensions():
    '''returns int\n\n
    getNumIndexDimensions()\n
    '''
def getBytesPerDimension():
    '''returns int\n\n
    getBytesPerDimension()\n
    '''
def size():
    '''returns long\n\n
    size()\n
    '''
def getDocCount():
    '''returns int\n\n
    getDocCount()\n
    '''
def checkIntegrity():
    '''returns None\n\n
    checkIntegrity()\n
    '''
def merge():
    '''returns None\n\n
    merge(final MergeState mergeState)\n
    '''
