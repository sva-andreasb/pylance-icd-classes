def JingleSession():
    '''    public JingleSession(final XMPPConnection conn, final Jid initiator, final Jid responder, final String sessionid, final List<JingleMediaManager> jingleMediaManagers)
    public JingleSession(final XMPPConnection conn, final JingleSessionRequest request, final Jid initiator, final Jid responder, final List<JingleMediaManager> jingleMediaManagers)
    '''
def getInitiator():
    '''    public Jid getInitiator()
    '''
def getConnection():
    '''    public XMPPConnection getConnection()
    '''
def setInitiator():
    '''    public void setInitiator(final Jid initiator)
    '''
def getMediaManagers():
    '''    public List<JingleMediaManager> getMediaManagers()
    '''
def setMediaManagers():
    '''    public void setMediaManagers(final List<JingleMediaManager> jingleMediaManagers)
    '''
def getResponder():
    '''    public Jid getResponder()
    '''
def setResponder():
    '''    public void setResponder(final Jid responder)
    '''
def getSid():
    '''    public String getSid()
    '''
def setSessionState():
    '''    public void setSessionState(final JingleSessionState stateIs)
    '''
def getSessionState():
    '''    public JingleSessionState getSessionState()
    '''
def isFullyEstablished():
    '''    public boolean isFullyEstablished()
    '''
def receivePacketAndRespond():
    '''    public synchronized void receivePacketAndRespond(final IQ iq)
    '''
def dispatchIncomingPacket():
    '''    public List<IQ> dispatchIncomingPacket(final IQ iq, final String id)
    '''
def addContentNegotiator():
    '''    public void addContentNegotiator(final ContentNegotiator inContentNegotiator)
    '''
def sendStanza():
    '''    public void sendStanza(final IQ iq)
    '''
def sendFormattedJingle():
    '''    public Jingle sendFormattedJingle(final Jingle jout)
    public Jingle sendFormattedJingle(final IQ iq, final Jingle jout)
    '''
def createAck():
    '''    public IQ createAck(final IQ iq)
    '''
def hashCode():
    '''    public int hashCode()
    '''
def equals():
    '''    public boolean equals(final Object obj)
    '''
def getInstanceFor():
    '''    public static synchronized JingleSession getInstanceFor(final XMPPConnection con)
    '''
def connectionTerminated():
    '''    public void connectionTerminated()
    '''
def processStanza():
    '''    public void processStanza(final Stanza packet)
    '''
def accept():
    '''    public boolean accept(final Stanza packet)
    '''
def addMediaListener():
    '''    public void addMediaListener(final JingleMediaListener li)
    '''
def removeMediaListener():
    '''    public void removeMediaListener(final JingleMediaListener li)
    '''
def addTransportListener():
    '''    public void addTransportListener(final JingleTransportListener li)
    '''
def removeTransportListener():
    '''    public void removeTransportListener(final JingleTransportListener li)
    '''
def setupListeners():
    '''    public void setupListeners()
    '''
def mediaClosed():
    '''    public void mediaClosed(final PayloadType cand)
    '''
def mediaEstablished():
    '''    public void mediaEstablished(final PayloadType pt)
    '''
def transportEstablished():
    '''    public void transportEstablished(final TransportCandidate local, final TransportCandidate remote)
    '''
def transportClosed():
    '''    public void transportClosed(final TransportCandidate cand)
    '''
def transportClosedOnError():
    '''    public void transportClosedOnError(final XMPPException e)
    '''
def terminate():
    '''    public void terminate()
    public void terminate(final String reason)
    '''
def close():
    '''    public void close()
    '''
def isClosed():
    '''    public boolean isClosed()
    '''
def createJingleError():
    '''    public IQ createJingleError(final IQ iq, final JingleError jingleError)
    '''
def mediaReceived():
    '''    public void mediaReceived(final String participant)
    '''
def startOutgoing():
    '''    public void startOutgoing()
    '''
def startIncoming():
    '''    public void startIncoming()
    '''
def addJingleMediaSession():
    '''    public void addJingleMediaSession(final String mediaManagerName, final JingleMediaSession mediaSession)
    '''
def getMediaSession():
    '''    public JingleMediaSession getMediaSession(final String mediaManagerName)
    '''
