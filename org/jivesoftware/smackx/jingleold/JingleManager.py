def JingleManager():
    '''public JingleManager(final XMPPConnection connection, final List<JingleMediaManager> jingleMediaManagers)
    '''
def entriesAdded():
    '''public void entriesAdded(final Collection<Jid> addresses)
    '''
def entriesUpdated():
    '''public void entriesUpdated(final Collection<Jid> addresses)
    '''
def entriesDeleted():
    '''public void entriesDeleted(final Collection<Jid> addresses)
    '''
def presenceChanged():
    '''public void presenceChanged(final Presence presence)
    '''
def setJingleServiceEnabled():
    '''public static void setJingleServiceEnabled()
    '''
def connectionCreated():
    '''public void connectionCreated(final XMPPConnection connection)
    '''
def setServiceEnabled():
    '''public static synchronized void setServiceEnabled(final XMPPConnection connection, final boolean enabled)
    '''
def isServiceEnabled():
    '''public static boolean isServiceEnabled(final XMPPConnection connection)
    public static boolean isServiceEnabled(final XMPPConnection connection, final Jid userID)
    '''
def getMediaManagers():
    '''public List<JingleMediaManager> getMediaManagers()
    '''
def setMediaManagers():
    '''public void setMediaManagers(final List<JingleMediaManager> jingleMediaManagers)
    '''
def addJingleSessionRequestListener():
    '''public synchronized void addJingleSessionRequestListener(final JingleSessionRequestListener jingleSessionRequestListener)
    '''
def removeJingleSessionRequestListener():
    '''public void removeJingleSessionRequestListener(final JingleSessionRequestListener jingleSessionRequestListener)
    '''
def addCreationListener():
    '''public void addCreationListener(final CreatedJingleSessionListener createdJingleSessionListener)
    '''
def removeCreationListener():
    '''public void removeCreationListener(final CreatedJingleSessionListener createdJingleSessionListener)
    '''
def triggerSessionCreated():
    '''public void triggerSessionCreated(final JingleSession jingleSession)
    '''
def sessionEstablished():
    '''public void sessionEstablished(final PayloadType pt, final TransportCandidate rc, final TransportCandidate lc, final JingleSession jingleSession)
    '''
def sessionDeclined():
    '''public void sessionDeclined(final String reason, final JingleSession jingleSession)
    '''
def sessionRedirected():
    '''public void sessionRedirected(final String redirection, final JingleSession jingleSession)
    '''
def sessionClosed():
    '''public void sessionClosed(final String reason, final JingleSession jingleSession)
    '''
def sessionClosedOnError():
    '''public void sessionClosedOnError(final XMPPException e, final JingleSession jingleSession)
    '''
def sessionMediaReceived():
    '''public void sessionMediaReceived(final JingleSession jingleSession, final String participant)
    '''
def accept():
    '''public boolean accept(final Stanza pin)
    '''
def processStanza():
    '''public void processStanza(final Stanza packet)
    '''
def disconnectAllSessions():
    '''public void disconnectAllSessions()
    '''
def createOutgoingJingleSession():
    '''public JingleSession createOutgoingJingleSession(final EntityFullJid responder)
    '''
def createIncomingJingleSession():
    '''public JingleSession createIncomingJingleSession(final JingleSessionRequest request)
    '''
def getSession():
    '''public JingleSession getSession(final String jid)
    '''
