AUTH_SCHEME_PRIORITY = "String  \"http.auth.scheme-priority\""
NTLM = "String  \"NTLM\""
DIGEST = "String  \"Digest\""
BASIC = "String  \"Basic\""
def registerAuthScheme():
    '''    public static synchronized void registerAuthScheme(final String id, final Class clazz)
    '''
def unregisterAuthScheme():
    '''    public static synchronized void unregisterAuthScheme(final String id)
    '''
def getAuthScheme():
    '''    public static synchronized AuthScheme getAuthScheme(final String id)
    '''
def getDefaultAuthPrefs():
    '''    public static synchronized List getDefaultAuthPrefs()
    '''
