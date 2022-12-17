def ():
    '''returns InFlightRequest\n\n
    (final Selectable selector, final Metadata metadata, final String clientId, final int maxInFlightRequestsPerConnection, final long reconnectBackoffMs, final long reconnectBackoffMax, final int socketSendBuffer, final int socketReceiveBuffer, final int requestTimeoutMs, final Time time, final boolean discoverBrokerVersions, final ApiVersions apiVersions, final LogContext logContext)\n
    (final Selectable selector, final Metadata metadata, final String clientId, final int maxInFlightRequestsPerConnection, final long reconnectBackoffMs, final long reconnectBackoffMax, final int socketSendBuffer, final int socketReceiveBuffer, final int requestTimeoutMs, final Time time, final boolean discoverBrokerVersions, final ApiVersions apiVersions, final Sensor throttleTimeSensor, final LogContext logContext)\n
    (final Selectable selector, final MetadataUpdater metadataUpdater, final String clientId, final int maxInFlightRequestsPerConnection, final long reconnectBackoffMs, final long reconnectBackoffMax, final int socketSendBuffer, final int socketReceiveBuffer, final int requestTimeoutMs, final Time time, final boolean discoverBrokerVersions, final ApiVersions apiVersions, final LogContext logContext)\n
    (final RequestHeader header, final long createdTimeMs, final String destination, final RequestCompletionHandler callback, final boolean expectResponse, final boolean isInternalRequest, final AbstractRequest request, final Send send, final long sendTimeMs)\n
    '''
def ready():
    '''returns boolean\n\n
    ready(final Node node, final long now)\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect(final String nodeId)\n
    '''
def close():
    '''returns None\n\n
    close(final String nodeId)\n
    close()\n
    '''
def connectionDelay():
    '''returns long\n\n
    connectionDelay(final Node node, final long now)\n
    '''
def connectionFailed():
    '''returns boolean\n\n
    connectionFailed(final Node node)\n
    '''
def authenticationException():
    '''returns AuthenticationException\n\n
    authenticationException(final Node node)\n
    '''
def isReady():
    '''returns boolean\n\n
    isReady(final Node node, final long now)\n
    '''
def send():
    '''returns None\n\n
    send(final ClientRequest request, final long now)\n
    '''
def poll():
    '''returns List<ClientResponse>\n\n
    poll(final long timeout, final long now)\n
    '''
def inFlightRequestCount():
    '''returns int\n\n
    inFlightRequestCount()\n
    inFlightRequestCount(final String node)\n
    '''
def hasInFlightRequests():
    '''returns boolean\n\n
    hasInFlightRequests()\n
    hasInFlightRequests(final String node)\n
    '''
def hasReadyNodes():
    '''returns boolean\n\n
    hasReadyNodes()\n
    '''
def wakeup():
    '''returns None\n\n
    wakeup()\n
    '''
def leastLoadedNode():
    '''returns Node\n\n
    leastLoadedNode(final long now)\n
    '''
def newClientRequest():
    '''returns ClientRequest\n\n
    newClientRequest(final String nodeId, final AbstractRequest.Builder<?> requestBuilder, final long createdTimeMs, final boolean expectResponse)\n
    newClientRequest(final String nodeId, final AbstractRequest.Builder<?> requestBuilder, final long createdTimeMs, final boolean expectResponse, final RequestCompletionHandler callback)\n
    '''
def discoverBrokerVersions():
    '''returns boolean\n\n
    discoverBrokerVersions()\n
    '''
def fetchNodes():
    '''returns List<Node>\n\n
    fetchNodes()\n
    '''
def isUpdateDue():
    '''returns boolean\n\n
    isUpdateDue(final long now)\n
    '''
def maybeUpdate():
    '''returns long\n\n
    maybeUpdate(final long now)\n
    '''
def handleDisconnection():
    '''returns None\n\n
    handleDisconnection(final String destination)\n
    '''
def handleAuthenticationFailure():
    '''returns None\n\n
    handleAuthenticationFailure(final AuthenticationException exception)\n
    '''
def handleCompletedMetadataResponse():
    '''returns None\n\n
    handleCompletedMetadataResponse(final RequestHeader requestHeader, final long now, final MetadataResponse response)\n
    '''
def requestUpdate():
    '''returns None\n\n
    requestUpdate()\n
    '''
def completed():
    '''returns ClientResponse\n\n
    completed(final AbstractResponse response, final long timeMs)\n
    '''
def disconnected():
    '''returns ClientResponse\n\n
    disconnected(final long timeMs)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
