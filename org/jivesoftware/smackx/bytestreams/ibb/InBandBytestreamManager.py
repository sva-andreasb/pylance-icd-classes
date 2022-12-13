MAXIMUM_BLOCK_SIZE = "int  65535"
def getByteStreamManager():
    '''    public static synchronized InBandBytestreamManager getByteStreamManager(final XMPPConnection connection)
    '''
def addIncomingBytestreamListener():
    '''    public void addIncomingBytestreamListener(final BytestreamListener listener)
    public void addIncomingBytestreamListener(final BytestreamListener listener, final Jid initiatorJID)
    '''
def removeIncomingBytestreamListener():
    '''    public void removeIncomingBytestreamListener(final BytestreamListener listener)
    public void removeIncomingBytestreamListener(final Jid initiatorJID)
    '''
def ignoreBytestreamRequestOnce():
    '''    public void ignoreBytestreamRequestOnce(final String sessionID)
    '''
def getDefaultBlockSize():
    '''    public int getDefaultBlockSize()
    '''
def setDefaultBlockSize():
    '''    public void setDefaultBlockSize(final int defaultBlockSize)
    '''
def getMaximumBlockSize():
    '''    public int getMaximumBlockSize()
    '''
def setMaximumBlockSize():
    '''    public void setMaximumBlockSize(final int maximumBlockSize)
    '''
def getStanza():
    '''    public StanzaType getStanza()
    '''
def setStanza():
    '''    public void setStanza(final StanzaType stanza)
    '''
def establishSession():
    '''    public InBandBytestreamSession establishSession(final Jid targetJID)
    public InBandBytestreamSession establishSession(final Jid targetJID, final String sessionID)
    '''
def connectionCreated():
    '''    public void connectionCreated(final XMPPConnection connection)
    '''
def connectionTerminated():
    '''    public void connectionTerminated()
    '''
def connected():
    '''    public void connected(final XMPPConnection connection)
    '''
