def getHost():
    '''returns String\n\n
    getHost()\n
    '''
def getPort():
    '''returns int\n\n
    getPort()\n
    '''
def getSocketFactory():
    '''returns SocketFactory\n\n
    getSocketFactory()\n
    '''
def newRequest():
    '''returns OutboundRequestIterator\n\n
    newRequest(final InvocationConstraints invocationConstraints)\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns OutboundRequest\n\n
    next()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def checkTrustEquivalence():
    '''returns boolean\n\n
    checkTrustEquivalence(final Object o)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def connect():
    '''returns Connection\n\n
    connect(final OutboundRequestHandle outboundRequestHandle)\n
    connect(final OutboundRequestHandle outboundRequestHandle, final Collection collection, final Collection collection2)\n
    '''
def getInputStream():
    '''returns InputStream\n\n
    getInputStream()\n
    '''
def getOutputStream():
    '''returns OutputStream\n\n
    getOutputStream()\n
    '''
def getChannel():
    '''returns SocketChannel\n\n
    getChannel()\n
    '''
def populateContext():
    '''returns None\n\n
    populateContext(final OutboundRequestHandle outboundRequestHandle, final Collection collection)\n
    '''
def getUnfulfilledConstraints():
    '''returns InvocationConstraints\n\n
    getUnfulfilledConstraints(final OutboundRequestHandle outboundRequestHandle)\n
    '''
def writeRequestData():
    '''returns None\n\n
    writeRequestData(final OutboundRequestHandle outboundRequestHandle, final OutputStream outputStream)\n
    '''
def readResponseData():
    '''returns IOException\n\n
    readResponseData(final OutboundRequestHandle outboundRequestHandle, final InputStream inputStream)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
