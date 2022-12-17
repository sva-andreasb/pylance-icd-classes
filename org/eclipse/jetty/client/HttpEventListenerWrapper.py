def ():
    '''returns HttpEventListenerWrapper\n\n
    ()\n
    (final HttpEventListener eventListener, final boolean delegating)\n
    '''
def getEventListener():
    '''returns HttpEventListener\n\n
    getEventListener()\n
    '''
def setEventListener():
    '''returns None\n\n
    setEventListener(final HttpEventListener listener)\n
    '''
def isDelegatingRequests():
    '''returns boolean\n\n
    isDelegatingRequests()\n
    '''
def isDelegatingResponses():
    '''returns boolean\n\n
    isDelegatingResponses()\n
    '''
def setDelegatingRequests():
    '''returns None\n\n
    setDelegatingRequests(final boolean delegating)\n
    '''
def setDelegatingResponses():
    '''returns None\n\n
    setDelegatingResponses(final boolean delegating)\n
    '''
def setDelegationResult():
    '''returns None\n\n
    setDelegationResult(final boolean result)\n
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
