def HttpClient():
'''public HttpClient()
public HttpClient(final HttpClientParams params)
public HttpClient(final HttpClientParams params, final HttpConnectionManager httpConnectionManager)
public HttpClient(final HttpConnectionManager httpConnectionManager)
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
def setStrictMode():
'''public synchronized void setStrictMode(final boolean strictMode)
'''
pass
def isStrictMode():
'''public synchronized boolean isStrictMode()
'''
pass
def setTimeout():
'''public synchronized void setTimeout(final int newTimeoutInMilliseconds)
'''
pass
def setHttpConnectionFactoryTimeout():
'''public synchronized void setHttpConnectionFactoryTimeout(final long timeout)
'''
pass
def setConnectionTimeout():
'''public synchronized void setConnectionTimeout(final int newTimeoutInMilliseconds)
'''
pass
def executeMethod():
'''public int executeMethod(final HttpMethod method)
public int executeMethod(final HostConfiguration hostConfiguration, final HttpMethod method)
public int executeMethod(HostConfiguration hostconfig, final HttpMethod method, final HttpState state)
'''
pass
def getHost():
'''public String getHost()
'''
pass
def getPort():
'''public int getPort()
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
def getHttpConnectionManager():
'''public synchronized HttpConnectionManager getHttpConnectionManager()
'''
pass
def setHttpConnectionManager():
'''public synchronized void setHttpConnectionManager(final HttpConnectionManager httpConnectionManager)
'''
pass
def getParams():
'''public HttpClientParams getParams()
'''
pass
def setParams():
'''public void setParams(final HttpClientParams params)
'''
pass
