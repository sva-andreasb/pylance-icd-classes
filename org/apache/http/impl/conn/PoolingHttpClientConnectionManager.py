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
pass
def close():
'''public void close()
'''
pass
def requestConnection():
'''public ConnectionRequest requestConnection(final HttpRoute route, final Object state)
'''
pass
def cancel():
'''public boolean cancel()
'''
pass
def get():
'''public HttpClientConnection get(final long timeout, final TimeUnit tunit)
'''
pass
def releaseConnection():
'''public void releaseConnection(final HttpClientConnection managedConn, final Object state, final long keepalive, final TimeUnit tunit)
'''
pass
def connect():
'''public void connect(final HttpClientConnection managedConn, final HttpRoute route, final int connectTimeout, final HttpContext context)
'''
pass
def upgrade():
'''public void upgrade(final HttpClientConnection managedConn, final HttpRoute route, final HttpContext context)
'''
pass
def routeComplete():
'''public void routeComplete(final HttpClientConnection managedConn, final HttpRoute route, final HttpContext context)
'''
pass
def shutdown():
'''public void shutdown()
'''
pass
def closeIdleConnections():
'''public void closeIdleConnections(final long idleTimeout, final TimeUnit tunit)
'''
pass
def closeExpiredConnections():
'''public void closeExpiredConnections()
'''
pass
def getMaxTotal():
'''public int getMaxTotal()
'''
pass
def setMaxTotal():
'''public void setMaxTotal(final int max)
'''
pass
def getDefaultMaxPerRoute():
'''public int getDefaultMaxPerRoute()
'''
pass
def setDefaultMaxPerRoute():
'''public void setDefaultMaxPerRoute(final int max)
'''
pass
def getMaxPerRoute():
'''public int getMaxPerRoute(final HttpRoute route)
'''
pass
def setMaxPerRoute():
'''public void setMaxPerRoute(final HttpRoute route, final int max)
'''
pass
def getTotalStats():
'''public PoolStats getTotalStats()
'''
pass
def getStats():
'''public PoolStats getStats(final HttpRoute route)
'''
pass
def getRoutes():
'''public Set<HttpRoute> getRoutes()
'''
pass
def getDefaultSocketConfig():
'''public SocketConfig getDefaultSocketConfig()
public SocketConfig getDefaultSocketConfig()
'''
pass
def setDefaultSocketConfig():
'''public void setDefaultSocketConfig(final SocketConfig defaultSocketConfig)
public void setDefaultSocketConfig(final SocketConfig defaultSocketConfig)
'''
pass
def getDefaultConnectionConfig():
'''public ConnectionConfig getDefaultConnectionConfig()
public ConnectionConfig getDefaultConnectionConfig()
'''
pass
def setDefaultConnectionConfig():
'''public void setDefaultConnectionConfig(final ConnectionConfig defaultConnectionConfig)
public void setDefaultConnectionConfig(final ConnectionConfig defaultConnectionConfig)
'''
pass
def getSocketConfig():
'''public SocketConfig getSocketConfig(final HttpHost host)
public SocketConfig getSocketConfig(final HttpHost host)
'''
pass
def setSocketConfig():
'''public void setSocketConfig(final HttpHost host, final SocketConfig socketConfig)
public void setSocketConfig(final HttpHost host, final SocketConfig socketConfig)
'''
pass
def getConnectionConfig():
'''public ConnectionConfig getConnectionConfig(final HttpHost host)
public ConnectionConfig getConnectionConfig(final HttpHost host)
'''
pass
def setConnectionConfig():
'''public void setConnectionConfig(final HttpHost host, final ConnectionConfig connectionConfig)
public void setConnectionConfig(final HttpHost host, final ConnectionConfig connectionConfig)
'''
pass
def getValidateAfterInactivity():
'''public int getValidateAfterInactivity()
'''
pass
def setValidateAfterInactivity():
'''public void setValidateAfterInactivity(final int ms)
'''
pass
def create():
'''public ManagedHttpClientConnection create(final HttpRoute route)
'''
pass
