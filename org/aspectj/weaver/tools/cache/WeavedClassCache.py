WEAVED_CLASS_CACHE_ENABLED = "String  \"aj.weaving.cache.enabled\""
CACHE_IMPL = "String  \"aj.weaving.cache.impl\""
def getName():
    '''returns String\n\n
    getName()\n
    '''
def createGeneratedCacheKey():
    '''returns CachedClassReference\n\n
    createGeneratedCacheKey(final String className)\n
    '''
def createCacheKey():
    '''returns CachedClassReference\n\n
    createCacheKey(final String className, final byte[] originalBytes)\n
    '''
def getCachingClassHandler():
    '''returns GeneratedClassHandler\n\n
    getCachingClassHandler()\n
    '''
def put():
    '''returns None\n\n
    put(final CachedClassReference ref, final byte[] classBytes, final byte[] weavedBytes)\n
    '''
def get():
    '''returns CachedClassEntry\n\n
    get(final CachedClassReference ref, final byte[] classBytes)\n
    '''
def ignore():
    '''returns None\n\n
    ignore(final CachedClassReference ref, final byte[] classBytes)\n
    '''
def remove():
    '''returns None\n\n
    remove(final CachedClassReference ref)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def getStats():
    '''returns CacheStatistics\n\n
    getStats()\n
    '''
