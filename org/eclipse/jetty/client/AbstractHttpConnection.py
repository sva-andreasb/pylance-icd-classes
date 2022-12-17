def setReserved():
    '''returns None\n\n
    setReserved(final boolean reserved)\n
    '''
def isReserved():
    '''returns boolean\n\n
    isReserved()\n
    '''
def getDestination():
    '''returns HttpDestination\n\n
    getDestination()\n
    '''
def setDestination():
    '''returns None\n\n
    setDestination(final HttpDestination destination)\n
    '''
def send():
    '''returns boolean\n\n
    send(final HttpExchange ex)\n
    '''
def isIdle():
    '''returns boolean\n\n
    isIdle()\n
    '''
def isSuspended():
    '''returns boolean\n\n
    isSuspended()\n
    '''
def onClose():
    '''returns None\n\n
    onClose()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def toDetailString():
    '''returns String\n\n
    toDetailString()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def setIdleTimeout():
    '''returns None\n\n
    setIdleTimeout()\n
    '''
def cancelIdleTimeout():
    '''returns boolean\n\n
    cancelIdleTimeout()\n
    '''
def dump():
    '''returns None\n\n
    dump()\n
    dump(final Appendable out, final String indent)\n
    '''
def startRequest():
    '''returns None\n\n
    startRequest(final Buffer method, final Buffer url, final Buffer version)\n
    '''
def startResponse():
    '''returns None\n\n
    startResponse(final Buffer version, final int status, final Buffer reason)\n
    '''
def parsedHeader():
    '''returns None\n\n
    parsedHeader(final Buffer name, final Buffer value)\n
    '''
def headerComplete():
    '''returns None\n\n
    headerComplete()\n
    '''
def content():
    '''returns None\n\n
    content(final Buffer ref)\n
    '''
def messageComplete():
    '''returns None\n\n
    messageComplete(final long contextLength)\n
    '''
def earlyEOF():
    '''returns None\n\n
    earlyEOF()\n
    '''
def expired():
    '''returns None\n\n
    expired()\n
    '''
def ():
    '''returns NonFinalResponseListener\n\n
    (final HttpExchange exchange)\n
    '''
def onRequestCommitted():
    '''returns None\n\n
    onRequestCommitted()\n
    '''
def onRequestComplete():
    '''returns None\n\n
    onRequestComplete()\n
    '''
def onResponseStatus():
    '''returns None\n\n
    onResponseStatus(final Buffer version, final int status, final Buffer reason)\n
    '''
def onResponseHeader():
    '''returns None\n\n
    onResponseHeader(final Buffer name, final Buffer value)\n
    '''
def onResponseHeaderComplete():
    '''returns None\n\n
    onResponseHeaderComplete()\n
    '''
def onResponseContent():
    '''returns None\n\n
    onResponseContent(final Buffer content)\n
    '''
def onResponseComplete():
    '''returns None\n\n
    onResponseComplete()\n
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
def onRetry():
    '''returns None\n\n
    onRetry()\n
    '''
