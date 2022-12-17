DEFAULT_PORT = "int  80"
_default_port = "int  80"
def ():
    '''returns HttpURL\n\n
    (final char[] escaped, final String charset)\n
    (final char[] escaped)\n
    (final String original, final String charset)\n
    (final String original)\n
    (final String host, final int port, final String path)\n
    (final String host, final int port, final String path, final String query)\n
    (final String user, final String password, final String host)\n
    (final String user, final String password, final String host, final int port)\n
    (final String user, final String password, final String host, final int port, final String path)\n
    (final String user, final String password, final String host, final int port, final String path, final String query)\n
    (final String host, final String path, final String query, final String fragment)\n
    (final String userinfo, final String host, final String path, final String query, final String fragment)\n
    (final String userinfo, final String host, final int port, final String path)\n
    (final String userinfo, final String host, final int port, final String path, final String query)\n
    (final String userinfo, final String host, final int port, final String path, final String query, final String fragment)\n
    (final String user, final String password, final String host, final int port, final String path, final String query, final String fragment)\n
    (final HttpURL base, final String relative)\n
    (final HttpURL base, final HttpURL relative)\n
    '''
def getRawScheme():
    '''returns char[]\n\n
    getRawScheme()\n
    '''
def getScheme():
    '''returns String\n\n
    getScheme()\n
    '''
def getPort():
    '''returns int\n\n
    getPort()\n
    '''
def setRawUserinfo():
    '''returns None\n\n
    setRawUserinfo(final char[] escapedUser, final char[] escapedPassword)\n
    '''
def setEscapedUserinfo():
    '''returns None\n\n
    setEscapedUserinfo(final String escapedUser, final String escapedPassword)\n
    '''
def setUserinfo():
    '''returns None\n\n
    setUserinfo(final String user, final String password)\n
    '''
def setRawUser():
    '''returns None\n\n
    setRawUser(final char[] escapedUser)\n
    '''
def setEscapedUser():
    '''returns None\n\n
    setEscapedUser(final String escapedUser)\n
    '''
def setUser():
    '''returns None\n\n
    setUser(final String user)\n
    '''
def getRawUser():
    '''returns char[]\n\n
    getRawUser()\n
    '''
def getEscapedUser():
    '''returns String\n\n
    getEscapedUser()\n
    '''
def getUser():
    '''returns String\n\n
    getUser()\n
    '''
def setRawPassword():
    '''returns None\n\n
    setRawPassword(final char[] escapedPassword)\n
    '''
def setEscapedPassword():
    '''returns None\n\n
    setEscapedPassword(final String escapedPassword)\n
    '''
def setPassword():
    '''returns None\n\n
    setPassword(final String password)\n
    '''
def getRawPassword():
    '''returns char[]\n\n
    getRawPassword()\n
    '''
def getEscapedPassword():
    '''returns String\n\n
    getEscapedPassword()\n
    '''
def getPassword():
    '''returns String\n\n
    getPassword()\n
    '''
def getRawCurrentHierPath():
    '''returns char[]\n\n
    getRawCurrentHierPath()\n
    '''
def getRawAboveHierPath():
    '''returns char[]\n\n
    getRawAboveHierPath()\n
    '''
def getRawPath():
    '''returns char[]\n\n
    getRawPath()\n
    '''
def setQuery():
    '''returns None\n\n
    setQuery(final String queryName, final String queryValue)\n
    setQuery(final String[] queryName, final String[] queryValue)\n
    '''
