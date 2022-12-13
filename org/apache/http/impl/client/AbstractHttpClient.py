def getParams():
'''public final synchronized HttpParams getParams()
'''
pass
def setParams():
'''public synchronized void setParams(final HttpParams params)
'''
pass
def getConnectionManager():
'''public final synchronized ClientConnectionManager getConnectionManager()
'''
pass
def getRequestExecutor():
'''public final synchronized HttpRequestExecutor getRequestExecutor()
'''
pass
def getAuthSchemes():
'''public final synchronized AuthSchemeRegistry getAuthSchemes()
'''
pass
def setAuthSchemes():
'''public synchronized void setAuthSchemes(final AuthSchemeRegistry registry)
'''
pass
def getConnectionBackoffStrategy():
'''public final synchronized ConnectionBackoffStrategy getConnectionBackoffStrategy()
'''
pass
def setConnectionBackoffStrategy():
'''public synchronized void setConnectionBackoffStrategy(final ConnectionBackoffStrategy strategy)
'''
pass
def getCookieSpecs():
'''public final synchronized CookieSpecRegistry getCookieSpecs()
'''
pass
def getBackoffManager():
'''public final synchronized BackoffManager getBackoffManager()
'''
pass
def setBackoffManager():
'''public synchronized void setBackoffManager(final BackoffManager manager)
'''
pass
def setCookieSpecs():
'''public synchronized void setCookieSpecs(final CookieSpecRegistry registry)
'''
pass
def getConnectionReuseStrategy():
'''public final synchronized ConnectionReuseStrategy getConnectionReuseStrategy()
'''
pass
def setReuseStrategy():
'''public synchronized void setReuseStrategy(final ConnectionReuseStrategy strategy)
'''
pass
def getConnectionKeepAliveStrategy():
'''public final synchronized ConnectionKeepAliveStrategy getConnectionKeepAliveStrategy()
'''
pass
def setKeepAliveStrategy():
'''public synchronized void setKeepAliveStrategy(final ConnectionKeepAliveStrategy strategy)
'''
pass
def getHttpRequestRetryHandler():
'''public final synchronized HttpRequestRetryHandler getHttpRequestRetryHandler()
'''
pass
def setHttpRequestRetryHandler():
'''public synchronized void setHttpRequestRetryHandler(final HttpRequestRetryHandler handler)
'''
pass
def getRedirectHandler():
'''public final synchronized RedirectHandler getRedirectHandler()
'''
pass
def setRedirectHandler():
'''public synchronized void setRedirectHandler(final RedirectHandler handler)
'''
pass
def getRedirectStrategy():
'''public final synchronized RedirectStrategy getRedirectStrategy()
'''
pass
def setRedirectStrategy():
'''public synchronized void setRedirectStrategy(final RedirectStrategy strategy)
'''
pass
def getTargetAuthenticationHandler():
'''public final synchronized AuthenticationHandler getTargetAuthenticationHandler()
'''
pass
def setTargetAuthenticationHandler():
'''public synchronized void setTargetAuthenticationHandler(final AuthenticationHandler handler)
'''
pass
def getTargetAuthenticationStrategy():
'''public final synchronized AuthenticationStrategy getTargetAuthenticationStrategy()
'''
pass
def setTargetAuthenticationStrategy():
'''public synchronized void setTargetAuthenticationStrategy(final AuthenticationStrategy strategy)
'''
pass
def getProxyAuthenticationHandler():
'''public final synchronized AuthenticationHandler getProxyAuthenticationHandler()
'''
pass
def setProxyAuthenticationHandler():
'''public synchronized void setProxyAuthenticationHandler(final AuthenticationHandler handler)
'''
pass
def getProxyAuthenticationStrategy():
'''public final synchronized AuthenticationStrategy getProxyAuthenticationStrategy()
'''
pass
def setProxyAuthenticationStrategy():
'''public synchronized void setProxyAuthenticationStrategy(final AuthenticationStrategy strategy)
'''
pass
def getCookieStore():
'''public final synchronized CookieStore getCookieStore()
'''
pass
def setCookieStore():
'''public synchronized void setCookieStore(final CookieStore cookieStore)
'''
pass
def getCredentialsProvider():
'''public final synchronized CredentialsProvider getCredentialsProvider()
'''
pass
def setCredentialsProvider():
'''public synchronized void setCredentialsProvider(final CredentialsProvider credsProvider)
'''
pass
def getRoutePlanner():
'''public final synchronized HttpRoutePlanner getRoutePlanner()
'''
pass
def setRoutePlanner():
'''public synchronized void setRoutePlanner(final HttpRoutePlanner routePlanner)
'''
pass
def getUserTokenHandler():
'''public final synchronized UserTokenHandler getUserTokenHandler()
'''
pass
def setUserTokenHandler():
'''public synchronized void setUserTokenHandler(final UserTokenHandler handler)
'''
pass
def getResponseInterceptorCount():
'''public synchronized int getResponseInterceptorCount()
'''
pass
def getResponseInterceptor():
'''public synchronized HttpResponseInterceptor getResponseInterceptor(final int index)
'''
pass
def getRequestInterceptor():
'''public synchronized HttpRequestInterceptor getRequestInterceptor(final int index)
'''
pass
def getRequestInterceptorCount():
'''public synchronized int getRequestInterceptorCount()
'''
pass
def addResponseInterceptor():
'''public synchronized void addResponseInterceptor(final HttpResponseInterceptor itcp)
public synchronized void addResponseInterceptor(final HttpResponseInterceptor itcp, final int index)
'''
pass
def clearResponseInterceptors():
'''public synchronized void clearResponseInterceptors()
'''
pass
def removeResponseInterceptorByClass():
'''public synchronized void removeResponseInterceptorByClass(final Class<? extends HttpResponseInterceptor> clazz)
'''
pass
def addRequestInterceptor():
'''public synchronized void addRequestInterceptor(final HttpRequestInterceptor itcp)
public synchronized void addRequestInterceptor(final HttpRequestInterceptor itcp, final int index)
'''
pass
def clearRequestInterceptors():
'''public synchronized void clearRequestInterceptors()
'''
pass
def removeRequestInterceptorByClass():
'''public synchronized void removeRequestInterceptorByClass(final Class<? extends HttpRequestInterceptor> clazz)
'''
pass
def close():
'''public void close()
'''
pass
