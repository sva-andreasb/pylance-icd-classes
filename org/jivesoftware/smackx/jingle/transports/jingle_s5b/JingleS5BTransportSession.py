def ():
    '''returns JingleS5BTransportSession\n\n
    (final JingleSession jingleSession)\n
    '''
def createTransport():
    '''returns JingleS5BTransport\n\n
    createTransport()\n
    createTransport(final String sid, final Bytestream.Mode mode)\n
    '''
def setTheirProposal():
    '''returns None\n\n
    setTheirProposal(final JingleContentTransport transport)\n
    '''
def setTheirTransport():
    '''returns None\n\n
    setTheirTransport(final JingleContentTransport transport)\n
    '''
def initiateOutgoingSession():
    '''returns None\n\n
    initiateOutgoingSession(final JingleTransportInitiationCallback callback)\n
    '''
def initiateIncomingSession():
    '''returns None\n\n
    initiateIncomingSession(final JingleTransportInitiationCallback callback)\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def handleTransportInfo():
    '''returns IQ\n\n
    handleTransportInfo(final Jingle transportInfo)\n
    '''
def handleCandidateUsed():
    '''returns IQ\n\n
    handleCandidateUsed(final Jingle jingle)\n
    '''
def handleCandidateActivate():
    '''returns IQ\n\n
    handleCandidateActivate(final Jingle jingle)\n
    '''
def handleCandidateError():
    '''returns IQ\n\n
    handleCandidateError(final Jingle jingle)\n
    '''
def handleProxyError():
    '''returns IQ\n\n
    handleProxyError(final Jingle jingle)\n
    '''
def transportManager():
    '''returns JingleS5BTransportManager\n\n
    transportManager()\n
    '''
