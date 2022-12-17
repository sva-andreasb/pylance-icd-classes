def ():
    '''returns Completion\n\n
    (final Cluster cluster, final boolean autoComplete, final Partitioner partitioner, final Serializer<K> keySerializer, final Serializer<V> valueSerializer)\n
    (final boolean autoComplete, final Serializer<K> keySerializer, final Serializer<V> valueSerializer)\n
    (final boolean autoComplete, final Partitioner partitioner, final Serializer<K> keySerializer, final Serializer<V> valueSerializer)\n
    ()\n
    (final long offset, final RecordMetadata metadata, final ProduceRequestResult result, final Callback callback)\n
    '''
def initTransactions():
    '''returns None\n\n
    initTransactions()\n
    '''
def beginTransaction():
    '''returns None\n\n
    beginTransaction()\n
    '''
def sendOffsetsToTransaction():
    '''returns None\n\n
    sendOffsetsToTransaction(final Map<TopicPartition, OffsetAndMetadata> offsets, final String consumerGroupId)\n
    '''
def commitTransaction():
    '''returns None\n\n
    commitTransaction()\n
    '''
def abortTransaction():
    '''returns None\n\n
    abortTransaction()\n
    '''
def partitionsFor():
    '''returns List<PartitionInfo>\n\n
    partitionsFor(final String topic)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    close(final long timeout, final TimeUnit timeUnit)\n
    '''
def closed():
    '''returns boolean\n\n
    closed()\n
    '''
def fenceProducer():
    '''returns None\n\n
    fenceProducer()\n
    '''
def transactionInitialized():
    '''returns boolean\n\n
    transactionInitialized()\n
    '''
def transactionInFlight():
    '''returns boolean\n\n
    transactionInFlight()\n
    '''
def transactionCommitted():
    '''returns boolean\n\n
    transactionCommitted()\n
    '''
def transactionAborted():
    '''returns boolean\n\n
    transactionAborted()\n
    '''
def flushed():
    '''returns boolean\n\n
    flushed()\n
    '''
def sentOffsets():
    '''returns boolean\n\n
    sentOffsets()\n
    '''
def commitCount():
    '''returns long\n\n
    commitCount()\n
    '''
def complete():
    '''returns None\n\n
    complete(final RuntimeException e)\n
    '''
