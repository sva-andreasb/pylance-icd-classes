def ():
    '''returns AbstractHttpClientConnection\n\n
    ()\n
    '''
def isResponseAvailable():
    '''returns boolean\n\n
    isResponseAvailable(final int timeout)\n
    '''
def sendRequestHeader():
    '''returns None\n\n
    sendRequestHeader(final HttpRequest request)\n
    '''
def sendRequestEntity():
    '''returns None\n\n
    sendRequestEntity(final HttpEntityEnclosingRequest request)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def receiveResponseHeader():
    '''returns HttpResponse\n\n
    receiveResponseHeader()\n
    '''
def receiveResponseEntity():
    '''returns None\n\n
    receiveResponseEntity(final HttpResponse response)\n
    '''
def isStale():
    '''returns boolean\n\n
    isStale()\n
    '''
def getMetrics():
    '''returns HttpConnectionMetrics\n\n
    getMetrics()\n
    '''
