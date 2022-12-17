NETWORK_THREAD_PREFIX = "String  \"kafka-producer-network-thread\""
def ():
    '''returns FutureFailure\n\n
    (final Map<String, Object> configs)\n
    (final Map<String, Object> configs, final Serializer<K> keySerializer, final Serializer<V> valueSerializer)\n
    (final Properties properties)\n
    (final Properties properties, final Serializer<K> keySerializer, final Serializer<V> valueSerializer)\n
    (final Exception exception)\n
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
def send():
    '''returns Future<RecordMetadata>\n\n
    send(final ProducerRecord<K, V> record)\n
    send(final ProducerRecord<K, V> record, final Callback callback)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
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
def cancel():
    '''returns boolean\n\n
    cancel(final boolean interrupt)\n
    '''
def get():
    '''returns RecordMetadata\n\n
    get()\n
    get(final long timeout, final TimeUnit unit)\n
    '''
def isCancelled():
    '''returns boolean\n\n
    isCancelled()\n
    '''
def isDone():
    '''returns boolean\n\n
    isDone()\n
    '''
def onCompletion():
    '''returns None\n\n
    onCompletion(RecordMetadata metadata, final Exception exception)\n
    '''
