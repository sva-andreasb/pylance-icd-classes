def ():
    '''returns ProducerRecord\n\n
    (final String topic, final Integer partition, final Long timestamp, final K key, final V value, final Iterable<Header> headers)\n
    (final String topic, final Integer partition, final Long timestamp, final K key, final V value)\n
    (final String topic, final Integer partition, final K key, final V value, final Iterable<Header> headers)\n
    (final String topic, final Integer partition, final K key, final V value)\n
    (final String topic, final K key, final V value)\n
    (final String topic, final V value)\n
    '''
def topic():
    '''returns String\n\n
    topic()\n
    '''
def headers():
    '''returns Headers\n\n
    headers()\n
    '''
def key():
    '''returns K\n\n
    key()\n
    '''
def value():
    '''returns V\n\n
    value()\n
    '''
def timestamp():
    '''returns Long\n\n
    timestamp()\n
    '''
def partition():
    '''returns Integer\n\n
    partition()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
