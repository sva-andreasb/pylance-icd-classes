def getInstanceFor():
    '''    public static synchronized JingleS5BTransportManager getInstanceFor(final XMPPConnection connection)
    '''
def getNamespace():
    '''    public String getNamespace()
    '''
def transportSession():
    '''    public JingleTransportSession<JingleS5BTransport> transportSession(final JingleSession jingleSession)
    '''
def authenticated():
    '''    public void authenticated(final XMPPConnection connection, final boolean resumed)
    '''
def createCandidateUsed():
    '''    public Jingle createCandidateUsed(final FullJid recipient, final FullJid initiator, final String sessionId, final JingleContent.Senders contentSenders, final JingleContent.Creator contentCreator, final String contentName, final String streamId, final String candidateId)
    '''
def createCandidateError():
    '''    public Jingle createCandidateError(final FullJid remote, final FullJid initiator, final String sessionId, final JingleContent.Senders senders, final JingleContent.Creator creator, final String name, final String streamId)
    '''
def createProxyError():
    '''    public Jingle createProxyError(final FullJid remote, final FullJid initiator, final String sessionId, final JingleContent.Senders senders, final JingleContent.Creator creator, final String name, final String streamId)
    '''
def createCandidateActivated():
    '''    public Jingle createCandidateActivated(final FullJid remote, final FullJid initiator, final String sessionId, final JingleContent.Senders senders, final JingleContent.Creator creator, final String name, final String streamId, final String candidateId)
    '''
def setUseLocalCandidates():
    '''    public static void setUseLocalCandidates(final boolean localCandidates)
    '''
def setUseExternalCandidates():
    '''    public static void setUseExternalCandidates(final boolean externalCandidates)
    '''
def isUseLocalCandidates():
    '''    public static boolean isUseLocalCandidates()
    '''
def isUseExternalCandidates():
    '''    public static boolean isUseExternalCandidates()
    '''
