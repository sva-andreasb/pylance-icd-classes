def ():
    '''returns AuthState\n\n
    ()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def getState():
    '''returns AuthProtocolState\n\n
    getState()\n
    '''
def setState():
    '''returns None\n\n
    setState(final AuthProtocolState state)\n
    '''
def getAuthScheme():
    '''returns AuthScheme\n\n
    getAuthScheme()\n
    '''
def getCredentials():
    '''returns Credentials\n\n
    getCredentials()\n
    '''
def update():
    '''returns None\n\n
    update(final AuthScheme authScheme, final Credentials credentials)\n
    update(final Queue<AuthOption> authOptions)\n
    '''
def getAuthOptions():
    '''returns Queue<AuthOption>\n\n
    getAuthOptions()\n
    '''
def hasAuthOptions():
    '''returns boolean\n\n
    hasAuthOptions()\n
    '''
def invalidate():
    '''returns None\n\n
    invalidate()\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid()\n
    '''
def setAuthScheme():
    '''returns None\n\n
    setAuthScheme(final AuthScheme authScheme)\n
    '''
def setCredentials():
    '''returns None\n\n
    setCredentials(final Credentials credentials)\n
    '''
def getAuthScope():
    '''returns AuthScope\n\n
    getAuthScope()\n
    '''
def setAuthScope():
    '''returns None\n\n
    setAuthScope(final AuthScope authScope)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
