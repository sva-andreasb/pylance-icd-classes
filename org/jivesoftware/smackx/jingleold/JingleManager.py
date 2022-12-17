def ():
    '''returns JingleManager\n\n
    (final XMPPConnection connection, final List<JingleMediaManager> jingleMediaManagers)\n
    '''
def entriesAdded():
    '''returns None\n\n
    entriesAdded(final Collection<Jid> addresses)\n
    '''
def entriesUpdated():
    '''returns None\n\n
    entriesUpdated(final Collection<Jid> addresses)\n
    '''
def entriesDeleted():
    '''returns None\n\n
    entriesDeleted(final Collection<Jid> addresses)\n
    '''
def presenceChanged():
    '''returns None\n\n
    presenceChanged(final Presence presence)\n
    '''
def connectionCreated():
    '''returns None\n\n
    connectionCreated(final XMPPConnection connection)\n
    '''
def getMediaManagers():
    '''returns List<JingleMediaManager>\n\n
    getMediaManagers()\n
    '''
def setMediaManagers():
    '''returns None\n\n
    setMediaManagers(final List<JingleMediaManager> jingleMediaManagers)\n
    '''
def removeJingleSessionRequestListener():
    '''returns None\n\n
    removeJingleSessionRequestListener(final JingleSessionRequestListener jingleSessionRequestListener)\n
    '''
def addCreationListener():
    '''returns None\n\n
    addCreationListener(final CreatedJingleSessionListener createdJingleSessionListener)\n
    '''
def removeCreationListener():
    '''returns None\n\n
    removeCreationListener(final CreatedJingleSessionListener createdJingleSessionListener)\n
    '''
def triggerSessionCreated():
    '''returns None\n\n
    triggerSessionCreated(final JingleSession jingleSession)\n
    '''
def sessionEstablished():
    '''returns None\n\n
    sessionEstablished(final PayloadType pt, final TransportCandidate rc, final TransportCandidate lc, final JingleSession jingleSession)\n
    '''
def sessionDeclined():
    '''returns None\n\n
    sessionDeclined(final String reason, final JingleSession jingleSession)\n
    '''
def sessionRedirected():
    '''returns None\n\n
    sessionRedirected(final String redirection, final JingleSession jingleSession)\n
    '''
def sessionClosed():
    '''returns None\n\n
    sessionClosed(final String reason, final JingleSession jingleSession)\n
    '''
def sessionClosedOnError():
    '''returns None\n\n
    sessionClosedOnError(final XMPPException e, final JingleSession jingleSession)\n
    '''
def sessionMediaReceived():
    '''returns None\n\n
    sessionMediaReceived(final JingleSession jingleSession, final String participant)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final Stanza pin)\n
    '''
def processStanza():
    '''returns None\n\n
    processStanza(final Stanza packet)\n
    '''
def disconnectAllSessions():
    '''returns None\n\n
    disconnectAllSessions()\n
    '''
def createOutgoingJingleSession():
    '''returns JingleSession\n\n
    createOutgoingJingleSession(final EntityFullJid responder)\n
    '''
def createIncomingJingleSession():
    '''returns JingleSession\n\n
    createIncomingJingleSession(final JingleSessionRequest request)\n
    '''
def getSession():
    '''returns JingleSession\n\n
    getSession(final String jid)\n
    '''
