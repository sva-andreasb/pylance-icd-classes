def JingleS5BTransportSession():
    '''public JingleS5BTransportSession(final JingleSession jingleSession)
    '''
def createTransport():
    '''public JingleS5BTransport createTransport()
    public JingleS5BTransport createTransport(final String sid, final Bytestream.Mode mode)
    '''
def setTheirProposal():
    '''public void setTheirProposal(final JingleContentTransport transport)
    '''
def setTheirTransport():
    '''public void setTheirTransport(final JingleContentTransport transport)
    '''
def initiateOutgoingSession():
    '''public void initiateOutgoingSession(final JingleTransportInitiationCallback callback)
    '''
def initiateIncomingSession():
    '''public void initiateIncomingSession(final JingleTransportInitiationCallback callback)
    '''
def getNamespace():
    '''public String getNamespace()
    '''
def handleTransportInfo():
    '''public IQ handleTransportInfo(final Jingle transportInfo)
    '''
def handleCandidateUsed():
    '''public IQ handleCandidateUsed(final Jingle jingle)
    '''
def handleCandidateActivate():
    '''public IQ handleCandidateActivate(final Jingle jingle)
    '''
def handleCandidateError():
    '''public IQ handleCandidateError(final Jingle jingle)
    '''
def handleProxyError():
    '''public IQ handleProxyError(final Jingle jingle)
    '''
def transportManager():
    '''public JingleS5BTransportManager transportManager()
    '''
