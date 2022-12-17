def ():
    '''returns HttpMethodBase\n\n
    ()\n
    (String uri)\n
    '''
def getURI():
    '''returns URI\n\n
    getURI()\n
    '''
def setURI():
    '''returns None\n\n
    setURI(final URI uri)\n
    '''
def setFollowRedirects():
    '''returns None\n\n
    setFollowRedirects(final boolean followRedirects)\n
    '''
def getFollowRedirects():
    '''returns boolean\n\n
    getFollowRedirects()\n
    '''
def setHttp11():
    '''returns None\n\n
    setHttp11(final boolean http11)\n
    '''
def getDoAuthentication():
    '''returns boolean\n\n
    getDoAuthentication()\n
    '''
def setDoAuthentication():
    '''returns None\n\n
    setDoAuthentication(final boolean doAuthentication)\n
    '''
def isHttp11():
    '''returns boolean\n\n
    isHttp11()\n
    '''
def setPath():
    '''returns None\n\n
    setPath(final String path)\n
    '''
def addRequestHeader():
    '''returns None\n\n
    addRequestHeader(final Header header)\n
    addRequestHeader(final String headerName, final String headerValue)\n
    '''
def addResponseFooter():
    '''returns None\n\n
    addResponseFooter(final Header footer)\n
    '''
def getPath():
    '''returns String\n\n
    getPath()\n
    '''
def setQueryString():
    '''returns None\n\n
    setQueryString(final String queryString)\n
    setQueryString(final NameValuePair[] params)\n
    '''
def getQueryString():
    '''returns String\n\n
    getQueryString()\n
    '''
def setRequestHeader():
    '''returns None\n\n
    setRequestHeader(final String headerName, final String headerValue)\n
    setRequestHeader(final Header header)\n
    '''
def getRequestHeader():
    '''returns Header\n\n
    getRequestHeader(final String headerName)\n
    '''
def getRequestHeaders():
    '''returns Header[]\n\n
    getRequestHeaders()\n
    getRequestHeaders(final String headerName)\n
    '''
def getResponseHeaders():
    '''returns Header[]\n\n
    getResponseHeaders(final String headerName)\n
    getResponseHeaders()\n
    '''
def getStatusCode():
    '''returns int\n\n
    getStatusCode()\n
    '''
def getStatusLine():
    '''returns StatusLine\n\n
    getStatusLine()\n
    '''
def getResponseHeader():
    '''returns Header\n\n
    getResponseHeader(final String headerName)\n
    '''
def getResponseContentLength():
    '''returns long\n\n
    getResponseContentLength()\n
    '''
def getResponseBody():
    '''returns byte[]\n\n
    getResponseBody()\n
    getResponseBody(final int maxlen)\n
    '''
def getResponseBodyAsStream():
    '''returns InputStream\n\n
    getResponseBodyAsStream()\n
    '''
def getResponseBodyAsString():
    '''returns String\n\n
    getResponseBodyAsString()\n
    getResponseBodyAsString(final int maxlen)\n
    '''
def getResponseFooters():
    '''returns Header[]\n\n
    getResponseFooters()\n
    '''
def getResponseFooter():
    '''returns Header\n\n
    getResponseFooter(final String footerName)\n
    '''
def getStatusText():
    '''returns String\n\n
    getStatusText()\n
    '''
def setStrictMode():
    '''returns None\n\n
    setStrictMode(final boolean strictMode)\n
    '''
def isStrictMode():
    '''returns boolean\n\n
    isStrictMode()\n
    '''
def execute():
    '''returns int\n\n
    execute(final HttpState state, final HttpConnection conn)\n
    '''
def abort():
    '''returns None\n\n
    abort()\n
    '''
def hasBeenUsed():
    '''returns boolean\n\n
    hasBeenUsed()\n
    '''
def recycle():
    '''returns None\n\n
    recycle()\n
    '''
def releaseConnection():
    '''returns None\n\n
    releaseConnection()\n
    '''
def removeRequestHeader():
    '''returns None\n\n
    removeRequestHeader(final String headerName)\n
    removeRequestHeader(final Header header)\n
    '''
def validate():
    '''returns boolean\n\n
    validate()\n
    '''
def responseConsumed():
    '''returns None\n\n
    responseConsumed()\n
    '''
def getParams():
    '''returns HttpMethodParams\n\n
    getParams()\n
    '''
def setParams():
    '''returns None\n\n
    setParams(final HttpMethodParams params)\n
    '''
def getEffectiveVersion():
    '''returns HttpVersion\n\n
    getEffectiveVersion()\n
    '''
def getProxyAuthenticationRealm():
    '''returns String\n\n
    getProxyAuthenticationRealm()\n
    '''
def getAuthenticationRealm():
    '''returns String\n\n
    getAuthenticationRealm()\n
    '''
def getRequestCharSet():
    '''returns String\n\n
    getRequestCharSet()\n
    '''
def getResponseCharSet():
    '''returns String\n\n
    getResponseCharSet()\n
    '''
def getRecoverableExceptionCount():
    '''returns int\n\n
    getRecoverableExceptionCount()\n
    '''
def getHostConfiguration():
    '''returns HostConfiguration\n\n
    getHostConfiguration()\n
    '''
def setHostConfiguration():
    '''returns None\n\n
    setHostConfiguration(final HostConfiguration hostconfig)\n
    '''
def getMethodRetryHandler():
    '''returns MethodRetryHandler\n\n
    getMethodRetryHandler()\n
    '''
def setMethodRetryHandler():
    '''returns None\n\n
    setMethodRetryHandler(final MethodRetryHandler handler)\n
    '''
def getHostAuthState():
    '''returns AuthState\n\n
    getHostAuthState()\n
    '''
def getProxyAuthState():
    '''returns AuthState\n\n
    getProxyAuthState()\n
    '''
def isAborted():
    '''returns boolean\n\n
    isAborted()\n
    '''
def isRequestSent():
    '''returns boolean\n\n
    isRequestSent()\n
    '''
