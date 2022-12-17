VERSION_70 = "int  7"
VERSION_72 = "int  8"
VERSION_74 = "int  9"
def ():
    '''returns FindSegmentsFile\n\n
    (final int indexCreatedVersionMajor)\n
    (final Directory directory)\n
    '''
def info():
    '''returns SegmentCommitInfo\n\n
    info(final int i)\n
    '''
def getSegmentsFileName():
    '''returns String\n\n
    getSegmentsFileName()\n
    '''
def getId():
    '''returns byte[]\n\n
    getId()\n
    '''
def write():
    '''returns None\n\n
    write(final Directory directory, final IndexOutput out)\n
    '''
def clone():
    '''returns SegmentInfos\n\n
    clone()\n
    '''
def getVersion():
    '''returns long\n\n
    getVersion()\n
    '''
def getGeneration():
    '''returns long\n\n
    getGeneration()\n
    '''
def getLastGeneration():
    '''returns long\n\n
    getLastGeneration()\n
    '''
def updateGeneration():
    '''returns None\n\n
    updateGeneration(final SegmentInfos other)\n
    '''
def setNextWriteGeneration():
    '''returns None\n\n
    setNextWriteGeneration(final long generation)\n
    '''
def files():
    '''returns Collection<String>\n\n
    files(final boolean includeSegmentsFile)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def setUserData():
    '''returns None\n\n
    setUserData(final Map<String, String> data, final boolean doIncrementVersion)\n
    '''
def totalMaxDoc():
    '''returns int\n\n
    totalMaxDoc()\n
    '''
def changed():
    '''returns None\n\n
    changed()\n
    '''
def iterator():
    '''returns Iterator<SegmentCommitInfo>\n\n
    iterator()\n
    '''
def asList():
    '''returns List<SegmentCommitInfo>\n\n
    asList()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def add():
    '''returns None\n\n
    add(final SegmentCommitInfo si)\n
    '''
def addAll():
    '''returns None\n\n
    addAll(final Iterable<SegmentCommitInfo> sis)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def remove():
    '''returns boolean\n\n
    remove(final SegmentCommitInfo si)\n
    '''
def getCommitLuceneVersion():
    '''returns Version\n\n
    getCommitLuceneVersion()\n
    '''
def getMinSegmentLuceneVersion():
    '''returns Version\n\n
    getMinSegmentLuceneVersion()\n
    '''
def getIndexCreatedVersionMajor():
    '''returns int\n\n
    getIndexCreatedVersionMajor()\n
    '''
def run():
    '''returns T\n\n
    run()\n
    run(final IndexCommit commit)\n
    '''
