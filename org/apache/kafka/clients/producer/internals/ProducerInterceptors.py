def ():
    '''returns ProducerInterceptors\n\n
    (final List<ProducerInterceptor<K, V>> interceptors)\n
    '''
def onAcknowledgement():
    '''returns None\n\n
    onAcknowledgement(final RecordMetadata metadata, final Exception exception)\n
    '''
def onSendError():
    '''returns None\n\n
    onSendError(final ProducerRecord<K, V> record, TopicPartition interceptTopicPartition, final Exception exception)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
