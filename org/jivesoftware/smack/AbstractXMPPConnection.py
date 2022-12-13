def execute():
    '''public void execute(final Runnable runnable)
    '''
def getConfiguration():
    '''public ConnectionConfiguration getConfiguration()
    '''
def getXMPPServiceDomain():
    '''public DomainBareJid getXMPPServiceDomain()
    '''
def getHost():
    '''public String getHost()
    '''
def getPort():
    '''public int getPort()
    '''
def connect():
    '''public synchronized AbstractXMPPConnection connect()
    '''
def login():
    '''public synchronized void login()
    public synchronized void login(final CharSequence username, final String password)
    public synchronized void login(final CharSequence username, final String password, final Resourcepart resource)
    '''
def isConnected():
    '''public final boolean isConnected()
    '''
def isAuthenticated():
    '''public final boolean isAuthenticated()
    '''
def getUser():
    '''public final EntityFullJid getUser()
    '''
def getStreamId():
    '''public String getStreamId()
    '''
def isAnonymous():
    '''public final boolean isAnonymous()
    '''
def getUsedSaslMechansism():
    '''public final String getUsedSaslMechansism()
    '''
def sendStanza():
    '''public void sendStanza(final Stanza stanza)
    '''
def disconnect():
    '''public void disconnect()
    public synchronized void disconnect(final Presence unavailablePresence)
    '''
def addConnectionListener():
    '''public void addConnectionListener(final ConnectionListener connectionListener)
    '''
def removeConnectionListener():
    '''public void removeConnectionListener(final ConnectionListener connectionListener)
    '''
def sendIqRequestAndWaitForResponse():
    '''public <I extends IQ> I sendIqRequestAndWaitForResponse(final IQ request)
    '''
def createStanzaCollectorAndSend():
    '''public StanzaCollector createStanzaCollectorAndSend(final IQ packet)
    public StanzaCollector createStanzaCollectorAndSend(final StanzaFilter packetFilter, final Stanza packet)
    '''
def createStanzaCollector():
    '''public StanzaCollector createStanzaCollector(final StanzaFilter packetFilter)
    public StanzaCollector createStanzaCollector(final StanzaCollector.Configuration configuration)
    '''
def removeStanzaCollector():
    '''public void removeStanzaCollector(final StanzaCollector collector)
    '''
def addSyncStanzaListener():
    '''public void addSyncStanzaListener(final StanzaListener packetListener, final StanzaFilter packetFilter)
    '''
def removeSyncStanzaListener():
    '''public boolean removeSyncStanzaListener(final StanzaListener packetListener)
    '''
def addAsyncStanzaListener():
    '''public void addAsyncStanzaListener(final StanzaListener packetListener, final StanzaFilter packetFilter)
    '''
def removeAsyncStanzaListener():
    '''public boolean removeAsyncStanzaListener(final StanzaListener packetListener)
    '''
def addPacketSendingListener():
    '''public void addPacketSendingListener(final StanzaListener packetListener, final StanzaFilter packetFilter)
    '''
def addStanzaSendingListener():
    '''public void addStanzaSendingListener(final StanzaListener packetListener, final StanzaFilter packetFilter)
    '''
def removePacketSendingListener():
    '''public void removePacketSendingListener(final StanzaListener packetListener)
    '''
def removeStanzaSendingListener():
    '''public void removeStanzaSendingListener(final StanzaListener packetListener)
    '''
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
def addPacketInterceptor():
    '''public void addPacketInterceptor(final StanzaListener packetInterceptor, final StanzaFilter packetFilter)
    '''
def addStanzaInterceptor():
    '''public void addStanzaInterceptor(final StanzaListener packetInterceptor, final StanzaFilter packetFilter)
    '''
def removePacketInterceptor():
    '''public void removePacketInterceptor(final StanzaListener packetInterceptor)
    '''
def removeStanzaInterceptor():
    '''public void removeStanzaInterceptor(final StanzaListener packetInterceptor)
    '''
def getReplyTimeout():
    '''public long getReplyTimeout()
    '''
def setReplyTimeout():
    '''public void setReplyTimeout(final long timeout)
    '''
def setUnknownIqRequestReplyMode():
    '''public void setUnknownIqRequestReplyMode(final SmackConfiguration.UnknownIqRequestReplyMode unknownIqRequestReplyMode)
    '''
def getConnectionCounter():
    '''public int getConnectionCounter()
    '''
def setFromMode():
    '''public void setFromMode(final FromMode fromMode)
    '''
def getFromMode():
    '''public FromMode getFromMode()
    '''
def getFeature():
    '''public <F extends ExtensionElement> F getFeature(final String element, final String namespace)
    '''
def hasFeature():
    '''public boolean hasFeature(final String element, final String namespace)
    '''
def sendStanzaWithResponseCallback():
    '''public void sendStanzaWithResponseCallback(final Stanza stanza, final StanzaFilter replyFilter, final StanzaListener callback)
    public void sendStanzaWithResponseCallback(final Stanza stanza, final StanzaFilter replyFilter, final StanzaListener callback, final ExceptionCallback exceptionCallback)
    public void sendStanzaWithResponseCallback(final Stanza stanza, final StanzaFilter replyFilter, final StanzaListener callback, final ExceptionCallback exceptionCallback, final long timeout)
    '''
def sendIqRequestAsync():
    '''public SmackFuture<IQ, Exception> sendIqRequestAsync(final IQ request)
    public SmackFuture<IQ, Exception> sendIqRequestAsync(final IQ request, final long timeout)
    '''
def sendAsync():
    '''public <S extends Stanza> SmackFuture<S, Exception> sendAsync(final S stanza, final StanzaFilter replyFilter)
    public <S extends Stanza> SmackFuture<S, Exception> sendAsync(final S stanza, final StanzaFilter replyFilter, final long timeout)
    '''
def processStanza():
    '''public void processStanza(final Stanza stanza)
    public void processStanza(final Stanza packet)
    public void processStanza(final Stanza packet)
    '''
def sendIqWithResponseCallback():
    '''public void sendIqWithResponseCallback(final IQ iqRequest, final StanzaListener callback)
    public void sendIqWithResponseCallback(final IQ iqRequest, final StanzaListener callback, final ExceptionCallback exceptionCallback)
    public void sendIqWithResponseCallback(final IQ iqRequest, final StanzaListener callback, final ExceptionCallback exceptionCallback, final long timeout)
    '''
def addOneTimeSyncCallback():
    '''public void addOneTimeSyncCallback(final StanzaListener callback, final StanzaFilter packetFilter)
    '''
def registerIQRequestHandler():
    '''public IQRequestHandler registerIQRequestHandler(final IQRequestHandler iqRequestHandler)
    '''
def unregisterIQRequestHandler():
    '''public final IQRequestHandler unregisterIQRequestHandler(final IQRequestHandler iqRequestHandler)
    public IQRequestHandler unregisterIQRequestHandler(final String element, final String namespace, final IQ.Type type)
    '''
def getLastStanzaReceived():
    '''public long getLastStanzaReceived()
    '''
def getAuthenticatedConnectionInitiallyEstablishedTimestamp():
    '''public final long getAuthenticatedConnectionInitiallyEstablishedTimestamp()
    '''
def setParsingExceptionCallback():
    '''public void setParsingExceptionCallback(final ParsingExceptionCallback callback)
    '''
def getParsingExceptionCallback():
    '''public ParsingExceptionCallback getParsingExceptionCallback()
    '''
def toString():
    '''public final String toString()
    '''
def setMaxAsyncOperations():
    '''public void setMaxAsyncOperations(final int maxAsyncOperations)
    '''
def newThread():
    '''public Thread newThread(final Runnable runnable)
    public Thread newThread(final Runnable runnable)
    '''
def uncaughtException():
    '''public void uncaughtException(final Thread t, final Throwable e)
    '''
def ListenerWrapper():
    '''public ListenerWrapper(final StanzaListener packetListener, final StanzaFilter packetFilter)
    '''
def filterMatches():
    '''public boolean filterMatches(final Stanza packet)
    public boolean filterMatches(final Stanza packet)
    '''
def getListener():
    '''public StanzaListener getListener()
    '''
def InterceptorWrapper():
    '''public InterceptorWrapper(final StanzaListener packetInterceptor, final StanzaFilter packetFilter)
    '''
def getInterceptor():
    '''public StanzaListener getInterceptor()
    '''
