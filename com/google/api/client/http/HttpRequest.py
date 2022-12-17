VERSION = "String  \"1.25.0\""
USER_AGENT_SUFFIX = "String  \"Google-HTTP-Java-Client/1.25.0 (gzip)\""
DEFAULT_NUMBER_OF_RETRIES = "int  10"
def getTransport():
    '''returns HttpTransport\n\n
    getTransport()\n
    '''
def getRequestMethod():
    '''returns String\n\n
    getRequestMethod()\n
    '''
def setRequestMethod():
    '''returns HttpRequest\n\n
    setRequestMethod(final String requestMethod)\n
    '''
def getUrl():
    '''returns GenericUrl\n\n
    getUrl()\n
    '''
def setUrl():
    '''returns HttpRequest\n\n
    setUrl(final GenericUrl url)\n
    '''
def getContent():
    '''returns HttpContent\n\n
    getContent()\n
    '''
def setContent():
    '''returns HttpRequest\n\n
    setContent(final HttpContent content)\n
    '''
def getEncoding():
    '''returns HttpEncoding\n\n
    getEncoding()\n
    '''
def setEncoding():
    '''returns HttpRequest\n\n
    setEncoding(final HttpEncoding encoding)\n
    '''
def getBackOffPolicy():
    '''returns BackOffPolicy\n\n
    getBackOffPolicy()\n
    '''
def setBackOffPolicy():
    '''returns HttpRequest\n\n
    setBackOffPolicy(final BackOffPolicy backOffPolicy)\n
    '''
def getContentLoggingLimit():
    '''returns int\n\n
    getContentLoggingLimit()\n
    '''
def setContentLoggingLimit():
    '''returns HttpRequest\n\n
    setContentLoggingLimit(final int contentLoggingLimit)\n
    '''
def isLoggingEnabled():
    '''returns boolean\n\n
    isLoggingEnabled()\n
    '''
def setLoggingEnabled():
    '''returns HttpRequest\n\n
    setLoggingEnabled(final boolean loggingEnabled)\n
    '''
def isCurlLoggingEnabled():
    '''returns boolean\n\n
    isCurlLoggingEnabled()\n
    '''
def setCurlLoggingEnabled():
    '''returns HttpRequest\n\n
    setCurlLoggingEnabled(final boolean curlLoggingEnabled)\n
    '''
def getConnectTimeout():
    '''returns int\n\n
    getConnectTimeout()\n
    '''
def setConnectTimeout():
    '''returns HttpRequest\n\n
    setConnectTimeout(final int connectTimeout)\n
    '''
def getReadTimeout():
    '''returns int\n\n
    getReadTimeout()\n
    '''
def setReadTimeout():
    '''returns HttpRequest\n\n
    setReadTimeout(final int readTimeout)\n
    '''
def getHeaders():
    '''returns HttpHeaders\n\n
    getHeaders()\n
    '''
def setHeaders():
    '''returns HttpRequest\n\n
    setHeaders(final HttpHeaders headers)\n
    '''
def getResponseHeaders():
    '''returns HttpHeaders\n\n
    getResponseHeaders()\n
    '''
def setResponseHeaders():
    '''returns HttpRequest\n\n
    setResponseHeaders(final HttpHeaders responseHeaders)\n
    '''
def getInterceptor():
    '''returns HttpExecuteInterceptor\n\n
    getInterceptor()\n
    '''
def setInterceptor():
    '''returns HttpRequest\n\n
    setInterceptor(final HttpExecuteInterceptor interceptor)\n
    '''
def getUnsuccessfulResponseHandler():
    '''returns HttpUnsuccessfulResponseHandler\n\n
    getUnsuccessfulResponseHandler()\n
    '''
def setUnsuccessfulResponseHandler():
    '''returns HttpRequest\n\n
    setUnsuccessfulResponseHandler(final HttpUnsuccessfulResponseHandler unsuccessfulResponseHandler)\n
    '''
def getIOExceptionHandler():
    '''returns HttpIOExceptionHandler\n\n
    getIOExceptionHandler()\n
    '''
def setIOExceptionHandler():
    '''returns HttpRequest\n\n
    setIOExceptionHandler(final HttpIOExceptionHandler ioExceptionHandler)\n
    '''
def getResponseInterceptor():
    '''returns HttpResponseInterceptor\n\n
    getResponseInterceptor()\n
    '''
def setResponseInterceptor():
    '''returns HttpRequest\n\n
    setResponseInterceptor(final HttpResponseInterceptor responseInterceptor)\n
    '''
def getNumberOfRetries():
    '''returns int\n\n
    getNumberOfRetries()\n
    '''
def setNumberOfRetries():
    '''returns HttpRequest\n\n
    setNumberOfRetries(final int numRetries)\n
    '''
def setParser():
    '''returns HttpRequest\n\n
    setParser(final ObjectParser parser)\n
    '''
def getFollowRedirects():
    '''returns boolean\n\n
    getFollowRedirects()\n
    '''
def setFollowRedirects():
    '''returns HttpRequest\n\n
    setFollowRedirects(final boolean followRedirects)\n
    '''
def getThrowExceptionOnExecuteError():
    '''returns boolean\n\n
    getThrowExceptionOnExecuteError()\n
    '''
def setThrowExceptionOnExecuteError():
    '''returns HttpRequest\n\n
    setThrowExceptionOnExecuteError(final boolean throwExceptionOnExecuteError)\n
    '''
def getRetryOnExecuteIOException():
    '''returns boolean\n\n
    getRetryOnExecuteIOException()\n
    '''
def setRetryOnExecuteIOException():
    '''returns HttpRequest\n\n
    setRetryOnExecuteIOException(final boolean retryOnExecuteIOException)\n
    '''
def getSuppressUserAgentSuffix():
    '''returns boolean\n\n
    getSuppressUserAgentSuffix()\n
    '''
def setSuppressUserAgentSuffix():
    '''returns HttpRequest\n\n
    setSuppressUserAgentSuffix(final boolean suppressUserAgentSuffix)\n
    '''
def execute():
    '''returns HttpResponse\n\n
    execute()\n
    '''
def executeAsync():
    '''returns Future<HttpResponse>\n\n
    executeAsync(final Executor executor)\n
    executeAsync()\n
    '''
def call():
    '''returns HttpResponse\n\n
    call()\n
    '''
def handleRedirect():
    '''returns boolean\n\n
    handleRedirect(final int statusCode, final HttpHeaders responseHeaders)\n
    '''
def getSleeper():
    '''returns Sleeper\n\n
    getSleeper()\n
    '''
def setSleeper():
    '''returns HttpRequest\n\n
    setSleeper(final Sleeper sleeper)\n
    '''
