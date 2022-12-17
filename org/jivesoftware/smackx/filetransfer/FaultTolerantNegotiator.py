def ():
    '''returns FaultTolerantNegotiator\n\n
    (final XMPPConnection connection, final StreamNegotiator primary, final StreamNegotiator secondary)\n
    '''
def newStreamInitiation():
    '''returns None\n\n
    newStreamInitiation(final Jid from, final String streamID)\n
    '''
def createIncomingStream():
    '''returns InputStream\n\n
    createIncomingStream(final StreamInitiation initiation)\n
    '''
def createOutgoingStream():
    '''returns OutputStream\n\n
    createOutgoingStream(final String streamID, final Jid initiator, final Jid target)\n
    '''
def getNamespaces():
    '''returns String[]\n\n
    getNamespaces()\n
    '''
