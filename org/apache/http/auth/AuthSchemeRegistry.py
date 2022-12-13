def AuthSchemeRegistry():
'''public AuthSchemeRegistry()
'''
pass
def register():
'''public void register(final String name, final AuthSchemeFactory factory)
'''
pass
def unregister():
'''public void unregister(final String name)
'''
pass
def getAuthScheme():
'''public AuthScheme getAuthScheme(final String name, final HttpParams params)
'''
pass
def getSchemeNames():
'''public List<String> getSchemeNames()
'''
pass
def setItems():
'''public void setItems(final Map<String, AuthSchemeFactory> map)
'''
pass
def lookup():
'''public AuthSchemeProvider lookup(final String name)
'''
pass
def create():
'''public AuthScheme create(final HttpContext context)
'''
pass
