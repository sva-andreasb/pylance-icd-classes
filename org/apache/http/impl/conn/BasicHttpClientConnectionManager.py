def BasicHttpClientConnectionManager():
    '''public BasicHttpClientConnectionManager(final Lookup<ConnectionSocketFactory> socketFactoryRegistry, final HttpConnectionFactory<HttpRoute, ManagedHttpClientConnection> connFactory, final SchemePortResolver schemePortResolver, final DnsResolver dnsResolver)
    public BasicHttpClientConnectionManager(final HttpClientConnectionOperator httpClientConnectionOperator, final HttpConnectionFactory<HttpRoute, ManagedHttpClientConnection> connFactory)
    public BasicHttpClientConnectionManager(final Lookup<ConnectionSocketFactory> socketFactoryRegistry, final HttpConnectionFactory<HttpRoute, ManagedHttpClientConnection> connFactory)
    public BasicHttpClientConnectionManager(final Lookup<ConnectionSocketFactory> socketFactoryRegistry)
    public BasicHttpClientConnectionManager()
    '''
def close():
    '''public void close()
    '''
def getSocketConfig():
    '''public synchronized SocketConfig getSocketConfig()
    '''
def setSocketConfig():
    '''public synchronized void setSocketConfig(final SocketConfig socketConfig)
    '''
def getConnectionConfig():
    '''public synchronized ConnectionConfig getConnectionConfig()
    '''
def setConnectionConfig():
    '''public synchronized void setConnectionConfig(final ConnectionConfig connConfig)
    '''
def requestConnection():
    '''public final ConnectionRequest requestConnection(final HttpRoute route, final Object state)
    '''
def cancel():
    '''public boolean cancel()
    '''
def get():
    '''public HttpClientConnection get(final long timeout, final TimeUnit tunit)
    '''
def releaseConnection():
    '''public synchronized void releaseConnection(final HttpClientConnection conn, final Object state, final long keepalive, final TimeUnit tunit)
    '''
def connect():
    '''public void connect(final HttpClientConnection conn, final HttpRoute route, final int connectTimeout, final HttpContext context)
    '''
def upgrade():
    '''public void upgrade(final HttpClientConnection conn, final HttpRoute route, final HttpContext context)
    '''
def routeComplete():
    '''public void routeComplete(final HttpClientConnection conn, final HttpRoute route, final HttpContext context)
    '''
def closeExpiredConnections():
    '''public synchronized void closeExpiredConnections()
    '''
def closeIdleConnections():
    '''public synchronized void closeIdleConnections(final long idletime, final TimeUnit tunit)
    '''
def shutdown():
    '''public synchronized void shutdown()
    '''
