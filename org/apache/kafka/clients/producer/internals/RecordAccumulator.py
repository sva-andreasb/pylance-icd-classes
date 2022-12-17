def ():
    '''returns ReadyCheckResult\n\n
    (final LogContext logContext, final int batchSize, final long totalSize, final CompressionType compression, final long lingerMs, final long retryBackoffMs, final Metrics metrics, final Time time, final ApiVersions apiVersions, final TransactionManager transactionManager)\n
    (final FutureRecordMetadata future, final boolean batchIsFull, final boolean newBatchCreated)\n
    (final Set<Node> readyNodes, final long nextReadyCheckDelayMs, final Set<String> unknownLeaderTopics)\n
    '''
def measure():
    '''returns double\n\n
    measure(final MetricConfig config, final long now)\n
    measure(final MetricConfig config, final long now)\n
    measure(final MetricConfig config, final long now)\n
    '''
def append():
    '''returns RecordAppendResult\n\n
    append(final TopicPartition tp, final long timestamp, final byte[] key, final byte[] value, Header[] headers, final Callback callback, final long maxTimeToBlock)\n
    '''
def expiredBatches():
    '''returns List<ProducerBatch>\n\n
    expiredBatches(final int requestTimeout, final long now)\n
    '''
def reenqueue():
    '''returns None\n\n
    reenqueue(final ProducerBatch batch, final long now)\n
    '''
def splitAndReenqueue():
    '''returns int\n\n
    splitAndReenqueue(final ProducerBatch bigBatch)\n
    '''
def ready():
    '''returns ReadyCheckResult\n\n
    ready(final Cluster cluster, final long nowMs)\n
    '''
def hasUndrained():
    '''returns boolean\n\n
    hasUndrained()\n
    '''
def deallocate():
    '''returns None\n\n
    deallocate(final ProducerBatch batch)\n
    '''
def beginFlush():
    '''returns None\n\n
    beginFlush()\n
    '''
def awaitFlushCompletion():
    '''returns None\n\n
    awaitFlushCompletion()\n
    '''
def hasIncomplete():
    '''returns boolean\n\n
    hasIncomplete()\n
    '''
def abortIncompleteBatches():
    '''returns None\n\n
    abortIncompleteBatches()\n
    '''
def mutePartition():
    '''returns None\n\n
    mutePartition(final TopicPartition tp)\n
    '''
def unmutePartition():
    '''returns None\n\n
    unmutePartition(final TopicPartition tp)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
