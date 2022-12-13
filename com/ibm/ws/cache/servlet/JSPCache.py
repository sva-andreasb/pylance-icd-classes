def JSPCache():
'''public JSPCache()
'''
pass
def setCache():
'''public void setCache(final DCache cache)
'''
pass
def setBatchUpdateDaemon():
'''public void setBatchUpdateDaemon(final BatchUpdateDaemon batchUpdateDaemon)
'''
pass
def setRemoteServices():
'''public void setRemoteServices(final RemoteServices remoteServices)
'''
pass
def setExternalCacheServices():
'''public void setExternalCacheServices(final com.ibm.ws.cache.intf.ExternalCacheServices externalCacheServices)
'''
pass
def setDefaultPriority():
'''public void setDefaultPriority(final int defaultPriority)
'''
pass
def start():
'''public void start()
'''
pass
def setExternalCacheFragment():
'''public void setExternalCacheFragment(final String id, final ExternalCacheFragment externalCacheFragment)
'''
pass
def setValue():
'''public void setValue(final EntryInfo entryInfo, final FragmentComposerMemento memento, final ExternalCacheFragment externalCacheFragment)
'''
pass
def setValidatorExpirationTime():
'''public void setValidatorExpirationTime(final EntryInfo entryInfo, final FragmentComposerMemento memento)
'''
pass
def updateStatisticsForVBC():
'''public void updateStatisticsForVBC(final CacheEntry cacheEntry, final boolean directive)
'''
pass
def getEntry():
'''public CacheEntry getEntry(final String id)
public CacheEntry getEntry(final EntryInfo entryInfo)
'''
pass
def isValid():
'''public boolean isValid(final String id)
'''
pass
def getValue():
'''public Object getValue(final EntryInfo entryInfo, final boolean askPermission)
'''
pass
def invalidateById():
'''public void invalidateById(final String id, final boolean waitOnInvalidation)
'''
pass
def invalidateByTemplate():
'''public void invalidateByTemplate(final String template, final boolean waitOnInvalidation)
'''
pass
def shouldPull():
'''public boolean shouldPull(final int share, final String id)
'''
pass
def preInvoke():
'''public void preInvoke(final String cacheGroup, final CacheProxyRequest request, final CacheProxyResponse response)
'''
pass
def postInvoke():
'''public void postInvoke(final String cacheGroup, final CacheProxyRequest request, final CacheProxyResponse response)
'''
pass
def isCascadeCachespecProperties():
'''public boolean isCascadeCachespecProperties()
'''
pass
def isAutoFlushIncludes():
'''public boolean isAutoFlushIncludes()
'''
pass
def alwaysSetSurrogateControlHdr():
'''public boolean alwaysSetSurrogateControlHdr()
'''
pass
def getFilteredStatusCodes():
'''public int[] getFilteredStatusCodes()
'''
pass
