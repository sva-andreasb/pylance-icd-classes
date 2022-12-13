def ExternalCacheServices():
    '''public ExternalCacheServices()
    '''
def getExternalCacheGroupNames():
    '''public Iterator getExternalCacheGroupNames()
    '''
def setExternalCacheGroups():
    '''public void setExternalCacheGroups(final HashMap externalCacheGroups)
    '''
def addExternalCacheAdapter():
    '''public void addExternalCacheAdapter(final String groupId, final String address, final String beanName)
    '''
def removeExternalCacheAdapter():
    '''public void removeExternalCacheAdapter(final String groupId, final String address)
    '''
def start():
    '''public void start()
    '''
def batchUpdate():
    '''public void batchUpdate(final HashMap invalidateIdEvents, final HashMap invalidateTemplateEvents, final ArrayList pushECFEvents)
    '''
def invalidateExternalCaches():
    '''public void invalidateExternalCaches(final HashMap invalidateIdEvents, final HashMap invalidateTemplateEvents)
    '''
def preInvoke():
    '''public void preInvoke(final String cacheGroup, final ServletCacheRequest req, final HttpServletResponse resp)
    '''
def postInvoke():
    '''public void postInvoke(final String cacheGroup, final ServletCacheRequest req, final HttpServletResponse resp)
    '''
