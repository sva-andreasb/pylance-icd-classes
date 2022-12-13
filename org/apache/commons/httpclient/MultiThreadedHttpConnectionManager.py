DEFAULT_MAX_HOST_CONNECTIONS = "int  2"
DEFAULT_MAX_TOTAL_CONNECTIONS = "int  20"
def shutdownAll():
'''public static void shutdownAll()
'''
pass
def MultiThreadedHttpConnectionManager():
'''public MultiThreadedHttpConnectionManager()
'''
pass
def shutdown():
'''public synchronized void shutdown()
public synchronized void shutdown()
public void shutdown()
'''
pass
def isConnectionStaleCheckingEnabled():
'''public boolean isConnectionStaleCheckingEnabled()
'''
pass
def setConnectionStaleCheckingEnabled():
'''public void setConnectionStaleCheckingEnabled(final boolean connectionStaleCheckingEnabled)
'''
pass
def setMaxConnectionsPerHost():
'''public void setMaxConnectionsPerHost(final int maxHostConnections)
'''
pass
def getMaxConnectionsPerHost():
'''public int getMaxConnectionsPerHost()
'''
pass
def setMaxTotalConnections():
'''public void setMaxTotalConnections(final int maxTotalConnections)
'''
pass
def getMaxTotalConnections():
'''public int getMaxTotalConnections()
'''
pass
def getConnection():
'''public HttpConnection getConnection(final HostConfiguration hostConfiguration)
public HttpConnection getConnection(final HostConfiguration hostConfiguration, final long timeout)
'''
pass
def getConnectionWithTimeout():
'''public HttpConnection getConnectionWithTimeout(final HostConfiguration hostConfiguration, final long timeout)
'''
pass
def getConnectionsInPool():
'''public int getConnectionsInPool(final HostConfiguration hostConfiguration)
public int getConnectionsInPool()
'''
pass
def getConnectionsInUse():
'''public int getConnectionsInUse(final HostConfiguration hostConfiguration)
public int getConnectionsInUse()
'''
pass
def deleteClosedConnections():
'''public void deleteClosedConnections()
public synchronized void deleteClosedConnections()
'''
pass
def closeIdleConnections():
'''public void closeIdleConnections(final long idleTimeout)
public synchronized void closeIdleConnections(final long idleTimeout)
'''
pass
def releaseConnection():
'''public void releaseConnection(HttpConnection conn)
public void releaseConnection()
'''
pass
def getParams():
'''public HttpConnectionManagerParams getParams()
public HttpConnectionParams getParams()
'''
pass
def setParams():
'''public void setParams(final HttpConnectionManagerParams params)
public void setParams(final HttpConnectionParams params)
'''
pass
def createConnection():
'''public synchronized HttpConnection createConnection(final HostConfiguration hostConfiguration)
'''
pass
def handleLostConnection():
'''public synchronized void handleLostConnection(final HostConfiguration config)
'''
pass
def getHostPool():
'''public synchronized HostConnectionPool getHostPool(final HostConfiguration hostConfiguration, final boolean create)
'''
pass
def getFreeConnection():
'''public synchronized HttpConnection getFreeConnection(final HostConfiguration hostConfiguration)
'''
pass
def deleteLeastUsedConnection():
'''public synchronized void deleteLeastUsedConnection()
'''
pass
def notifyWaitingThread():
'''public synchronized void notifyWaitingThread(final HostConfiguration configuration)
public synchronized void notifyWaitingThread(final HostConnectionPool hostPool)
'''
pass
def freeConnection():
'''public void freeConnection(final HttpConnection conn)
'''
pass
def ReferenceQueueThread():
'''public ReferenceQueueThread()
'''
pass
def run():
'''public void run()
'''
pass
def HttpConnectionWithReference():
'''public HttpConnectionWithReference(final HostConfiguration hostConfiguration)
'''
pass
def HttpConnectionAdapter():
'''public HttpConnectionAdapter(final HttpConnection connection)
'''
pass
def close():
'''public void close()
'''
pass
def getLocalAddress():
'''public InetAddress getLocalAddress()
'''
pass
def isStaleCheckingEnabled():
'''public boolean isStaleCheckingEnabled()
'''
pass
def setLocalAddress():
'''public void setLocalAddress(final InetAddress localAddress)
'''
pass
def setStaleCheckingEnabled():
'''public void setStaleCheckingEnabled(final boolean staleCheckEnabled)
'''
pass
def getHost():
'''public String getHost()
'''
pass
def getHttpConnectionManager():
'''public HttpConnectionManager getHttpConnectionManager()
'''
pass
def getLastResponseInputStream():
'''public InputStream getLastResponseInputStream()
'''
pass
def getPort():
'''public int getPort()
'''
pass
def getProtocol():
'''public Protocol getProtocol()
'''
pass
def getProxyHost():
'''public String getProxyHost()
'''
pass
def getProxyPort():
'''public int getProxyPort()
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
def isOpen():
'''public boolean isOpen()
'''
pass
def closeIfStale():
'''public boolean closeIfStale()
'''
pass
def isProxied():
'''public boolean isProxied()
'''
pass
def isResponseAvailable():
'''public boolean isResponseAvailable()
public boolean isResponseAvailable(final int timeout)
'''
pass
def isSecure():
'''public boolean isSecure()
'''
pass
def isTransparent():
'''public boolean isTransparent()
'''
pass
def open():
'''public void open()
'''
pass
def print():
'''public void print(final String data)
public void print(final String data, final String charset)
'''
pass
def printLine():
'''public void printLine()
public void printLine(final String data)
public void printLine(final String data, final String charset)
'''
pass
def readLine():
'''public String readLine()
public String readLine(final String charset)
'''
pass
def setConnectionTimeout():
'''public void setConnectionTimeout(final int timeout)
'''
pass
def setHost():
'''public void setHost(final String host)
'''
pass
def setHttpConnectionManager():
'''public void setHttpConnectionManager(final HttpConnectionManager httpConnectionManager)
'''
pass
def setLastResponseInputStream():
'''public void setLastResponseInputStream(final InputStream inStream)
'''
pass
def setPort():
'''public void setPort(final int port)
'''
pass
def setProtocol():
'''public void setProtocol(final Protocol protocol)
'''
pass
def setProxyHost():
'''public void setProxyHost(final String host)
'''
pass
def setProxyPort():
'''public void setProxyPort(final int port)
'''
pass
def setSoTimeout():
'''public void setSoTimeout(final int timeout)
'''
pass
def shutdownOutput():
'''public void shutdownOutput()
'''
pass
def tunnelCreated():
'''public void tunnelCreated()
'''
pass
def write():
'''public void write(final byte[] data, final int offset, final int length)
public void write(final byte[] data)
'''
pass
def writeLine():
'''public void writeLine()
public void writeLine(final byte[] data)
'''
pass
def flushRequestOutputStream():
'''public void flushRequestOutputStream()
'''
pass
def getSoTimeout():
'''public int getSoTimeout()
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
def getSendBufferSize():
'''public int getSendBufferSize()
'''
pass
def setSendBufferSize():
'''public void setSendBufferSize(final int sendBufferSize)
'''
pass
def setSocketTimeout():
'''public void setSocketTimeout(final int timeout)
'''
pass
