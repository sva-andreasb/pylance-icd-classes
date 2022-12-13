def ProxyClient():
'''public ProxyClient()
public ProxyClient(final HttpClientParams params)
'''
pass
def getState():
'''public synchronized HttpState getState()
'''
pass
def setState():
'''public synchronized void setState(final HttpState state)
'''
pass
def getHostConfiguration():
'''public synchronized HostConfiguration getHostConfiguration()
'''
pass
def setHostConfiguration():
'''public synchronized void setHostConfiguration(final HostConfiguration hostConfiguration)
'''
pass
def getParams():
'''public synchronized HttpClientParams getParams()
public HttpConnectionManagerParams getParams()
'''
pass
def setParams():
'''public synchronized void setParams(final HttpClientParams params)
public void setParams(final HttpConnectionManagerParams params)
'''
pass
def connect():
'''public ConnectResponse connect()
'''
pass
def getConnectMethod():
'''public ConnectMethod getConnectMethod()
'''
pass
def getSocket():
'''public Socket getSocket()
'''
pass
def closeIdleConnections():
'''public void closeIdleConnections(final long idleTimeout)
'''
pass
def getConnection():
'''public HttpConnection getConnection()
public HttpConnection getConnection(final HostConfiguration hostConfiguration, final long timeout)
public HttpConnection getConnection(final HostConfiguration hostConfiguration)
'''
pass
def setConnectionParams():
'''public void setConnectionParams(final HttpParams httpParams)
'''
pass
def getConnectionWithTimeout():
'''public HttpConnection getConnectionWithTimeout(final HostConfiguration hostConfiguration, final long timeout)
'''
pass
def releaseConnection():
'''public void releaseConnection(final HttpConnection conn)
'''
pass
