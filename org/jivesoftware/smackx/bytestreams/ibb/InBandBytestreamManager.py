MAXIMUM_BLOCK_SIZE = "int  65535"
def addIncomingBytestreamListener():
    '''returns None\n\n
    addIncomingBytestreamListener(final BytestreamListener listener)\n
    addIncomingBytestreamListener(final BytestreamListener listener, final Jid initiatorJID)\n
    '''
def removeIncomingBytestreamListener():
    '''returns None\n\n
    removeIncomingBytestreamListener(final BytestreamListener listener)\n
    removeIncomingBytestreamListener(final Jid initiatorJID)\n
    '''
def ignoreBytestreamRequestOnce():
    '''returns None\n\n
    ignoreBytestreamRequestOnce(final String sessionID)\n
    '''
def getDefaultBlockSize():
    '''returns int\n\n
    getDefaultBlockSize()\n
    '''
def setDefaultBlockSize():
    '''returns None\n\n
    setDefaultBlockSize(final int defaultBlockSize)\n
    '''
def getMaximumBlockSize():
    '''returns int\n\n
    getMaximumBlockSize()\n
    '''
def setMaximumBlockSize():
    '''returns None\n\n
    setMaximumBlockSize(final int maximumBlockSize)\n
    '''
def getStanza():
    '''returns StanzaType\n\n
    getStanza()\n
    '''
def setStanza():
    '''returns None\n\n
    setStanza(final StanzaType stanza)\n
    '''
def establishSession():
    '''returns InBandBytestreamSession\n\n
    establishSession(final Jid targetJID)\n
    establishSession(final Jid targetJID, final String sessionID)\n
    '''
def connectionCreated():
    '''returns None\n\n
    connectionCreated(final XMPPConnection connection)\n
    '''
def connectionTerminated():
    '''returns None\n\n
    connectionTerminated()\n
    '''
def connected():
    '''returns None\n\n
    connected(final XMPPConnection connection)\n
    '''
