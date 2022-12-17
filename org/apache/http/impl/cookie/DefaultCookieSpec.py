def ():
    '''returns DefaultCookieSpec\n\n
    (final String[] datepatterns, final boolean oneHeader)\n
    ()\n
    '''
def parse():
    '''returns List<Cookie>\n\n
    parse(final Header header, final CookieOrigin origin)\n
    '''
def validate():
    '''returns None\n\n
    validate(final Cookie cookie, final CookieOrigin origin)\n
    '''
def match():
    '''returns boolean\n\n
    match(final Cookie cookie, final CookieOrigin origin)\n
    '''
def formatCookies():
    '''returns List<Header>\n\n
    formatCookies(final List<Cookie> cookies)\n
    '''
def getVersion():
    '''returns int\n\n
    getVersion()\n
    '''
def getVersionHeader():
    '''returns Header\n\n
    getVersionHeader()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
