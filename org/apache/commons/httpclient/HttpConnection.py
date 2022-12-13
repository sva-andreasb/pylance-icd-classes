def HttpConnection():
    '''    public HttpConnection(final String host, final int port)
    public HttpConnection(final String host, final int port, final Protocol protocol)
    public HttpConnection(final String host, final String virtualHost, final int port, final Protocol protocol)
    public HttpConnection(final String proxyHost, final int proxyPort, final String host, final int port)
    public HttpConnection(final HostConfiguration hostConfiguration)
    public HttpConnection(final String proxyHost, final int proxyPort, final String host, final String virtualHost, final int port, final Protocol protocol)
    public HttpConnection(final String proxyHost, final int proxyPort, final String host, final int port, final Protocol protocol)
    '''
def getHost():
    '''    public String getHost()
    '''
def setHost():
    '''    public void setHost(final String host)
    '''
def getVirtualHost():
    '''    public String getVirtualHost()
    '''
def setVirtualHost():
    '''    public void setVirtualHost(final String host)
    '''
def getPort():
    '''    public int getPort()
    '''
def setPort():
    '''    public void setPort(final int port)
    '''
def getProxyHost():
    '''    public String getProxyHost()
    '''
def setProxyHost():
    '''    public void setProxyHost(final String host)
    '''
def getProxyPort():
    '''    public int getProxyPort()
    '''
def setProxyPort():
    '''    public void setProxyPort(final int port)
    '''
def isSecure():
    '''    public boolean isSecure()
    '''
def getProtocol():
    '''    public Protocol getProtocol()
    '''
def setProtocol():
    '''    public void setProtocol(final Protocol protocol)
    '''
def getLocalAddress():
    '''    public InetAddress getLocalAddress()
    '''
def setLocalAddress():
    '''    public void setLocalAddress(final InetAddress localAddress)
    '''
def isOpen():
    '''    public boolean isOpen()
    '''
def closeIfStale():
    '''    public boolean closeIfStale()
    '''
def isStaleCheckingEnabled():
    '''    public boolean isStaleCheckingEnabled()
    '''
def setStaleCheckingEnabled():
    '''    public void setStaleCheckingEnabled(final boolean staleCheckEnabled)
    '''
def isProxied():
    '''    public boolean isProxied()
    '''
def setLastResponseInputStream():
    '''    public void setLastResponseInputStream(final InputStream inStream)
    '''
def getLastResponseInputStream():
    '''    public InputStream getLastResponseInputStream()
    '''
def getParams():
    '''    public HttpConnectionParams getParams()
    '''
def setParams():
    '''    public void setParams(final HttpConnectionParams params)
    '''
def setSoTimeout():
    '''    public void setSoTimeout(final int timeout)
    '''
def setSocketTimeout():
    '''    public void setSocketTimeout(final int timeout)
    '''
def getSoTimeout():
    '''    public int getSoTimeout()
    '''
def setConnectionTimeout():
    '''    public void setConnectionTimeout(final int timeout)
    '''
def open():
    '''    public void open()
    '''
def tunnelCreated():
    '''    public void tunnelCreated()
    '''
def isTransparent():
    '''    public boolean isTransparent()
    '''
def flushRequestOutputStream():
    '''    public void flushRequestOutputStream()
    '''
def getRequestOutputStream():
    '''    public OutputStream getRequestOutputStream()
    '''
def getResponseInputStream():
    '''    public InputStream getResponseInputStream()
    '''
def isResponseAvailable():
    '''    public boolean isResponseAvailable()
    public boolean isResponseAvailable(final int timeout)
    '''
def write():
    '''    public void write(final byte[] data)
    public void write(final byte[] data, final int offset, final int length)
    '''
def writeLine():
    '''    public void writeLine(final byte[] data)
    public void writeLine()
    '''
def print():
    '''    public void print(final String data)
    public void print(final String data, final String charset)
    '''
def printLine():
    '''    public void printLine(final String data)
    public void printLine(final String data, final String charset)
    public void printLine()
    '''
def readLine():
    '''    public String readLine()
    public String readLine(final String charset)
    '''
def shutdownOutput():
    '''    public void shutdownOutput()
    '''
def close():
    '''    public void close()
    '''
def getHttpConnectionManager():
    '''    public HttpConnectionManager getHttpConnectionManager()
    '''
def setHttpConnectionManager():
    '''    public void setHttpConnectionManager(final HttpConnectionManager httpConnectionManager)
    '''
def releaseConnection():
    '''    public void releaseConnection()
    '''
def getSendBufferSize():
    '''    public int getSendBufferSize()
    '''
def setSendBufferSize():
    '''    public void setSendBufferSize(final int sendBufferSize)
    '''
