def HttpConnection():
'''public HttpConnection(final String host, final int port)
public HttpConnection(final String host, final int port, final Protocol protocol)
public HttpConnection(final String host, final String virtualHost, final int port, final Protocol protocol)
public HttpConnection(final String proxyHost, final int proxyPort, final String host, final int port)
public HttpConnection(final HostConfiguration hostConfiguration)
public HttpConnection(final String proxyHost, final int proxyPort, final String host, final String virtualHost, final int port, final Protocol protocol)
public HttpConnection(final String proxyHost, final int proxyPort, final String host, final int port, final Protocol protocol)
'''
pass
def getHost():
'''public String getHost()
'''
pass
def setHost():
'''public void setHost(final String host)
'''
pass
def getVirtualHost():
'''public String getVirtualHost()
'''
pass
def setVirtualHost():
'''public void setVirtualHost(final String host)
'''
pass
def getPort():
'''public int getPort()
'''
pass
def setPort():
'''public void setPort(final int port)
'''
pass
def getProxyHost():
'''public String getProxyHost()
'''
pass
def setProxyHost():
'''public void setProxyHost(final String host)
'''
pass
def getProxyPort():
'''public int getProxyPort()
'''
pass
def setProxyPort():
'''public void setProxyPort(final int port)
'''
pass
def isSecure():
'''public boolean isSecure()
'''
pass
def getProtocol():
'''public Protocol getProtocol()
'''
pass
def setProtocol():
'''public void setProtocol(final Protocol protocol)
'''
pass
def getLocalAddress():
'''public InetAddress getLocalAddress()
'''
pass
def setLocalAddress():
'''public void setLocalAddress(final InetAddress localAddress)
'''
pass
def isOpen():
'''public boolean isOpen()
'''
pass
def closeIfStale():
'''public boolean closeIfStale()
'''
pass
def isStaleCheckingEnabled():
'''public boolean isStaleCheckingEnabled()
'''
pass
def setStaleCheckingEnabled():
'''public void setStaleCheckingEnabled(final boolean staleCheckEnabled)
'''
pass
def isProxied():
'''public boolean isProxied()
'''
pass
def setLastResponseInputStream():
'''public void setLastResponseInputStream(final InputStream inStream)
'''
pass
def getLastResponseInputStream():
'''public InputStream getLastResponseInputStream()
'''
pass
def getParams():
'''public HttpConnectionParams getParams()
'''
pass
def setParams():
'''public void setParams(final HttpConnectionParams params)
'''
pass
def setSoTimeout():
'''public void setSoTimeout(final int timeout)
'''
pass
def setSocketTimeout():
'''public void setSocketTimeout(final int timeout)
'''
pass
def getSoTimeout():
'''public int getSoTimeout()
'''
pass
def setConnectionTimeout():
'''public void setConnectionTimeout(final int timeout)
'''
pass
def open():
'''public void open()
'''
pass
def tunnelCreated():
'''public void tunnelCreated()
'''
pass
def isTransparent():
'''public boolean isTransparent()
'''
pass
def flushRequestOutputStream():
'''public void flushRequestOutputStream()
'''
pass
def getRequestOutputStream():
'''public OutputStream getRequestOutputStream()
'''
pass
def getResponseInputStream():
'''public InputStream getResponseInputStream()
'''
pass
def isResponseAvailable():
'''public boolean isResponseAvailable()
public boolean isResponseAvailable(final int timeout)
'''
pass
def write():
'''public void write(final byte[] data)
public void write(final byte[] data, final int offset, final int length)
'''
pass
def writeLine():
'''public void writeLine(final byte[] data)
public void writeLine()
'''
pass
def print():
'''public void print(final String data)
public void print(final String data, final String charset)
'''
pass
def printLine():
'''public void printLine(final String data)
public void printLine(final String data, final String charset)
public void printLine()
'''
pass
def readLine():
'''public String readLine()
public String readLine(final String charset)
'''
pass
def shutdownOutput():
'''public void shutdownOutput()
'''
pass
def close():
'''public void close()
'''
pass
def getHttpConnectionManager():
'''public HttpConnectionManager getHttpConnectionManager()
'''
pass
def setHttpConnectionManager():
'''public void setHttpConnectionManager(final HttpConnectionManager httpConnectionManager)
'''
pass
def releaseConnection():
'''public void releaseConnection()
'''
pass
def getSendBufferSize():
'''public int getSendBufferSize()
'''
pass
def setSendBufferSize():
'''public void setSendBufferSize(final int sendBufferSize)
'''
pass
