SI_NAMESPACE = "String  \"http://jabber.org/protocol/si\""
SI_PROFILE_FILE_TRANSFER_NAMESPACE = "String  \"http://jabber.org/protocol/si/profile/file-transfer\""
def selectStreamNegotiator():
    '''returns StreamNegotiator\n\n
    selectStreamNegotiator(final FileTransferRequest request)\n
    '''
def negotiateOutgoingTransfer():
    '''returns StreamNegotiator\n\n
    negotiateOutgoingTransfer(final Jid userID, final String streamID, final String fileName, final long size, final String desc, final int responseTimeout)\n
    '''
