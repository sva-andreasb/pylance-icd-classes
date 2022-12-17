def ():
    '''returns ConsumerCoordinator\n\n
    (final LogContext logContext, final ConsumerNetworkClient client, final String groupId, final int rebalanceTimeoutMs, final int sessionTimeoutMs, final int heartbeatIntervalMs, final List<PartitionAssignor> assignors, final Metadata metadata, final SubscriptionState subscriptions, final Metrics metrics, final String metricGrpPrefix, final Time time, final long retryBackoffMs, final boolean autoCommitEnabled, final int autoCommitIntervalMs, final ConsumerInterceptors<?, ?> interceptors, final boolean excludeInternalTopics, final boolean leaveGroupOnClose)\n
    '''
def protocolType():
    '''returns String\n\n
    protocolType()\n
    '''
def updatePatternSubscription():
    '''returns None\n\n
    updatePatternSubscription(final Cluster cluster)\n
    '''
def onMetadataUpdate():
    '''returns None\n\n
    onMetadataUpdate(final Cluster cluster, final Set<String> unavailableTopics)\n
    '''
def poll():
    '''returns None\n\n
    poll(long now, final long remainingMs)\n
    '''
def timeToNextPoll():
    '''returns long\n\n
    timeToNextPoll(final long now)\n
    '''
def needRejoin():
    '''returns boolean\n\n
    needRejoin()\n
    '''
def refreshCommittedOffsetsIfNeeded():
    '''returns None\n\n
    refreshCommittedOffsetsIfNeeded()\n
    '''
def close():
    '''returns None\n\n
    close(final long timeoutMs)\n
    '''
def commitOffsetsAsync():
    '''returns None\n\n
    commitOffsetsAsync(final Map<TopicPartition, OffsetAndMetadata> offsets, final OffsetCommitCallback callback)\n
    '''
def onSuccess():
    '''returns None\n\n
    onSuccess(final Void value)\n
    onSuccess(final Void value)\n
    '''
def onFailure():
    '''returns None\n\n
    onFailure(final RuntimeException e)\n
    onFailure(final RuntimeException e)\n
    '''
def commitOffsetsSync():
    '''returns boolean\n\n
    commitOffsetsSync(final Map<TopicPartition, OffsetAndMetadata> offsets, final long timeoutMs)\n
    '''
def maybeAutoCommitOffsetsAsync():
    '''returns None\n\n
    maybeAutoCommitOffsetsAsync(final long now)\n
    '''
def onComplete():
    '''returns None\n\n
    onComplete(final Map<TopicPartition, OffsetAndMetadata> offsets, final Exception exception)\n
    onComplete(final Map<TopicPartition, OffsetAndMetadata> offsets, final Exception exception)\n
    '''
def handle():
    '''returns None\n\n
    handle(final OffsetCommitResponse commitResponse, final RequestFuture<Void> future)\n
    handle(final OffsetFetchResponse response, final RequestFuture<Map<TopicPartition, OffsetAndMetadata>> future)\n
    '''
def measure():
    '''returns double\n\n
    measure(final MetricConfig config, final long now)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def invoke():
    '''returns None\n\n
    invoke()\n
    '''
