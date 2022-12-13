CACHE_TYPE_JAXRPC = "int  1"
NOT_SHARED = "int  1"
SHARED_PULL = "int  3"
SHARED_PUSH = "int  2"
SHARED_PUSH_PULL = "int  4"
HIGH = "int  3"
BALANCED = "int  1"
LOW = "int  0"
CUSTOM = "int  2"
EVICTION_RANDOM = "int  1"
EVICTION_SIZE_BASED = "int  2"
EVICTION_NONE = "int  0"
DISKCACHE_MORE = "String  \"DISKCACHE_MORE\""
def isCachingEnabled():
    '''public static boolean isCachingEnabled()
    '''
def isServletCachingEnabled():
    '''public static boolean isServletCachingEnabled()
    '''
def isObjectCachingEnabled():
    '''public static boolean isObjectCachingEnabled()
    '''
def getCache():
    '''public static Cache getCache(final String instanceName)
    '''
def getConfiguredServletCacheInstanceNames():
    '''public static final ArrayList getConfiguredServletCacheInstanceNames()
    '''
def getCacheInstanceNames():
    '''public static final ArrayList getCacheInstanceNames()
    '''
def getPolicyServletCacheInstanceNames():
    '''public static final ArrayList getPolicyServletCacheInstanceNames()
    '''
def getConfigEntries():
    '''public static final ArrayList getConfigEntries(final String instanceName)
    public static final ArrayList getConfigEntries()
    '''
