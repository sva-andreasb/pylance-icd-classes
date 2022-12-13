SHARED = "int  0"
NOT_SHARED = "int  1"
def ExternalCacheGroup():
'''public ExternalCacheGroup(final String id, final int type)
'''
pass
def getId():
'''public String getId()
'''
pass
def getType():
'''public int getType()
'''
pass
def addExternalCacheAdapter():
'''public void addExternalCacheAdapter(final String address, final String beanName)
'''
pass
def removeExternalCacheAdapter():
'''public void removeExternalCacheAdapter(final String address)
'''
pass
def invalidatePages():
'''public void invalidatePages(final ValueSet urlValueSet)
'''
pass
def invalidateIds():
'''public void invalidateIds(final HashMap ids)
public void invalidateIds(final HashSet ids)
'''
pass
def clear():
'''public void clear(final InvalidateByTemplateEvent ie)
'''
pass
def invalidateTemplate():
'''public void invalidateTemplate(final InvalidateByTemplateEvent ie)
'''
pass
def writePages():
'''public void writePages(final ArrayList contentVector)
'''
pass
def preInvoke():
'''public void preInvoke(final ServletCacheRequest req, final HttpServletResponse resp)
'''
pass
def postInvoke():
'''public void postInvoke(final ServletCacheRequest req, final HttpServletResponse resp)
'''
pass
