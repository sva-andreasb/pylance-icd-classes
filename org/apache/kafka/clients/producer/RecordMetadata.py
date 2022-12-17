UNKNOWN_PARTITION = "int  -1"
def ():
    '''returns RecordMetadata\n\n
    (final TopicPartition topicPartition, final long baseOffset, final long relativeOffset, final long timestamp, final Long checksum, final int serializedKeySize, final int serializedValueSize)\n
    (final TopicPartition topicPartition, final long baseOffset, final long relativeOffset, final long timestamp, final long checksum, final int serializedKeySize, final int serializedValueSize)\n
    '''
def hasOffset():
    '''returns boolean\n\n
    hasOffset()\n
    '''
def offset():
    '''returns long\n\n
    offset()\n
    '''
def hasTimestamp():
    '''returns boolean\n\n
    hasTimestamp()\n
    '''
def timestamp():
    '''returns long\n\n
    timestamp()\n
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
def topic():
    '''returns String\n\n
    topic()\n
    '''
def partition():
    '''returns int\n\n
    partition()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
