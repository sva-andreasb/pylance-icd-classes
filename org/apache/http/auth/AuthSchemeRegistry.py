def ():
    '''returns AuthSchemeRegistry\n\n
    ()\n
    '''
def register():
    '''returns None\n\n
    register(final String name, final AuthSchemeFactory factory)\n
    '''
def unregister():
    '''returns None\n\n
    unregister(final String name)\n
    '''
def getAuthScheme():
    '''returns AuthScheme\n\n
    getAuthScheme(final String name, final HttpParams params)\n
    '''
def getSchemeNames():
    '''returns List<String>\n\n
    getSchemeNames()\n
    '''
def setItems():
    '''returns None\n\n
    setItems(final Map<String, AuthSchemeFactory> map)\n
    '''
def lookup():
    '''returns AuthSchemeProvider\n\n
    lookup(final String name)\n
    '''
def create():
    '''returns AuthScheme\n\n
    create(final HttpContext context)\n
    '''
