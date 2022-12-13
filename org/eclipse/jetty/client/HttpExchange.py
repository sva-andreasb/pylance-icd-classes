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
'''public HttpExchange()
'''
pass
def getStatus():
'''public int getStatus()
'''
pass
def waitForStatus():
'''public void waitForStatus(final int status)
'''
pass
def waitForDone():
'''public int waitForDone()
'''
pass
def reset():
'''public void reset()
'''
pass
def isDone():
'''public boolean isDone()
public boolean isDone(final int status)
'''
pass
def getEventListener():
'''public HttpEventListener getEventListener()
'''
pass
def setEventListener():
'''public void setEventListener(final HttpEventListener listener)
'''
pass
def setTimeout():
'''public void setTimeout(final long timeout)
'''
pass
def getTimeout():
'''public long getTimeout()
'''
pass
def setURL():
'''public void setURL(final String url)
'''
pass
def setAddress():
'''public void setAddress(final Address address)
'''
pass
def getAddress():
'''public Address getAddress()
'''
pass
def getLocalAddress():
'''public Address getLocalAddress()
'''
pass
def setScheme():
'''public void setScheme(final Buffer scheme)
public void setScheme(final String scheme)
'''
pass
def getScheme():
'''public Buffer getScheme()
'''
pass
def setVersion():
'''public void setVersion(final int version)
public void setVersion(final String version)
'''
pass
def getVersion():
'''public int getVersion()
'''
pass
def setMethod():
'''public void setMethod(final String method)
'''
pass
def getMethod():
'''public String getMethod()
'''
pass
def getURI():
'''public String getURI()
'''
pass
def getRequestURI():
'''public String getRequestURI()
'''
pass
def setURI():
'''public void setURI(final String uri)
public void setURI(final URI uri)
'''
pass
def setRequestURI():
'''public void setRequestURI(final String uri)
'''
pass
def addRequestHeader():
'''public void addRequestHeader(final String name, final String value)
public void addRequestHeader(final Buffer name, final Buffer value)
'''
pass
def setRequestHeader():
'''public void setRequestHeader(final String name, final String value)
public void setRequestHeader(final Buffer name, final Buffer value)
'''
pass
def setRequestContentType():
'''public void setRequestContentType(final String value)
'''
pass
def getRequestFields():
'''public HttpFields getRequestFields()
'''
pass
def setRequestContent():
'''public void setRequestContent(final Buffer requestContent)
'''
pass
def setRequestContentSource():
'''public void setRequestContentSource(final InputStream stream)
'''
pass
def getRequestContentSource():
'''public InputStream getRequestContentSource()
'''
pass
def getRequestContentChunk():
'''public Buffer getRequestContentChunk(Buffer buffer)
'''
pass
def getRequestContent():
'''public Buffer getRequestContent()
'''
pass
def getRetryStatus():
'''public boolean getRetryStatus()
'''
pass
def setRetryStatus():
'''public void setRetryStatus(final boolean retryStatus)
'''
pass
def cancel():
'''public void cancel()
'''
pass
def toState():
'''public static String toState(final int s)
'''
pass
def toString():
'''public String toString()
'''
pass
def configureListeners():
'''public boolean configureListeners()
'''
pass
def setConfigureListeners():
'''public void setConfigureListeners(final boolean autoConfigure)
'''
pass
def expired():
'''public void expired()
'''
pass
def onConnectionFailed():
'''public void onConnectionFailed(final Throwable ex)
'''
pass
def onException():
'''public void onException(final Throwable ex)
'''
pass
def onExpire():
'''public void onExpire()
'''
pass
def onRequestCommitted():
'''public void onRequestCommitted()
'''
pass
def onRequestComplete():
'''public void onRequestComplete()
'''
pass
def onResponseComplete():
'''public void onResponseComplete()
'''
pass
def onResponseContent():
'''public void onResponseContent(final Buffer content)
'''
pass
def onResponseHeader():
'''public void onResponseHeader(final Buffer name, final Buffer value)
'''
pass
def onResponseHeaderComplete():
'''public void onResponseHeaderComplete()
'''
pass
def onResponseStatus():
'''public void onResponseStatus(final Buffer version, final int status, final Buffer reason)
'''
pass
def onRetry():
'''public void onRetry()
'''
pass
def CachedExchange():
'''public CachedExchange(final boolean cacheFields)
'''
pass
