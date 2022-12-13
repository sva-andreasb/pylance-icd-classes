HTTP_ROUTE = "String  http.route""
REDIRECT_LOCATIONS = "String  http.protocol.redirect-locations""
COOKIESPEC_REGISTRY = "String  http.cookiespec-registry""
COOKIE_SPEC = "String  http.cookie-spec""
COOKIE_ORIGIN = "String  http.cookie-origin""
COOKIE_STORE = "String  http.cookie-store""
CREDS_PROVIDER = "String  http.auth.credentials-provider""
AUTH_CACHE = "String  http.auth.auth-cache""
TARGET_AUTH_STATE = "String  http.auth.target-scope""
PROXY_AUTH_STATE = "String  http.auth.proxy-scope""
USER_TOKEN = "String  http.user-token""
AUTHSCHEME_REGISTRY = "String  http.authscheme-registry""
REQUEST_CONFIG = "String  http.request-config""
def adapt():
'''public static HttpClientContext adapt(final HttpContext context)
'''
pass
def create():
'''public static HttpClientContext create()
'''
pass
def HttpClientContext():
'''public HttpClientContext(final HttpContext context)
public HttpClientContext()
'''
pass
def getHttpRoute():
'''public RouteInfo getHttpRoute()
'''
pass
def getRedirectLocations():
'''public List<URI> getRedirectLocations()
'''
pass
def getCookieStore():
'''public CookieStore getCookieStore()
'''
pass
def setCookieStore():
'''public void setCookieStore(final CookieStore cookieStore)
'''
pass
def getCookieSpec():
'''public CookieSpec getCookieSpec()
'''
pass
def getCookieOrigin():
'''public CookieOrigin getCookieOrigin()
'''
pass
def getCookieSpecRegistry():
'''public Lookup<CookieSpecProvider> getCookieSpecRegistry()
'''
pass
def setCookieSpecRegistry():
'''public void setCookieSpecRegistry(final Lookup<CookieSpecProvider> lookup)
'''
pass
def getAuthSchemeRegistry():
'''public Lookup<AuthSchemeProvider> getAuthSchemeRegistry()
'''
pass
def setAuthSchemeRegistry():
'''public void setAuthSchemeRegistry(final Lookup<AuthSchemeProvider> lookup)
'''
pass
def getCredentialsProvider():
'''public CredentialsProvider getCredentialsProvider()
'''
pass
def setCredentialsProvider():
'''public void setCredentialsProvider(final CredentialsProvider credentialsProvider)
'''
pass
def getAuthCache():
'''public AuthCache getAuthCache()
'''
pass
def setAuthCache():
'''public void setAuthCache(final AuthCache authCache)
'''
pass
def getTargetAuthState():
'''public AuthState getTargetAuthState()
'''
pass
def getProxyAuthState():
'''public AuthState getProxyAuthState()
'''
pass
def getUserToken():
'''public <T> T getUserToken(final Class<T> clazz)
public Object getUserToken()
'''
pass
def setUserToken():
'''public void setUserToken(final Object obj)
'''
pass
def getRequestConfig():
'''public RequestConfig getRequestConfig()
'''
pass
def setRequestConfig():
'''public void setRequestConfig(final RequestConfig config)
'''
pass
