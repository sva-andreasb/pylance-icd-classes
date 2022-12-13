def HttpMethodBase():
'''public HttpMethodBase()
public HttpMethodBase(String uri)
'''
pass
def getURI():
'''public URI getURI()
'''
pass
def setURI():
'''public void setURI(final URI uri)
'''
pass
def setFollowRedirects():
'''public void setFollowRedirects(final boolean followRedirects)
'''
pass
def getFollowRedirects():
'''public boolean getFollowRedirects()
'''
pass
def setHttp11():
'''public void setHttp11(final boolean http11)
'''
pass
def getDoAuthentication():
'''public boolean getDoAuthentication()
'''
pass
def setDoAuthentication():
'''public void setDoAuthentication(final boolean doAuthentication)
'''
pass
def isHttp11():
'''public boolean isHttp11()
'''
pass
def setPath():
'''public void setPath(final String path)
'''
pass
def addRequestHeader():
'''public void addRequestHeader(final Header header)
public void addRequestHeader(final String headerName, final String headerValue)
'''
pass
def addResponseFooter():
'''public void addResponseFooter(final Header footer)
'''
pass
def getPath():
'''public String getPath()
'''
pass
def setQueryString():
'''public void setQueryString(final String queryString)
public void setQueryString(final NameValuePair[] params)
'''
pass
def getQueryString():
'''public String getQueryString()
'''
pass
def setRequestHeader():
'''public void setRequestHeader(final String headerName, final String headerValue)
public void setRequestHeader(final Header header)
'''
pass
def getRequestHeader():
'''public Header getRequestHeader(final String headerName)
'''
pass
def getRequestHeaders():
'''public Header[] getRequestHeaders()
public Header[] getRequestHeaders(final String headerName)
'''
pass
def getResponseHeaders():
'''public Header[] getResponseHeaders(final String headerName)
public Header[] getResponseHeaders()
'''
pass
def getStatusCode():
'''public int getStatusCode()
'''
pass
def getStatusLine():
'''public StatusLine getStatusLine()
'''
pass
def getResponseHeader():
'''public Header getResponseHeader(final String headerName)
'''
pass
def getResponseContentLength():
'''public long getResponseContentLength()
'''
pass
def getResponseBody():
'''public byte[] getResponseBody()
public byte[] getResponseBody(final int maxlen)
'''
pass
def getResponseBodyAsStream():
'''public InputStream getResponseBodyAsStream()
'''
pass
def getResponseBodyAsString():
'''public String getResponseBodyAsString()
public String getResponseBodyAsString(final int maxlen)
'''
pass
def getResponseFooters():
'''public Header[] getResponseFooters()
'''
pass
def getResponseFooter():
'''public Header getResponseFooter(final String footerName)
'''
pass
def getStatusText():
'''public String getStatusText()
'''
pass
def setStrictMode():
'''public void setStrictMode(final boolean strictMode)
'''
pass
def isStrictMode():
'''public boolean isStrictMode()
'''
pass
def execute():
'''public int execute(final HttpState state, final HttpConnection conn)
'''
pass
def abort():
'''public void abort()
'''
pass
def hasBeenUsed():
'''public boolean hasBeenUsed()
'''
pass
def recycle():
'''public void recycle()
'''
pass
def releaseConnection():
'''public void releaseConnection()
'''
pass
def removeRequestHeader():
'''public void removeRequestHeader(final String headerName)
public void removeRequestHeader(final Header header)
'''
pass
def validate():
'''public boolean validate()
'''
pass
def responseConsumed():
'''public void responseConsumed()
'''
pass
def getParams():
'''public HttpMethodParams getParams()
'''
pass
def setParams():
'''public void setParams(final HttpMethodParams params)
'''
pass
def getEffectiveVersion():
'''public HttpVersion getEffectiveVersion()
'''
pass
def getProxyAuthenticationRealm():
'''public String getProxyAuthenticationRealm()
'''
pass
def getAuthenticationRealm():
'''public String getAuthenticationRealm()
'''
pass
def getRequestCharSet():
'''public String getRequestCharSet()
'''
pass
def getResponseCharSet():
'''public String getResponseCharSet()
'''
pass
def getRecoverableExceptionCount():
'''public int getRecoverableExceptionCount()
'''
pass
def getHostConfiguration():
'''public HostConfiguration getHostConfiguration()
'''
pass
def setHostConfiguration():
'''public void setHostConfiguration(final HostConfiguration hostconfig)
'''
pass
def getMethodRetryHandler():
'''public MethodRetryHandler getMethodRetryHandler()
'''
pass
def setMethodRetryHandler():
'''public void setMethodRetryHandler(final MethodRetryHandler handler)
'''
pass
def getHostAuthState():
'''public AuthState getHostAuthState()
'''
pass
def getProxyAuthState():
'''public AuthState getProxyAuthState()
'''
pass
def isAborted():
'''public boolean isAborted()
'''
pass
def isRequestSent():
'''public boolean isRequestSent()
'''
pass
