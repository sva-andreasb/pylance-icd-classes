def JingleSession():
'''public JingleSession(final XMPPConnection conn, final Jid initiator, final Jid responder, final String sessionid, final List<JingleMediaManager> jingleMediaManagers)
public JingleSession(final XMPPConnection conn, final JingleSessionRequest request, final Jid initiator, final Jid responder, final List<JingleMediaManager> jingleMediaManagers)
'''
pass
def getInitiator():
'''public Jid getInitiator()
'''
pass
def getConnection():
'''public XMPPConnection getConnection()
'''
pass
def setInitiator():
'''public void setInitiator(final Jid initiator)
'''
pass
def getMediaManagers():
'''public List<JingleMediaManager> getMediaManagers()
'''
pass
def setMediaManagers():
'''public void setMediaManagers(final List<JingleMediaManager> jingleMediaManagers)
'''
pass
def getResponder():
'''public Jid getResponder()
'''
pass
def setResponder():
'''public void setResponder(final Jid responder)
'''
pass
def getSid():
'''public String getSid()
'''
pass
def setSessionState():
'''public void setSessionState(final JingleSessionState stateIs)
'''
pass
def getSessionState():
'''public JingleSessionState getSessionState()
'''
pass
def isFullyEstablished():
'''public boolean isFullyEstablished()
'''
pass
def receivePacketAndRespond():
'''public synchronized void receivePacketAndRespond(final IQ iq)
'''
pass
def dispatchIncomingPacket():
'''public List<IQ> dispatchIncomingPacket(final IQ iq, final String id)
'''
pass
def addContentNegotiator():
'''public void addContentNegotiator(final ContentNegotiator inContentNegotiator)
'''
pass
def sendStanza():
'''public void sendStanza(final IQ iq)
'''
pass
def sendFormattedJingle():
'''public Jingle sendFormattedJingle(final Jingle jout)
public Jingle sendFormattedJingle(final IQ iq, final Jingle jout)
'''
pass
def createAck():
'''public IQ createAck(final IQ iq)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
def getInstanceFor():
'''public static synchronized JingleSession getInstanceFor(final XMPPConnection con)
'''
pass
def connectionTerminated():
'''public void connectionTerminated()
'''
pass
def processStanza():
'''public void processStanza(final Stanza packet)
'''
pass
def accept():
'''public boolean accept(final Stanza packet)
'''
pass
def addMediaListener():
'''public void addMediaListener(final JingleMediaListener li)
'''
pass
def removeMediaListener():
'''public void removeMediaListener(final JingleMediaListener li)
'''
pass
def addTransportListener():
'''public void addTransportListener(final JingleTransportListener li)
'''
pass
def removeTransportListener():
'''public void removeTransportListener(final JingleTransportListener li)
'''
pass
def setupListeners():
'''public void setupListeners()
'''
pass
def mediaClosed():
'''public void mediaClosed(final PayloadType cand)
'''
pass
def mediaEstablished():
'''public void mediaEstablished(final PayloadType pt)
'''
pass
def transportEstablished():
'''public void transportEstablished(final TransportCandidate local, final TransportCandidate remote)
'''
pass
def transportClosed():
'''public void transportClosed(final TransportCandidate cand)
'''
pass
def transportClosedOnError():
'''public void transportClosedOnError(final XMPPException e)
'''
pass
def terminate():
'''public void terminate()
public void terminate(final String reason)
'''
pass
def close():
'''public void close()
'''
pass
def isClosed():
'''public boolean isClosed()
'''
pass
def createJingleError():
'''public IQ createJingleError(final IQ iq, final JingleError jingleError)
'''
pass
def mediaReceived():
'''public void mediaReceived(final String participant)
'''
pass
def startOutgoing():
'''public void startOutgoing()
'''
pass
def startIncoming():
'''public void startIncoming()
'''
pass
def addJingleMediaSession():
'''public void addJingleMediaSession(final String mediaManagerName, final JingleMediaSession mediaSession)
'''
pass
def getMediaSession():
'''public JingleMediaSession getMediaSession(final String mediaManagerName)
'''
pass
