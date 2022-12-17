def ():
    '''returns ListOffsetResult\n\n
    (final LogContext logContext, final ConsumerNetworkClient client, final int minBytes, final int maxBytes, final int maxWaitMs, final int fetchSize, final int maxPollRecords, final boolean checkCrcs, final Deserializer<K> keyDeserializer, final Deserializer<V> valueDeserializer, final Metadata metadata, final SubscriptionState subscriptions, final Metrics metrics, final FetcherMetricsRegistry metricsRegistry, final Time time, final long retryBackoffMs, final long requestTimeoutMs, final IsolationLevel isolationLevel)\n
    (final Map<TopicPartition, OffsetData> fetchedOffsets, final Set<TopicPartition> partitionsNeedingRetry)\n
    ()\n
    '''
def hasCompletedFetches():
    '''returns boolean\n\n
    hasCompletedFetches()\n
    '''
def sendFetches():
    '''returns int\n\n
    sendFetches()\n
    '''
def onSuccess():
    '''returns None\n\n
    onSuccess(final ClientResponse resp)\n
    onSuccess(final ListOffsetResult result)\n
    onSuccess(final ListOffsetResult partialResult)\n
    onSuccess(final ClientResponse response, final RequestFuture<ListOffsetResult> future)\n
    '''
def onFailure():
    '''returns None\n\n
    onFailure(final RuntimeException e)\n
    onFailure(final RuntimeException e)\n
    onFailure(final RuntimeException e)\n
    '''
def resetOffsetsIfNeeded():
    '''returns None\n\n
    resetOffsetsIfNeeded()\n
    '''
def onAssignment():
    '''returns None\n\n
    onAssignment(final Set<TopicPartition> assignment)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def compare():
    '''returns int\n\n
    compare(final FetchResponse.AbortedTransaction o1, final FetchResponse.AbortedTransaction o2)\n
    '''
def record():
    '''returns None\n\n
    record(final TopicPartition partition, final int bytes, final int records)\n
    '''
