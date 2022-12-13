def JingleManager():
'''public JingleManager(final XMPPConnection connection, final List<JingleMediaManager> jingleMediaManagers)
'''
pass
def entriesAdded():
'''public void entriesAdded(final Collection<Jid> addresses)
'''
pass
def entriesUpdated():
'''public void entriesUpdated(final Collection<Jid> addresses)
'''
pass
def entriesDeleted():
'''public void entriesDeleted(final Collection<Jid> addresses)
'''
pass
def presenceChanged():
'''public void presenceChanged(final Presence presence)
'''
pass
def setJingleServiceEnabled():
'''public static void setJingleServiceEnabled()
'''
pass
def connectionCreated():
'''public void connectionCreated(final XMPPConnection connection)
'''
pass
def setServiceEnabled():
'''public static synchronized void setServiceEnabled(final XMPPConnection connection, final boolean enabled)
'''
pass
def isServiceEnabled():
'''public static boolean isServiceEnabled(final XMPPConnection connection)
public static boolean isServiceEnabled(final XMPPConnection connection, final Jid userID)
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
def addJingleSessionRequestListener():
'''public synchronized void addJingleSessionRequestListener(final JingleSessionRequestListener jingleSessionRequestListener)
'''
pass
def removeJingleSessionRequestListener():
'''public void removeJingleSessionRequestListener(final JingleSessionRequestListener jingleSessionRequestListener)
'''
pass
def addCreationListener():
'''public void addCreationListener(final CreatedJingleSessionListener createdJingleSessionListener)
'''
pass
def removeCreationListener():
'''public void removeCreationListener(final CreatedJingleSessionListener createdJingleSessionListener)
'''
pass
def triggerSessionCreated():
'''public void triggerSessionCreated(final JingleSession jingleSession)
'''
pass
def sessionEstablished():
'''public void sessionEstablished(final PayloadType pt, final TransportCandidate rc, final TransportCandidate lc, final JingleSession jingleSession)
'''
pass
def sessionDeclined():
'''public void sessionDeclined(final String reason, final JingleSession jingleSession)
'''
pass
def sessionRedirected():
'''public void sessionRedirected(final String redirection, final JingleSession jingleSession)
'''
pass
def sessionClosed():
'''public void sessionClosed(final String reason, final JingleSession jingleSession)
'''
pass
def sessionClosedOnError():
'''public void sessionClosedOnError(final XMPPException e, final JingleSession jingleSession)
'''
pass
def sessionMediaReceived():
'''public void sessionMediaReceived(final JingleSession jingleSession, final String participant)
'''
pass
def accept():
'''public boolean accept(final Stanza pin)
'''
pass
def processStanza():
'''public void processStanza(final Stanza packet)
'''
pass
def disconnectAllSessions():
'''public void disconnectAllSessions()
'''
pass
def createOutgoingJingleSession():
'''public JingleSession createOutgoingJingleSession(final EntityFullJid responder)
'''
pass
def createIncomingJingleSession():
'''public JingleSession createIncomingJingleSession(final JingleSessionRequest request)
'''
pass
def getSession():
'''public JingleSession getSession(final String jid)
'''
pass
