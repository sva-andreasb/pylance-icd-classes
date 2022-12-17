MEDIA_NAME = "String  \"Multi\""
def ():
    '''returns MultiMediaManager\n\n
    (final JingleTransportManager transportManager)\n
    '''
def addMediaManager():
    '''returns None\n\n
    addMediaManager(final JingleMediaManager manager)\n
    '''
def removeMediaManager():
    '''returns None\n\n
    removeMediaManager(final JingleMediaManager manager)\n
    '''
def getPayloads():
    '''returns List<PayloadType>\n\n
    getPayloads()\n
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
