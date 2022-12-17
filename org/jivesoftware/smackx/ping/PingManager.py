def run():
    '''returns None\n\n
    run()\n
    '''
def handleIQRequest():
    '''returns IQ\n\n
    handleIQRequest(final IQ iqRequest)\n
    '''
def authenticated():
    '''returns None\n\n
    authenticated(final XMPPConnection connection, final boolean resumed)\n
    '''
def connectionTerminated():
    '''returns None\n\n
    connectionTerminated()\n
    '''
def handleStanza():
    '''returns None\n\n
    handleStanza(final Stanza packet)\n
    '''
def isNonFatalException():
    '''returns boolean\n\n
    isNonFatalException(final Exception exception)\n
    '''
def onSuccess():
    '''returns None\n\n
    onSuccess(final IQ result)\n
    '''
def processException():
    '''returns None\n\n
    processException(final Exception exception)\n
    '''
def ping():
    '''returns boolean\n\n
    ping(final Jid jid, final long pingTimeout)\n
    ping(final Jid jid)\n
    '''
def isPingSupported():
    '''returns boolean\n\n
    isPingSupported(final Jid jid)\n
    '''
def pingMyServer():
    '''returns boolean\n\n
    pingMyServer()\n
    pingMyServer(final boolean notifyListeners)\n
    pingMyServer(final boolean notifyListeners, final long pingTimeout)\n
    '''
def setPingInterval():
    '''returns None\n\n
    setPingInterval(final int pingInterval)\n
    '''
def getPingInterval():
    '''returns int\n\n
    getPingInterval()\n
    '''
def registerPingFailedListener():
    '''returns None\n\n
    registerPingFailedListener(final PingFailedListener listener)\n
    '''
def unregisterPingFailedListener():
    '''returns None\n\n
    unregisterPingFailedListener(final PingFailedListener listener)\n
    '''
def connectionCreated():
    '''returns None\n\n
    connectionCreated(final XMPPConnection connection)\n
    '''
