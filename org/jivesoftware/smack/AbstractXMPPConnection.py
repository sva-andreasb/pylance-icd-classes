def execute():
    '''returns None\n\n
    execute(final Runnable runnable)\n
    '''
def getConfiguration():
    '''returns ConnectionConfiguration\n\n
    getConfiguration()\n
    '''
def getXMPPServiceDomain():
    '''returns DomainBareJid\n\n
    getXMPPServiceDomain()\n
    '''
def getHost():
    '''returns String\n\n
    getHost()\n
    '''
def getPort():
    '''returns int\n\n
    getPort()\n
    '''
def getStreamId():
    '''returns String\n\n
    getStreamId()\n
    '''
def sendStanza():
    '''returns None\n\n
    sendStanza(final Stanza stanza)\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect()\n
    '''
def addConnectionListener():
    '''returns None\n\n
    addConnectionListener(final ConnectionListener connectionListener)\n
    '''
def removeConnectionListener():
    '''returns None\n\n
    removeConnectionListener(final ConnectionListener connectionListener)\n
    '''
def createStanzaCollectorAndSend():
    '''returns StanzaCollector\n\n
    createStanzaCollectorAndSend(final IQ packet)\n
    createStanzaCollectorAndSend(final StanzaFilter packetFilter, final Stanza packet)\n
    '''
def createStanzaCollector():
    '''returns StanzaCollector\n\n
    createStanzaCollector(final StanzaFilter packetFilter)\n
    createStanzaCollector(final StanzaCollector.Configuration configuration)\n
    '''
def removeStanzaCollector():
    '''returns None\n\n
    removeStanzaCollector(final StanzaCollector collector)\n
    '''
def addSyncStanzaListener():
    '''returns None\n\n
    addSyncStanzaListener(final StanzaListener packetListener, final StanzaFilter packetFilter)\n
    '''
def removeSyncStanzaListener():
    '''returns boolean\n\n
    removeSyncStanzaListener(final StanzaListener packetListener)\n
    '''
def addAsyncStanzaListener():
    '''returns None\n\n
    addAsyncStanzaListener(final StanzaListener packetListener, final StanzaFilter packetFilter)\n
    '''
def removeAsyncStanzaListener():
    '''returns boolean\n\n
    removeAsyncStanzaListener(final StanzaListener packetListener)\n
    '''
def addPacketSendingListener():
    '''returns None\n\n
    addPacketSendingListener(final StanzaListener packetListener, final StanzaFilter packetFilter)\n
    '''
def addStanzaSendingListener():
    '''returns None\n\n
    addStanzaSendingListener(final StanzaListener packetListener, final StanzaFilter packetFilter)\n
    '''
def removePacketSendingListener():
    '''returns None\n\n
    removePacketSendingListener(final StanzaListener packetListener)\n
    '''
def removeStanzaSendingListener():
    '''returns None\n\n
    removeStanzaSendingListener(final StanzaListener packetListener)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def addPacketInterceptor():
    '''returns None\n\n
    addPacketInterceptor(final StanzaListener packetInterceptor, final StanzaFilter packetFilter)\n
    '''
def addStanzaInterceptor():
    '''returns None\n\n
    addStanzaInterceptor(final StanzaListener packetInterceptor, final StanzaFilter packetFilter)\n
    '''
def removePacketInterceptor():
    '''returns None\n\n
    removePacketInterceptor(final StanzaListener packetInterceptor)\n
    '''
def removeStanzaInterceptor():
    '''returns None\n\n
    removeStanzaInterceptor(final StanzaListener packetInterceptor)\n
    '''
def getReplyTimeout():
    '''returns long\n\n
    getReplyTimeout()\n
    '''
def setReplyTimeout():
    '''returns None\n\n
    setReplyTimeout(final long timeout)\n
    '''
def setUnknownIqRequestReplyMode():
    '''returns None\n\n
    setUnknownIqRequestReplyMode(final SmackConfiguration.UnknownIqRequestReplyMode unknownIqRequestReplyMode)\n
    '''
def getConnectionCounter():
    '''returns int\n\n
    getConnectionCounter()\n
    '''
def setFromMode():
    '''returns None\n\n
    setFromMode(final FromMode fromMode)\n
    '''
def getFromMode():
    '''returns FromMode\n\n
    getFromMode()\n
    '''
def hasFeature():
    '''returns boolean\n\n
    hasFeature(final String element, final String namespace)\n
    '''
def sendStanzaWithResponseCallback():
    '''returns None\n\n
    sendStanzaWithResponseCallback(final Stanza stanza, final StanzaFilter replyFilter, final StanzaListener callback)\n
    sendStanzaWithResponseCallback(final Stanza stanza, final StanzaFilter replyFilter, final StanzaListener callback, final ExceptionCallback exceptionCallback)\n
    sendStanzaWithResponseCallback(final Stanza stanza, final StanzaFilter replyFilter, final StanzaListener callback, final ExceptionCallback exceptionCallback, final long timeout)\n
    '''
def processStanza():
    '''returns None\n\n
    processStanza(final Stanza stanza)\n
    processStanza(final Stanza packet)\n
    processStanza(final Stanza packet)\n
    '''
def sendIqWithResponseCallback():
    '''returns None\n\n
    sendIqWithResponseCallback(final IQ iqRequest, final StanzaListener callback)\n
    sendIqWithResponseCallback(final IQ iqRequest, final StanzaListener callback, final ExceptionCallback exceptionCallback)\n
    sendIqWithResponseCallback(final IQ iqRequest, final StanzaListener callback, final ExceptionCallback exceptionCallback, final long timeout)\n
    '''
def addOneTimeSyncCallback():
    '''returns None\n\n
    addOneTimeSyncCallback(final StanzaListener callback, final StanzaFilter packetFilter)\n
    '''
def registerIQRequestHandler():
    '''returns IQRequestHandler\n\n
    registerIQRequestHandler(final IQRequestHandler iqRequestHandler)\n
    '''
def unregisterIQRequestHandler():
    '''returns IQRequestHandler\n\n
    unregisterIQRequestHandler(final String element, final String namespace, final IQ.Type type)\n
    '''
def getLastStanzaReceived():
    '''returns long\n\n
    getLastStanzaReceived()\n
    '''
def setParsingExceptionCallback():
    '''returns None\n\n
    setParsingExceptionCallback(final ParsingExceptionCallback callback)\n
    '''
def getParsingExceptionCallback():
    '''returns ParsingExceptionCallback\n\n
    getParsingExceptionCallback()\n
    '''
def setMaxAsyncOperations():
    '''returns None\n\n
    setMaxAsyncOperations(final int maxAsyncOperations)\n
    '''
def newThread():
    '''returns Thread\n\n
    newThread(final Runnable runnable)\n
    newThread(final Runnable runnable)\n
    '''
def uncaughtException():
    '''returns None\n\n
    uncaughtException(final Thread t, final Throwable e)\n
    '''
def ():
    '''returns InterceptorWrapper\n\n
    (final StanzaListener packetListener, final StanzaFilter packetFilter)\n
    (final StanzaListener packetInterceptor, final StanzaFilter packetFilter)\n
    '''
def filterMatches():
    '''returns boolean\n\n
    filterMatches(final Stanza packet)\n
    filterMatches(final Stanza packet)\n
    '''
def getListener():
    '''returns StanzaListener\n\n
    getListener()\n
    '''
def getInterceptor():
    '''returns StanzaListener\n\n
    getInterceptor()\n
    '''
