STATUS_START = "int  0"
STATUS_WAITING_FOR_CONNECTION = "int  1"
STATUS_WAITING_FOR_COMMIT = "int  2"
STATUS_SENDING_REQUEST = "int  3"
STATUS_WAITING_FOR_RESPONSE = "int  4"
STATUS_PARSING_HEADERS = "int  5"
STATUS_PARSING_CONTENT = "int  6"
STATUS_COMPLETED = "int  7"
STATUS_EXPIRED = "int  8"
STATUS_EXCEPTED = "int  9"
STATUS_CANCELLING = "int  10"
STATUS_CANCELLED = "int  11"
def HttpExchange():
    '''    public HttpExchange()
    '''
def getStatus():
    '''    public int getStatus()
    '''
def waitForStatus():
    '''    public void waitForStatus(final int status)
    '''
def waitForDone():
    '''    public int waitForDone()
    '''
def reset():
    '''    public void reset()
    '''
def isDone():
    '''    public boolean isDone()
    public boolean isDone(final int status)
    '''
def getEventListener():
    '''    public HttpEventListener getEventListener()
    '''
def setEventListener():
    '''    public void setEventListener(final HttpEventListener listener)
    '''
def setTimeout():
    '''    public void setTimeout(final long timeout)
    '''
def getTimeout():
    '''    public long getTimeout()
    '''
def setURL():
    '''    public void setURL(final String url)
    '''
def setAddress():
    '''    public void setAddress(final Address address)
    '''
def getAddress():
    '''    public Address getAddress()
    '''
def getLocalAddress():
    '''    public Address getLocalAddress()
    '''
def setScheme():
    '''    public void setScheme(final Buffer scheme)
    public void setScheme(final String scheme)
    '''
def getScheme():
    '''    public Buffer getScheme()
    '''
def setVersion():
    '''    public void setVersion(final int version)
    public void setVersion(final String version)
    '''
def getVersion():
    '''    public int getVersion()
    '''
def setMethod():
    '''    public void setMethod(final String method)
    '''
def getMethod():
    '''    public String getMethod()
    '''
def getURI():
    '''    public String getURI()
    '''
def getRequestURI():
    '''    public String getRequestURI()
    '''
def setURI():
    '''    public void setURI(final String uri)
    public void setURI(final URI uri)
    '''
def setRequestURI():
    '''    public void setRequestURI(final String uri)
    '''
def addRequestHeader():
    '''    public void addRequestHeader(final String name, final String value)
    public void addRequestHeader(final Buffer name, final Buffer value)
    '''
def setRequestHeader():
    '''    public void setRequestHeader(final String name, final String value)
    public void setRequestHeader(final Buffer name, final Buffer value)
    '''
def setRequestContentType():
    '''    public void setRequestContentType(final String value)
    '''
def getRequestFields():
    '''    public HttpFields getRequestFields()
    '''
def setRequestContent():
    '''    public void setRequestContent(final Buffer requestContent)
    '''
def setRequestContentSource():
    '''    public void setRequestContentSource(final InputStream stream)
    '''
def getRequestContentSource():
    '''    public InputStream getRequestContentSource()
    '''
def getRequestContentChunk():
    '''    public Buffer getRequestContentChunk(Buffer buffer)
    '''
def getRequestContent():
    '''    public Buffer getRequestContent()
    '''
def getRetryStatus():
    '''    public boolean getRetryStatus()
    '''
def setRetryStatus():
    '''    public void setRetryStatus(final boolean retryStatus)
    '''
def cancel():
    '''    public void cancel()
    '''
def toState():
    '''    public static String toState(final int s)
    '''
def toString():
    '''    public String toString()
    '''
def configureListeners():
    '''    public boolean configureListeners()
    '''
def setConfigureListeners():
    '''    public void setConfigureListeners(final boolean autoConfigure)
    '''
def expired():
    '''    public void expired()
    '''
def onConnectionFailed():
    '''    public void onConnectionFailed(final Throwable ex)
    '''
def onException():
    '''    public void onException(final Throwable ex)
    '''
def onExpire():
    '''    public void onExpire()
    '''
def onRequestCommitted():
    '''    public void onRequestCommitted()
    '''
def onRequestComplete():
    '''    public void onRequestComplete()
    '''
def onResponseComplete():
    '''    public void onResponseComplete()
    '''
def onResponseContent():
    '''    public void onResponseContent(final Buffer content)
    '''
def onResponseHeader():
    '''    public void onResponseHeader(final Buffer name, final Buffer value)
    '''
def onResponseHeaderComplete():
    '''    public void onResponseHeaderComplete()
    '''
def onResponseStatus():
    '''    public void onResponseStatus(final Buffer version, final int status, final Buffer reason)
    '''
def onRetry():
    '''    public void onRetry()
    '''
def CachedExchange():
    '''    public CachedExchange(final boolean cacheFields)
    '''
