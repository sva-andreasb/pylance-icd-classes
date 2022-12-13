def Message():
    '''public Message(final String message, final ISourceLocation location, final boolean isError)
    public Message(final String message, final ISourceLocation location, final boolean isError, final ISourceLocation[] extraSourceLocations)
    public Message(final String message, final String details, final Kind kind, final ISourceLocation sourceLocation, final Throwable thrown, final ISourceLocation[] extraSourceLocations)
    public Message(final String message, final String details, final Kind kind, final ISourceLocation sLoc, final Throwable thrown, final ISourceLocation[] otherLocs, final boolean declared, final int id, final int sourcestart, final int sourceend)
    public Message(final String message, final Kind kind, final Throwable thrown, final ISourceLocation sourceLocation)
    '''
def getKind():
    '''public Kind getKind()
    '''
def isError():
    '''public boolean isError()
    '''
def isWarning():
    '''public boolean isWarning()
    '''
def isDebug():
    '''public boolean isDebug()
    '''
def isTaskTag():
    '''public boolean isTaskTag()
    '''
def isInfo():
    '''public boolean isInfo()
    '''
def isAbort():
    '''public boolean isAbort()
    '''
def getDeclared():
    '''public boolean getDeclared()
    '''
def isFailed():
    '''public boolean isFailed()
    '''
def getMessage():
    '''public final String getMessage()
    '''
def getThrown():
    '''public final Throwable getThrown()
    '''
def getSourceLocation():
    '''public final ISourceLocation getSourceLocation()
    '''
def toString():
    '''public String toString()
    '''
def getDetails():
    '''public String getDetails()
    '''
def getExtraSourceLocations():
    '''public List<ISourceLocation> getExtraSourceLocations()
    '''
def getID():
    '''public int getID()
    '''
def getSourceStart():
    '''public int getSourceStart()
    '''
def getSourceEnd():
    '''public int getSourceEnd()
    '''
