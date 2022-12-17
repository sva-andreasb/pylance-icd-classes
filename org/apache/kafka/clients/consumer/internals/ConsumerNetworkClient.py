def ():
    '''returns ConsumerNetworkClient\n\n
    (final LogContext logContext, final KafkaClient client, final Metadata metadata, final Time time, final long retryBackoffMs, final long requestTimeoutMs, final int maxPollTimeoutMs)\n
    '''
def send():
    '''returns RequestFuture<ClientResponse>\n\n
    send(final Node node, final AbstractRequest.Builder<?> requestBuilder)\n
    '''
def leastLoadedNode():
    '''returns Node\n\n
    leastLoadedNode()\n
    '''
def hasReadyNodes():
    '''returns boolean\n\n
    hasReadyNodes()\n
    '''
def awaitMetadataUpdate():
    '''returns boolean\n\n
    awaitMetadataUpdate()\n
    awaitMetadataUpdate(final long timeout)\n
    '''
def ensureFreshMetadata():
    '''returns None\n\n
    ensureFreshMetadata()\n
    '''
def wakeup():
    '''returns None\n\n
    wakeup()\n
    '''
def poll():
    '''returns None\n\n
    poll(final RequestFuture<?> future)\n
    poll(final RequestFuture<?> future, final long timeout)\n
    poll(final long timeout)\n
    poll(final long timeout, final long now, final PollCondition pollCondition)\n
    poll(long timeout, long now, final PollCondition pollCondition, final boolean disableWakeup)\n
    '''
def pollNoWakeup():
    '''returns None\n\n
    pollNoWakeup()\n
    '''
def awaitPendingRequests():
    '''returns boolean\n\n
    awaitPendingRequests(final Node node, final long timeoutMs)\n
    '''
def pendingRequestCount():
    '''returns int\n\n
    pendingRequestCount(final Node node)\n
    pendingRequestCount()\n
    '''
def hasPendingRequests():
    '''returns boolean\n\n
    hasPendingRequests(final Node node)\n
    hasPendingRequests()\n
    '''
def disconnectAsync():
    '''returns None\n\n
    disconnectAsync(final Node node)\n
    '''
def maybeTriggerWakeup():
    '''returns None\n\n
    maybeTriggerWakeup()\n
    '''
def disableWakeups():
    '''returns None\n\n
    disableWakeups()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def connectionFailed():
    '''returns boolean\n\n
    connectionFailed(final Node node)\n
    '''
def tryConnect():
    '''returns None\n\n
    tryConnect(final Node node)\n
    '''
def fireCompletion():
    '''returns None\n\n
    fireCompletion()\n
    '''
def onFailure():
    '''returns None\n\n
    onFailure(final RuntimeException e)\n
    '''
def onComplete():
    '''returns None\n\n
    onComplete(final ClientResponse response)\n
    '''
def put():
    '''returns None\n\n
    put(final Node node, final ClientRequest request)\n
    '''
def requestCount():
    '''returns int\n\n
    requestCount(final Node node)\n
    requestCount()\n
    '''
def hasRequests():
    '''returns boolean\n\n
    hasRequests(final Node node)\n
    hasRequests()\n
    '''
def removeExpiredRequests():
    '''returns Collection<ClientRequest>\n\n
    removeExpiredRequests(final long now, final long unsentExpiryMs)\n
    '''
def clean():
    '''returns None\n\n
    clean()\n
    '''
def remove():
    '''returns Collection<ClientRequest>\n\n
    remove(final Node node)\n
    '''
def requestIterator():
    '''returns Iterator<ClientRequest>\n\n
    requestIterator(final Node node)\n
    '''
def nodes():
    '''returns Collection<Node>\n\n
    nodes()\n
    '''
