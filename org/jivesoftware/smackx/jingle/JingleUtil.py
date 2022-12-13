def JingleUtil():
    '''public JingleUtil(final XMPPConnection connection)
    '''
def createSessionInitiate():
    '''public Jingle createSessionInitiate(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContent.Senders contentSenders, final JingleContentDescription description, final JingleContentTransport transport)
    '''
def createSessionInitiateFileOffer():
    '''public Jingle createSessionInitiateFileOffer(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentDescription description, final JingleContentTransport transport)
    '''
def sendSessionInitiateFileOffer():
    '''public IQ sendSessionInitiateFileOffer(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentDescription description, final JingleContentTransport transport)
    '''
def sendSessionInitiate():
    '''public IQ sendSessionInitiate(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContent.Senders contentSenders, final JingleContentDescription description, final JingleContentTransport transport)
    '''
def createSessionAccept():
    '''public Jingle createSessionAccept(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContent.Senders contentSenders, final JingleContentDescription description, final JingleContentTransport transport)
    '''
def sendSessionAccept():
    '''public IQ sendSessionAccept(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContent.Senders contentSenders, final JingleContentDescription description, final JingleContentTransport transport)
    '''
def createSessionTerminate():
    '''public Jingle createSessionTerminate(final FullJid recipient, final String sessionId, final JingleReason reason)
    public Jingle createSessionTerminate(final FullJid recipient, final String sessionId, final JingleReason.Reason reason)
    '''
def createSessionTerminateDecline():
    '''public Jingle createSessionTerminateDecline(final FullJid recipient, final String sessionId)
    '''
def sendSessionTerminateDecline():
    '''public IQ sendSessionTerminateDecline(final FullJid recipient, final String sessionId)
    '''
def createSessionTerminateSuccess():
    '''public Jingle createSessionTerminateSuccess(final FullJid recipient, final String sessionId)
    '''
def sendSessionTerminateSuccess():
    '''public IQ sendSessionTerminateSuccess(final FullJid recipient, final String sessionId)
    '''
def createSessionTerminateBusy():
    '''public Jingle createSessionTerminateBusy(final FullJid recipient, final String sessionId)
    '''
def sendSessionTerminateBusy():
    '''public IQ sendSessionTerminateBusy(final FullJid recipient, final String sessionId)
    '''
def createSessionTerminateAlternativeSession():
    '''public Jingle createSessionTerminateAlternativeSession(final FullJid recipient, final String sessionId, final String altSessionId)
    '''
def sendSessionTerminateAlternativeSession():
    '''public IQ sendSessionTerminateAlternativeSession(final FullJid recipient, final String sessionId, final String altSessionId)
    '''
def createSessionTerminateCancel():
    '''public Jingle createSessionTerminateCancel(final FullJid recipient, final String sessionId)
    '''
def sendSessionTerminateCancel():
    '''public IQ sendSessionTerminateCancel(final FullJid recipient, final String sessionId)
    '''
def createSessionTerminateContentCancel():
    '''public Jingle createSessionTerminateContentCancel(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName)
    '''
def sendSessionTerminateContentCancel():
    '''public IQ sendSessionTerminateContentCancel(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName)
    '''
def createSessionTerminateUnsupportedTransports():
    '''public Jingle createSessionTerminateUnsupportedTransports(final FullJid recipient, final String sessionId)
    '''
def sendSessionTerminateUnsupportedTransports():
    '''public IQ sendSessionTerminateUnsupportedTransports(final FullJid recipient, final String sessionId)
    '''
def createSessionTerminateFailedTransport():
    '''public Jingle createSessionTerminateFailedTransport(final FullJid recipient, final String sessionId)
    '''
def sendSessionTerminateFailedTransport():
    '''public IQ sendSessionTerminateFailedTransport(final FullJid recipient, final String sessionId)
    '''
def createSessionTerminateUnsupportedApplications():
    '''public Jingle createSessionTerminateUnsupportedApplications(final FullJid recipient, final String sessionId)
    '''
def sendSessionTerminateUnsupportedApplications():
    '''public IQ sendSessionTerminateUnsupportedApplications(final FullJid recipient, final String sessionId)
    '''
def createSessionTerminateFailedApplication():
    '''public Jingle createSessionTerminateFailedApplication(final FullJid recipient, final String sessionId)
    '''
def sendSessionTerminateFailedApplication():
    '''public IQ sendSessionTerminateFailedApplication(final FullJid recipient, final String sessionId)
    '''
def createSessionTerminateIncompatibleParameters():
    '''public Jingle createSessionTerminateIncompatibleParameters(final FullJid recipient, final String sessionId)
    '''
def sendSessionTerminateIncompatibleParameters():
    '''public IQ sendSessionTerminateIncompatibleParameters(final FullJid recipient, final String sessionId)
    '''
def sendContentRejectFileNotAvailable():
    '''public IQ sendContentRejectFileNotAvailable(final FullJid recipient, final String sessionId, final JingleContentDescription description)
    '''
def createSessionPing():
    '''public Jingle createSessionPing(final FullJid recipient, final String sessionId)
    '''
def sendSessionPing():
    '''public IQ sendSessionPing(final FullJid recipient, final String sessionId)
    '''
def createAck():
    '''public IQ createAck(final Jingle jingle)
    '''
def sendAck():
    '''public void sendAck(final Jingle jingle)
    '''
def createTransportReplace():
    '''public Jingle createTransportReplace(final FullJid recipient, final FullJid initiator, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentTransport transport)
    '''
def sendTransportReplace():
    '''public IQ sendTransportReplace(final FullJid recipient, final FullJid initiator, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentTransport transport)
    '''
def createTransportAccept():
    '''public Jingle createTransportAccept(final FullJid recipient, final FullJid initiator, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentTransport transport)
    '''
def sendTransportAccept():
    '''public IQ sendTransportAccept(final FullJid recipient, final FullJid initiator, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentTransport transport)
    '''
def createTransportReject():
    '''public Jingle createTransportReject(final FullJid recipient, final FullJid initiator, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentTransport transport)
    '''
def sendTransportReject():
    '''public IQ sendTransportReject(final FullJid recipient, final FullJid initiator, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentTransport transport)
    '''
def createErrorUnknownSession():
    '''public IQ createErrorUnknownSession(final Jingle request)
    '''
def sendErrorUnknownSession():
    '''public void sendErrorUnknownSession(final Jingle request)
    '''
def createErrorUnknownInitiator():
    '''public IQ createErrorUnknownInitiator(final Jingle request)
    '''
def sendErrorUnknownInitiator():
    '''public void sendErrorUnknownInitiator(final Jingle request)
    '''
def createErrorUnsupportedInfo():
    '''public IQ createErrorUnsupportedInfo(final Jingle request)
    '''
def sendErrorUnsupportedInfo():
    '''public void sendErrorUnsupportedInfo(final Jingle request)
    '''
def createErrorTieBreak():
    '''public IQ createErrorTieBreak(final Jingle request)
    '''
def sendErrorTieBreak():
    '''public void sendErrorTieBreak(final Jingle request)
    '''
def createErrorOutOfOrder():
    '''public IQ createErrorOutOfOrder(final Jingle request)
    '''
def sendErrorOutOfOrder():
    '''public void sendErrorOutOfOrder(final Jingle request)
    '''
def createErrorMalformedRequest():
    '''public IQ createErrorMalformedRequest(final Jingle request)
    '''
def sendErrorMalformedRequest():
    '''public void sendErrorMalformedRequest(final Jingle request)
    '''
