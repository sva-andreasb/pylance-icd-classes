NAMESPACE_V1 = "String  \"urn:xmpp:jingle:transports:s5b:1\""
ATTR_DSTADDR = "String  \"dstaddr\""
ATTR_MODE = "String  \"mode\""
ATTR_SID = "String  \"sid\""
def getStreamId():
    '''returns String\n\n
    getStreamId()\n
    '''
def getDestinationAddress():
    '''returns String\n\n
    getDestinationAddress()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def hasCandidate():
    '''returns boolean\n\n
    hasCandidate(final String candidateId)\n
    '''
def getCandidate():
    '''returns JingleS5BTransportCandidate\n\n
    getCandidate(final String candidateId)\n
    '''
def ():
    '''returns Builder\n\n
    ()\n
    '''
def setStreamId():
    '''returns Builder\n\n
    setStreamId(final String sid)\n
    '''
def setDestinationAddress():
    '''returns Builder\n\n
    setDestinationAddress(final String dstAddr)\n
    '''
def setMode():
    '''returns Builder\n\n
    setMode(final Bytestream.Mode mode)\n
    '''
def addTransportCandidate():
    '''returns Builder\n\n
    addTransportCandidate(final JingleS5BTransportCandidate candidate)\n
    '''
def setTransportInfo():
    '''returns Builder\n\n
    setTransportInfo(final JingleContentTransportInfo info)\n
    '''
def setCandidateUsed():
    '''returns Builder\n\n
    setCandidateUsed(final String candidateId)\n
    '''
def setCandidateActivated():
    '''returns Builder\n\n
    setCandidateActivated(final String candidateId)\n
    '''
def setCandidateError():
    '''returns Builder\n\n
    setCandidateError()\n
    '''
def setProxyError():
    '''returns Builder\n\n
    setProxyError()\n
    '''
def build():
    '''returns JingleS5BTransport\n\n
    build()\n
    '''
