def ExternalCacheServices():
'''public ExternalCacheServices()
'''
pass
def getExternalCacheGroupNames():
'''public Iterator getExternalCacheGroupNames()
'''
pass
def setExternalCacheGroups():
'''public void setExternalCacheGroups(final HashMap externalCacheGroups)
'''
pass
def addExternalCacheAdapter():
'''public void addExternalCacheAdapter(final String groupId, final String address, final String beanName)
'''
pass
def removeExternalCacheAdapter():
'''public void removeExternalCacheAdapter(final String groupId, final String address)
'''
pass
def start():
'''public void start()
'''
pass
def batchUpdate():
'''public void batchUpdate(final HashMap invalidateIdEvents, final HashMap invalidateTemplateEvents, final ArrayList pushECFEvents)
'''
pass
def invalidateExternalCaches():
'''public void invalidateExternalCaches(final HashMap invalidateIdEvents, final HashMap invalidateTemplateEvents)
'''
pass
def preInvoke():
'''public void preInvoke(final String cacheGroup, final ServletCacheRequest req, final HttpServletResponse resp)
'''
pass
def postInvoke():
'''public void postInvoke(final String cacheGroup, final ServletCacheRequest req, final HttpServletResponse resp)
'''
pass
