def ():
    '''returns FixedTransportManager\n\n
    (final FixedResolver inResolver)\n
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
def sessionCreated():
    '''returns None\n\n
    sessionCreated(final JingleSession jingleSession)\n
    '''
