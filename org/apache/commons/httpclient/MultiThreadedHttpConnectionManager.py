DEFAULT_MAX_HOST_CONNECTIONS = "int  2"
DEFAULT_MAX_TOTAL_CONNECTIONS = "int  20"
def shutdownAll():
    '''    public static void shutdownAll()
    '''
def MultiThreadedHttpConnectionManager():
    '''    public MultiThreadedHttpConnectionManager()
    '''
def shutdown():
    '''    public synchronized void shutdown()
    public synchronized void shutdown()
    public void shutdown()
    '''
def isConnectionStaleCheckingEnabled():
    '''    public boolean isConnectionStaleCheckingEnabled()
    '''
def setConnectionStaleCheckingEnabled():
    '''    public void setConnectionStaleCheckingEnabled(final boolean connectionStaleCheckingEnabled)
    '''
def setMaxConnectionsPerHost():
    '''    public void setMaxConnectionsPerHost(final int maxHostConnections)
    '''
def getMaxConnectionsPerHost():
    '''    public int getMaxConnectionsPerHost()
    '''
def setMaxTotalConnections():
    '''    public void setMaxTotalConnections(final int maxTotalConnections)
    '''
def getMaxTotalConnections():
    '''    public int getMaxTotalConnections()
    '''
def getConnection():
    '''    public HttpConnection getConnection(final HostConfiguration hostConfiguration)
    public HttpConnection getConnection(final HostConfiguration hostConfiguration, final long timeout)
    '''
def getConnectionWithTimeout():
    '''    public HttpConnection getConnectionWithTimeout(final HostConfiguration hostConfiguration, final long timeout)
    '''
def getConnectionsInPool():
    '''    public int getConnectionsInPool(final HostConfiguration hostConfiguration)
    public int getConnectionsInPool()
    '''
def getConnectionsInUse():
    '''    public int getConnectionsInUse(final HostConfiguration hostConfiguration)
    public int getConnectionsInUse()
    '''
def deleteClosedConnections():
    '''    public void deleteClosedConnections()
    public synchronized void deleteClosedConnections()
    '''
def closeIdleConnections():
    '''    public void closeIdleConnections(final long idleTimeout)
    public synchronized void closeIdleConnections(final long idleTimeout)
    '''
def releaseConnection():
    '''    public void releaseConnection(HttpConnection conn)
    public void releaseConnection()
    '''
def getParams():
    '''    public HttpConnectionManagerParams getParams()
    public HttpConnectionParams getParams()
    '''
def setParams():
    '''    public void setParams(final HttpConnectionManagerParams params)
    public void setParams(final HttpConnectionParams params)
    '''
def createConnection():
    '''    public synchronized HttpConnection createConnection(final HostConfiguration hostConfiguration)
    '''
def handleLostConnection():
    '''    public synchronized void handleLostConnection(final HostConfiguration config)
    '''
def getHostPool():
    '''    public synchronized HostConnectionPool getHostPool(final HostConfiguration hostConfiguration, final boolean create)
    '''
def getFreeConnection():
    '''    public synchronized HttpConnection getFreeConnection(final HostConfiguration hostConfiguration)
    '''
def deleteLeastUsedConnection():
    '''    public synchronized void deleteLeastUsedConnection()
    '''
def notifyWaitingThread():
    '''    public synchronized void notifyWaitingThread(final HostConfiguration configuration)
    public synchronized void notifyWaitingThread(final HostConnectionPool hostPool)
    '''
def freeConnection():
    '''    public void freeConnection(final HttpConnection conn)
    '''
def ReferenceQueueThread():
    '''    public ReferenceQueueThread()
    '''
def run():
    '''    public void run()
    '''
def HttpConnectionWithReference():
    '''    public HttpConnectionWithReference(final HostConfiguration hostConfiguration)
    '''
def HttpConnectionAdapter():
    '''    public HttpConnectionAdapter(final HttpConnection connection)
    '''
def close():
    '''    public void close()
    '''
def getLocalAddress():
    '''    public InetAddress getLocalAddress()
    '''
def isStaleCheckingEnabled():
    '''    public boolean isStaleCheckingEnabled()
    '''
def setLocalAddress():
    '''    public void setLocalAddress(final InetAddress localAddress)
    '''
def setStaleCheckingEnabled():
    '''    public void setStaleCheckingEnabled(final boolean staleCheckEnabled)
    '''
def getHost():
    '''    public String getHost()
    '''
def getHttpConnectionManager():
    '''    public HttpConnectionManager getHttpConnectionManager()
    '''
def getLastResponseInputStream():
    '''    public InputStream getLastResponseInputStream()
    '''
def getPort():
    '''    public int getPort()
    '''
def getProtocol():
    '''    public Protocol getProtocol()
    '''
def getProxyHost():
    '''    public String getProxyHost()
    '''
def getProxyPort():
    '''    public int getProxyPort()
    '''
def getRequestOutputStream():
    '''    public OutputStream getRequestOutputStream()
    '''
def getResponseInputStream():
    '''    public InputStream getResponseInputStream()
    '''
def isOpen():
    '''    public boolean isOpen()
    '''
def closeIfStale():
    '''    public boolean closeIfStale()
    '''
def isProxied():
    '''    public boolean isProxied()
    '''
def isResponseAvailable():
    '''    public boolean isResponseAvailable()
    public boolean isResponseAvailable(final int timeout)
    '''
def isSecure():
    '''    public boolean isSecure()
    '''
def isTransparent():
    '''    public boolean isTransparent()
    '''
def open():
    '''    public void open()
    '''
def print():
    '''    public void print(final String data)
    public void print(final String data, final String charset)
    '''
def printLine():
    '''    public void printLine()
    public void printLine(final String data)
    public void printLine(final String data, final String charset)
    '''
def readLine():
    '''    public String readLine()
    public String readLine(final String charset)
    '''
def setConnectionTimeout():
    '''    public void setConnectionTimeout(final int timeout)
    '''
def setHost():
    '''    public void setHost(final String host)
    '''
def setHttpConnectionManager():
    '''    public void setHttpConnectionManager(final HttpConnectionManager httpConnectionManager)
    '''
def setLastResponseInputStream():
    '''    public void setLastResponseInputStream(final InputStream inStream)
    '''
def setPort():
    '''    public void setPort(final int port)
    '''
def setProtocol():
    '''    public void setProtocol(final Protocol protocol)
    '''
def setProxyHost():
    '''    public void setProxyHost(final String host)
    '''
def setProxyPort():
    '''    public void setProxyPort(final int port)
    '''
def setSoTimeout():
    '''    public void setSoTimeout(final int timeout)
    '''
def shutdownOutput():
    '''    public void shutdownOutput()
    '''
def tunnelCreated():
    '''    public void tunnelCreated()
    '''
def write():
    '''    public void write(final byte[] data, final int offset, final int length)
    public void write(final byte[] data)
    '''
def writeLine():
    '''    public void writeLine()
    public void writeLine(final byte[] data)
    '''
def flushRequestOutputStream():
    '''    public void flushRequestOutputStream()
    '''
def getSoTimeout():
    '''    public int getSoTimeout()
    '''
def getVirtualHost():
    '''    public String getVirtualHost()
    '''
def setVirtualHost():
    '''    public void setVirtualHost(final String host)
    '''
def getSendBufferSize():
    '''    public int getSendBufferSize()
    '''
def setSendBufferSize():
    '''    public void setSendBufferSize(final int sendBufferSize)
    '''
def setSocketTimeout():
    '''    public void setSocketTimeout(final int timeout)
    '''
