def ():
    '''returns BasicObjectEndpoint\n\n
    (final Endpoint ep, final Uuid id, final boolean dgc)\n
    '''
def newCall():
    '''returns OutboundRequestIterator\n\n
    newCall(final InvocationConstraints invocationConstraints)\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns OutboundRequest\n\n
    next()\n
    '''
def executeCall():
    '''returns RemoteException\n\n
    executeCall(final OutboundRequest outboundRequest)\n
    '''
def getEndpoint():
    '''returns Endpoint\n\n
    getEndpoint()\n
    '''
def getObjectIdentifier():
    '''returns Uuid\n\n
    getObjectIdentifier()\n
    '''
def getEnableDGC():
    '''returns boolean\n\n
    getEnableDGC()\n
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
def acknowledgmentReceived():
    '''returns None\n\n
    acknowledgmentReceived(final boolean b)\n
    '''
def validateObject():
    '''returns None\n\n
    validateObject()\n
    '''
