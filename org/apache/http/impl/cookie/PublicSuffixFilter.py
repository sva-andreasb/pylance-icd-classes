def ():
    '''returns PublicSuffixFilter\n\n
    (final CookieAttributeHandler wrapped)\n
    '''
def setPublicSuffixes():
    '''returns None\n\n
    setPublicSuffixes(final Collection<String> suffixes)\n
    '''
def setExceptions():
    '''returns None\n\n
    setExceptions(final Collection<String> exceptions)\n
    '''
def match():
    '''returns boolean\n\n
    match(final Cookie cookie, final CookieOrigin origin)\n
    '''
def parse():
    '''returns None\n\n
    parse(final SetCookie cookie, final String value)\n
    '''
def validate():
    '''returns None\n\n
    validate(final Cookie cookie, final CookieOrigin origin)\n
    '''
