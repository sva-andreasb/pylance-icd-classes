def setReserved():
    '''public void setReserved(final boolean reserved)
    '''
def isReserved():
    '''public boolean isReserved()
    '''
def getDestination():
    '''public HttpDestination getDestination()
    '''
def setDestination():
    '''public void setDestination(final HttpDestination destination)
    '''
def send():
    '''public boolean send(final HttpExchange ex)
    '''
def isIdle():
    '''public boolean isIdle()
    '''
def isSuspended():
    '''public boolean isSuspended()
    '''
def onClose():
    '''public void onClose()
    '''
def toString():
    '''public String toString()
    '''
def toDetailString():
    '''public String toDetailString()
    '''
def close():
    '''public void close()
    '''
def setIdleTimeout():
    '''public void setIdleTimeout()
    '''
def cancelIdleTimeout():
    '''public boolean cancelIdleTimeout()
    '''
def dump():
    '''public String dump()
    public void dump(final Appendable out, final String indent)
    '''
def startRequest():
    '''public void startRequest(final Buffer method, final Buffer url, final Buffer version)
    '''
def startResponse():
    '''public void startResponse(final Buffer version, final int status, final Buffer reason)
    '''
def parsedHeader():
    '''public void parsedHeader(final Buffer name, final Buffer value)
    '''
def headerComplete():
    '''public void headerComplete()
    '''
def content():
    '''public void content(final Buffer ref)
    '''
def messageComplete():
    '''public void messageComplete(final long contextLength)
    '''
def earlyEOF():
    '''public void earlyEOF()
    '''
def expired():
    '''public void expired()
    '''
def NonFinalResponseListener():
    '''public NonFinalResponseListener(final HttpExchange exchange)
    '''
def onRequestCommitted():
    '''public void onRequestCommitted()
    '''
def onRequestComplete():
    '''public void onRequestComplete()
    '''
def onResponseStatus():
    '''public void onResponseStatus(final Buffer version, final int status, final Buffer reason)
    '''
def onResponseHeader():
    '''public void onResponseHeader(final Buffer name, final Buffer value)
    '''
def onResponseHeaderComplete():
    '''public void onResponseHeaderComplete()
    '''
def onResponseContent():
    '''public void onResponseContent(final Buffer content)
    '''
def onResponseComplete():
    '''public void onResponseComplete()
    '''
def onConnectionFailed():
    '''public void onConnectionFailed(final Throwable ex)
    '''
def onException():
    '''public void onException(final Throwable ex)
    '''
def onExpire():
    '''public void onExpire()
    '''
def onRetry():
    '''public void onRetry()
    '''
