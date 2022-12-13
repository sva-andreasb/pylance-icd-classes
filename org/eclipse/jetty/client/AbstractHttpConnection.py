def setReserved():
'''public void setReserved(final boolean reserved)
'''
pass
def isReserved():
'''public boolean isReserved()
'''
pass
def getDestination():
'''public HttpDestination getDestination()
'''
pass
def setDestination():
'''public void setDestination(final HttpDestination destination)
'''
pass
def send():
'''public boolean send(final HttpExchange ex)
'''
pass
def isIdle():
'''public boolean isIdle()
'''
pass
def isSuspended():
'''public boolean isSuspended()
'''
pass
def onClose():
'''public void onClose()
'''
pass
def toString():
'''public String toString()
'''
pass
def toDetailString():
'''public String toDetailString()
'''
pass
def close():
'''public void close()
'''
pass
def setIdleTimeout():
'''public void setIdleTimeout()
'''
pass
def cancelIdleTimeout():
'''public boolean cancelIdleTimeout()
'''
pass
def dump():
'''public String dump()
public void dump(final Appendable out, final String indent)
'''
pass
def startRequest():
'''public void startRequest(final Buffer method, final Buffer url, final Buffer version)
'''
pass
def startResponse():
'''public void startResponse(final Buffer version, final int status, final Buffer reason)
'''
pass
def parsedHeader():
'''public void parsedHeader(final Buffer name, final Buffer value)
'''
pass
def headerComplete():
'''public void headerComplete()
'''
pass
def content():
'''public void content(final Buffer ref)
'''
pass
def messageComplete():
'''public void messageComplete(final long contextLength)
'''
pass
def earlyEOF():
'''public void earlyEOF()
'''
pass
def expired():
'''public void expired()
'''
pass
def NonFinalResponseListener():
'''public NonFinalResponseListener(final HttpExchange exchange)
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
def onResponseStatus():
'''public void onResponseStatus(final Buffer version, final int status, final Buffer reason)
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
def onResponseContent():
'''public void onResponseContent(final Buffer content)
'''
pass
def onResponseComplete():
'''public void onResponseComplete()
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
def onRetry():
'''public void onRetry()
'''
pass
