def ():
    '''returns FieldDimensions\n\n
    (final FieldInfo[] infos)\n
    (final int dimensionCount, final int indexDimensionCount, final int dimensionNumBytes)\n
    '''
def hasFreq():
    '''returns boolean\n\n
    hasFreq()\n
    '''
def hasProx():
    '''returns boolean\n\n
    hasProx()\n
    '''
def hasPayloads():
    '''returns boolean\n\n
    hasPayloads()\n
    '''
def hasOffsets():
    '''returns boolean\n\n
    hasOffsets()\n
    '''
def hasVectors():
    '''returns boolean\n\n
    hasVectors()\n
    '''
def hasNorms():
    '''returns boolean\n\n
    hasNorms()\n
    '''
def hasDocValues():
    '''returns boolean\n\n
    hasDocValues()\n
    '''
def hasPointValues():
    '''returns boolean\n\n
    hasPointValues()\n
    '''
def getSoftDeletesField():
    '''returns String\n\n
    getSoftDeletesField()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def iterator():
    '''returns Iterator<FieldInfo>\n\n
    iterator()\n
    '''
def fieldInfo():
    '''returns FieldInfo\n\n
    fieldInfo(final String fieldName)\n
    fieldInfo(final int fieldNumber)\n
    fieldInfo(final String fieldName)\n
    '''
def add():
    '''returns FieldInfo\n\n
    add(final FieldInfos other)\n
    add(final FieldInfo fi)\n
    add(final FieldInfo fi, final long dvGen)\n
    '''
def getOrAdd():
    '''returns FieldInfo\n\n
    getOrAdd(final String name)\n
    '''
