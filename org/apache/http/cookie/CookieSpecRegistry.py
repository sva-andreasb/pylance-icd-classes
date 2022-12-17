def ():
    '''returns CookieSpecRegistry\n\n
    ()\n
    '''
def register():
    '''returns None\n\n
    register(final String name, final CookieSpecFactory factory)\n
    '''
def unregister():
    '''returns None\n\n
    unregister(final String id)\n
    '''
def getCookieSpec():
    '''returns CookieSpec\n\n
    getCookieSpec(final String name, final HttpParams params)\n
    getCookieSpec(final String name)\n
    '''
def getSpecNames():
    '''returns List<String>\n\n
    getSpecNames()\n
    '''
def setItems():
    '''returns None\n\n
    setItems(final Map<String, CookieSpecFactory> map)\n
    '''
def lookup():
    '''returns CookieSpecProvider\n\n
    lookup(final String name)\n
    '''
def create():
    '''returns CookieSpec\n\n
    create(final HttpContext context)\n
    '''
