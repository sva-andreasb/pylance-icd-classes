def ():
    '''returns JingleUtil\n\n
    (final XMPPConnection connection)\n
    '''
def createSessionInitiate():
    '''returns Jingle\n\n
    createSessionInitiate(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContent.Senders contentSenders, final JingleContentDescription description, final JingleContentTransport transport)\n
    '''
def createSessionInitiateFileOffer():
    '''returns Jingle\n\n
    createSessionInitiateFileOffer(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentDescription description, final JingleContentTransport transport)\n
    '''
def sendSessionInitiateFileOffer():
    '''returns IQ\n\n
    sendSessionInitiateFileOffer(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentDescription description, final JingleContentTransport transport)\n
    '''
def sendSessionInitiate():
    '''returns IQ\n\n
    sendSessionInitiate(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContent.Senders contentSenders, final JingleContentDescription description, final JingleContentTransport transport)\n
    '''
def createSessionAccept():
    '''returns Jingle\n\n
    createSessionAccept(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContent.Senders contentSenders, final JingleContentDescription description, final JingleContentTransport transport)\n
    '''
def sendSessionAccept():
    '''returns IQ\n\n
    sendSessionAccept(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContent.Senders contentSenders, final JingleContentDescription description, final JingleContentTransport transport)\n
    '''
def createSessionTerminate():
    '''returns Jingle\n\n
    createSessionTerminate(final FullJid recipient, final String sessionId, final JingleReason reason)\n
    createSessionTerminate(final FullJid recipient, final String sessionId, final JingleReason.Reason reason)\n
    '''
def createSessionTerminateDecline():
    '''returns Jingle\n\n
    createSessionTerminateDecline(final FullJid recipient, final String sessionId)\n
    '''
def sendSessionTerminateDecline():
    '''returns IQ\n\n
    sendSessionTerminateDecline(final FullJid recipient, final String sessionId)\n
    '''
def createSessionTerminateSuccess():
    '''returns Jingle\n\n
    createSessionTerminateSuccess(final FullJid recipient, final String sessionId)\n
    '''
def sendSessionTerminateSuccess():
    '''returns IQ\n\n
    sendSessionTerminateSuccess(final FullJid recipient, final String sessionId)\n
    '''
def createSessionTerminateBusy():
    '''returns Jingle\n\n
    createSessionTerminateBusy(final FullJid recipient, final String sessionId)\n
    '''
def sendSessionTerminateBusy():
    '''returns IQ\n\n
    sendSessionTerminateBusy(final FullJid recipient, final String sessionId)\n
    '''
def createSessionTerminateAlternativeSession():
    '''returns Jingle\n\n
    createSessionTerminateAlternativeSession(final FullJid recipient, final String sessionId, final String altSessionId)\n
    '''
def sendSessionTerminateAlternativeSession():
    '''returns IQ\n\n
    sendSessionTerminateAlternativeSession(final FullJid recipient, final String sessionId, final String altSessionId)\n
    '''
def createSessionTerminateCancel():
    '''returns Jingle\n\n
    createSessionTerminateCancel(final FullJid recipient, final String sessionId)\n
    '''
def sendSessionTerminateCancel():
    '''returns IQ\n\n
    sendSessionTerminateCancel(final FullJid recipient, final String sessionId)\n
    '''
def createSessionTerminateContentCancel():
    '''returns Jingle\n\n
    createSessionTerminateContentCancel(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName)\n
    '''
def sendSessionTerminateContentCancel():
    '''returns IQ\n\n
    sendSessionTerminateContentCancel(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName)\n
    '''
def createSessionTerminateUnsupportedTransports():
    '''returns Jingle\n\n
    createSessionTerminateUnsupportedTransports(final FullJid recipient, final String sessionId)\n
    '''
def sendSessionTerminateUnsupportedTransports():
    '''returns IQ\n\n
    sendSessionTerminateUnsupportedTransports(final FullJid recipient, final String sessionId)\n
    '''
def createSessionTerminateFailedTransport():
    '''returns Jingle\n\n
    createSessionTerminateFailedTransport(final FullJid recipient, final String sessionId)\n
    '''
def sendSessionTerminateFailedTransport():
    '''returns IQ\n\n
    sendSessionTerminateFailedTransport(final FullJid recipient, final String sessionId)\n
    '''
def createSessionTerminateUnsupportedApplications():
    '''returns Jingle\n\n
    createSessionTerminateUnsupportedApplications(final FullJid recipient, final String sessionId)\n
    '''
def sendSessionTerminateUnsupportedApplications():
    '''returns IQ\n\n
    sendSessionTerminateUnsupportedApplications(final FullJid recipient, final String sessionId)\n
    '''
def createSessionTerminateFailedApplication():
    '''returns Jingle\n\n
    createSessionTerminateFailedApplication(final FullJid recipient, final String sessionId)\n
    '''
def sendSessionTerminateFailedApplication():
    '''returns IQ\n\n
    sendSessionTerminateFailedApplication(final FullJid recipient, final String sessionId)\n
    '''
def createSessionTerminateIncompatibleParameters():
    '''returns Jingle\n\n
    createSessionTerminateIncompatibleParameters(final FullJid recipient, final String sessionId)\n
    '''
def sendSessionTerminateIncompatibleParameters():
    '''returns IQ\n\n
    sendSessionTerminateIncompatibleParameters(final FullJid recipient, final String sessionId)\n
    '''
def sendContentRejectFileNotAvailable():
    '''returns IQ\n\n
    sendContentRejectFileNotAvailable(final FullJid recipient, final String sessionId, final JingleContentDescription description)\n
    '''
def createSessionPing():
    '''returns Jingle\n\n
    createSessionPing(final FullJid recipient, final String sessionId)\n
    '''
def sendSessionPing():
    '''returns IQ\n\n
    sendSessionPing(final FullJid recipient, final String sessionId)\n
    '''
def createAck():
    '''returns IQ\n\n
    createAck(final Jingle jingle)\n
    '''
def sendAck():
    '''returns None\n\n
    sendAck(final Jingle jingle)\n
    '''
def createTransportReplace():
    '''returns Jingle\n\n
    createTransportReplace(final FullJid recipient, final FullJid initiator, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentTransport transport)\n
    '''
def sendTransportReplace():
    '''returns IQ\n\n
    sendTransportReplace(final FullJid recipient, final FullJid initiator, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentTransport transport)\n
    '''
def createTransportAccept():
    '''returns Jingle\n\n
    createTransportAccept(final FullJid recipient, final FullJid initiator, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentTransport transport)\n
    '''
def sendTransportAccept():
    '''returns IQ\n\n
    sendTransportAccept(final FullJid recipient, final FullJid initiator, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentTransport transport)\n
    '''
def createTransportReject():
    '''returns Jingle\n\n
    createTransportReject(final FullJid recipient, final FullJid initiator, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentTransport transport)\n
    '''
def sendTransportReject():
    '''returns IQ\n\n
    sendTransportReject(final FullJid recipient, final FullJid initiator, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentTransport transport)\n
    '''
def createErrorUnknownSession():
    '''returns IQ\n\n
    createErrorUnknownSession(final Jingle request)\n
    '''
def sendErrorUnknownSession():
    '''returns None\n\n
    sendErrorUnknownSession(final Jingle request)\n
    '''
def createErrorUnknownInitiator():
    '''returns IQ\n\n
    createErrorUnknownInitiator(final Jingle request)\n
    '''
def sendErrorUnknownInitiator():
    '''returns None\n\n
    sendErrorUnknownInitiator(final Jingle request)\n
    '''
def createErrorUnsupportedInfo():
    '''returns IQ\n\n
    createErrorUnsupportedInfo(final Jingle request)\n
    '''
def sendErrorUnsupportedInfo():
    '''returns None\n\n
    sendErrorUnsupportedInfo(final Jingle request)\n
    '''
def createErrorTieBreak():
    '''returns IQ\n\n
    createErrorTieBreak(final Jingle request)\n
    '''
def sendErrorTieBreak():
    '''returns None\n\n
    sendErrorTieBreak(final Jingle request)\n
    '''
def createErrorOutOfOrder():
    '''returns IQ\n\n
    createErrorOutOfOrder(final Jingle request)\n
    '''
def sendErrorOutOfOrder():
    '''returns None\n\n
    sendErrorOutOfOrder(final Jingle request)\n
    '''
def createErrorMalformedRequest():
    '''returns IQ\n\n
    createErrorMalformedRequest(final Jingle request)\n
    '''
def sendErrorMalformedRequest():
    '''returns None\n\n
    sendErrorMalformedRequest(final Jingle request)\n
    '''
