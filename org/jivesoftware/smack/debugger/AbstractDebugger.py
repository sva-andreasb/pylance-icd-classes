def AbstractDebugger():
    '''    public AbstractDebugger(final XMPPConnection connection)
    '''
def read():
    '''    public void read(final String str)
    '''
def write():
    '''    public void write(final String str)
    '''
def connected():
    '''    public void connected(final XMPPConnection connection)
    '''
def authenticated():
    '''    public void authenticated(final XMPPConnection connection, final boolean resumed)
    '''
def connectionClosed():
    '''    public void connectionClosed()
    '''
def connectionClosedOnError():
    '''    public void connectionClosedOnError(final Exception e)
    '''
def reconnectionFailed():
    '''    public void reconnectionFailed(final Exception e)
    '''
def reconnectingIn():
    '''    public void reconnectingIn(final int seconds)
    '''
def newConnectionReader():
    '''    public Reader newConnectionReader(final Reader newReader)
    '''
def newConnectionWriter():
    '''    public Writer newConnectionWriter(final Writer newWriter)
    '''
def userHasLogged():
    '''    public void userHasLogged(final EntityFullJid user)
    '''
def onIncomingStreamElement():
    '''    public void onIncomingStreamElement(final TopLevelStreamElement streamElement)
    '''
def onOutgoingStreamElement():
    '''    public void onOutgoingStreamElement(final TopLevelStreamElement streamElement)
    '''
