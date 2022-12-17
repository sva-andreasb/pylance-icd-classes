def ():
    '''returns Builder\n\n
    (final Map<TopicPartition, Integer> epochsByPartition, final short version)\n
    (final Struct struct, final short version)\n
    ()\n
    (final Map<TopicPartition, Integer> epochsByPartition)\n
    '''
def getErrorResponse():
    '''returns AbstractResponse\n\n
    getErrorResponse(final int throttleTimeMs, final Throwable e)\n
    '''
def add():
    '''returns Builder\n\n
    add(final TopicPartition topicPartition, final Integer epoch)\n
    '''
def build():
    '''returns OffsetsForLeaderEpochRequest\n\n
    build(final short version)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
