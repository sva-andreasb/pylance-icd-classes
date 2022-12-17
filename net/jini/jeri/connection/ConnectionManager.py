def ():
    '''returns ConnectionManager\n\n
    (final ConnectionEndpoint ep)\n
    '''
def newRequest():
    '''returns OutboundRequestIterator\n\n
    newRequest(final OutboundRequestHandle outboundRequestHandle)\n
    '''
def getRequestOutputStream():
    '''returns OutputStream\n\n
    getRequestOutputStream()\n
    '''
def getResponseInputStream():
    '''returns InputStream\n\n
    getResponseInputStream()\n
    '''
def populateContext():
    '''returns None\n\n
    populateContext(final Collection collection)\n
    '''
def getUnfulfilledConstraints():
    '''returns InvocationConstraints\n\n
    getUnfulfilledConstraints()\n
    '''
def getDeliveryStatus():
    '''returns boolean\n\n
    getDeliveryStatus()\n
    '''
def abort():
    '''returns None\n\n
    abort()\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] b, final int off, final int len)\n
    '''
def skip():
    '''returns long\n\n
    skip(final long n)\n
    '''
def available():
    '''returns int\n\n
    available()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
