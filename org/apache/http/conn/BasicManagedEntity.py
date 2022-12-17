def ():
    '''returns BasicManagedEntity\n\n
    (final HttpEntity entity, final ManagedClientConnection conn, final boolean reuse)\n
    '''
def isRepeatable():
    '''returns boolean\n\n
    isRepeatable()\n
    '''
def getContent():
    '''returns InputStream\n\n
    getContent()\n
    '''
def consumeContent():
    '''returns None\n\n
    consumeContent()\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final OutputStream outstream)\n
    '''
def releaseConnection():
    '''returns None\n\n
    releaseConnection()\n
    '''
def abortConnection():
    '''returns None\n\n
    abortConnection()\n
    '''
def eofDetected():
    '''returns boolean\n\n
    eofDetected(final InputStream wrapped)\n
    '''
def streamClosed():
    '''returns boolean\n\n
    streamClosed(final InputStream wrapped)\n
    '''
def streamAbort():
    '''returns boolean\n\n
    streamAbort(final InputStream wrapped)\n
    '''
