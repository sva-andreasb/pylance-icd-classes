def ():
    '''returns Message\n\n
    (final String message, final ISourceLocation location, final boolean isError)\n
    (final String message, final ISourceLocation location, final boolean isError, final ISourceLocation[] extraSourceLocations)\n
    (final String message, final String details, final Kind kind, final ISourceLocation sourceLocation, final Throwable thrown, final ISourceLocation[] extraSourceLocations)\n
    (final String message, final String details, final Kind kind, final ISourceLocation sLoc, final Throwable thrown, final ISourceLocation[] otherLocs, final boolean declared, final int id, final int sourcestart, final int sourceend)\n
    (final String message, final Kind kind, final Throwable thrown, final ISourceLocation sourceLocation)\n
    '''
def getKind():
    '''returns Kind\n\n
    getKind()\n
    '''
def isError():
    '''returns boolean\n\n
    isError()\n
    '''
def isWarning():
    '''returns boolean\n\n
    isWarning()\n
    '''
def isDebug():
    '''returns boolean\n\n
    isDebug()\n
    '''
def isTaskTag():
    '''returns boolean\n\n
    isTaskTag()\n
    '''
def isInfo():
    '''returns boolean\n\n
    isInfo()\n
    '''
def isAbort():
    '''returns boolean\n\n
    isAbort()\n
    '''
def getDeclared():
    '''returns boolean\n\n
    getDeclared()\n
    '''
def isFailed():
    '''returns boolean\n\n
    isFailed()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getDetails():
    '''returns String\n\n
    getDetails()\n
    '''
def getExtraSourceLocations():
    '''returns List<ISourceLocation>\n\n
    getExtraSourceLocations()\n
    '''
def getID():
    '''returns int\n\n
    getID()\n
    '''
def getSourceStart():
    '''returns int\n\n
    getSourceStart()\n
    '''
def getSourceEnd():
    '''returns int\n\n
    getSourceEnd()\n
    '''
