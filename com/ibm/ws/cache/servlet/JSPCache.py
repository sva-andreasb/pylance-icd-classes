def JSPCache():
    '''public JSPCache()
    '''
def setCache():
    '''public void setCache(final DCache cache)
    '''
def setBatchUpdateDaemon():
    '''public void setBatchUpdateDaemon(final BatchUpdateDaemon batchUpdateDaemon)
    '''
def setRemoteServices():
    '''public void setRemoteServices(final RemoteServices remoteServices)
    '''
def setExternalCacheServices():
    '''public void setExternalCacheServices(final com.ibm.ws.cache.intf.ExternalCacheServices externalCacheServices)
    '''
def setDefaultPriority():
    '''public void setDefaultPriority(final int defaultPriority)
    '''
def start():
    '''public void start()
    '''
def setExternalCacheFragment():
    '''public void setExternalCacheFragment(final String id, final ExternalCacheFragment externalCacheFragment)
    '''
def setValue():
    '''public void setValue(final EntryInfo entryInfo, final FragmentComposerMemento memento, final ExternalCacheFragment externalCacheFragment)
    '''
def setValidatorExpirationTime():
    '''public void setValidatorExpirationTime(final EntryInfo entryInfo, final FragmentComposerMemento memento)
    '''
def updateStatisticsForVBC():
    '''public void updateStatisticsForVBC(final CacheEntry cacheEntry, final boolean directive)
    '''
def getEntry():
    '''public CacheEntry getEntry(final String id)
    public CacheEntry getEntry(final EntryInfo entryInfo)
    '''
def isValid():
    '''public boolean isValid(final String id)
    '''
def getValue():
    '''public Object getValue(final EntryInfo entryInfo, final boolean askPermission)
    '''
def invalidateById():
    '''public void invalidateById(final String id, final boolean waitOnInvalidation)
    '''
def invalidateByTemplate():
    '''public void invalidateByTemplate(final String template, final boolean waitOnInvalidation)
    '''
def shouldPull():
    '''public boolean shouldPull(final int share, final String id)
    '''
def preInvoke():
    '''public void preInvoke(final String cacheGroup, final CacheProxyRequest request, final CacheProxyResponse response)
    '''
def postInvoke():
    '''public void postInvoke(final String cacheGroup, final CacheProxyRequest request, final CacheProxyResponse response)
    '''
def isCascadeCachespecProperties():
    '''public boolean isCascadeCachespecProperties()
    '''
def isAutoFlushIncludes():
    '''public boolean isAutoFlushIncludes()
    '''
def alwaysSetSurrogateControlHdr():
    '''public boolean alwaysSetSurrogateControlHdr()
    '''
def getFilteredStatusCodes():
    '''public int[] getFilteredStatusCodes()
    '''
