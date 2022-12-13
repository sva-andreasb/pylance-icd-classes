def HttpEventListenerWrapper():
    '''    public HttpEventListenerWrapper()
    public HttpEventListenerWrapper(final HttpEventListener eventListener, final boolean delegating)
    '''
def getEventListener():
    '''    public HttpEventListener getEventListener()
    '''
def setEventListener():
    '''    public void setEventListener(final HttpEventListener listener)
    '''
def isDelegatingRequests():
    '''    public boolean isDelegatingRequests()
    '''
def isDelegatingResponses():
    '''    public boolean isDelegatingResponses()
    '''
def setDelegatingRequests():
    '''    public void setDelegatingRequests(final boolean delegating)
    '''
def setDelegatingResponses():
    '''    public void setDelegatingResponses(final boolean delegating)
    '''
def setDelegationResult():
    '''    public void setDelegationResult(final boolean result)
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
