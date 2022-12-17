UNKNOWN = "int  0"
PROTOCOL_CHARSET = "int  1"
DOCUMENT_CHARSET = "int  2"
def ():
    '''returns DefaultCharsetChanged\n\n
    (final String s, final boolean escaped, final String charset)\n
    (final String s, final boolean escaped)\n
    (final char[] escaped, final String charset)\n
    (final char[] escaped)\n
    (final String original, final String charset)\n
    (final String original)\n
    (final String scheme, final String schemeSpecificPart, final String fragment)\n
    (final String scheme, final String authority, final String path, final String query, final String fragment)\n
    (final String scheme, final String userinfo, final String host, final int port)\n
    (final String scheme, final String userinfo, final String host, final int port, final String path)\n
    (final String scheme, final String userinfo, final String host, final int port, final String path, final String query)\n
    (final String scheme, final String userinfo, final String host, final int port, final String path, final String query, final String fragment)\n
    (final String scheme, final String host, final String path, final String fragment)\n
    (final URI base, final String relative)\n
    (final URI base, final String relative, final boolean escaped)\n
    (final URI base, final URI relative)\n
    (final int reasonCode, final String reason)\n
    '''
def isAbsoluteURI():
    '''returns boolean\n\n
    isAbsoluteURI()\n
    '''
def isRelativeURI():
    '''returns boolean\n\n
    isRelativeURI()\n
    '''
def isHierPart():
    '''returns boolean\n\n
    isHierPart()\n
    '''
def isOpaquePart():
    '''returns boolean\n\n
    isOpaquePart()\n
    '''
def isNetPath():
    '''returns boolean\n\n
    isNetPath()\n
    '''
def isAbsPath():
    '''returns boolean\n\n
    isAbsPath()\n
    '''
def isRelPath():
    '''returns boolean\n\n
    isRelPath()\n
    '''
def hasAuthority():
    '''returns boolean\n\n
    hasAuthority()\n
    '''
def isRegName():
    '''returns boolean\n\n
    isRegName()\n
    '''
def isServer():
    '''returns boolean\n\n
    isServer()\n
    '''
def hasUserinfo():
    '''returns boolean\n\n
    hasUserinfo()\n
    '''
def isHostname():
    '''returns boolean\n\n
    isHostname()\n
    '''
def isIPv4address():
    '''returns boolean\n\n
    isIPv4address()\n
    '''
def isIPv6reference():
    '''returns boolean\n\n
    isIPv6reference()\n
    '''
def hasQuery():
    '''returns boolean\n\n
    hasQuery()\n
    '''
def hasFragment():
    '''returns boolean\n\n
    hasFragment()\n
    '''
def getProtocolCharset():
    '''returns String\n\n
    getProtocolCharset()\n
    '''
def getRawScheme():
    '''returns char[]\n\n
    getRawScheme()\n
    '''
def getScheme():
    '''returns String\n\n
    getScheme()\n
    '''
def setRawAuthority():
    '''returns None\n\n
    setRawAuthority(final char[] escapedAuthority)\n
    '''
def setEscapedAuthority():
    '''returns None\n\n
    setEscapedAuthority(final String escapedAuthority)\n
    '''
def getRawAuthority():
    '''returns char[]\n\n
    getRawAuthority()\n
    '''
def getEscapedAuthority():
    '''returns String\n\n
    getEscapedAuthority()\n
    '''
def getAuthority():
    '''returns String\n\n
    getAuthority()\n
    '''
def getRawUserinfo():
    '''returns char[]\n\n
    getRawUserinfo()\n
    '''
def getEscapedUserinfo():
    '''returns String\n\n
    getEscapedUserinfo()\n
    '''
def getUserinfo():
    '''returns String\n\n
    getUserinfo()\n
    '''
def getRawHost():
    '''returns char[]\n\n
    getRawHost()\n
    '''
def getHost():
    '''returns String\n\n
    getHost()\n
    '''
def getPort():
    '''returns int\n\n
    getPort()\n
    '''
def setRawPath():
    '''returns None\n\n
    setRawPath(char[] escapedPath)\n
    '''
def setEscapedPath():
    '''returns None\n\n
    setEscapedPath(final String escapedPath)\n
    '''
def setPath():
    '''returns None\n\n
    setPath(final String path)\n
    '''
def getRawCurrentHierPath():
    '''returns char[]\n\n
    getRawCurrentHierPath()\n
    '''
def getEscapedCurrentHierPath():
    '''returns String\n\n
    getEscapedCurrentHierPath()\n
    '''
def getCurrentHierPath():
    '''returns String\n\n
    getCurrentHierPath()\n
    '''
def getRawAboveHierPath():
    '''returns char[]\n\n
    getRawAboveHierPath()\n
    '''
def getEscapedAboveHierPath():
    '''returns String\n\n
    getEscapedAboveHierPath()\n
    '''
def getAboveHierPath():
    '''returns String\n\n
    getAboveHierPath()\n
    '''
def getRawPath():
    '''returns char[]\n\n
    getRawPath()\n
    '''
def getEscapedPath():
    '''returns String\n\n
    getEscapedPath()\n
    '''
def getPath():
    '''returns String\n\n
    getPath()\n
    '''
def getRawName():
    '''returns char[]\n\n
    getRawName()\n
    '''
def getEscapedName():
    '''returns String\n\n
    getEscapedName()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getRawPathQuery():
    '''returns char[]\n\n
    getRawPathQuery()\n
    '''
def getEscapedPathQuery():
    '''returns String\n\n
    getEscapedPathQuery()\n
    '''
def getPathQuery():
    '''returns String\n\n
    getPathQuery()\n
    '''
def setRawQuery():
    '''returns None\n\n
    setRawQuery(char[] escapedQuery)\n
    '''
def setEscapedQuery():
    '''returns None\n\n
    setEscapedQuery(final String escapedQuery)\n
    '''
def setQuery():
    '''returns None\n\n
    setQuery(final String query)\n
    '''
def getRawQuery():
    '''returns char[]\n\n
    getRawQuery()\n
    '''
def getEscapedQuery():
    '''returns String\n\n
    getEscapedQuery()\n
    '''
def getQuery():
    '''returns String\n\n
    getQuery()\n
    '''
def setRawFragment():
    '''returns None\n\n
    setRawFragment(final char[] escapedFragment)\n
    '''
def setEscapedFragment():
    '''returns None\n\n
    setEscapedFragment(final String escapedFragment)\n
    '''
def setFragment():
    '''returns None\n\n
    setFragment(final String fragment)\n
    '''
def getRawFragment():
    '''returns char[]\n\n
    getRawFragment()\n
    '''
def getEscapedFragment():
    '''returns String\n\n
    getEscapedFragment()\n
    '''
def getFragment():
    '''returns String\n\n
    getFragment()\n
    '''
def normalize():
    '''returns None\n\n
    normalize()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Object obj)\n
    '''
def getRawURI():
    '''returns char[]\n\n
    getRawURI()\n
    '''
def getEscapedURI():
    '''returns String\n\n
    getEscapedURI()\n
    '''
def getURI():
    '''returns String\n\n
    getURI()\n
    '''
def getRawURIReference():
    '''returns char[]\n\n
    getRawURIReference()\n
    '''
def getEscapedURIReference():
    '''returns String\n\n
    getEscapedURIReference()\n
    '''
def getURIReference():
    '''returns String\n\n
    getURIReference()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getReasonCode():
    '''returns int\n\n
    getReasonCode()\n
    '''
def getReason():
    '''returns String\n\n
    getReason()\n
    '''
