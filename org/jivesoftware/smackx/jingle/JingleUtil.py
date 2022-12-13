def JingleUtil():
'''public JingleUtil(final XMPPConnection connection)
'''
pass
def createSessionInitiate():
'''public Jingle createSessionInitiate(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContent.Senders contentSenders, final JingleContentDescription description, final JingleContentTransport transport)
'''
pass
def createSessionInitiateFileOffer():
'''public Jingle createSessionInitiateFileOffer(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentDescription description, final JingleContentTransport transport)
'''
pass
def sendSessionInitiateFileOffer():
'''public IQ sendSessionInitiateFileOffer(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentDescription description, final JingleContentTransport transport)
'''
pass
def sendSessionInitiate():
'''public IQ sendSessionInitiate(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContent.Senders contentSenders, final JingleContentDescription description, final JingleContentTransport transport)
'''
pass
def createSessionAccept():
'''public Jingle createSessionAccept(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContent.Senders contentSenders, final JingleContentDescription description, final JingleContentTransport transport)
'''
pass
def sendSessionAccept():
'''public IQ sendSessionAccept(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContent.Senders contentSenders, final JingleContentDescription description, final JingleContentTransport transport)
'''
pass
def createSessionTerminate():
'''public Jingle createSessionTerminate(final FullJid recipient, final String sessionId, final JingleReason reason)
public Jingle createSessionTerminate(final FullJid recipient, final String sessionId, final JingleReason.Reason reason)
'''
pass
def createSessionTerminateDecline():
'''public Jingle createSessionTerminateDecline(final FullJid recipient, final String sessionId)
'''
pass
def sendSessionTerminateDecline():
'''public IQ sendSessionTerminateDecline(final FullJid recipient, final String sessionId)
'''
pass
def createSessionTerminateSuccess():
'''public Jingle createSessionTerminateSuccess(final FullJid recipient, final String sessionId)
'''
pass
def sendSessionTerminateSuccess():
'''public IQ sendSessionTerminateSuccess(final FullJid recipient, final String sessionId)
'''
pass
def createSessionTerminateBusy():
'''public Jingle createSessionTerminateBusy(final FullJid recipient, final String sessionId)
'''
pass
def sendSessionTerminateBusy():
'''public IQ sendSessionTerminateBusy(final FullJid recipient, final String sessionId)
'''
pass
def createSessionTerminateAlternativeSession():
'''public Jingle createSessionTerminateAlternativeSession(final FullJid recipient, final String sessionId, final String altSessionId)
'''
pass
def sendSessionTerminateAlternativeSession():
'''public IQ sendSessionTerminateAlternativeSession(final FullJid recipient, final String sessionId, final String altSessionId)
'''
pass
def createSessionTerminateCancel():
'''public Jingle createSessionTerminateCancel(final FullJid recipient, final String sessionId)
'''
pass
def sendSessionTerminateCancel():
'''public IQ sendSessionTerminateCancel(final FullJid recipient, final String sessionId)
'''
pass
def createSessionTerminateContentCancel():
'''public Jingle createSessionTerminateContentCancel(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName)
'''
pass
def sendSessionTerminateContentCancel():
'''public IQ sendSessionTerminateContentCancel(final FullJid recipient, final String sessionId, final JingleContent.Creator contentCreator, final String contentName)
'''
pass
def createSessionTerminateUnsupportedTransports():
'''public Jingle createSessionTerminateUnsupportedTransports(final FullJid recipient, final String sessionId)
'''
pass
def sendSessionTerminateUnsupportedTransports():
'''public IQ sendSessionTerminateUnsupportedTransports(final FullJid recipient, final String sessionId)
'''
pass
def createSessionTerminateFailedTransport():
'''public Jingle createSessionTerminateFailedTransport(final FullJid recipient, final String sessionId)
'''
pass
def sendSessionTerminateFailedTransport():
'''public IQ sendSessionTerminateFailedTransport(final FullJid recipient, final String sessionId)
'''
pass
def createSessionTerminateUnsupportedApplications():
'''public Jingle createSessionTerminateUnsupportedApplications(final FullJid recipient, final String sessionId)
'''
pass
def sendSessionTerminateUnsupportedApplications():
'''public IQ sendSessionTerminateUnsupportedApplications(final FullJid recipient, final String sessionId)
'''
pass
def createSessionTerminateFailedApplication():
'''public Jingle createSessionTerminateFailedApplication(final FullJid recipient, final String sessionId)
'''
pass
def sendSessionTerminateFailedApplication():
'''public IQ sendSessionTerminateFailedApplication(final FullJid recipient, final String sessionId)
'''
pass
def createSessionTerminateIncompatibleParameters():
'''public Jingle createSessionTerminateIncompatibleParameters(final FullJid recipient, final String sessionId)
'''
pass
def sendSessionTerminateIncompatibleParameters():
'''public IQ sendSessionTerminateIncompatibleParameters(final FullJid recipient, final String sessionId)
'''
pass
def sendContentRejectFileNotAvailable():
'''public IQ sendContentRejectFileNotAvailable(final FullJid recipient, final String sessionId, final JingleContentDescription description)
'''
pass
def createSessionPing():
'''public Jingle createSessionPing(final FullJid recipient, final String sessionId)
'''
pass
def sendSessionPing():
'''public IQ sendSessionPing(final FullJid recipient, final String sessionId)
'''
pass
def createAck():
'''public IQ createAck(final Jingle jingle)
'''
pass
def sendAck():
'''public void sendAck(final Jingle jingle)
'''
pass
def createTransportReplace():
'''public Jingle createTransportReplace(final FullJid recipient, final FullJid initiator, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentTransport transport)
'''
pass
def sendTransportReplace():
'''public IQ sendTransportReplace(final FullJid recipient, final FullJid initiator, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentTransport transport)
'''
pass
def createTransportAccept():
'''public Jingle createTransportAccept(final FullJid recipient, final FullJid initiator, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentTransport transport)
'''
pass
def sendTransportAccept():
'''public IQ sendTransportAccept(final FullJid recipient, final FullJid initiator, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentTransport transport)
'''
pass
def createTransportReject():
'''public Jingle createTransportReject(final FullJid recipient, final FullJid initiator, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentTransport transport)
'''
pass
def sendTransportReject():
'''public IQ sendTransportReject(final FullJid recipient, final FullJid initiator, final String sessionId, final JingleContent.Creator contentCreator, final String contentName, final JingleContentTransport transport)
'''
pass
def createErrorUnknownSession():
'''public IQ createErrorUnknownSession(final Jingle request)
'''
pass
def sendErrorUnknownSession():
'''public void sendErrorUnknownSession(final Jingle request)
'''
pass
def createErrorUnknownInitiator():
'''public IQ createErrorUnknownInitiator(final Jingle request)
'''
pass
def sendErrorUnknownInitiator():
'''public void sendErrorUnknownInitiator(final Jingle request)
'''
pass
def createErrorUnsupportedInfo():
'''public IQ createErrorUnsupportedInfo(final Jingle request)
'''
pass
def sendErrorUnsupportedInfo():
'''public void sendErrorUnsupportedInfo(final Jingle request)
'''
pass
def createErrorTieBreak():
'''public IQ createErrorTieBreak(final Jingle request)
'''
pass
def sendErrorTieBreak():
'''public void sendErrorTieBreak(final Jingle request)
'''
pass
def createErrorOutOfOrder():
'''public IQ createErrorOutOfOrder(final Jingle request)
'''
pass
def sendErrorOutOfOrder():
'''public void sendErrorOutOfOrder(final Jingle request)
'''
pass
def createErrorMalformedRequest():
'''public IQ createErrorMalformedRequest(final Jingle request)
'''
pass
def sendErrorMalformedRequest():
'''public void sendErrorMalformedRequest(final Jingle request)
'''
pass
