def AuthSchemeRegistry():
    '''    public AuthSchemeRegistry()
    '''
def register():
    '''    public void register(final String name, final AuthSchemeFactory factory)
    '''
def unregister():
    '''    public void unregister(final String name)
    '''
def getAuthScheme():
    '''    public AuthScheme getAuthScheme(final String name, final HttpParams params)
    '''
def getSchemeNames():
    '''    public List<String> getSchemeNames()
    '''
def setItems():
    '''    public void setItems(final Map<String, AuthSchemeFactory> map)
    '''
def lookup():
    '''    public AuthSchemeProvider lookup(final String name)
    '''
def create():
    '''    public AuthScheme create(final HttpContext context)
    '''
