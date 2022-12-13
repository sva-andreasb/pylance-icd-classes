def HttpMethodBase():
    '''public HttpMethodBase()
    public HttpMethodBase(String uri)
    '''
def getURI():
    '''public URI getURI()
    '''
def setURI():
    '''public void setURI(final URI uri)
    '''
def setFollowRedirects():
    '''public void setFollowRedirects(final boolean followRedirects)
    '''
def getFollowRedirects():
    '''public boolean getFollowRedirects()
    '''
def setHttp11():
    '''public void setHttp11(final boolean http11)
    '''
def getDoAuthentication():
    '''public boolean getDoAuthentication()
    '''
def setDoAuthentication():
    '''public void setDoAuthentication(final boolean doAuthentication)
    '''
def isHttp11():
    '''public boolean isHttp11()
    '''
def setPath():
    '''public void setPath(final String path)
    '''
def addRequestHeader():
    '''public void addRequestHeader(final Header header)
    public void addRequestHeader(final String headerName, final String headerValue)
    '''
def addResponseFooter():
    '''public void addResponseFooter(final Header footer)
    '''
def getPath():
    '''public String getPath()
    '''
def setQueryString():
    '''public void setQueryString(final String queryString)
    public void setQueryString(final NameValuePair[] params)
    '''
def getQueryString():
    '''public String getQueryString()
    '''
def setRequestHeader():
    '''public void setRequestHeader(final String headerName, final String headerValue)
    public void setRequestHeader(final Header header)
    '''
def getRequestHeader():
    '''public Header getRequestHeader(final String headerName)
    '''
def getRequestHeaders():
    '''public Header[] getRequestHeaders()
    public Header[] getRequestHeaders(final String headerName)
    '''
def getResponseHeaders():
    '''public Header[] getResponseHeaders(final String headerName)
    public Header[] getResponseHeaders()
    '''
def getStatusCode():
    '''public int getStatusCode()
    '''
def getStatusLine():
    '''public StatusLine getStatusLine()
    '''
def getResponseHeader():
    '''public Header getResponseHeader(final String headerName)
    '''
def getResponseContentLength():
    '''public long getResponseContentLength()
    '''
def getResponseBody():
    '''public byte[] getResponseBody()
    public byte[] getResponseBody(final int maxlen)
    '''
def getResponseBodyAsStream():
    '''public InputStream getResponseBodyAsStream()
    '''
def getResponseBodyAsString():
    '''public String getResponseBodyAsString()
    public String getResponseBodyAsString(final int maxlen)
    '''
def getResponseFooters():
    '''public Header[] getResponseFooters()
    '''
def getResponseFooter():
    '''public Header getResponseFooter(final String footerName)
    '''
def getStatusText():
    '''public String getStatusText()
    '''
def setStrictMode():
    '''public void setStrictMode(final boolean strictMode)
    '''
def isStrictMode():
    '''public boolean isStrictMode()
    '''
def execute():
    '''public int execute(final HttpState state, final HttpConnection conn)
    '''
def abort():
    '''public void abort()
    '''
def hasBeenUsed():
    '''public boolean hasBeenUsed()
    '''
def recycle():
    '''public void recycle()
    '''
def releaseConnection():
    '''public void releaseConnection()
    '''
def removeRequestHeader():
    '''public void removeRequestHeader(final String headerName)
    public void removeRequestHeader(final Header header)
    '''
def validate():
    '''public boolean validate()
    '''
def responseConsumed():
    '''public void responseConsumed()
    '''
def getParams():
    '''public HttpMethodParams getParams()
    '''
def setParams():
    '''public void setParams(final HttpMethodParams params)
    '''
def getEffectiveVersion():
    '''public HttpVersion getEffectiveVersion()
    '''
def getProxyAuthenticationRealm():
    '''public String getProxyAuthenticationRealm()
    '''
def getAuthenticationRealm():
    '''public String getAuthenticationRealm()
    '''
def getRequestCharSet():
    '''public String getRequestCharSet()
    '''
def getResponseCharSet():
    '''public String getResponseCharSet()
    '''
def getRecoverableExceptionCount():
    '''public int getRecoverableExceptionCount()
    '''
def getHostConfiguration():
    '''public HostConfiguration getHostConfiguration()
    '''
def setHostConfiguration():
    '''public void setHostConfiguration(final HostConfiguration hostconfig)
    '''
def getMethodRetryHandler():
    '''public MethodRetryHandler getMethodRetryHandler()
    '''
def setMethodRetryHandler():
    '''public void setMethodRetryHandler(final MethodRetryHandler handler)
    '''
def getHostAuthState():
    '''public AuthState getHostAuthState()
    '''
def getProxyAuthState():
    '''public AuthState getProxyAuthState()
    '''
def isAborted():
    '''public boolean isAborted()
    '''
def isRequestSent():
    '''public boolean isRequestSent()
    '''
