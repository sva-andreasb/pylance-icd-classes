def ():
    '''returns ExternalCacheServices\n\n
    ()\n
    '''
def getExternalCacheGroupNames():
    '''returns Iterator\n\n
    getExternalCacheGroupNames()\n
    '''
def setExternalCacheGroups():
    '''returns None\n\n
    setExternalCacheGroups(final HashMap externalCacheGroups)\n
    '''
def addExternalCacheAdapter():
    '''returns None\n\n
    addExternalCacheAdapter(final String groupId, final String address, final String beanName)\n
    '''
def removeExternalCacheAdapter():
    '''returns None\n\n
    removeExternalCacheAdapter(final String groupId, final String address)\n
    '''
def start():
    '''returns None\n\n
    start()\n
    '''
def batchUpdate():
    '''returns None\n\n
    batchUpdate(final HashMap invalidateIdEvents, final HashMap invalidateTemplateEvents, final ArrayList pushECFEvents)\n
    '''
def invalidateExternalCaches():
    '''returns None\n\n
    invalidateExternalCaches(final HashMap invalidateIdEvents, final HashMap invalidateTemplateEvents)\n
    '''
def preInvoke():
    '''returns None\n\n
    preInvoke(final String cacheGroup, final ServletCacheRequest req, final HttpServletResponse resp)\n
    '''
def postInvoke():
    '''returns None\n\n
    postInvoke(final String cacheGroup, final ServletCacheRequest req, final HttpServletResponse resp)\n
    '''
