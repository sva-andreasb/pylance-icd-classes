def ():
    '''returns AbstractDebugger\n\n
    (final XMPPConnection connection)\n
    '''
def read():
    '''returns None\n\n
    read(final String str)\n
    '''
def write():
    '''returns None\n\n
    write(final String str)\n
    '''
def connected():
    '''returns None\n\n
    connected(final XMPPConnection connection)\n
    '''
def authenticated():
    '''returns None\n\n
    authenticated(final XMPPConnection connection, final boolean resumed)\n
    '''
def connectionClosed():
    '''returns None\n\n
    connectionClosed()\n
    '''
def connectionClosedOnError():
    '''returns None\n\n
    connectionClosedOnError(final Exception e)\n
    '''
def reconnectionFailed():
    '''returns None\n\n
    reconnectionFailed(final Exception e)\n
    '''
def reconnectingIn():
    '''returns None\n\n
    reconnectingIn(final int seconds)\n
    '''
def newConnectionReader():
    '''returns Reader\n\n
    newConnectionReader(final Reader newReader)\n
    '''
def newConnectionWriter():
    '''returns Writer\n\n
    newConnectionWriter(final Writer newWriter)\n
    '''
def userHasLogged():
    '''returns None\n\n
    userHasLogged(final EntityFullJid user)\n
    '''
def onIncomingStreamElement():
    '''returns None\n\n
    onIncomingStreamElement(final TopLevelStreamElement streamElement)\n
    '''
def onOutgoingStreamElement():
    '''returns None\n\n
    onOutgoingStreamElement(final TopLevelStreamElement streamElement)\n
    '''
