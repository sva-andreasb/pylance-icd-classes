INITIATOR = "String  \"initiator\""
RESPONDER = "String  \"responder\""
def ():
    '''returns ContentNegotiator\n\n
    (final JingleSession session, final String inCreator, final String inName)\n
    '''
def dispatchIncomingPacket():
    '''returns List<IQ>\n\n
    dispatchIncomingPacket(final IQ iq, final String id)\n
    '''
def getCreator():
    '''returns String\n\n
    getCreator()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getJingleMediaSession():
    '''returns JingleMediaSession\n\n
    getJingleMediaSession()\n
    '''
def addTransportNegotiator():
    '''returns None\n\n
    addTransportNegotiator(final TransportNegotiator transportNegotiator)\n
    '''
def setJingleTransportManager():
    '''returns None\n\n
    setJingleTransportManager(final JingleTransportManager jingleTransportManager)\n
    '''
def getTransportManager():
    '''returns JingleTransportManager\n\n
    getTransportManager()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getMediaNegotiator():
    '''returns MediaNegotiator\n\n
    getMediaNegotiator()\n
    '''
def getTransportNegotiator():
    '''returns TransportNegotiator\n\n
    getTransportNegotiator()\n
    '''
def isFullyEstablished():
    '''returns boolean\n\n
    isFullyEstablished()\n
    '''
def getJingleContent():
    '''returns JingleContent\n\n
    getJingleContent()\n
    '''
def triggerContentEstablished():
    '''returns None\n\n
    triggerContentEstablished()\n
    '''
def stopJingleMediaSession():
    '''returns None\n\n
    stopJingleMediaSession()\n
    '''
def getNegotiatorState():
    '''returns JingleNegotiatorState\n\n
    getNegotiatorState()\n
    '''
