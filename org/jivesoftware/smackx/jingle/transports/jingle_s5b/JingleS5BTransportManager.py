def getInstanceFor():
'''public static synchronized JingleS5BTransportManager getInstanceFor(final XMPPConnection connection)
'''
pass
def getNamespace():
'''public String getNamespace()
'''
pass
def transportSession():
'''public JingleTransportSession<JingleS5BTransport> transportSession(final JingleSession jingleSession)
'''
pass
def authenticated():
'''public void authenticated(final XMPPConnection connection, final boolean resumed)
'''
pass
def createCandidateUsed():
'''public Jingle createCandidateUsed(final FullJid recipient, final FullJid initiator, final String sessionId, final JingleContent.Senders contentSenders, final JingleContent.Creator contentCreator, final String contentName, final String streamId, final String candidateId)
'''
pass
def createCandidateError():
'''public Jingle createCandidateError(final FullJid remote, final FullJid initiator, final String sessionId, final JingleContent.Senders senders, final JingleContent.Creator creator, final String name, final String streamId)
'''
pass
def createProxyError():
'''public Jingle createProxyError(final FullJid remote, final FullJid initiator, final String sessionId, final JingleContent.Senders senders, final JingleContent.Creator creator, final String name, final String streamId)
'''
pass
def createCandidateActivated():
'''public Jingle createCandidateActivated(final FullJid remote, final FullJid initiator, final String sessionId, final JingleContent.Senders senders, final JingleContent.Creator creator, final String name, final String streamId, final String candidateId)
'''
pass
def setUseLocalCandidates():
'''public static void setUseLocalCandidates(final boolean localCandidates)
'''
pass
def setUseExternalCandidates():
'''public static void setUseExternalCandidates(final boolean externalCandidates)
'''
pass
def isUseLocalCandidates():
'''public static boolean isUseLocalCandidates()
'''
pass
def isUseExternalCandidates():
'''public static boolean isUseExternalCandidates()
'''
pass
