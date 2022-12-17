NODENAME = "String  \"payload-type\""
NAMESPACE = "String  \"urn:xmpp:tmp:jingle:apps:rtp\""
def ():
    '''returns Audio\n\n
    ()\n
    ()\n
    (final JinglePayloadType pt)\n
    (final PayloadType payload)\n
    ()\n
    (final PayloadType.Audio audio)\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    '''
def addJinglePayloadType():
    '''returns None\n\n
    addJinglePayloadType(final JinglePayloadType pt)\n
    '''
def addAudioPayloadTypes():
    '''returns None\n\n
    addAudioPayloadTypes(final List<PayloadType.Audio> pts)\n
    '''
def getJinglePayloadTypes():
    '''returns Iterator<JinglePayloadType>\n\n
    getJinglePayloadTypes()\n
    '''
def getJinglePayloadTypesList():
    '''returns ArrayList<JinglePayloadType>\n\n
    getJinglePayloadTypesList()\n
    '''
def getJinglePayloadTypesCount():
    '''returns int\n\n
    getJinglePayloadTypesCount()\n
    '''
def toXML():
    '''returns String\n\n
    toXML(final String enclosingNamespace)\n
    toXML()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def getPayloadType():
    '''returns PayloadType\n\n
    getPayloadType()\n
    '''
def setPayload():
    '''returns None\n\n
    setPayload(final PayloadType payload)\n
    '''
