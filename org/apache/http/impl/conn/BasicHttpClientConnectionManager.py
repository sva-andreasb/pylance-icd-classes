def ():
    '''returns BasicHttpClientConnectionManager\n\n
    (final Lookup<ConnectionSocketFactory> socketFactoryRegistry, final HttpConnectionFactory<HttpRoute, ManagedHttpClientConnection> connFactory, final SchemePortResolver schemePortResolver, final DnsResolver dnsResolver)\n
    (final HttpClientConnectionOperator httpClientConnectionOperator, final HttpConnectionFactory<HttpRoute, ManagedHttpClientConnection> connFactory)\n
    (final Lookup<ConnectionSocketFactory> socketFactoryRegistry, final HttpConnectionFactory<HttpRoute, ManagedHttpClientConnection> connFactory)\n
    (final Lookup<ConnectionSocketFactory> socketFactoryRegistry)\n
    ()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def cancel():
    '''returns boolean\n\n
    cancel()\n
    '''
def get():
    '''returns HttpClientConnection\n\n
    get(final long timeout, final TimeUnit tunit)\n
    '''
def connect():
    '''returns None\n\n
    connect(final HttpClientConnection conn, final HttpRoute route, final int connectTimeout, final HttpContext context)\n
    '''
def upgrade():
    '''returns None\n\n
    upgrade(final HttpClientConnection conn, final HttpRoute route, final HttpContext context)\n
    '''
def routeComplete():
    '''returns None\n\n
    routeComplete(final HttpClientConnection conn, final HttpRoute route, final HttpContext context)\n
    '''
