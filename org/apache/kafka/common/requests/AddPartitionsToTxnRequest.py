def ():
    '''returns Builder\n\n
    (final Struct struct, final short version)\n
    (final String transactionalId, final long producerId, final short producerEpoch, final List<TopicPartition> partitions)\n
    '''
def transactionalId():
    '''returns String\n\n
    transactionalId()\n
    '''
def producerId():
    '''returns long\n\n
    producerId()\n
    '''
def producerEpoch():
    '''returns short\n\n
    producerEpoch()\n
    '''
def partitions():
    '''returns List<TopicPartition>\n\n
    partitions()\n
    partitions()\n
    '''
def getErrorResponse():
    '''returns AddPartitionsToTxnResponse\n\n
    getErrorResponse(final int throttleTimeMs, final Throwable e)\n
    '''
def build():
    '''returns AddPartitionsToTxnRequest\n\n
    build(final short version)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
