def ():
    '''returns HttpConnection\n\n
    (final String host, final int port)\n
    (final String host, final int port, final Protocol protocol)\n
    (final String host, final String virtualHost, final int port, final Protocol protocol)\n
    (final String proxyHost, final int proxyPort, final String host, final int port)\n
    (final HostConfiguration hostConfiguration)\n
    (final String proxyHost, final int proxyPort, final String host, final String virtualHost, final int port, final Protocol protocol)\n
    (final String proxyHost, final int proxyPort, final String host, final int port, final Protocol protocol)\n
    '''
def getHost():
    '''returns String\n\n
    getHost()\n
    '''
def setHost():
    '''returns None\n\n
    setHost(final String host)\n
    '''
def getVirtualHost():
    '''returns String\n\n
    getVirtualHost()\n
    '''
def setVirtualHost():
    '''returns None\n\n
    setVirtualHost(final String host)\n
    '''
def getPort():
    '''returns int\n\n
    getPort()\n
    '''
def setPort():
    '''returns None\n\n
    setPort(final int port)\n
    '''
def getProxyHost():
    '''returns String\n\n
    getProxyHost()\n
    '''
def setProxyHost():
    '''returns None\n\n
    setProxyHost(final String host)\n
    '''
def getProxyPort():
    '''returns int\n\n
    getProxyPort()\n
    '''
def setProxyPort():
    '''returns None\n\n
    setProxyPort(final int port)\n
    '''
def isSecure():
    '''returns boolean\n\n
    isSecure()\n
    '''
def getProtocol():
    '''returns Protocol\n\n
    getProtocol()\n
    '''
def setProtocol():
    '''returns None\n\n
    setProtocol(final Protocol protocol)\n
    '''
def getLocalAddress():
    '''returns InetAddress\n\n
    getLocalAddress()\n
    '''
def setLocalAddress():
    '''returns None\n\n
    setLocalAddress(final InetAddress localAddress)\n
    '''
def isOpen():
    '''returns boolean\n\n
    isOpen()\n
    '''
def closeIfStale():
    '''returns boolean\n\n
    closeIfStale()\n
    '''
def isStaleCheckingEnabled():
    '''returns boolean\n\n
    isStaleCheckingEnabled()\n
    '''
def setStaleCheckingEnabled():
    '''returns None\n\n
    setStaleCheckingEnabled(final boolean staleCheckEnabled)\n
    '''
def isProxied():
    '''returns boolean\n\n
    isProxied()\n
    '''
def setLastResponseInputStream():
    '''returns None\n\n
    setLastResponseInputStream(final InputStream inStream)\n
    '''
def getLastResponseInputStream():
    '''returns InputStream\n\n
    getLastResponseInputStream()\n
    '''
def getParams():
    '''returns HttpConnectionParams\n\n
    getParams()\n
    '''
def setParams():
    '''returns None\n\n
    setParams(final HttpConnectionParams params)\n
    '''
def setSoTimeout():
    '''returns None\n\n
    setSoTimeout(final int timeout)\n
    '''
def setSocketTimeout():
    '''returns None\n\n
    setSocketTimeout(final int timeout)\n
    '''
def getSoTimeout():
    '''returns int\n\n
    getSoTimeout()\n
    '''
def setConnectionTimeout():
    '''returns None\n\n
    setConnectionTimeout(final int timeout)\n
    '''
def open():
    '''returns None\n\n
    open()\n
    '''
def tunnelCreated():
    '''returns None\n\n
    tunnelCreated()\n
    '''
def isTransparent():
    '''returns boolean\n\n
    isTransparent()\n
    '''
def flushRequestOutputStream():
    '''returns None\n\n
    flushRequestOutputStream()\n
    '''
def getRequestOutputStream():
    '''returns OutputStream\n\n
    getRequestOutputStream()\n
    '''
def getResponseInputStream():
    '''returns InputStream\n\n
    getResponseInputStream()\n
    '''
def isResponseAvailable():
    '''returns boolean\n\n
    isResponseAvailable()\n
    isResponseAvailable(final int timeout)\n
    '''
def write():
    '''returns None\n\n
    write(final byte[] data)\n
    write(final byte[] data, final int offset, final int length)\n
    '''
def writeLine():
    '''returns None\n\n
    writeLine(final byte[] data)\n
    writeLine()\n
    '''
def print():
    '''returns None\n\n
    print(final String data)\n
    print(final String data, final String charset)\n
    '''
def printLine():
    '''returns None\n\n
    printLine(final String data)\n
    printLine(final String data, final String charset)\n
    printLine()\n
    '''
def readLine():
    '''returns String\n\n
    readLine()\n
    readLine(final String charset)\n
    '''
def shutdownOutput():
    '''returns None\n\n
    shutdownOutput()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getHttpConnectionManager():
    '''returns HttpConnectionManager\n\n
    getHttpConnectionManager()\n
    '''
def setHttpConnectionManager():
    '''returns None\n\n
    setHttpConnectionManager(final HttpConnectionManager httpConnectionManager)\n
    '''
def releaseConnection():
    '''returns None\n\n
    releaseConnection()\n
    '''
def getSendBufferSize():
    '''returns int\n\n
    getSendBufferSize()\n
    '''
def setSendBufferSize():
    '''returns None\n\n
    setSendBufferSize(final int sendBufferSize)\n
    '''
