def isOpen():
    '''returns boolean\n\n
    isOpen()\n
    '''
def isStale():
    '''returns boolean\n\n
    isStale()\n
    '''
def setSocketTimeout():
    '''returns None\n\n
    setSocketTimeout(final int timeout)\n
    '''
def getSocketTimeout():
    '''returns int\n\n
    getSocketTimeout()\n
    '''
def getMetrics():
    '''returns HttpConnectionMetrics\n\n
    getMetrics()\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def isResponseAvailable():
    '''returns boolean\n\n
    isResponseAvailable(final int timeout)\n
    '''
def receiveResponseEntity():
    '''returns None\n\n
    receiveResponseEntity(final HttpResponse response)\n
    '''
def receiveResponseHeader():
    '''returns HttpResponse\n\n
    receiveResponseHeader()\n
    '''
def sendRequestEntity():
    '''returns None\n\n
    sendRequestEntity(final HttpEntityEnclosingRequest request)\n
    '''
def sendRequestHeader():
    '''returns None\n\n
    sendRequestHeader(final HttpRequest request)\n
    '''
def getLocalAddress():
    '''returns InetAddress\n\n
    getLocalAddress()\n
    '''
def getLocalPort():
    '''returns int\n\n
    getLocalPort()\n
    '''
def getRemoteAddress():
    '''returns InetAddress\n\n
    getRemoteAddress()\n
    '''
def getRemotePort():
    '''returns int\n\n
    getRemotePort()\n
    '''
def isSecure():
    '''returns boolean\n\n
    isSecure()\n
    '''
def bind():
    '''returns None\n\n
    bind(final Socket socket)\n
    '''
def getSocket():
    '''returns Socket\n\n
    getSocket()\n
    '''
def getSSLSession():
    '''returns SSLSession\n\n
    getSSLSession()\n
    '''
def markReusable():
    '''returns None\n\n
    markReusable()\n
    '''
def unmarkReusable():
    '''returns None\n\n
    unmarkReusable()\n
    '''
def isMarkedReusable():
    '''returns boolean\n\n
    isMarkedReusable()\n
    '''
def setIdleDuration():
    '''returns None\n\n
    setIdleDuration(final long duration, final TimeUnit unit)\n
    '''
def getAttribute():
    '''returns Object\n\n
    getAttribute(final String id)\n
    '''
def removeAttribute():
    '''returns Object\n\n
    removeAttribute(final String id)\n
    '''
def setAttribute():
    '''returns None\n\n
    setAttribute(final String id, final Object obj)\n
    '''
