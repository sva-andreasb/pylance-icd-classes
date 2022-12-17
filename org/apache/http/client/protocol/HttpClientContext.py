HTTP_ROUTE = "String  \"http.route\""
REDIRECT_LOCATIONS = "String  \"http.protocol.redirect-locations\""
COOKIESPEC_REGISTRY = "String  \"http.cookiespec-registry\""
COOKIE_SPEC = "String  \"http.cookie-spec\""
COOKIE_ORIGIN = "String  \"http.cookie-origin\""
COOKIE_STORE = "String  \"http.cookie-store\""
CREDS_PROVIDER = "String  \"http.auth.credentials-provider\""
AUTH_CACHE = "String  \"http.auth.auth-cache\""
TARGET_AUTH_STATE = "String  \"http.auth.target-scope\""
PROXY_AUTH_STATE = "String  \"http.auth.proxy-scope\""
USER_TOKEN = "String  \"http.user-token\""
AUTHSCHEME_REGISTRY = "String  \"http.authscheme-registry\""
REQUEST_CONFIG = "String  \"http.request-config\""
def ():
    '''returns HttpClientContext\n\n
    (final HttpContext context)\n
    ()\n
    '''
def getHttpRoute():
    '''returns RouteInfo\n\n
    getHttpRoute()\n
    '''
def getRedirectLocations():
    '''returns List<URI>\n\n
    getRedirectLocations()\n
    '''
def getCookieStore():
    '''returns CookieStore\n\n
    getCookieStore()\n
    '''
def setCookieStore():
    '''returns None\n\n
    setCookieStore(final CookieStore cookieStore)\n
    '''
def getCookieSpec():
    '''returns CookieSpec\n\n
    getCookieSpec()\n
    '''
def getCookieOrigin():
    '''returns CookieOrigin\n\n
    getCookieOrigin()\n
    '''
def getCookieSpecRegistry():
    '''returns Lookup<CookieSpecProvider>\n\n
    getCookieSpecRegistry()\n
    '''
def setCookieSpecRegistry():
    '''returns None\n\n
    setCookieSpecRegistry(final Lookup<CookieSpecProvider> lookup)\n
    '''
def getAuthSchemeRegistry():
    '''returns Lookup<AuthSchemeProvider>\n\n
    getAuthSchemeRegistry()\n
    '''
def setAuthSchemeRegistry():
    '''returns None\n\n
    setAuthSchemeRegistry(final Lookup<AuthSchemeProvider> lookup)\n
    '''
def getCredentialsProvider():
    '''returns CredentialsProvider\n\n
    getCredentialsProvider()\n
    '''
def setCredentialsProvider():
    '''returns None\n\n
    setCredentialsProvider(final CredentialsProvider credentialsProvider)\n
    '''
def getAuthCache():
    '''returns AuthCache\n\n
    getAuthCache()\n
    '''
def setAuthCache():
    '''returns None\n\n
    setAuthCache(final AuthCache authCache)\n
    '''
def getTargetAuthState():
    '''returns AuthState\n\n
    getTargetAuthState()\n
    '''
def getProxyAuthState():
    '''returns AuthState\n\n
    getProxyAuthState()\n
    '''
def getUserToken():
    '''returns Object\n\n
    getUserToken()\n
    '''
def setUserToken():
    '''returns None\n\n
    setUserToken(final Object obj)\n
    '''
def getRequestConfig():
    '''returns RequestConfig\n\n
    getRequestConfig()\n
    '''
def setRequestConfig():
    '''returns None\n\n
    setRequestConfig(final RequestConfig config)\n
    '''
