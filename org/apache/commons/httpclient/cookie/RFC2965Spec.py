SET_COOKIE2_KEY = "String  \"set-cookie2\""
def ():
    '''returns RFC2965Spec\n\n
    ()\n
    '''
def parse():
    '''returns None\n\n
    parse(final String host, final int port, final String path, final boolean secure, final Header header)\n
    parse(String host, final int port, String path, final boolean secure, final String header)\n
    parse(final Cookie cookie, final String path)\n
    parse(final Cookie cookie, String domain)\n
    parse(final Cookie cookie, final String portValue)\n
    parse(final Cookie cookie, final String value)\n
    parse(final Cookie cookie, final String secure)\n
    parse(final Cookie cookie, final String comment)\n
    parse(final Cookie cookie, final String commenturl)\n
    parse(final Cookie cookie, final String commenturl)\n
    parse(final Cookie cookie, final String value)\n
    '''
def parseAttribute():
    '''returns None\n\n
    parseAttribute(final NameValuePair attribute, final Cookie cookie)\n
    '''
def validate():
    '''returns None\n\n
    validate(final String host, final int port, final String path, final boolean secure, final Cookie cookie)\n
    validate(final Cookie cookie, final CookieOrigin origin)\n
    validate(final Cookie cookie, final CookieOrigin origin)\n
    validate(final Cookie cookie, final CookieOrigin origin)\n
    validate(final Cookie cookie, final CookieOrigin origin)\n
    validate(final Cookie cookie, final CookieOrigin origin)\n
    validate(final Cookie cookie, final CookieOrigin origin)\n
    validate(final Cookie cookie, final CookieOrigin origin)\n
    validate(final Cookie cookie, final CookieOrigin origin)\n
    validate(final Cookie cookie, final CookieOrigin origin)\n
    '''
def match():
    '''returns boolean\n\n
    match(final String host, final int port, final String path, final boolean secure, final Cookie cookie)\n
    match(final Cookie cookie, final CookieOrigin origin)\n
    match(final Cookie cookie, final CookieOrigin origin)\n
    match(final Cookie cookie, final CookieOrigin origin)\n
    match(final Cookie cookie, final CookieOrigin origin)\n
    match(final Cookie cookie, final CookieOrigin origin)\n
    match(final Cookie cookie, final CookieOrigin origin)\n
    match(final Cookie cookie, final CookieOrigin origin)\n
    match(final Cookie cookie, final CookieOrigin origin)\n
    match(final Cookie cookie, final CookieOrigin origin)\n
    '''
def formatCookie():
    '''returns String\n\n
    formatCookie(final Cookie cookie)\n
    '''
def formatCookies():
    '''returns String\n\n
    formatCookies(final Cookie[] cookies)\n
    '''
def domainMatch():
    '''returns boolean\n\n
    domainMatch(final String host, final String domain)\n
    '''
def getVersion():
    '''returns int\n\n
    getVersion()\n
    '''
def getVersionHeader():
    '''returns Header\n\n
    getVersionHeader()\n
    '''
