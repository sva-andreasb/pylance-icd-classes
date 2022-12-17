def ():
    '''returns KafkaConsumer\n\n
    (final Map<String, Object> configs)\n
    (final Map<String, Object> configs, final Deserializer<K> keyDeserializer, final Deserializer<V> valueDeserializer)\n
    (final Properties properties)\n
    (final Properties properties, final Deserializer<K> keyDeserializer, final Deserializer<V> valueDeserializer)\n
    '''
def assignment():
    '''returns Set<TopicPartition>\n\n
    assignment()\n
    '''
def subscription():
    '''returns Set<String>\n\n
    subscription()\n
    '''
def subscribe():
    '''returns None\n\n
    subscribe(final Collection<String> topics, final ConsumerRebalanceListener listener)\n
    subscribe(final Collection<String> topics)\n
    subscribe(final Pattern pattern, final ConsumerRebalanceListener listener)\n
    subscribe(final Pattern pattern)\n
    '''
def unsubscribe():
    '''returns None\n\n
    unsubscribe()\n
    '''
def assign():
    '''returns None\n\n
    assign(final Collection<TopicPartition> partitions)\n
    '''
def shouldBlock():
    '''returns boolean\n\n
    shouldBlock()\n
    '''
def commitSync():
    '''returns None\n\n
    commitSync()\n
    commitSync(final Map<TopicPartition, OffsetAndMetadata> offsets)\n
    '''
def commitAsync():
    '''returns None\n\n
    commitAsync()\n
    commitAsync(final OffsetCommitCallback callback)\n
    commitAsync(final Map<TopicPartition, OffsetAndMetadata> offsets, final OffsetCommitCallback callback)\n
    '''
def seek():
    '''returns None\n\n
    seek(final TopicPartition partition, final long offset)\n
    '''
def seekToBeginning():
    '''returns None\n\n
    seekToBeginning(final Collection<TopicPartition> partitions)\n
    '''
def seekToEnd():
    '''returns None\n\n
    seekToEnd(final Collection<TopicPartition> partitions)\n
    '''
def position():
    '''returns long\n\n
    position(final TopicPartition partition)\n
    '''
def committed():
    '''returns OffsetAndMetadata\n\n
    committed(final TopicPartition partition)\n
    '''
def partitionsFor():
    '''returns List<PartitionInfo>\n\n
    partitionsFor(final String topic)\n
    '''
def pause():
    '''returns None\n\n
    pause(final Collection<TopicPartition> partitions)\n
    '''
def resume():
    '''returns None\n\n
    resume(final Collection<TopicPartition> partitions)\n
    '''
def paused():
    '''returns Set<TopicPartition>\n\n
    paused()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    close(final long timeout, final TimeUnit timeUnit)\n
    '''
def wakeup():
    '''returns None\n\n
    wakeup()\n
    '''
