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
def adapt():
    '''    public static HttpClientContext adapt(final HttpContext context)
    '''
def create():
    '''    public static HttpClientContext create()
    '''
def HttpClientContext():
    '''    public HttpClientContext(final HttpContext context)
    public HttpClientContext()
    '''
def getHttpRoute():
    '''    public RouteInfo getHttpRoute()
    '''
def getRedirectLocations():
    '''    public List<URI> getRedirectLocations()
    '''
def getCookieStore():
    '''    public CookieStore getCookieStore()
    '''
def setCookieStore():
    '''    public void setCookieStore(final CookieStore cookieStore)
    '''
def getCookieSpec():
    '''    public CookieSpec getCookieSpec()
    '''
def getCookieOrigin():
    '''    public CookieOrigin getCookieOrigin()
    '''
def getCookieSpecRegistry():
    '''    public Lookup<CookieSpecProvider> getCookieSpecRegistry()
    '''
def setCookieSpecRegistry():
    '''    public void setCookieSpecRegistry(final Lookup<CookieSpecProvider> lookup)
    '''
def getAuthSchemeRegistry():
    '''    public Lookup<AuthSchemeProvider> getAuthSchemeRegistry()
    '''
def setAuthSchemeRegistry():
    '''    public void setAuthSchemeRegistry(final Lookup<AuthSchemeProvider> lookup)
    '''
def getCredentialsProvider():
    '''    public CredentialsProvider getCredentialsProvider()
    '''
def setCredentialsProvider():
    '''    public void setCredentialsProvider(final CredentialsProvider credentialsProvider)
    '''
def getAuthCache():
    '''    public AuthCache getAuthCache()
    '''
def setAuthCache():
    '''    public void setAuthCache(final AuthCache authCache)
    '''
def getTargetAuthState():
    '''    public AuthState getTargetAuthState()
    '''
def getProxyAuthState():
    '''    public AuthState getProxyAuthState()
    '''
def getUserToken():
    '''    public <T> T getUserToken(final Class<T> clazz)
    public Object getUserToken()
    '''
def setUserToken():
    '''    public void setUserToken(final Object obj)
    '''
def getRequestConfig():
    '''    public RequestConfig getRequestConfig()
    '''
def setRequestConfig():
    '''    public void setRequestConfig(final RequestConfig config)
    '''
