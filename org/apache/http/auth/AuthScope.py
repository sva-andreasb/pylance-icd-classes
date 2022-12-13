ANY_PORT = "int  -1"
def AuthScope():
    '''public AuthScope(final String host, final int port, final String realm, final String schemeName)
    public AuthScope(final HttpHost origin, final String realm, final String schemeName)
    public AuthScope(final HttpHost origin)
    public AuthScope(final String host, final int port, final String realm)
    public AuthScope(final String host, final int port)
    public AuthScope(final AuthScope authscope)
    '''
def getOrigin():
    '''public HttpHost getOrigin()
    '''
def getHost():
    '''public String getHost()
    '''
def getPort():
    '''public int getPort()
    '''
def getRealm():
    '''public String getRealm()
    '''
def getScheme():
    '''public String getScheme()
    '''
def match():
    '''public int match(final AuthScope that)
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def toString():
    '''public String toString()
    '''
def hashCode():
    '''public int hashCode()
    '''
