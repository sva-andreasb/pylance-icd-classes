VERSION = "String  \"1.25.0\""
USER_AGENT_SUFFIX = "String  \"Google-HTTP-Java-Client/1.25.0 (gzip)\""
DEFAULT_NUMBER_OF_RETRIES = "int  10"
def getTransport():
    '''    public HttpTransport getTransport()
    '''
def getRequestMethod():
    '''    public String getRequestMethod()
    '''
def setRequestMethod():
    '''    public HttpRequest setRequestMethod(final String requestMethod)
    '''
def getUrl():
    '''    public GenericUrl getUrl()
    '''
def setUrl():
    '''    public HttpRequest setUrl(final GenericUrl url)
    '''
def getContent():
    '''    public HttpContent getContent()
    '''
def setContent():
    '''    public HttpRequest setContent(final HttpContent content)
    '''
def getEncoding():
    '''    public HttpEncoding getEncoding()
    '''
def setEncoding():
    '''    public HttpRequest setEncoding(final HttpEncoding encoding)
    '''
def getBackOffPolicy():
    '''    public BackOffPolicy getBackOffPolicy()
    '''
def setBackOffPolicy():
    '''    public HttpRequest setBackOffPolicy(final BackOffPolicy backOffPolicy)
    '''
def getContentLoggingLimit():
    '''    public int getContentLoggingLimit()
    '''
def setContentLoggingLimit():
    '''    public HttpRequest setContentLoggingLimit(final int contentLoggingLimit)
    '''
def isLoggingEnabled():
    '''    public boolean isLoggingEnabled()
    '''
def setLoggingEnabled():
    '''    public HttpRequest setLoggingEnabled(final boolean loggingEnabled)
    '''
def isCurlLoggingEnabled():
    '''    public boolean isCurlLoggingEnabled()
    '''
def setCurlLoggingEnabled():
    '''    public HttpRequest setCurlLoggingEnabled(final boolean curlLoggingEnabled)
    '''
def getConnectTimeout():
    '''    public int getConnectTimeout()
    '''
def setConnectTimeout():
    '''    public HttpRequest setConnectTimeout(final int connectTimeout)
    '''
def getReadTimeout():
    '''    public int getReadTimeout()
    '''
def setReadTimeout():
    '''    public HttpRequest setReadTimeout(final int readTimeout)
    '''
def getHeaders():
    '''    public HttpHeaders getHeaders()
    '''
def setHeaders():
    '''    public HttpRequest setHeaders(final HttpHeaders headers)
    '''
def getResponseHeaders():
    '''    public HttpHeaders getResponseHeaders()
    '''
def setResponseHeaders():
    '''    public HttpRequest setResponseHeaders(final HttpHeaders responseHeaders)
    '''
def getInterceptor():
    '''    public HttpExecuteInterceptor getInterceptor()
    '''
def setInterceptor():
    '''    public HttpRequest setInterceptor(final HttpExecuteInterceptor interceptor)
    '''
def getUnsuccessfulResponseHandler():
    '''    public HttpUnsuccessfulResponseHandler getUnsuccessfulResponseHandler()
    '''
def setUnsuccessfulResponseHandler():
    '''    public HttpRequest setUnsuccessfulResponseHandler(final HttpUnsuccessfulResponseHandler unsuccessfulResponseHandler)
    '''
def getIOExceptionHandler():
    '''    public HttpIOExceptionHandler getIOExceptionHandler()
    '''
def setIOExceptionHandler():
    '''    public HttpRequest setIOExceptionHandler(final HttpIOExceptionHandler ioExceptionHandler)
    '''
def getResponseInterceptor():
    '''    public HttpResponseInterceptor getResponseInterceptor()
    '''
def setResponseInterceptor():
    '''    public HttpRequest setResponseInterceptor(final HttpResponseInterceptor responseInterceptor)
    '''
def getNumberOfRetries():
    '''    public int getNumberOfRetries()
    '''
def setNumberOfRetries():
    '''    public HttpRequest setNumberOfRetries(final int numRetries)
    '''
def setParser():
    '''    public HttpRequest setParser(final ObjectParser parser)
    '''
def getParser():
    '''    public final ObjectParser getParser()
    '''
def getFollowRedirects():
    '''    public boolean getFollowRedirects()
    '''
def setFollowRedirects():
    '''    public HttpRequest setFollowRedirects(final boolean followRedirects)
    '''
def getThrowExceptionOnExecuteError():
    '''    public boolean getThrowExceptionOnExecuteError()
    '''
def setThrowExceptionOnExecuteError():
    '''    public HttpRequest setThrowExceptionOnExecuteError(final boolean throwExceptionOnExecuteError)
    '''
def getRetryOnExecuteIOException():
    '''    public boolean getRetryOnExecuteIOException()
    '''
def setRetryOnExecuteIOException():
    '''    public HttpRequest setRetryOnExecuteIOException(final boolean retryOnExecuteIOException)
    '''
def getSuppressUserAgentSuffix():
    '''    public boolean getSuppressUserAgentSuffix()
    '''
def setSuppressUserAgentSuffix():
    '''    public HttpRequest setSuppressUserAgentSuffix(final boolean suppressUserAgentSuffix)
    '''
def execute():
    '''    public HttpResponse execute()
    '''
def executeAsync():
    '''    public Future<HttpResponse> executeAsync(final Executor executor)
    public Future<HttpResponse> executeAsync()
    '''
def call():
    '''    public HttpResponse call()
    '''
def handleRedirect():
    '''    public boolean handleRedirect(final int statusCode, final HttpHeaders responseHeaders)
    '''
def getSleeper():
    '''    public Sleeper getSleeper()
    '''
def setSleeper():
    '''    public HttpRequest setSleeper(final Sleeper sleeper)
    '''
