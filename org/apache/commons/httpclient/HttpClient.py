def HttpClient():
    '''public HttpClient()
    public HttpClient(final HttpClientParams params)
    public HttpClient(final HttpClientParams params, final HttpConnectionManager httpConnectionManager)
    public HttpClient(final HttpConnectionManager httpConnectionManager)
    '''
def getState():
    '''public synchronized HttpState getState()
    '''
def setState():
    '''public synchronized void setState(final HttpState state)
    '''
def setStrictMode():
    '''public synchronized void setStrictMode(final boolean strictMode)
    '''
def isStrictMode():
    '''public synchronized boolean isStrictMode()
    '''
def setTimeout():
    '''public synchronized void setTimeout(final int newTimeoutInMilliseconds)
    '''
def setHttpConnectionFactoryTimeout():
    '''public synchronized void setHttpConnectionFactoryTimeout(final long timeout)
    '''
def setConnectionTimeout():
    '''public synchronized void setConnectionTimeout(final int newTimeoutInMilliseconds)
    '''
def executeMethod():
    '''public int executeMethod(final HttpMethod method)
    public int executeMethod(final HostConfiguration hostConfiguration, final HttpMethod method)
    public int executeMethod(HostConfiguration hostconfig, final HttpMethod method, final HttpState state)
    '''
def getHost():
    '''public String getHost()
    '''
def getPort():
    '''public int getPort()
    '''
def getHostConfiguration():
    '''public synchronized HostConfiguration getHostConfiguration()
    '''
def setHostConfiguration():
    '''public synchronized void setHostConfiguration(final HostConfiguration hostConfiguration)
    '''
def getHttpConnectionManager():
    '''public synchronized HttpConnectionManager getHttpConnectionManager()
    '''
def setHttpConnectionManager():
    '''public synchronized void setHttpConnectionManager(final HttpConnectionManager httpConnectionManager)
    '''
def getParams():
    '''public HttpClientParams getParams()
    '''
def setParams():
    '''public void setParams(final HttpClientParams params)
    '''
