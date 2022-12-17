def ():
    '''returns JSPCache\n\n
    ()\n
    '''
def setCache():
    '''returns None\n\n
    setCache(final DCache cache)\n
    '''
def setBatchUpdateDaemon():
    '''returns None\n\n
    setBatchUpdateDaemon(final BatchUpdateDaemon batchUpdateDaemon)\n
    '''
def setRemoteServices():
    '''returns None\n\n
    setRemoteServices(final RemoteServices remoteServices)\n
    '''
def setExternalCacheServices():
    '''returns None\n\n
    setExternalCacheServices(final com.ibm.ws.cache.intf.ExternalCacheServices externalCacheServices)\n
    '''
def setDefaultPriority():
    '''returns None\n\n
    setDefaultPriority(final int defaultPriority)\n
    '''
def start():
    '''returns None\n\n
    start()\n
    '''
def setExternalCacheFragment():
    '''returns None\n\n
    setExternalCacheFragment(final String id, final ExternalCacheFragment externalCacheFragment)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final EntryInfo entryInfo, final FragmentComposerMemento memento, final ExternalCacheFragment externalCacheFragment)\n
    '''
def setValidatorExpirationTime():
    '''returns None\n\n
    setValidatorExpirationTime(final EntryInfo entryInfo, final FragmentComposerMemento memento)\n
    '''
def updateStatisticsForVBC():
    '''returns None\n\n
    updateStatisticsForVBC(final CacheEntry cacheEntry, final boolean directive)\n
    '''
def getEntry():
    '''returns CacheEntry\n\n
    getEntry(final String id)\n
    getEntry(final EntryInfo entryInfo)\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid(final String id)\n
    '''
def getValue():
    '''returns Object\n\n
    getValue(final EntryInfo entryInfo, final boolean askPermission)\n
    '''
def invalidateById():
    '''returns None\n\n
    invalidateById(final String id, final boolean waitOnInvalidation)\n
    '''
def invalidateByTemplate():
    '''returns None\n\n
    invalidateByTemplate(final String template, final boolean waitOnInvalidation)\n
    '''
def shouldPull():
    '''returns boolean\n\n
    shouldPull(final int share, final String id)\n
    '''
def preInvoke():
    '''returns None\n\n
    preInvoke(final String cacheGroup, final CacheProxyRequest request, final CacheProxyResponse response)\n
    '''
def postInvoke():
    '''returns None\n\n
    postInvoke(final String cacheGroup, final CacheProxyRequest request, final CacheProxyResponse response)\n
    '''
def isCascadeCachespecProperties():
    '''returns boolean\n\n
    isCascadeCachespecProperties()\n
    '''
def isAutoFlushIncludes():
    '''returns boolean\n\n
    isAutoFlushIncludes()\n
    '''
def alwaysSetSurrogateControlHdr():
    '''returns boolean\n\n
    alwaysSetSurrogateControlHdr()\n
    '''
def getFilteredStatusCodes():
    '''returns int[]\n\n
    getFilteredStatusCodes()\n
    '''
