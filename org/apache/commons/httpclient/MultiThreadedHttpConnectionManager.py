DEFAULT_MAX_HOST_CONNECTIONS = "int  2"
DEFAULT_MAX_TOTAL_CONNECTIONS = "int  20"
def ():
    '''returns HttpConnectionAdapter\n\n
    ()\n
    ()\n
    (final HostConfiguration hostConfiguration)\n
    (final HttpConnection connection)\n
    '''
def isConnectionStaleCheckingEnabled():
    '''returns boolean\n\n
    isConnectionStaleCheckingEnabled()\n
    '''
def setConnectionStaleCheckingEnabled():
    '''returns None\n\n
    setConnectionStaleCheckingEnabled(final boolean connectionStaleCheckingEnabled)\n
    '''
def setMaxConnectionsPerHost():
    '''returns None\n\n
    setMaxConnectionsPerHost(final int maxHostConnections)\n
    '''
def getMaxConnectionsPerHost():
    '''returns int\n\n
    getMaxConnectionsPerHost()\n
    '''
def setMaxTotalConnections():
    '''returns None\n\n
    setMaxTotalConnections(final int maxTotalConnections)\n
    '''
def getMaxTotalConnections():
    '''returns int\n\n
    getMaxTotalConnections()\n
    '''
def getConnection():
    '''returns HttpConnection\n\n
    getConnection(final HostConfiguration hostConfiguration)\n
    getConnection(final HostConfiguration hostConfiguration, final long timeout)\n
    '''
def getConnectionWithTimeout():
    '''returns HttpConnection\n\n
    getConnectionWithTimeout(final HostConfiguration hostConfiguration, final long timeout)\n
    '''
def getConnectionsInPool():
    '''returns int\n\n
    getConnectionsInPool(final HostConfiguration hostConfiguration)\n
    getConnectionsInPool()\n
    '''
def getConnectionsInUse():
    '''returns int\n\n
    getConnectionsInUse(final HostConfiguration hostConfiguration)\n
    getConnectionsInUse()\n
    '''
def deleteClosedConnections():
    '''returns None\n\n
    deleteClosedConnections()\n
    '''
def closeIdleConnections():
    '''returns None\n\n
    closeIdleConnections(final long idleTimeout)\n
    '''
def releaseConnection():
    '''returns None\n\n
    releaseConnection(HttpConnection conn)\n
    releaseConnection()\n
    '''
def getParams():
    '''returns HttpConnectionParams\n\n
    getParams()\n
    getParams()\n
    '''
def setParams():
    '''returns None\n\n
    setParams(final HttpConnectionManagerParams params)\n
    setParams(final HttpConnectionParams params)\n
    '''
def freeConnection():
    '''returns None\n\n
    freeConnection(final HttpConnection conn)\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getLocalAddress():
    '''returns InetAddress\n\n
    getLocalAddress()\n
    '''
def isStaleCheckingEnabled():
    '''returns boolean\n\n
    isStaleCheckingEnabled()\n
    '''
def setLocalAddress():
    '''returns None\n\n
    setLocalAddress(final InetAddress localAddress)\n
    '''
def setStaleCheckingEnabled():
    '''returns None\n\n
    setStaleCheckingEnabled(final boolean staleCheckEnabled)\n
    '''
def getHost():
    '''returns String\n\n
    getHost()\n
    '''
def getHttpConnectionManager():
    '''returns HttpConnectionManager\n\n
    getHttpConnectionManager()\n
    '''
def getLastResponseInputStream():
    '''returns InputStream\n\n
    getLastResponseInputStream()\n
    '''
def getPort():
    '''returns int\n\n
    getPort()\n
    '''
def getProtocol():
    '''returns Protocol\n\n
    getProtocol()\n
    '''
def getProxyHost():
    '''returns String\n\n
    getProxyHost()\n
    '''
def getProxyPort():
    '''returns int\n\n
    getProxyPort()\n
    '''
def getRequestOutputStream():
    '''returns OutputStream\n\n
    getRequestOutputStream()\n
    '''
def getResponseInputStream():
    '''returns InputStream\n\n
    getResponseInputStream()\n
    '''
def isOpen():
    '''returns boolean\n\n
    isOpen()\n
    '''
def closeIfStale():
    '''returns boolean\n\n
    closeIfStale()\n
    '''
def isProxied():
    '''returns boolean\n\n
    isProxied()\n
    '''
def isResponseAvailable():
    '''returns boolean\n\n
    isResponseAvailable()\n
    isResponseAvailable(final int timeout)\n
    '''
def isSecure():
    '''returns boolean\n\n
    isSecure()\n
    '''
def isTransparent():
    '''returns boolean\n\n
    isTransparent()\n
    '''
def open():
    '''returns None\n\n
    open()\n
    '''
def print():
    '''returns None\n\n
    print(final String data)\n
    print(final String data, final String charset)\n
    '''
def printLine():
    '''returns None\n\n
    printLine()\n
    printLine(final String data)\n
    printLine(final String data, final String charset)\n
    '''
def readLine():
    '''returns String\n\n
    readLine()\n
    readLine(final String charset)\n
    '''
def setConnectionTimeout():
    '''returns None\n\n
    setConnectionTimeout(final int timeout)\n
    '''
def setHost():
    '''returns None\n\n
    setHost(final String host)\n
    '''
def setHttpConnectionManager():
    '''returns None\n\n
    setHttpConnectionManager(final HttpConnectionManager httpConnectionManager)\n
    '''
def setLastResponseInputStream():
    '''returns None\n\n
    setLastResponseInputStream(final InputStream inStream)\n
    '''
def setPort():
    '''returns None\n\n
    setPort(final int port)\n
    '''
def setProtocol():
    '''returns None\n\n
    setProtocol(final Protocol protocol)\n
    '''
def setProxyHost():
    '''returns None\n\n
    setProxyHost(final String host)\n
    '''
def setProxyPort():
    '''returns None\n\n
    setProxyPort(final int port)\n
    '''
def setSoTimeout():
    '''returns None\n\n
    setSoTimeout(final int timeout)\n
    '''
def shutdownOutput():
    '''returns None\n\n
    shutdownOutput()\n
    '''
def tunnelCreated():
    '''returns None\n\n
    tunnelCreated()\n
    '''
def write():
    '''returns None\n\n
    write(final byte[] data, final int offset, final int length)\n
    write(final byte[] data)\n
    '''
def writeLine():
    '''returns None\n\n
    writeLine()\n
    writeLine(final byte[] data)\n
    '''
def flushRequestOutputStream():
    '''returns None\n\n
    flushRequestOutputStream()\n
    '''
def getSoTimeout():
    '''returns int\n\n
    getSoTimeout()\n
    '''
def getVirtualHost():
    '''returns String\n\n
    getVirtualHost()\n
    '''
def setVirtualHost():
    '''returns None\n\n
    setVirtualHost(final String host)\n
    '''
def getSendBufferSize():
    '''returns int\n\n
    getSendBufferSize()\n
    '''
def setSendBufferSize():
    '''returns None\n\n
    setSendBufferSize(final int sendBufferSize)\n
    '''
def setSocketTimeout():
    '''returns None\n\n
    setSocketTimeout(final int timeout)\n
    '''
