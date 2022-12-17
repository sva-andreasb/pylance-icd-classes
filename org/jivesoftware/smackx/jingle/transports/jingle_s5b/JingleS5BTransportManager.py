def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def transportSession():
    '''returns JingleTransportSession<JingleS5BTransport>\n\n
    transportSession(final JingleSession jingleSession)\n
    '''
def authenticated():
    '''returns None\n\n
    authenticated(final XMPPConnection connection, final boolean resumed)\n
    '''
def createCandidateUsed():
    '''returns Jingle\n\n
    createCandidateUsed(final FullJid recipient, final FullJid initiator, final String sessionId, final JingleContent.Senders contentSenders, final JingleContent.Creator contentCreator, final String contentName, final String streamId, final String candidateId)\n
    '''
def createCandidateError():
    '''returns Jingle\n\n
    createCandidateError(final FullJid remote, final FullJid initiator, final String sessionId, final JingleContent.Senders senders, final JingleContent.Creator creator, final String name, final String streamId)\n
    '''
def createProxyError():
    '''returns Jingle\n\n
    createProxyError(final FullJid remote, final FullJid initiator, final String sessionId, final JingleContent.Senders senders, final JingleContent.Creator creator, final String name, final String streamId)\n
    '''
def createCandidateActivated():
    '''returns Jingle\n\n
    createCandidateActivated(final FullJid remote, final FullJid initiator, final String sessionId, final JingleContent.Senders senders, final JingleContent.Creator creator, final String name, final String streamId, final String candidateId)\n
    '''
