def ():
    '''returns MalformedURIException\n\n
    ()\n
    (final URI p_other)\n
    (final String p_uriSpec)\n
    (final String p_uriSpec, final boolean allowNonAbsoluteURI)\n
    (final URI p_base, final String p_uriSpec)\n
    (final URI p_base, final String p_uriSpec, final boolean allowNonAbsoluteURI)\n
    (final String p_scheme, final String p_schemeSpecificPart)\n
    (final String p_scheme, final String p_host, final String p_path, final String p_queryString, final String p_fragment)\n
    (final String p_scheme, final String p_userinfo, final String p_host, final int p_port, final String p_path, final String p_queryString, final String p_fragment)\n
    ()\n
    (final String p_msg)\n
    '''
def absolutize():
    '''returns None\n\n
    absolutize(final URI p_base)\n
    '''
def getScheme():
    '''returns String\n\n
    getScheme()\n
    '''
def getSchemeSpecificPart():
    '''returns String\n\n
    getSchemeSpecificPart()\n
    '''
def getUserinfo():
    '''returns String\n\n
    getUserinfo()\n
    '''
def getHost():
    '''returns String\n\n
    getHost()\n
    '''
def getPort():
    '''returns int\n\n
    getPort()\n
    '''
def getRegBasedAuthority():
    '''returns String\n\n
    getRegBasedAuthority()\n
    '''
def getPath():
    '''returns String\n\n
    getPath(final boolean p_includeQueryString, final boolean p_includeFragment)\n
    getPath()\n
    '''
def getQueryString():
    '''returns String\n\n
    getQueryString()\n
    '''
def getFragment():
    '''returns String\n\n
    getFragment()\n
    '''
def setScheme():
    '''returns None\n\n
    setScheme(final String p_scheme)\n
    '''
def setUserinfo():
    '''returns None\n\n
    setUserinfo(final String p_userinfo)\n
    '''
def setHost():
    '''returns None\n\n
    setHost(final String p_host)\n
    '''
def setPort():
    '''returns None\n\n
    setPort(final int p_port)\n
    '''
def setRegBasedAuthority():
    '''returns None\n\n
    setRegBasedAuthority(final String authority)\n
    '''
def setPath():
    '''returns None\n\n
    setPath(final String p_path)\n
    '''
def appendPath():
    '''returns None\n\n
    appendPath(final String p_addToPath)\n
    '''
def setQueryString():
    '''returns None\n\n
    setQueryString(final String p_queryString)\n
    '''
def setFragment():
    '''returns None\n\n
    setFragment(final String p_fragment)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object p_test)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def isGenericURI():
    '''returns boolean\n\n
    isGenericURI()\n
    '''
def isAbsoluteURI():
    '''returns boolean\n\n
    isAbsoluteURI()\n
    '''
