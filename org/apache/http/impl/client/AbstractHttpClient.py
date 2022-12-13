def getParams():
    '''    public final synchronized HttpParams getParams()
    '''
def setParams():
    '''    public synchronized void setParams(final HttpParams params)
    '''
def getConnectionManager():
    '''    public final synchronized ClientConnectionManager getConnectionManager()
    '''
def getRequestExecutor():
    '''    public final synchronized HttpRequestExecutor getRequestExecutor()
    '''
def getAuthSchemes():
    '''    public final synchronized AuthSchemeRegistry getAuthSchemes()
    '''
def setAuthSchemes():
    '''    public synchronized void setAuthSchemes(final AuthSchemeRegistry registry)
    '''
def getConnectionBackoffStrategy():
    '''    public final synchronized ConnectionBackoffStrategy getConnectionBackoffStrategy()
    '''
def setConnectionBackoffStrategy():
    '''    public synchronized void setConnectionBackoffStrategy(final ConnectionBackoffStrategy strategy)
    '''
def getCookieSpecs():
    '''    public final synchronized CookieSpecRegistry getCookieSpecs()
    '''
def getBackoffManager():
    '''    public final synchronized BackoffManager getBackoffManager()
    '''
def setBackoffManager():
    '''    public synchronized void setBackoffManager(final BackoffManager manager)
    '''
def setCookieSpecs():
    '''    public synchronized void setCookieSpecs(final CookieSpecRegistry registry)
    '''
def getConnectionReuseStrategy():
    '''    public final synchronized ConnectionReuseStrategy getConnectionReuseStrategy()
    '''
def setReuseStrategy():
    '''    public synchronized void setReuseStrategy(final ConnectionReuseStrategy strategy)
    '''
def getConnectionKeepAliveStrategy():
    '''    public final synchronized ConnectionKeepAliveStrategy getConnectionKeepAliveStrategy()
    '''
def setKeepAliveStrategy():
    '''    public synchronized void setKeepAliveStrategy(final ConnectionKeepAliveStrategy strategy)
    '''
def getHttpRequestRetryHandler():
    '''    public final synchronized HttpRequestRetryHandler getHttpRequestRetryHandler()
    '''
def setHttpRequestRetryHandler():
    '''    public synchronized void setHttpRequestRetryHandler(final HttpRequestRetryHandler handler)
    '''
def getRedirectHandler():
    '''    public final synchronized RedirectHandler getRedirectHandler()
    '''
def setRedirectHandler():
    '''    public synchronized void setRedirectHandler(final RedirectHandler handler)
    '''
def getRedirectStrategy():
    '''    public final synchronized RedirectStrategy getRedirectStrategy()
    '''
def setRedirectStrategy():
    '''    public synchronized void setRedirectStrategy(final RedirectStrategy strategy)
    '''
def getTargetAuthenticationHandler():
    '''    public final synchronized AuthenticationHandler getTargetAuthenticationHandler()
    '''
def setTargetAuthenticationHandler():
    '''    public synchronized void setTargetAuthenticationHandler(final AuthenticationHandler handler)
    '''
def getTargetAuthenticationStrategy():
    '''    public final synchronized AuthenticationStrategy getTargetAuthenticationStrategy()
    '''
def setTargetAuthenticationStrategy():
    '''    public synchronized void setTargetAuthenticationStrategy(final AuthenticationStrategy strategy)
    '''
def getProxyAuthenticationHandler():
    '''    public final synchronized AuthenticationHandler getProxyAuthenticationHandler()
    '''
def setProxyAuthenticationHandler():
    '''    public synchronized void setProxyAuthenticationHandler(final AuthenticationHandler handler)
    '''
def getProxyAuthenticationStrategy():
    '''    public final synchronized AuthenticationStrategy getProxyAuthenticationStrategy()
    '''
def setProxyAuthenticationStrategy():
    '''    public synchronized void setProxyAuthenticationStrategy(final AuthenticationStrategy strategy)
    '''
def getCookieStore():
    '''    public final synchronized CookieStore getCookieStore()
    '''
def setCookieStore():
    '''    public synchronized void setCookieStore(final CookieStore cookieStore)
    '''
def getCredentialsProvider():
    '''    public final synchronized CredentialsProvider getCredentialsProvider()
    '''
def setCredentialsProvider():
    '''    public synchronized void setCredentialsProvider(final CredentialsProvider credsProvider)
    '''
def getRoutePlanner():
    '''    public final synchronized HttpRoutePlanner getRoutePlanner()
    '''
def setRoutePlanner():
    '''    public synchronized void setRoutePlanner(final HttpRoutePlanner routePlanner)
    '''
def getUserTokenHandler():
    '''    public final synchronized UserTokenHandler getUserTokenHandler()
    '''
def setUserTokenHandler():
    '''    public synchronized void setUserTokenHandler(final UserTokenHandler handler)
    '''
def getResponseInterceptorCount():
    '''    public synchronized int getResponseInterceptorCount()
    '''
def getResponseInterceptor():
    '''    public synchronized HttpResponseInterceptor getResponseInterceptor(final int index)
    '''
def getRequestInterceptor():
    '''    public synchronized HttpRequestInterceptor getRequestInterceptor(final int index)
    '''
def getRequestInterceptorCount():
    '''    public synchronized int getRequestInterceptorCount()
    '''
def addResponseInterceptor():
    '''    public synchronized void addResponseInterceptor(final HttpResponseInterceptor itcp)
    public synchronized void addResponseInterceptor(final HttpResponseInterceptor itcp, final int index)
    '''
def clearResponseInterceptors():
    '''    public synchronized void clearResponseInterceptors()
    '''
def removeResponseInterceptorByClass():
    '''    public synchronized void removeResponseInterceptorByClass(final Class<? extends HttpResponseInterceptor> clazz)
    '''
def addRequestInterceptor():
    '''    public synchronized void addRequestInterceptor(final HttpRequestInterceptor itcp)
    public synchronized void addRequestInterceptor(final HttpRequestInterceptor itcp, final int index)
    '''
def clearRequestInterceptors():
    '''    public synchronized void clearRequestInterceptors()
    '''
def removeRequestInterceptorByClass():
    '''    public synchronized void removeRequestInterceptorByClass(final Class<? extends HttpRequestInterceptor> clazz)
    '''
def close():
    '''    public void close()
    '''
