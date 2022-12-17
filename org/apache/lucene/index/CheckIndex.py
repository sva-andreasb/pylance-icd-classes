def ():
    '''returns Options\n\n
    (final Directory dir)\n
    (final Directory dir, final Lock writeLock)\n
    (final String fieldName, final int maxDoc, final PointValues values)\n
    ()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def setDoSlowChecks():
    '''returns None\n\n
    setDoSlowChecks(final boolean v)\n
    '''
def doSlowChecks():
    '''returns boolean\n\n
    doSlowChecks()\n
    '''
def setFailFast():
    '''returns None\n\n
    setFailFast(final boolean v)\n
    '''
def getFailFast():
    '''returns boolean\n\n
    getFailFast()\n
    '''
def getChecksumsOnly():
    '''returns boolean\n\n
    getChecksumsOnly()\n
    '''
def setChecksumsOnly():
    '''returns None\n\n
    setChecksumsOnly(final boolean v)\n
    '''
def setInfoStream():
    '''returns None\n\n
    setInfoStream(final PrintStream out, final boolean verbose)\n
    setInfoStream(final PrintStream out)\n
    '''
def checkIndex():
    '''returns Status\n\n
    checkIndex()\n
    checkIndex(final List<String> onlySegments)\n
    '''
def exorciseIndex():
    '''returns None\n\n
    exorciseIndex(final Status result)\n
    '''
def doCheck():
    '''returns int\n\n
    doCheck(final Options opts)\n
    '''
def getPointCountSeen():
    '''returns long\n\n
    getPointCountSeen()\n
    '''
def getDocCountSeen():
    '''returns long\n\n
    getDocCountSeen()\n
    '''
def visit():
    '''returns None\n\n
    visit(final int docID)\n
    visit(final int docID, final byte[] packedValue)\n
    visit(final int docID)\n
    visit(final int docID, final byte[] packedValue)\n
    '''
def getDirImpl():
    '''returns String\n\n
    getDirImpl()\n
    '''
def getIndexPath():
    '''returns String\n\n
    getIndexPath()\n
    '''
def setOut():
    '''returns None\n\n
    setOut(final PrintStream out)\n
    '''
