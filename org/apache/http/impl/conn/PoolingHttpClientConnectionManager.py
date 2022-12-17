def ():
    '''returns PoolingHttpClientConnectionManager\n\n
    ()\n
    (final long timeToLive, final TimeUnit tunit)\n
    (final Registry<ConnectionSocketFactory> socketFactoryRegistry)\n
    (final Registry<ConnectionSocketFactory> socketFactoryRegistry, final DnsResolver dnsResolver)\n
    (final Registry<ConnectionSocketFactory> socketFactoryRegistry, final HttpConnectionFactory<HttpRoute, ManagedHttpClientConnection> connFactory)\n
    (final HttpConnectionFactory<HttpRoute, ManagedHttpClientConnection> connFactory)\n
    (final Registry<ConnectionSocketFactory> socketFactoryRegistry, final HttpConnectionFactory<HttpRoute, ManagedHttpClientConnection> connFactory, final DnsResolver dnsResolver)\n
    (final Registry<ConnectionSocketFactory> socketFactoryRegistry, final HttpConnectionFactory<HttpRoute, ManagedHttpClientConnection> connFactory, final SchemePortResolver schemePortResolver, final DnsResolver dnsResolver, final long timeToLive, final TimeUnit tunit)\n
    (final HttpClientConnectionOperator httpClientConnectionOperator, final HttpConnectionFactory<HttpRoute, ManagedHttpClientConnection> connFactory, final long timeToLive, final TimeUnit tunit)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def requestConnection():
    '''returns ConnectionRequest\n\n
    requestConnection(final HttpRoute route, final Object state)\n
    '''
def cancel():
    '''returns boolean\n\n
    cancel()\n
    '''
def get():
    '''returns HttpClientConnection\n\n
    get(final long timeout, final TimeUnit tunit)\n
    '''
def releaseConnection():
    '''returns None\n\n
    releaseConnection(final HttpClientConnection managedConn, final Object state, final long keepalive, final TimeUnit tunit)\n
    '''
def connect():
    '''returns None\n\n
    connect(final HttpClientConnection managedConn, final HttpRoute route, final int connectTimeout, final HttpContext context)\n
    '''
def upgrade():
    '''returns None\n\n
    upgrade(final HttpClientConnection managedConn, final HttpRoute route, final HttpContext context)\n
    '''
def routeComplete():
    '''returns None\n\n
    routeComplete(final HttpClientConnection managedConn, final HttpRoute route, final HttpContext context)\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def closeIdleConnections():
    '''returns None\n\n
    closeIdleConnections(final long idleTimeout, final TimeUnit tunit)\n
    '''
def closeExpiredConnections():
    '''returns None\n\n
    closeExpiredConnections()\n
    '''
def getMaxTotal():
    '''returns int\n\n
    getMaxTotal()\n
    '''
def setMaxTotal():
    '''returns None\n\n
    setMaxTotal(final int max)\n
    '''
def getDefaultMaxPerRoute():
    '''returns int\n\n
    getDefaultMaxPerRoute()\n
    '''
def setDefaultMaxPerRoute():
    '''returns None\n\n
    setDefaultMaxPerRoute(final int max)\n
    '''
def getMaxPerRoute():
    '''returns int\n\n
    getMaxPerRoute(final HttpRoute route)\n
    '''
def setMaxPerRoute():
    '''returns None\n\n
    setMaxPerRoute(final HttpRoute route, final int max)\n
    '''
def getTotalStats():
    '''returns PoolStats\n\n
    getTotalStats()\n
    '''
def getStats():
    '''returns PoolStats\n\n
    getStats(final HttpRoute route)\n
    '''
def getRoutes():
    '''returns Set<HttpRoute>\n\n
    getRoutes()\n
    '''
def getDefaultSocketConfig():
    '''returns SocketConfig\n\n
    getDefaultSocketConfig()\n
    getDefaultSocketConfig()\n
    '''
def setDefaultSocketConfig():
    '''returns None\n\n
    setDefaultSocketConfig(final SocketConfig defaultSocketConfig)\n
    setDefaultSocketConfig(final SocketConfig defaultSocketConfig)\n
    '''
def getDefaultConnectionConfig():
    '''returns ConnectionConfig\n\n
    getDefaultConnectionConfig()\n
    getDefaultConnectionConfig()\n
    '''
def setDefaultConnectionConfig():
    '''returns None\n\n
    setDefaultConnectionConfig(final ConnectionConfig defaultConnectionConfig)\n
    setDefaultConnectionConfig(final ConnectionConfig defaultConnectionConfig)\n
    '''
def getSocketConfig():
    '''returns SocketConfig\n\n
    getSocketConfig(final HttpHost host)\n
    getSocketConfig(final HttpHost host)\n
    '''
def setSocketConfig():
    '''returns None\n\n
    setSocketConfig(final HttpHost host, final SocketConfig socketConfig)\n
    setSocketConfig(final HttpHost host, final SocketConfig socketConfig)\n
    '''
def getConnectionConfig():
    '''returns ConnectionConfig\n\n
    getConnectionConfig(final HttpHost host)\n
    getConnectionConfig(final HttpHost host)\n
    '''
def setConnectionConfig():
    '''returns None\n\n
    setConnectionConfig(final HttpHost host, final ConnectionConfig connectionConfig)\n
    setConnectionConfig(final HttpHost host, final ConnectionConfig connectionConfig)\n
    '''
def getValidateAfterInactivity():
    '''returns int\n\n
    getValidateAfterInactivity()\n
    '''
def setValidateAfterInactivity():
    '''returns None\n\n
    setValidateAfterInactivity(final int ms)\n
    '''
def create():
    '''returns ManagedHttpClientConnection\n\n
    create(final HttpRoute route)\n
    '''
