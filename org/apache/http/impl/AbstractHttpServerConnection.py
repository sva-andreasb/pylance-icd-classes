def ():
    '''returns AbstractHttpServerConnection\n\n
    ()\n
    '''
def receiveRequestHeader():
    '''returns HttpRequest\n\n
    receiveRequestHeader()\n
    '''
def receiveRequestEntity():
    '''returns None\n\n
    receiveRequestEntity(final HttpEntityEnclosingRequest request)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def sendResponseHeader():
    '''returns None\n\n
    sendResponseHeader(final HttpResponse response)\n
    '''
def sendResponseEntity():
    '''returns None\n\n
    sendResponseEntity(final HttpResponse response)\n
    '''
def isStale():
    '''returns boolean\n\n
    isStale()\n
    '''
def getMetrics():
    '''returns HttpConnectionMetrics\n\n
    getMetrics()\n
    '''
