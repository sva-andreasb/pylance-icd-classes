def CookieSpecRegistry():
    '''    public CookieSpecRegistry()
    '''
def register():
    '''    public void register(final String name, final CookieSpecFactory factory)
    '''
def unregister():
    '''    public void unregister(final String id)
    '''
def getCookieSpec():
    '''    public CookieSpec getCookieSpec(final String name, final HttpParams params)
    public CookieSpec getCookieSpec(final String name)
    '''
def getSpecNames():
    '''    public List<String> getSpecNames()
    '''
def setItems():
    '''    public void setItems(final Map<String, CookieSpecFactory> map)
    '''
def lookup():
    '''    public CookieSpecProvider lookup(final String name)
    '''
def create():
    '''    public CookieSpec create(final HttpContext context)
    '''
