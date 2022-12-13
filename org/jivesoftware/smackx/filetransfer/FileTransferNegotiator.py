SI_NAMESPACE = "String  \"http://jabber.org/protocol/si\""
SI_PROFILE_FILE_TRANSFER_NAMESPACE = "String  \"http://jabber.org/protocol/si/profile/file-transfer\""
def getInstanceFor():
    '''public static synchronized FileTransferNegotiator getInstanceFor(final XMPPConnection connection)
    '''
def isServiceEnabled():
    '''public static boolean isServiceEnabled(final XMPPConnection connection)
    '''
def getSupportedProtocols():
    '''public static Collection<String> getSupportedProtocols()
    '''
def selectStreamNegotiator():
    '''public StreamNegotiator selectStreamNegotiator(final FileTransferRequest request)
    '''
def getNextStreamID():
    '''public static String getNextStreamID()
    '''
def negotiateOutgoingTransfer():
    '''public StreamNegotiator negotiateOutgoingTransfer(final Jid userID, final String streamID, final String fileName, final long size, final String desc, final int responseTimeout)
    '''
