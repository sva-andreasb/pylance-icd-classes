def BridgedTransportManager():
    '''    public BridgedTransportManager(final XMPPConnection xmppConnection)
    '''
def sessionEstablished():
    '''    public void sessionEstablished(final PayloadType pt, final TransportCandidate rc, final TransportCandidate lc, final JingleSession jingleSession)
    '''
def sessionDeclined():
    '''    public void sessionDeclined(final String reason, final JingleSession jingleSession)
    '''
def sessionRedirected():
    '''    public void sessionRedirected(final String redirection, final JingleSession jingleSession)
    '''
def sessionClosed():
    '''    public void sessionClosed(final String reason, final JingleSession jingleSession)
    '''
def sessionClosedOnError():
    '''    public void sessionClosedOnError(final XMPPException e, final JingleSession jingleSession)
    '''
def sessionMediaReceived():
    '''    public void sessionMediaReceived(final JingleSession jingleSession, final String participant)
    '''
def sessionCreated():
    '''    public void sessionCreated(final JingleSession jingleSession)
    '''
