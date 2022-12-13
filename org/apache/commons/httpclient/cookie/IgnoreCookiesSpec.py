def parse():
'''public Cookie[] parse(final String host, final int port, final String path, final boolean secure, final String header)
public Cookie[] parse(final String host, final int port, final String path, final boolean secure, final Header header)
'''
pass
def getValidDateFormats():
'''public Collection getValidDateFormats()
'''
pass
def setValidDateFormats():
'''public void setValidDateFormats(final Collection datepatterns)
'''
pass
def formatCookie():
'''public String formatCookie(final Cookie cookie)
'''
pass
def formatCookieHeader():
'''public Header formatCookieHeader(final Cookie cookie)
public Header formatCookieHeader(final Cookie[] cookies)
'''
pass
def formatCookies():
'''public String formatCookies(final Cookie[] cookies)
'''
pass
def match():
'''public boolean match(final String host, final int port, final String path, final boolean secure, final Cookie cookie)
public Cookie[] match(final String host, final int port, final String path, final boolean secure, final Cookie[] cookies)
'''
pass
def parseAttribute():
'''public void parseAttribute(final NameValuePair attribute, final Cookie cookie)
'''
pass
def validate():
'''public void validate(final String host, final int port, final String path, final boolean secure, final Cookie cookie)
'''
pass
def domainMatch():
'''public boolean domainMatch(final String host, final String domain)
'''
pass
def pathMatch():
'''public boolean pathMatch(final String path, final String topmostPath)
'''
pass
