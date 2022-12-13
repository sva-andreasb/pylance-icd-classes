def execute():
'''public void execute(final Runnable runnable)
'''
pass
def getConfiguration():
'''public ConnectionConfiguration getConfiguration()
'''
pass
def getXMPPServiceDomain():
'''public DomainBareJid getXMPPServiceDomain()
'''
pass
def getHost():
'''public String getHost()
'''
pass
def getPort():
'''public int getPort()
'''
pass
def connect():
'''public synchronized AbstractXMPPConnection connect()
'''
pass
def login():
'''public synchronized void login()
public synchronized void login(final CharSequence username, final String password)
public synchronized void login(final CharSequence username, final String password, final Resourcepart resource)
'''
pass
def isConnected():
'''public final boolean isConnected()
'''
pass
def isAuthenticated():
'''public final boolean isAuthenticated()
'''
pass
def getUser():
'''public final EntityFullJid getUser()
'''
pass
def getStreamId():
'''public String getStreamId()
'''
pass
def isAnonymous():
'''public final boolean isAnonymous()
'''
pass
def getUsedSaslMechansism():
'''public final String getUsedSaslMechansism()
'''
pass
def sendStanza():
'''public void sendStanza(final Stanza stanza)
'''
pass
def disconnect():
'''public void disconnect()
public synchronized void disconnect(final Presence unavailablePresence)
'''
pass
def addConnectionListener():
'''public void addConnectionListener(final ConnectionListener connectionListener)
'''
pass
def removeConnectionListener():
'''public void removeConnectionListener(final ConnectionListener connectionListener)
'''
pass
def sendIqRequestAndWaitForResponse():
'''public <I extends IQ> I sendIqRequestAndWaitForResponse(final IQ request)
'''
pass
def createStanzaCollectorAndSend():
'''public StanzaCollector createStanzaCollectorAndSend(final IQ packet)
public StanzaCollector createStanzaCollectorAndSend(final StanzaFilter packetFilter, final Stanza packet)
'''
pass
def createStanzaCollector():
'''public StanzaCollector createStanzaCollector(final StanzaFilter packetFilter)
public StanzaCollector createStanzaCollector(final StanzaCollector.Configuration configuration)
'''
pass
def removeStanzaCollector():
'''public void removeStanzaCollector(final StanzaCollector collector)
'''
pass
def addSyncStanzaListener():
'''public void addSyncStanzaListener(final StanzaListener packetListener, final StanzaFilter packetFilter)
'''
pass
def removeSyncStanzaListener():
'''public boolean removeSyncStanzaListener(final StanzaListener packetListener)
'''
pass
def addAsyncStanzaListener():
'''public void addAsyncStanzaListener(final StanzaListener packetListener, final StanzaFilter packetFilter)
'''
pass
def removeAsyncStanzaListener():
'''public boolean removeAsyncStanzaListener(final StanzaListener packetListener)
'''
pass
def addPacketSendingListener():
'''public void addPacketSendingListener(final StanzaListener packetListener, final StanzaFilter packetFilter)
'''
pass
def addStanzaSendingListener():
'''public void addStanzaSendingListener(final StanzaListener packetListener, final StanzaFilter packetFilter)
'''
pass
def removePacketSendingListener():
'''public void removePacketSendingListener(final StanzaListener packetListener)
'''
pass
def removeStanzaSendingListener():
'''public void removeStanzaSendingListener(final StanzaListener packetListener)
'''
pass
def run():
'''public void run()
public void run()
public void run()
public void run()
public void run()
public void run()
public void run()
public void run()
public void run()
'''
pass
def addPacketInterceptor():
'''public void addPacketInterceptor(final StanzaListener packetInterceptor, final StanzaFilter packetFilter)
'''
pass
def addStanzaInterceptor():
'''public void addStanzaInterceptor(final StanzaListener packetInterceptor, final StanzaFilter packetFilter)
'''
pass
def removePacketInterceptor():
'''public void removePacketInterceptor(final StanzaListener packetInterceptor)
'''
pass
def removeStanzaInterceptor():
'''public void removeStanzaInterceptor(final StanzaListener packetInterceptor)
'''
pass
def getReplyTimeout():
'''public long getReplyTimeout()
'''
pass
def setReplyTimeout():
'''public void setReplyTimeout(final long timeout)
'''
pass
def setUnknownIqRequestReplyMode():
'''public void setUnknownIqRequestReplyMode(final SmackConfiguration.UnknownIqRequestReplyMode unknownIqRequestReplyMode)
'''
pass
def getConnectionCounter():
'''public int getConnectionCounter()
'''
pass
def setFromMode():
'''public void setFromMode(final FromMode fromMode)
'''
pass
def getFromMode():
'''public FromMode getFromMode()
'''
pass
def getFeature():
'''public <F extends ExtensionElement> F getFeature(final String element, final String namespace)
'''
pass
def hasFeature():
'''public boolean hasFeature(final String element, final String namespace)
'''
pass
def sendStanzaWithResponseCallback():
'''public void sendStanzaWithResponseCallback(final Stanza stanza, final StanzaFilter replyFilter, final StanzaListener callback)
public void sendStanzaWithResponseCallback(final Stanza stanza, final StanzaFilter replyFilter, final StanzaListener callback, final ExceptionCallback exceptionCallback)
public void sendStanzaWithResponseCallback(final Stanza stanza, final StanzaFilter replyFilter, final StanzaListener callback, final ExceptionCallback exceptionCallback, final long timeout)
'''
pass
def sendIqRequestAsync():
'''public SmackFuture<IQ, Exception> sendIqRequestAsync(final IQ request)
public SmackFuture<IQ, Exception> sendIqRequestAsync(final IQ request, final long timeout)
'''
pass
def sendAsync():
'''public <S extends Stanza> SmackFuture<S, Exception> sendAsync(final S stanza, final StanzaFilter replyFilter)
public <S extends Stanza> SmackFuture<S, Exception> sendAsync(final S stanza, final StanzaFilter replyFilter, final long timeout)
'''
pass
def processStanza():
'''public void processStanza(final Stanza stanza)
public void processStanza(final Stanza packet)
public void processStanza(final Stanza packet)
'''
pass
def sendIqWithResponseCallback():
'''public void sendIqWithResponseCallback(final IQ iqRequest, final StanzaListener callback)
public void sendIqWithResponseCallback(final IQ iqRequest, final StanzaListener callback, final ExceptionCallback exceptionCallback)
public void sendIqWithResponseCallback(final IQ iqRequest, final StanzaListener callback, final ExceptionCallback exceptionCallback, final long timeout)
'''
pass
def addOneTimeSyncCallback():
'''public void addOneTimeSyncCallback(final StanzaListener callback, final StanzaFilter packetFilter)
'''
pass
def registerIQRequestHandler():
'''public IQRequestHandler registerIQRequestHandler(final IQRequestHandler iqRequestHandler)
'''
pass
def unregisterIQRequestHandler():
'''public final IQRequestHandler unregisterIQRequestHandler(final IQRequestHandler iqRequestHandler)
public IQRequestHandler unregisterIQRequestHandler(final String element, final String namespace, final IQ.Type type)
'''
pass
def getLastStanzaReceived():
'''public long getLastStanzaReceived()
'''
pass
def getAuthenticatedConnectionInitiallyEstablishedTimestamp():
'''public final long getAuthenticatedConnectionInitiallyEstablishedTimestamp()
'''
pass
def setParsingExceptionCallback():
'''public void setParsingExceptionCallback(final ParsingExceptionCallback callback)
'''
pass
def getParsingExceptionCallback():
'''public ParsingExceptionCallback getParsingExceptionCallback()
'''
pass
def toString():
'''public final String toString()
'''
pass
def setMaxAsyncOperations():
'''public void setMaxAsyncOperations(final int maxAsyncOperations)
'''
pass
def newThread():
'''public Thread newThread(final Runnable runnable)
public Thread newThread(final Runnable runnable)
'''
pass
def uncaughtException():
'''public void uncaughtException(final Thread t, final Throwable e)
'''
pass
def ListenerWrapper():
'''public ListenerWrapper(final StanzaListener packetListener, final StanzaFilter packetFilter)
'''
pass
def filterMatches():
'''public boolean filterMatches(final Stanza packet)
public boolean filterMatches(final Stanza packet)
'''
pass
def getListener():
'''public StanzaListener getListener()
'''
pass
def InterceptorWrapper():
'''public InterceptorWrapper(final StanzaListener packetInterceptor, final StanzaFilter packetFilter)
'''
pass
def getInterceptor():
'''public StanzaListener getInterceptor()
'''
pass
