defStrVersion = "String  \"x.x.x.x\""
defIntVersion = "int  0"
regEx = "String  \"\\p{XDigit}{1,4}\\.\\p{XDigit}{1,4}\\.\\p{XDigit}{1,4}\\.\\p{XDigit}{1,4}\""
def FileVersion():
    '''    public FileVersion()
    public FileVersion(final String strVersion)
    public FileVersion(final long longVersion)
    '''
def setVersion():
    '''    public void setVersion(final long longVersion)
    public void setVersion(final String strVersion)
    '''
def getVersionAsLong():
    '''    public long getVersionAsLong()
    '''
def getVersionAsString():
    '''    public String getVersionAsString()
    '''
def isUpToDate():
    '''    public boolean isUpToDate(final FileVersion fileVersion)
    '''
def convertToLong():
    '''    public static long convertToLong(final String s)
    '''
def convertToString():
    '''    public static String convertToString(final long n)
    '''
def getMessage():
    '''    public static String getMessage(final String s)
    '''
