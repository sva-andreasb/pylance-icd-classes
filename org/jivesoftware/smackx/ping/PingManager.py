def getInstanceFor():
'''public static synchronized PingManager getInstanceFor(final XMPPConnection connection)
'''
pass
def setDefaultPingInterval():
'''public static void setDefaultPingInterval(final int interval)
'''
pass
def run():
'''public void run()
'''
pass
def handleIQRequest():
'''public IQ handleIQRequest(final IQ iqRequest)
'''
pass
def authenticated():
'''public void authenticated(final XMPPConnection connection, final boolean resumed)
'''
pass
def connectionTerminated():
'''public void connectionTerminated()
'''
pass
def pingAsync():
'''public SmackFuture<Boolean, Exception> pingAsync(final Jid jid)
public SmackFuture<Boolean, Exception> pingAsync(final Jid jid, final long pongTimeout)
'''
pass
def handleStanza():
'''public void handleStanza(final Stanza packet)
'''
pass
def isNonFatalException():
'''public boolean isNonFatalException(final Exception exception)
'''
pass
def onSuccess():
'''public void onSuccess(final IQ result)
'''
pass
def processException():
'''public void processException(final Exception exception)
'''
pass
def ping():
'''public boolean ping(final Jid jid, final long pingTimeout)
public boolean ping(final Jid jid)
'''
pass
def isPingSupported():
'''public boolean isPingSupported(final Jid jid)
'''
pass
def pingMyServer():
'''public boolean pingMyServer()
public boolean pingMyServer(final boolean notifyListeners)
public boolean pingMyServer(final boolean notifyListeners, final long pingTimeout)
'''
pass
def setPingInterval():
'''public void setPingInterval(final int pingInterval)
'''
pass
def getPingInterval():
'''public int getPingInterval()
'''
pass
def registerPingFailedListener():
'''public void registerPingFailedListener(final PingFailedListener listener)
'''
pass
def unregisterPingFailedListener():
'''public void unregisterPingFailedListener(final PingFailedListener listener)
'''
pass
def pingServerIfNecessary():
'''public synchronized void pingServerIfNecessary()
'''
pass
def connectionCreated():
'''public void connectionCreated(final XMPPConnection connection)
'''
pass
