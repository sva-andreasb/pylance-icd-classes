def ():
    '''returns SegmentCommitInfo\n\n
    (final SegmentInfo info, final int delCount, final int softDelCount, final long delGen, final long fieldInfosGen, final long docValuesGen)\n
    '''
def setDocValuesUpdatesFiles():
    '''returns None\n\n
    setDocValuesUpdatesFiles(final Map<Integer, Set<String>> dvUpdatesFiles)\n
    '''
def getFieldInfosFiles():
    '''returns Set<String>\n\n
    getFieldInfosFiles()\n
    '''
def setFieldInfosFiles():
    '''returns None\n\n
    setFieldInfosFiles(final Set<String> fieldInfosFiles)\n
    '''
def sizeInBytes():
    '''returns long\n\n
    sizeInBytes()\n
    '''
def files():
    '''returns Collection<String>\n\n
    files()\n
    '''
def hasDeletions():
    '''returns boolean\n\n
    hasDeletions()\n
    '''
def hasFieldUpdates():
    '''returns boolean\n\n
    hasFieldUpdates()\n
    '''
def getNextFieldInfosGen():
    '''returns long\n\n
    getNextFieldInfosGen()\n
    '''
def getFieldInfosGen():
    '''returns long\n\n
    getFieldInfosGen()\n
    '''
def getNextDocValuesGen():
    '''returns long\n\n
    getNextDocValuesGen()\n
    '''
def getDocValuesGen():
    '''returns long\n\n
    getDocValuesGen()\n
    '''
def getNextDelGen():
    '''returns long\n\n
    getNextDelGen()\n
    '''
def getDelGen():
    '''returns long\n\n
    getDelGen()\n
    '''
def getDelCount():
    '''returns int\n\n
    getDelCount()\n
    '''
def getSoftDelCount():
    '''returns int\n\n
    getSoftDelCount()\n
    '''
def toString():
    '''returns String\n\n
    toString(final int pendingDelCount)\n
    toString()\n
    '''
def clone():
    '''returns SegmentCommitInfo\n\n
    clone()\n
    '''
