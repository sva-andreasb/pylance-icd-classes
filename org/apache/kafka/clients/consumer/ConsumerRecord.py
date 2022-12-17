NO_TIMESTAMP = "long  -1L"
NULL_SIZE = "int  -1"
NULL_CHECKSUM = "int  -1"
def ():
    '''returns ConsumerRecord\n\n
    (final String topic, final int partition, final long offset, final K key, final V value)\n
    (final String topic, final int partition, final long offset, final long timestamp, final TimestampType timestampType, final long checksum, final int serializedKeySize, final int serializedValueSize, final K key, final V value)\n
    (final String topic, final int partition, final long offset, final long timestamp, final TimestampType timestampType, final Long checksum, final int serializedKeySize, final int serializedValueSize, final K key, final V value, final Headers headers)\n
    '''
def topic():
    '''returns String\n\n
    topic()\n
    '''
def partition():
    '''returns int\n\n
    partition()\n
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
def offset():
    '''returns long\n\n
    offset()\n
    '''
def timestamp():
    '''returns long\n\n
    timestamp()\n
    '''
def timestampType():
    '''returns TimestampType\n\n
    timestampType()\n
    '''
def checksum():
    '''returns long\n\n
    checksum()\n
    '''
def serializedKeySize():
    '''returns int\n\n
    serializedKeySize()\n
    '''
def serializedValueSize():
    '''returns int\n\n
    serializedValueSize()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
