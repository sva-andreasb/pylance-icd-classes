def HostConfiguration():
    '''public HostConfiguration()
    public HostConfiguration(final HostConfiguration hostConfiguration)
    '''
def clone():
    '''public Object clone()
    '''
def toString():
    '''public synchronized String toString()
    '''
def hostEquals():
    '''public synchronized boolean hostEquals(final HttpConnection connection)
    '''
def proxyEquals():
    '''public synchronized boolean proxyEquals(final HttpConnection connection)
    '''
def isHostSet():
    '''public synchronized boolean isHostSet()
    '''
def setHost():
    '''public synchronized void setHost(final HttpHost host)
    public synchronized void setHost(final String host, final int port, final String protocol)
    public synchronized void setHost(final String host, final String virtualHost, final int port, final Protocol protocol)
    public synchronized void setHost(final String host, final int port, final Protocol protocol)
    public synchronized void setHost(final String host, final int port)
    public synchronized void setHost(final String host)
    public synchronized void setHost(final URI uri)
    '''
def getHostURL():
    '''public synchronized String getHostURL()
    '''
def getHost():
    '''public synchronized String getHost()
    '''
def getVirtualHost():
    '''public synchronized String getVirtualHost()
    '''
def getPort():
    '''public synchronized int getPort()
    '''
def getProtocol():
    '''public synchronized Protocol getProtocol()
    '''
def isProxySet():
    '''public synchronized boolean isProxySet()
    '''
def setProxyHost():
    '''public synchronized void setProxyHost(final ProxyHost proxyHost)
    '''
def setProxy():
    '''public synchronized void setProxy(final String proxyHost, final int proxyPort)
    '''
def getProxyHost():
    '''public synchronized String getProxyHost()
    '''
def getProxyPort():
    '''public synchronized int getProxyPort()
    '''
def setLocalAddress():
    '''public synchronized void setLocalAddress(final InetAddress localAddress)
    '''
def getLocalAddress():
    '''public synchronized InetAddress getLocalAddress()
    '''
def getParams():
    '''public HostParams getParams()
    '''
def setParams():
    '''public void setParams(final HostParams params)
    '''
def equals():
    '''public synchronized boolean equals(final Object o)
    '''
def hashCode():
    '''public synchronized int hashCode()
    '''
