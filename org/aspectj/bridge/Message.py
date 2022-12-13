def Message():
'''public Message(final String message, final ISourceLocation location, final boolean isError)
public Message(final String message, final ISourceLocation location, final boolean isError, final ISourceLocation[] extraSourceLocations)
public Message(final String message, final String details, final Kind kind, final ISourceLocation sourceLocation, final Throwable thrown, final ISourceLocation[] extraSourceLocations)
public Message(final String message, final String details, final Kind kind, final ISourceLocation sLoc, final Throwable thrown, final ISourceLocation[] otherLocs, final boolean declared, final int id, final int sourcestart, final int sourceend)
public Message(final String message, final Kind kind, final Throwable thrown, final ISourceLocation sourceLocation)
'''
pass
def getKind():
'''public Kind getKind()
'''
pass
def isError():
'''public boolean isError()
'''
pass
def isWarning():
'''public boolean isWarning()
'''
pass
def isDebug():
'''public boolean isDebug()
'''
pass
def isTaskTag():
'''public boolean isTaskTag()
'''
pass
def isInfo():
'''public boolean isInfo()
'''
pass
def isAbort():
'''public boolean isAbort()
'''
pass
def getDeclared():
'''public boolean getDeclared()
'''
pass
def isFailed():
'''public boolean isFailed()
'''
pass
def getMessage():
'''public final String getMessage()
'''
pass
def getThrown():
'''public final Throwable getThrown()
'''
pass
def getSourceLocation():
'''public final ISourceLocation getSourceLocation()
'''
pass
def toString():
'''public String toString()
'''
pass
def getDetails():
'''public String getDetails()
'''
pass
def getExtraSourceLocations():
'''public List<ISourceLocation> getExtraSourceLocations()
'''
pass
def getID():
'''public int getID()
'''
pass
def getSourceStart():
'''public int getSourceStart()
'''
pass
def getSourceEnd():
'''public int getSourceEnd()
'''
pass
