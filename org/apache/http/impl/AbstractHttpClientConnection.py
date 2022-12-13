def AbstractHttpClientConnection():
    '''public AbstractHttpClientConnection()
    '''
def isResponseAvailable():
    '''public boolean isResponseAvailable(final int timeout)
    '''
def sendRequestHeader():
    '''public void sendRequestHeader(final HttpRequest request)
    '''
def sendRequestEntity():
    '''public void sendRequestEntity(final HttpEntityEnclosingRequest request)
    '''
def flush():
    '''public void flush()
    '''
def receiveResponseHeader():
    '''public HttpResponse receiveResponseHeader()
    '''
def receiveResponseEntity():
    '''public void receiveResponseEntity(final HttpResponse response)
    '''
def isStale():
    '''public boolean isStale()
    '''
def getMetrics():
    '''public HttpConnectionMetrics getMetrics()
    '''
