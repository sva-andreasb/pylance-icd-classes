def BridgedTransportManager():
'''public BridgedTransportManager(final XMPPConnection xmppConnection)
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
def sessionCreated():
'''public void sessionCreated(final JingleSession jingleSession)
'''
pass
