def parse():
    '''returns Cookie[]\n\n
    parse(final String host, final int port, final String path, final boolean secure, final String header)\n
    parse(final String host, final int port, final String path, final boolean secure, final Header header)\n
    '''
def getValidDateFormats():
    '''returns Collection\n\n
    getValidDateFormats()\n
    '''
def setValidDateFormats():
    '''returns None\n\n
    setValidDateFormats(final Collection datepatterns)\n
    '''
def formatCookie():
    '''returns String\n\n
    formatCookie(final Cookie cookie)\n
    '''
def formatCookieHeader():
    '''returns Header\n\n
    formatCookieHeader(final Cookie cookie)\n
    formatCookieHeader(final Cookie[] cookies)\n
    '''
def formatCookies():
    '''returns String\n\n
    formatCookies(final Cookie[] cookies)\n
    '''
def match():
    '''returns Cookie[]\n\n
    match(final String host, final int port, final String path, final boolean secure, final Cookie cookie)\n
    match(final String host, final int port, final String path, final boolean secure, final Cookie[] cookies)\n
    '''
def parseAttribute():
    '''returns None\n\n
    parseAttribute(final NameValuePair attribute, final Cookie cookie)\n
    '''
def validate():
    '''returns None\n\n
    validate(final String host, final int port, final String path, final boolean secure, final Cookie cookie)\n
    '''
def domainMatch():
    '''returns boolean\n\n
    domainMatch(final String host, final String domain)\n
    '''
def pathMatch():
    '''returns boolean\n\n
    pathMatch(final String path, final String topmostPath)\n
    '''
