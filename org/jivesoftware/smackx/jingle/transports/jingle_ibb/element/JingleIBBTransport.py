NAMESPACE_V1 = "String  \"urn:xmpp:jingle:transports:ibb:1\""
ATTR_BLOCK_SIZE = "String  \"block-size\""
ATTR_SID = "String  \"sid\""
DEFAULT_BLOCK_SIZE = "short  4096"
def JingleIBBTransport():
    '''public JingleIBBTransport()
    public JingleIBBTransport(final String sid)
    public JingleIBBTransport(final short blockSize)
    public JingleIBBTransport(final short blockSize, final String sid)
    '''
def getSessionId():
    '''public String getSessionId()
    '''
def getBlockSize():
    '''public short getBlockSize()
    '''
def getNamespace():
    '''public String getNamespace()
    '''
def equals():
    '''public boolean equals(final Object other)
    '''
def hashCode():
    '''public int hashCode()
    '''
