def ():
    '''returns CommittedOffset\n\n
    (final short version, final String transactionalId, final String consumerGroupId, final long producerId, final short producerEpoch, final Map<TopicPartition, CommittedOffset> offsets)\n
    (final Struct struct, final short version)\n
    (final String transactionalId, final String consumerGroupId, final long producerId, final short producerEpoch, final Map<TopicPartition, CommittedOffset> offsets)\n
    (final long offset, final String metadata)\n
    '''
def transactionalId():
    '''returns String\n\n
    transactionalId()\n
    '''
def consumerGroupId():
    '''returns String\n\n
    consumerGroupId()\n
    consumerGroupId()\n
    '''
def producerId():
    '''returns long\n\n
    producerId()\n
    '''
def producerEpoch():
    '''returns short\n\n
    producerEpoch()\n
    '''
def getErrorResponse():
    '''returns TxnOffsetCommitResponse\n\n
    getErrorResponse(final int throttleTimeMs, final Throwable e)\n
    '''
def build():
    '''returns TxnOffsetCommitRequest\n\n
    build(final short version)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def offset():
    '''returns long\n\n
    offset()\n
    '''
def metadata():
    '''returns String\n\n
    metadata()\n
    '''
