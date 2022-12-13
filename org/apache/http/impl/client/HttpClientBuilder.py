def create():
'''public static HttpClientBuilder create()
'''
pass
def setRequestExecutor():
'''public final HttpClientBuilder setRequestExecutor(final HttpRequestExecutor requestExec)
'''
pass
def setHostnameVerifier():
'''public final HttpClientBuilder setHostnameVerifier(final X509HostnameVerifier hostnameVerifier)
'''
pass
def setSSLHostnameVerifier():
'''public final HttpClientBuilder setSSLHostnameVerifier(final HostnameVerifier hostnameVerifier)
'''
pass
def setPublicSuffixMatcher():
'''public final HttpClientBuilder setPublicSuffixMatcher(final PublicSuffixMatcher publicSuffixMatcher)
'''
pass
def setSslcontext():
'''public final HttpClientBuilder setSslcontext(final SSLContext sslcontext)
'''
pass
def setSSLContext():
'''public final HttpClientBuilder setSSLContext(final SSLContext sslContext)
'''
pass
def setSSLSocketFactory():
'''public final HttpClientBuilder setSSLSocketFactory(final LayeredConnectionSocketFactory sslSocketFactory)
'''
pass
def setMaxConnTotal():
'''public final HttpClientBuilder setMaxConnTotal(final int maxConnTotal)
'''
pass
def setMaxConnPerRoute():
'''public final HttpClientBuilder setMaxConnPerRoute(final int maxConnPerRoute)
'''
pass
def setDefaultSocketConfig():
'''public final HttpClientBuilder setDefaultSocketConfig(final SocketConfig config)
'''
pass
def setDefaultConnectionConfig():
'''public final HttpClientBuilder setDefaultConnectionConfig(final ConnectionConfig config)
'''
pass
def setConnectionTimeToLive():
'''public final HttpClientBuilder setConnectionTimeToLive(final long connTimeToLive, final TimeUnit connTimeToLiveTimeUnit)
'''
pass
def setConnectionManager():
'''public final HttpClientBuilder setConnectionManager(final HttpClientConnectionManager connManager)
'''
pass
def setConnectionManagerShared():
'''public final HttpClientBuilder setConnectionManagerShared(final boolean shared)
'''
pass
def setConnectionReuseStrategy():
'''public final HttpClientBuilder setConnectionReuseStrategy(final ConnectionReuseStrategy reuseStrategy)
'''
pass
def setKeepAliveStrategy():
'''public final HttpClientBuilder setKeepAliveStrategy(final ConnectionKeepAliveStrategy keepAliveStrategy)
'''
pass
def setTargetAuthenticationStrategy():
'''public final HttpClientBuilder setTargetAuthenticationStrategy(final AuthenticationStrategy targetAuthStrategy)
'''
pass
def setProxyAuthenticationStrategy():
'''public final HttpClientBuilder setProxyAuthenticationStrategy(final AuthenticationStrategy proxyAuthStrategy)
'''
pass
def setUserTokenHandler():
'''public final HttpClientBuilder setUserTokenHandler(final UserTokenHandler userTokenHandler)
'''
pass
def disableConnectionState():
'''public final HttpClientBuilder disableConnectionState()
'''
pass
def setSchemePortResolver():
'''public final HttpClientBuilder setSchemePortResolver(final SchemePortResolver schemePortResolver)
'''
pass
def setUserAgent():
'''public final HttpClientBuilder setUserAgent(final String userAgent)
'''
pass
def setDefaultHeaders():
'''public final HttpClientBuilder setDefaultHeaders(final Collection<? extends Header> defaultHeaders)
'''
pass
def addInterceptorFirst():
'''public final HttpClientBuilder addInterceptorFirst(final HttpResponseInterceptor itcp)
public final HttpClientBuilder addInterceptorFirst(final HttpRequestInterceptor itcp)
'''
pass
def addInterceptorLast():
'''public final HttpClientBuilder addInterceptorLast(final HttpResponseInterceptor itcp)
public final HttpClientBuilder addInterceptorLast(final HttpRequestInterceptor itcp)
'''
pass
def disableCookieManagement():
'''public final HttpClientBuilder disableCookieManagement()
'''
pass
def disableContentCompression():
'''public final HttpClientBuilder disableContentCompression()
'''
pass
def disableAuthCaching():
'''public final HttpClientBuilder disableAuthCaching()
'''
pass
def setHttpProcessor():
'''public final HttpClientBuilder setHttpProcessor(final HttpProcessor httpprocessor)
'''
pass
def setDnsResolver():
'''public final HttpClientBuilder setDnsResolver(final DnsResolver dnsResolver)
'''
pass
def setRetryHandler():
'''public final HttpClientBuilder setRetryHandler(final HttpRequestRetryHandler retryHandler)
'''
pass
def disableAutomaticRetries():
'''public final HttpClientBuilder disableAutomaticRetries()
'''
pass
def setProxy():
'''public final HttpClientBuilder setProxy(final HttpHost proxy)
'''
pass
def setRoutePlanner():
'''public final HttpClientBuilder setRoutePlanner(final HttpRoutePlanner routePlanner)
'''
pass
def setRedirectStrategy():
'''public final HttpClientBuilder setRedirectStrategy(final RedirectStrategy redirectStrategy)
'''
pass
def disableRedirectHandling():
'''public final HttpClientBuilder disableRedirectHandling()
'''
pass
def setConnectionBackoffStrategy():
'''public final HttpClientBuilder setConnectionBackoffStrategy(final ConnectionBackoffStrategy connectionBackoffStrategy)
'''
pass
def setBackoffManager():
'''public final HttpClientBuilder setBackoffManager(final BackoffManager backoffManager)
'''
pass
def setServiceUnavailableRetryStrategy():
'''public final HttpClientBuilder setServiceUnavailableRetryStrategy(final ServiceUnavailableRetryStrategy serviceUnavailStrategy)
'''
pass
def setDefaultCookieStore():
'''public final HttpClientBuilder setDefaultCookieStore(final CookieStore cookieStore)
'''
pass
def setDefaultCredentialsProvider():
'''public final HttpClientBuilder setDefaultCredentialsProvider(final CredentialsProvider credentialsProvider)
'''
pass
def setDefaultAuthSchemeRegistry():
'''public final HttpClientBuilder setDefaultAuthSchemeRegistry(final Lookup<AuthSchemeProvider> authSchemeRegistry)
'''
pass
def setDefaultCookieSpecRegistry():
'''public final HttpClientBuilder setDefaultCookieSpecRegistry(final Lookup<CookieSpecProvider> cookieSpecRegistry)
'''
pass
def setContentDecoderRegistry():
'''public final HttpClientBuilder setContentDecoderRegistry(final Map<String, InputStreamFactory> contentDecoderMap)
'''
pass
def setDefaultRequestConfig():
'''public final HttpClientBuilder setDefaultRequestConfig(final RequestConfig config)
'''
pass
def useSystemProperties():
'''public final HttpClientBuilder useSystemProperties()
'''
pass
def evictExpiredConnections():
'''public final HttpClientBuilder evictExpiredConnections()
'''
pass
def evictIdleConnections():
'''public final HttpClientBuilder evictIdleConnections(final Long maxIdleTime, final TimeUnit maxIdleTimeUnit)
public final HttpClientBuilder evictIdleConnections(final long maxIdleTime, final TimeUnit maxIdleTimeUnit)
'''
pass
def build():
'''public CloseableHttpClient build()
'''
pass
def close():
'''public void close()
public void close()
'''
pass
