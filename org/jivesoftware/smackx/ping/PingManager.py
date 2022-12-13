def getInstanceFor():
    '''    public static synchronized PingManager getInstanceFor(final XMPPConnection connection)
    '''
def setDefaultPingInterval():
    '''    public static void setDefaultPingInterval(final int interval)
    '''
def run():
    '''    public void run()
    '''
def handleIQRequest():
    '''    public IQ handleIQRequest(final IQ iqRequest)
    '''
def authenticated():
    '''    public void authenticated(final XMPPConnection connection, final boolean resumed)
    '''
def connectionTerminated():
    '''    public void connectionTerminated()
    '''
def pingAsync():
    '''    public SmackFuture<Boolean, Exception> pingAsync(final Jid jid)
    public SmackFuture<Boolean, Exception> pingAsync(final Jid jid, final long pongTimeout)
    '''
def handleStanza():
    '''    public void handleStanza(final Stanza packet)
    '''
def isNonFatalException():
    '''    public boolean isNonFatalException(final Exception exception)
    '''
def onSuccess():
    '''    public void onSuccess(final IQ result)
    '''
def processException():
    '''    public void processException(final Exception exception)
    '''
def ping():
    '''    public boolean ping(final Jid jid, final long pingTimeout)
    public boolean ping(final Jid jid)
    '''
def isPingSupported():
    '''    public boolean isPingSupported(final Jid jid)
    '''
def pingMyServer():
    '''    public boolean pingMyServer()
    public boolean pingMyServer(final boolean notifyListeners)
    public boolean pingMyServer(final boolean notifyListeners, final long pingTimeout)
    '''
def setPingInterval():
    '''    public void setPingInterval(final int pingInterval)
    '''
def getPingInterval():
    '''    public int getPingInterval()
    '''
def registerPingFailedListener():
    '''    public void registerPingFailedListener(final PingFailedListener listener)
    '''
def unregisterPingFailedListener():
    '''    public void unregisterPingFailedListener(final PingFailedListener listener)
    '''
def pingServerIfNecessary():
    '''    public synchronized void pingServerIfNecessary()
    '''
def connectionCreated():
    '''    public void connectionCreated(final XMPPConnection connection)
    '''
