SHARED = "int  0"
NOT_SHARED = "int  1"
def ExternalCacheGroup():
    '''    public ExternalCacheGroup(final String id, final int type)
    '''
def getId():
    '''    public String getId()
    '''
def getType():
    '''    public int getType()
    '''
def addExternalCacheAdapter():
    '''    public void addExternalCacheAdapter(final String address, final String beanName)
    '''
def removeExternalCacheAdapter():
    '''    public void removeExternalCacheAdapter(final String address)
    '''
def invalidatePages():
    '''    public void invalidatePages(final ValueSet urlValueSet)
    '''
def invalidateIds():
    '''    public void invalidateIds(final HashMap ids)
    public void invalidateIds(final HashSet ids)
    '''
def clear():
    '''    public void clear(final InvalidateByTemplateEvent ie)
    '''
def invalidateTemplate():
    '''    public void invalidateTemplate(final InvalidateByTemplateEvent ie)
    '''
def writePages():
    '''    public void writePages(final ArrayList contentVector)
    '''
def preInvoke():
    '''    public void preInvoke(final ServletCacheRequest req, final HttpServletResponse resp)
    '''
def postInvoke():
    '''    public void postInvoke(final ServletCacheRequest req, final HttpServletResponse resp)
    '''
