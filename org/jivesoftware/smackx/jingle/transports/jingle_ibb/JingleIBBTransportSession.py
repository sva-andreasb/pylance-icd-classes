def ():
    '''returns JingleIBBTransportSession\n\n
    (final JingleSession session)\n
    '''
def createTransport():
    '''returns JingleIBBTransport\n\n
    createTransport()\n
    '''
def setTheirProposal():
    '''returns None\n\n
    setTheirProposal(final JingleContentTransport transport)\n
    '''
def initiateOutgoingSession():
    '''returns None\n\n
    initiateOutgoingSession(final JingleTransportInitiationCallback callback)\n
    '''
def initiateIncomingSession():
    '''returns None\n\n
    initiateIncomingSession(final JingleTransportInitiationCallback callback)\n
    '''
def incomingBytestreamRequest():
    '''returns None\n\n
    incomingBytestreamRequest(final BytestreamRequest request)\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def handleTransportInfo():
    '''returns IQ\n\n
    handleTransportInfo(final Jingle transportInfo)\n
    '''
def transportManager():
    '''returns JingleTransportManager<JingleIBBTransport>\n\n
    transportManager()\n
    '''
