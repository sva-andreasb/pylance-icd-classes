def ():
    '''returns IPCConnectorReadCallback\n\n
    (final IPCConnectorInbound channel, final VirtualConnection vc, final boolean asynch, final String profileKey)\n
    (final IPCConnectorInboundLink link)\n
    (final IPCConnectorInboundLink link)\n
    '''
def ready():
    '''returns None\n\n
    ready(final VirtualConnection vc)\n
    '''
def close():
    '''returns None\n\n
    close(final VirtualConnection vc, final Exception e)\n
    '''
def doWork():
    '''returns None\n\n
    doWork(final int mode)\n
    '''
def readMoreData():
    '''returns boolean\n\n
    readMoreData(final int mode)\n
    '''
def writeData():
    '''returns None\n\n
    writeData(final byte[] reply)\n
    '''
def cleanupForNextWrite():
    '''returns None\n\n
    cleanupForNextWrite()\n
    '''
def complete():
    '''returns None\n\n
    complete(final VirtualConnection vc, final TCPWriteRequestContext wsc)\n
    complete(final VirtualConnection vc, final TCPReadRequestContext rsc)\n
    '''
def error():
    '''returns None\n\n
    error(final VirtualConnection vc, final TCPWriteRequestContext wsc, final IOException t)\n
    error(final VirtualConnection vc, final TCPReadRequestContext rsc, final IOException t)\n
    '''
