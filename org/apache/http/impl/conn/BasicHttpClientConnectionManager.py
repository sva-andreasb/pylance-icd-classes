def BasicHttpClientConnectionManager():
'''public BasicHttpClientConnectionManager(final Lookup<ConnectionSocketFactory> socketFactoryRegistry, final HttpConnectionFactory<HttpRoute, ManagedHttpClientConnection> connFactory, final SchemePortResolver schemePortResolver, final DnsResolver dnsResolver)
public BasicHttpClientConnectionManager(final HttpClientConnectionOperator httpClientConnectionOperator, final HttpConnectionFactory<HttpRoute, ManagedHttpClientConnection> connFactory)
public BasicHttpClientConnectionManager(final Lookup<ConnectionSocketFactory> socketFactoryRegistry, final HttpConnectionFactory<HttpRoute, ManagedHttpClientConnection> connFactory)
public BasicHttpClientConnectionManager(final Lookup<ConnectionSocketFactory> socketFactoryRegistry)
public BasicHttpClientConnectionManager()
'''
pass
def close():
'''public void close()
'''
pass
def getSocketConfig():
'''public synchronized SocketConfig getSocketConfig()
'''
pass
def setSocketConfig():
'''public synchronized void setSocketConfig(final SocketConfig socketConfig)
'''
pass
def getConnectionConfig():
'''public synchronized ConnectionConfig getConnectionConfig()
'''
pass
def setConnectionConfig():
'''public synchronized void setConnectionConfig(final ConnectionConfig connConfig)
'''
pass
def requestConnection():
'''public final ConnectionRequest requestConnection(final HttpRoute route, final Object state)
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
'''public synchronized void releaseConnection(final HttpClientConnection conn, final Object state, final long keepalive, final TimeUnit tunit)
'''
pass
def connect():
'''public void connect(final HttpClientConnection conn, final HttpRoute route, final int connectTimeout, final HttpContext context)
'''
pass
def upgrade():
'''public void upgrade(final HttpClientConnection conn, final HttpRoute route, final HttpContext context)
'''
pass
def routeComplete():
'''public void routeComplete(final HttpClientConnection conn, final HttpRoute route, final HttpContext context)
'''
pass
def closeExpiredConnections():
'''public synchronized void closeExpiredConnections()
'''
pass
def closeIdleConnections():
'''public synchronized void closeIdleConnections(final long idletime, final TimeUnit tunit)
'''
pass
def shutdown():
'''public synchronized void shutdown()
'''
pass
