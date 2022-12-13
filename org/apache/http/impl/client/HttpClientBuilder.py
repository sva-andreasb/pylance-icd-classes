def create():
    '''    public static HttpClientBuilder create()
    '''
def setRequestExecutor():
    '''    public final HttpClientBuilder setRequestExecutor(final HttpRequestExecutor requestExec)
    '''
def setHostnameVerifier():
    '''    public final HttpClientBuilder setHostnameVerifier(final X509HostnameVerifier hostnameVerifier)
    '''
def setSSLHostnameVerifier():
    '''    public final HttpClientBuilder setSSLHostnameVerifier(final HostnameVerifier hostnameVerifier)
    '''
def setPublicSuffixMatcher():
    '''    public final HttpClientBuilder setPublicSuffixMatcher(final PublicSuffixMatcher publicSuffixMatcher)
    '''
def setSslcontext():
    '''    public final HttpClientBuilder setSslcontext(final SSLContext sslcontext)
    '''
def setSSLContext():
    '''    public final HttpClientBuilder setSSLContext(final SSLContext sslContext)
    '''
def setSSLSocketFactory():
    '''    public final HttpClientBuilder setSSLSocketFactory(final LayeredConnectionSocketFactory sslSocketFactory)
    '''
def setMaxConnTotal():
    '''    public final HttpClientBuilder setMaxConnTotal(final int maxConnTotal)
    '''
def setMaxConnPerRoute():
    '''    public final HttpClientBuilder setMaxConnPerRoute(final int maxConnPerRoute)
    '''
def setDefaultSocketConfig():
    '''    public final HttpClientBuilder setDefaultSocketConfig(final SocketConfig config)
    '''
def setDefaultConnectionConfig():
    '''    public final HttpClientBuilder setDefaultConnectionConfig(final ConnectionConfig config)
    '''
def setConnectionTimeToLive():
    '''    public final HttpClientBuilder setConnectionTimeToLive(final long connTimeToLive, final TimeUnit connTimeToLiveTimeUnit)
    '''
def setConnectionManager():
    '''    public final HttpClientBuilder setConnectionManager(final HttpClientConnectionManager connManager)
    '''
def setConnectionManagerShared():
    '''    public final HttpClientBuilder setConnectionManagerShared(final boolean shared)
    '''
def setConnectionReuseStrategy():
    '''    public final HttpClientBuilder setConnectionReuseStrategy(final ConnectionReuseStrategy reuseStrategy)
    '''
def setKeepAliveStrategy():
    '''    public final HttpClientBuilder setKeepAliveStrategy(final ConnectionKeepAliveStrategy keepAliveStrategy)
    '''
def setTargetAuthenticationStrategy():
    '''    public final HttpClientBuilder setTargetAuthenticationStrategy(final AuthenticationStrategy targetAuthStrategy)
    '''
def setProxyAuthenticationStrategy():
    '''    public final HttpClientBuilder setProxyAuthenticationStrategy(final AuthenticationStrategy proxyAuthStrategy)
    '''
def setUserTokenHandler():
    '''    public final HttpClientBuilder setUserTokenHandler(final UserTokenHandler userTokenHandler)
    '''
def disableConnectionState():
    '''    public final HttpClientBuilder disableConnectionState()
    '''
def setSchemePortResolver():
    '''    public final HttpClientBuilder setSchemePortResolver(final SchemePortResolver schemePortResolver)
    '''
def setUserAgent():
    '''    public final HttpClientBuilder setUserAgent(final String userAgent)
    '''
def setDefaultHeaders():
    '''    public final HttpClientBuilder setDefaultHeaders(final Collection<? extends Header> defaultHeaders)
    '''
def addInterceptorFirst():
    '''    public final HttpClientBuilder addInterceptorFirst(final HttpResponseInterceptor itcp)
    public final HttpClientBuilder addInterceptorFirst(final HttpRequestInterceptor itcp)
    '''
def addInterceptorLast():
    '''    public final HttpClientBuilder addInterceptorLast(final HttpResponseInterceptor itcp)
    public final HttpClientBuilder addInterceptorLast(final HttpRequestInterceptor itcp)
    '''
def disableCookieManagement():
    '''    public final HttpClientBuilder disableCookieManagement()
    '''
def disableContentCompression():
    '''    public final HttpClientBuilder disableContentCompression()
    '''
def disableAuthCaching():
    '''    public final HttpClientBuilder disableAuthCaching()
    '''
def setHttpProcessor():
    '''    public final HttpClientBuilder setHttpProcessor(final HttpProcessor httpprocessor)
    '''
def setDnsResolver():
    '''    public final HttpClientBuilder setDnsResolver(final DnsResolver dnsResolver)
    '''
def setRetryHandler():
    '''    public final HttpClientBuilder setRetryHandler(final HttpRequestRetryHandler retryHandler)
    '''
def disableAutomaticRetries():
    '''    public final HttpClientBuilder disableAutomaticRetries()
    '''
def setProxy():
    '''    public final HttpClientBuilder setProxy(final HttpHost proxy)
    '''
def setRoutePlanner():
    '''    public final HttpClientBuilder setRoutePlanner(final HttpRoutePlanner routePlanner)
    '''
def setRedirectStrategy():
    '''    public final HttpClientBuilder setRedirectStrategy(final RedirectStrategy redirectStrategy)
    '''
def disableRedirectHandling():
    '''    public final HttpClientBuilder disableRedirectHandling()
    '''
def setConnectionBackoffStrategy():
    '''    public final HttpClientBuilder setConnectionBackoffStrategy(final ConnectionBackoffStrategy connectionBackoffStrategy)
    '''
def setBackoffManager():
    '''    public final HttpClientBuilder setBackoffManager(final BackoffManager backoffManager)
    '''
def setServiceUnavailableRetryStrategy():
    '''    public final HttpClientBuilder setServiceUnavailableRetryStrategy(final ServiceUnavailableRetryStrategy serviceUnavailStrategy)
    '''
def setDefaultCookieStore():
    '''    public final HttpClientBuilder setDefaultCookieStore(final CookieStore cookieStore)
    '''
def setDefaultCredentialsProvider():
    '''    public final HttpClientBuilder setDefaultCredentialsProvider(final CredentialsProvider credentialsProvider)
    '''
def setDefaultAuthSchemeRegistry():
    '''    public final HttpClientBuilder setDefaultAuthSchemeRegistry(final Lookup<AuthSchemeProvider> authSchemeRegistry)
    '''
def setDefaultCookieSpecRegistry():
    '''    public final HttpClientBuilder setDefaultCookieSpecRegistry(final Lookup<CookieSpecProvider> cookieSpecRegistry)
    '''
def setContentDecoderRegistry():
    '''    public final HttpClientBuilder setContentDecoderRegistry(final Map<String, InputStreamFactory> contentDecoderMap)
    '''
def setDefaultRequestConfig():
    '''    public final HttpClientBuilder setDefaultRequestConfig(final RequestConfig config)
    '''
def useSystemProperties():
    '''    public final HttpClientBuilder useSystemProperties()
    '''
def evictExpiredConnections():
    '''    public final HttpClientBuilder evictExpiredConnections()
    '''
def evictIdleConnections():
    '''    public final HttpClientBuilder evictIdleConnections(final Long maxIdleTime, final TimeUnit maxIdleTimeUnit)
    public final HttpClientBuilder evictIdleConnections(final long maxIdleTime, final TimeUnit maxIdleTimeUnit)
    '''
def build():
    '''    public CloseableHttpClient build()
    '''
def close():
    '''    public void close()
    public void close()
    '''
