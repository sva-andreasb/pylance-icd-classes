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
def ():
    '''returns CachedExchange\n\n
    ()\n
    (final boolean cacheFields)\n
    '''
def getStatus():
    '''returns int\n\n
    getStatus()\n
    '''
def waitForStatus():
    '''returns None\n\n
    waitForStatus(final int status)\n
    '''
def waitForDone():
    '''returns int\n\n
    waitForDone()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def isDone():
    '''returns boolean\n\n
    isDone()\n
    isDone(final int status)\n
    '''
def getEventListener():
    '''returns HttpEventListener\n\n
    getEventListener()\n
    '''
def setEventListener():
    '''returns None\n\n
    setEventListener(final HttpEventListener listener)\n
    '''
def setTimeout():
    '''returns None\n\n
    setTimeout(final long timeout)\n
    '''
def getTimeout():
    '''returns long\n\n
    getTimeout()\n
    '''
def setURL():
    '''returns None\n\n
    setURL(final String url)\n
    '''
def setAddress():
    '''returns None\n\n
    setAddress(final Address address)\n
    '''
def getAddress():
    '''returns Address\n\n
    getAddress()\n
    '''
def getLocalAddress():
    '''returns Address\n\n
    getLocalAddress()\n
    '''
def setScheme():
    '''returns None\n\n
    setScheme(final Buffer scheme)\n
    setScheme(final String scheme)\n
    '''
def getScheme():
    '''returns Buffer\n\n
    getScheme()\n
    '''
def setVersion():
    '''returns None\n\n
    setVersion(final int version)\n
    setVersion(final String version)\n
    '''
def getVersion():
    '''returns int\n\n
    getVersion()\n
    '''
def setMethod():
    '''returns None\n\n
    setMethod(final String method)\n
    '''
def getMethod():
    '''returns String\n\n
    getMethod()\n
    '''
def getURI():
    '''returns String\n\n
    getURI()\n
    '''
def getRequestURI():
    '''returns String\n\n
    getRequestURI()\n
    '''
def setURI():
    '''returns None\n\n
    setURI(final String uri)\n
    setURI(final URI uri)\n
    '''
def setRequestURI():
    '''returns None\n\n
    setRequestURI(final String uri)\n
    '''
def addRequestHeader():
    '''returns None\n\n
    addRequestHeader(final String name, final String value)\n
    addRequestHeader(final Buffer name, final Buffer value)\n
    '''
def setRequestHeader():
    '''returns None\n\n
    setRequestHeader(final String name, final String value)\n
    setRequestHeader(final Buffer name, final Buffer value)\n
    '''
def setRequestContentType():
    '''returns None\n\n
    setRequestContentType(final String value)\n
    '''
def getRequestFields():
    '''returns HttpFields\n\n
    getRequestFields()\n
    '''
def setRequestContent():
    '''returns None\n\n
    setRequestContent(final Buffer requestContent)\n
    '''
def setRequestContentSource():
    '''returns None\n\n
    setRequestContentSource(final InputStream stream)\n
    '''
def getRequestContentSource():
    '''returns InputStream\n\n
    getRequestContentSource()\n
    '''
def getRequestContentChunk():
    '''returns Buffer\n\n
    getRequestContentChunk(Buffer buffer)\n
    '''
def getRequestContent():
    '''returns Buffer\n\n
    getRequestContent()\n
    '''
def getRetryStatus():
    '''returns boolean\n\n
    getRetryStatus()\n
    '''
def setRetryStatus():
    '''returns None\n\n
    setRetryStatus(final boolean retryStatus)\n
    '''
def cancel():
    '''returns None\n\n
    cancel()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def configureListeners():
    '''returns boolean\n\n
    configureListeners()\n
    '''
def setConfigureListeners():
    '''returns None\n\n
    setConfigureListeners(final boolean autoConfigure)\n
    '''
def expired():
    '''returns None\n\n
    expired()\n
    '''
def onConnectionFailed():
    '''returns None\n\n
    onConnectionFailed(final Throwable ex)\n
    '''
def onException():
    '''returns None\n\n
    onException(final Throwable ex)\n
    '''
def onExpire():
    '''returns None\n\n
    onExpire()\n
    '''
def onRequestCommitted():
    '''returns None\n\n
    onRequestCommitted()\n
    '''
def onRequestComplete():
    '''returns None\n\n
    onRequestComplete()\n
    '''
def onResponseComplete():
    '''returns None\n\n
    onResponseComplete()\n
    '''
def onResponseContent():
    '''returns None\n\n
    onResponseContent(final Buffer content)\n
    '''
def onResponseHeader():
    '''returns None\n\n
    onResponseHeader(final Buffer name, final Buffer value)\n
    '''
def onResponseHeaderComplete():
    '''returns None\n\n
    onResponseHeaderComplete()\n
    '''
def onResponseStatus():
    '''returns None\n\n
    onResponseStatus(final Buffer version, final int status, final Buffer reason)\n
    '''
def onRetry():
    '''returns None\n\n
    onRetry()\n
    '''
