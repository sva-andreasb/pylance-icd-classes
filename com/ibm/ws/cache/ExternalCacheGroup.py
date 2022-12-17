SHARED = "int  0"
NOT_SHARED = "int  1"
def ():
    '''returns ExternalCacheGroup\n\n
    (final String id, final int type)\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
def addExternalCacheAdapter():
    '''returns None\n\n
    addExternalCacheAdapter(final String address, final String beanName)\n
    '''
def removeExternalCacheAdapter():
    '''returns None\n\n
    removeExternalCacheAdapter(final String address)\n
    '''
def invalidatePages():
    '''returns None\n\n
    invalidatePages(final ValueSet urlValueSet)\n
    '''
def invalidateIds():
    '''returns None\n\n
    invalidateIds(final HashMap ids)\n
    invalidateIds(final HashSet ids)\n
    '''
def clear():
    '''returns None\n\n
    clear(final InvalidateByTemplateEvent ie)\n
    '''
def invalidateTemplate():
    '''returns None\n\n
    invalidateTemplate(final InvalidateByTemplateEvent ie)\n
    '''
def writePages():
    '''returns None\n\n
    writePages(final ArrayList contentVector)\n
    '''
def preInvoke():
    '''returns None\n\n
    preInvoke(final ServletCacheRequest req, final HttpServletResponse resp)\n
    '''
def postInvoke():
    '''returns None\n\n
    postInvoke(final ServletCacheRequest req, final HttpServletResponse resp)\n
    '''
