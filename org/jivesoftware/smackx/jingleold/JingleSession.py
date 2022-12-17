def ():
    '''returns JingleSession\n\n
    (final XMPPConnection conn, final Jid initiator, final Jid responder, final String sessionid, final List<JingleMediaManager> jingleMediaManagers)\n
    (final XMPPConnection conn, final JingleSessionRequest request, final Jid initiator, final Jid responder, final List<JingleMediaManager> jingleMediaManagers)\n
    '''
def getInitiator():
    '''returns Jid\n\n
    getInitiator()\n
    '''
def getConnection():
    '''returns XMPPConnection\n\n
    getConnection()\n
    '''
def setInitiator():
    '''returns None\n\n
    setInitiator(final Jid initiator)\n
    '''
def getMediaManagers():
    '''returns List<JingleMediaManager>\n\n
    getMediaManagers()\n
    '''
def setMediaManagers():
    '''returns None\n\n
    setMediaManagers(final List<JingleMediaManager> jingleMediaManagers)\n
    '''
def getResponder():
    '''returns Jid\n\n
    getResponder()\n
    '''
def setResponder():
    '''returns None\n\n
    setResponder(final Jid responder)\n
    '''
def getSid():
    '''returns String\n\n
    getSid()\n
    '''
def setSessionState():
    '''returns None\n\n
    setSessionState(final JingleSessionState stateIs)\n
    '''
def getSessionState():
    '''returns JingleSessionState\n\n
    getSessionState()\n
    '''
def isFullyEstablished():
    '''returns boolean\n\n
    isFullyEstablished()\n
    '''
def dispatchIncomingPacket():
    '''returns List<IQ>\n\n
    dispatchIncomingPacket(final IQ iq, final String id)\n
    '''
def addContentNegotiator():
    '''returns None\n\n
    addContentNegotiator(final ContentNegotiator inContentNegotiator)\n
    '''
def sendStanza():
    '''returns None\n\n
    sendStanza(final IQ iq)\n
    '''
def sendFormattedJingle():
    '''returns Jingle\n\n
    sendFormattedJingle(final Jingle jout)\n
    sendFormattedJingle(final IQ iq, final Jingle jout)\n
    '''
def createAck():
    '''returns IQ\n\n
    createAck(final IQ iq)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def connectionTerminated():
    '''returns None\n\n
    connectionTerminated()\n
    '''
def processStanza():
    '''returns None\n\n
    processStanza(final Stanza packet)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final Stanza packet)\n
    '''
def addMediaListener():
    '''returns None\n\n
    addMediaListener(final JingleMediaListener li)\n
    '''
def removeMediaListener():
    '''returns None\n\n
    removeMediaListener(final JingleMediaListener li)\n
    '''
def addTransportListener():
    '''returns None\n\n
    addTransportListener(final JingleTransportListener li)\n
    '''
def removeTransportListener():
    '''returns None\n\n
    removeTransportListener(final JingleTransportListener li)\n
    '''
def setupListeners():
    '''returns None\n\n
    setupListeners()\n
    '''
def mediaClosed():
    '''returns None\n\n
    mediaClosed(final PayloadType cand)\n
    '''
def mediaEstablished():
    '''returns None\n\n
    mediaEstablished(final PayloadType pt)\n
    '''
def transportEstablished():
    '''returns None\n\n
    transportEstablished(final TransportCandidate local, final TransportCandidate remote)\n
    '''
def transportClosed():
    '''returns None\n\n
    transportClosed(final TransportCandidate cand)\n
    '''
def transportClosedOnError():
    '''returns None\n\n
    transportClosedOnError(final XMPPException e)\n
    '''
def terminate():
    '''returns None\n\n
    terminate()\n
    terminate(final String reason)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
def createJingleError():
    '''returns IQ\n\n
    createJingleError(final IQ iq, final JingleError jingleError)\n
    '''
def mediaReceived():
    '''returns None\n\n
    mediaReceived(final String participant)\n
    '''
def startOutgoing():
    '''returns None\n\n
    startOutgoing()\n
    '''
def startIncoming():
    '''returns None\n\n
    startIncoming()\n
    '''
def addJingleMediaSession():
    '''returns None\n\n
    addJingleMediaSession(final String mediaManagerName, final JingleMediaSession mediaSession)\n
    '''
def getMediaSession():
    '''returns JingleMediaSession\n\n
    getMediaSession(final String mediaManagerName)\n
    '''
