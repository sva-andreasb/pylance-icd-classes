SET_COOKIE_KEY = "String  \"set-cookie\""
def ():
    '''returns RFC2109Spec\n\n
    ()\n
    '''
def parseAttribute():
    '''returns None\n\n
    parseAttribute(final NameValuePair attribute, final Cookie cookie)\n
    '''
def validate():
    '''returns None\n\n
    validate(String host, final int port, final String path, final boolean secure, final Cookie cookie)\n
    '''
def domainMatch():
    '''returns boolean\n\n
    domainMatch(final String host, final String domain)\n
    '''
def formatCookie():
    '''returns String\n\n
    formatCookie(final Cookie cookie)\n
    '''
def formatCookies():
    '''returns String\n\n
    formatCookies(final Cookie[] cookies)\n
    '''
