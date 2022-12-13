def PoolingHttpClientConnectionManager():
    '''public PoolingHttpClientConnectionManager()
    public PoolingHttpClientConnectionManager(final long timeToLive, final TimeUnit tunit)
    public PoolingHttpClientConnectionManager(final Registry<ConnectionSocketFactory> socketFactoryRegistry)
    public PoolingHttpClientConnectionManager(final Registry<ConnectionSocketFactory> socketFactoryRegistry, final DnsResolver dnsResolver)
    public PoolingHttpClientConnectionManager(final Registry<ConnectionSocketFactory> socketFactoryRegistry, final HttpConnectionFactory<HttpRoute, ManagedHttpClientConnection> connFactory)
    public PoolingHttpClientConnectionManager(final HttpConnectionFactory<HttpRoute, ManagedHttpClientConnection> connFactory)
    public PoolingHttpClientConnectionManager(final Registry<ConnectionSocketFactory> socketFactoryRegistry, final HttpConnectionFactory<HttpRoute, ManagedHttpClientConnection> connFactory, final DnsResolver dnsResolver)
    public PoolingHttpClientConnectionManager(final Registry<ConnectionSocketFactory> socketFactoryRegistry, final HttpConnectionFactory<HttpRoute, ManagedHttpClientConnection> connFactory, final SchemePortResolver schemePortResolver, final DnsResolver dnsResolver, final long timeToLive, final TimeUnit tunit)
    public PoolingHttpClientConnectionManager(final HttpClientConnectionOperator httpClientConnectionOperator, final HttpConnectionFactory<HttpRoute, ManagedHttpClientConnection> connFactory, final long timeToLive, final TimeUnit tunit)
    '''
def close():
    '''public void close()
    '''
def requestConnection():
    '''public ConnectionRequest requestConnection(final HttpRoute route, final Object state)
    '''
def cancel():
    '''public boolean cancel()
    '''
def get():
    '''public HttpClientConnection get(final long timeout, final TimeUnit tunit)
    '''
def releaseConnection():
    '''public void releaseConnection(final HttpClientConnection managedConn, final Object state, final long keepalive, final TimeUnit tunit)
    '''
def connect():
    '''public void connect(final HttpClientConnection managedConn, final HttpRoute route, final int connectTimeout, final HttpContext context)
    '''
def upgrade():
    '''public void upgrade(final HttpClientConnection managedConn, final HttpRoute route, final HttpContext context)
    '''
def routeComplete():
    '''public void routeComplete(final HttpClientConnection managedConn, final HttpRoute route, final HttpContext context)
    '''
def shutdown():
    '''public void shutdown()
    '''
def closeIdleConnections():
    '''public void closeIdleConnections(final long idleTimeout, final TimeUnit tunit)
    '''
def closeExpiredConnections():
    '''public void closeExpiredConnections()
    '''
def getMaxTotal():
    '''public int getMaxTotal()
    '''
def setMaxTotal():
    '''public void setMaxTotal(final int max)
    '''
def getDefaultMaxPerRoute():
    '''public int getDefaultMaxPerRoute()
    '''
def setDefaultMaxPerRoute():
    '''public void setDefaultMaxPerRoute(final int max)
    '''
def getMaxPerRoute():
    '''public int getMaxPerRoute(final HttpRoute route)
    '''
def setMaxPerRoute():
    '''public void setMaxPerRoute(final HttpRoute route, final int max)
    '''
def getTotalStats():
    '''public PoolStats getTotalStats()
    '''
def getStats():
    '''public PoolStats getStats(final HttpRoute route)
    '''
def getRoutes():
    '''public Set<HttpRoute> getRoutes()
    '''
def getDefaultSocketConfig():
    '''public SocketConfig getDefaultSocketConfig()
    public SocketConfig getDefaultSocketConfig()
    '''
def setDefaultSocketConfig():
    '''public void setDefaultSocketConfig(final SocketConfig defaultSocketConfig)
    public void setDefaultSocketConfig(final SocketConfig defaultSocketConfig)
    '''
def getDefaultConnectionConfig():
    '''public ConnectionConfig getDefaultConnectionConfig()
    public ConnectionConfig getDefaultConnectionConfig()
    '''
def setDefaultConnectionConfig():
    '''public void setDefaultConnectionConfig(final ConnectionConfig defaultConnectionConfig)
    public void setDefaultConnectionConfig(final ConnectionConfig defaultConnectionConfig)
    '''
def getSocketConfig():
    '''public SocketConfig getSocketConfig(final HttpHost host)
    public SocketConfig getSocketConfig(final HttpHost host)
    '''
def setSocketConfig():
    '''public void setSocketConfig(final HttpHost host, final SocketConfig socketConfig)
    public void setSocketConfig(final HttpHost host, final SocketConfig socketConfig)
    '''
def getConnectionConfig():
    '''public ConnectionConfig getConnectionConfig(final HttpHost host)
    public ConnectionConfig getConnectionConfig(final HttpHost host)
    '''
def setConnectionConfig():
    '''public void setConnectionConfig(final HttpHost host, final ConnectionConfig connectionConfig)
    public void setConnectionConfig(final HttpHost host, final ConnectionConfig connectionConfig)
    '''
def getValidateAfterInactivity():
    '''public int getValidateAfterInactivity()
    '''
def setValidateAfterInactivity():
    '''public void setValidateAfterInactivity(final int ms)
    '''
def create():
    '''public ManagedHttpClientConnection create(final HttpRoute route)
    '''
