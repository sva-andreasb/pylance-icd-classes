MEDIA_NAME = "String  \"TestMedia\""
def ():
    '''returns TestMediaManager\n\n
    (final JingleTransportManager transportManager)\n
    '''
def getPayloads():
    '''returns List<PayloadType>\n\n
    getPayloads()\n
    '''
def setPayloads():
    '''returns None\n\n
    setPayloads(final List<PayloadType> payloads)\n
    '''
def createMediaSession():
    '''returns JingleMediaSession\n\n
    createMediaSession(final PayloadType payloadType, final TransportCandidate remote, final TransportCandidate local, final JingleSession jingleSession)\n
    '''
def getPreferredPayloadType():
    '''returns PayloadType\n\n
    getPreferredPayloadType()\n
    '''
def setPreferredPayloadType():
    '''returns None\n\n
    setPreferredPayloadType(final PayloadType preferredPayloadType)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
