MAXIMUM_BLOCK_SIZE = "int  65535"
def getByteStreamManager():
'''public static synchronized InBandBytestreamManager getByteStreamManager(final XMPPConnection connection)
'''
pass
def addIncomingBytestreamListener():
'''public void addIncomingBytestreamListener(final BytestreamListener listener)
public void addIncomingBytestreamListener(final BytestreamListener listener, final Jid initiatorJID)
'''
pass
def removeIncomingBytestreamListener():
'''public void removeIncomingBytestreamListener(final BytestreamListener listener)
public void removeIncomingBytestreamListener(final Jid initiatorJID)
'''
pass
def ignoreBytestreamRequestOnce():
'''public void ignoreBytestreamRequestOnce(final String sessionID)
'''
pass
def getDefaultBlockSize():
'''public int getDefaultBlockSize()
'''
pass
def setDefaultBlockSize():
'''public void setDefaultBlockSize(final int defaultBlockSize)
'''
pass
def getMaximumBlockSize():
'''public int getMaximumBlockSize()
'''
pass
def setMaximumBlockSize():
'''public void setMaximumBlockSize(final int maximumBlockSize)
'''
pass
def getStanza():
'''public StanzaType getStanza()
'''
pass
def setStanza():
'''public void setStanza(final StanzaType stanza)
'''
pass
def establishSession():
'''public InBandBytestreamSession establishSession(final Jid targetJID)
public InBandBytestreamSession establishSession(final Jid targetJID, final String sessionID)
'''
pass
def connectionCreated():
'''public void connectionCreated(final XMPPConnection connection)
'''
pass
def connectionTerminated():
'''public void connectionTerminated()
'''
pass
def connected():
'''public void connected(final XMPPConnection connection)
'''
pass
