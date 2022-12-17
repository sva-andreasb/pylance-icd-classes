HEARTBEAT_THREAD_PREFIX = "String  \"kafka-coordinator-heartbeat-thread\""
def ():
    '''returns Generation\n\n
    (final LogContext logContext, final ConsumerNetworkClient client, final String groupId, final int rebalanceTimeoutMs, final int sessionTimeoutMs, final int heartbeatIntervalMs, final Metrics metrics, final String metricGrpPrefix, final Time time, final long retryBackoffMs, final boolean leaveGroupOnClose)\n
    (final Metrics metrics, final String metricGrpPrefix)\n
    (final int generationId, final String memberId, final String protocol)\n
    '''
def ensureActiveGroup():
    '''returns None\n\n
    ensureActiveGroup()\n
    '''
def onSuccess():
    '''returns None\n\n
    onSuccess(final ByteBuffer value)\n
    onSuccess(final ClientResponse resp, final RequestFuture<Void> future)\n
    onSuccess(final ClientResponse clientResponse, final RequestFuture<T> future)\n
    onSuccess(final Void value)\n
    '''
def onFailure():
    '''returns None\n\n
    onFailure(final RuntimeException e)\n
    onFailure(final RuntimeException e, final RequestFuture<Void> future)\n
    onFailure(final RuntimeException e, final RequestFuture<T> future)\n
    onFailure(final RuntimeException e)\n
    '''
def coordinatorUnknown():
    '''returns boolean\n\n
    coordinatorUnknown()\n
    '''
def handle():
    '''returns None\n\n
    handle(final JoinGroupResponse joinResponse, final RequestFuture<ByteBuffer> future)\n
    handle(final SyncGroupResponse syncResponse, final RequestFuture<ByteBuffer> future)\n
    handle(final LeaveGroupResponse leaveResponse, final RequestFuture<Void> future)\n
    handle(final HeartbeatResponse heartbeatResponse, final RequestFuture<Void> future)\n
    '''
def measure():
    '''returns double\n\n
    measure(final MetricConfig config, final long now)\n
    '''
def enable():
    '''returns None\n\n
    enable()\n
    '''
def disable():
    '''returns None\n\n
    disable()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
