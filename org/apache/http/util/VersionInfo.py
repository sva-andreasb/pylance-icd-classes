UNAVAILABLE = "String  \"UNAVAILABLE\""
VERSION_PROPERTY_FILE = "String  \"version.properties\""
PROPERTY_MODULE = "String  \"info.module\""
PROPERTY_RELEASE = "String  \"info.release\""
PROPERTY_TIMESTAMP = "String  \"info.timestamp\""
def getPackage():
    '''    public final String getPackage()
    '''
def getModule():
    '''    public final String getModule()
    '''
def getRelease():
    '''    public final String getRelease()
    '''
def getTimestamp():
    '''    public final String getTimestamp()
    '''
def getClassloader():
    '''    public final String getClassloader()
    '''
def toString():
    '''    public String toString()
    '''
def loadVersionInfo():
    '''    public static VersionInfo[] loadVersionInfo(final String[] pckgs, final ClassLoader clsldr)
    public static VersionInfo loadVersionInfo(final String pckg, final ClassLoader clsldr)
    '''
def getUserAgent():
    '''    public static String getUserAgent(final String name, final String pkg, final Class<?> cls)
    '''
