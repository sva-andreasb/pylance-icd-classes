def CookieSpecRegistry():
'''public CookieSpecRegistry()
'''
pass
def register():
'''public void register(final String name, final CookieSpecFactory factory)
'''
pass
def unregister():
'''public void unregister(final String id)
'''
pass
def getCookieSpec():
'''public CookieSpec getCookieSpec(final String name, final HttpParams params)
public CookieSpec getCookieSpec(final String name)
'''
pass
def getSpecNames():
'''public List<String> getSpecNames()
'''
pass
def setItems():
'''public void setItems(final Map<String, CookieSpecFactory> map)
'''
pass
def lookup():
'''public CookieSpecProvider lookup(final String name)
'''
pass
def create():
'''public CookieSpec create(final HttpContext context)
'''
pass
