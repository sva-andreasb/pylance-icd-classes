def ():
    '''returns ConsoleDebugger\n\n
    (final Connection connection, final Writer writer, final Reader reader)\n
    '''
def read():
    '''returns None\n\n
    read(final String str)\n
    '''
def write():
    '''returns None\n\n
    write(final String str)\n
    '''
def processPacket():
    '''returns None\n\n
    processPacket(final Packet packet)\n
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
def reconnectionSuccessful():
    '''returns None\n\n
    reconnectionSuccessful()\n
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
    userHasLogged(final String user)\n
    '''
def getReader():
    '''returns Reader\n\n
    getReader()\n
    '''
def getWriter():
    '''returns Writer\n\n
    getWriter()\n
    '''
def getReaderListener():
    '''returns PacketListener\n\n
    getReaderListener()\n
    '''
def getWriterListener():
    '''returns PacketListener\n\n
    getWriterListener()\n
    '''
