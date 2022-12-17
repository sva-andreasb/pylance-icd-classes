def ():
    '''returns Builder\n\n
    (final Struct struct, final short version)\n
    (final long producerId, final short producerEpoch, final int coordinatorEpoch, final TransactionResult result, final List<TopicPartition> partitions)\n
    (final List<TxnMarkerEntry> markers)\n
    '''
def markers():
    '''returns List<TxnMarkerEntry>\n\n
    markers()\n
    '''
def getErrorResponse():
    '''returns WriteTxnMarkersResponse\n\n
    getErrorResponse(final int throttleTimeMs, final Throwable e)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    hashCode()\n
    '''
def producerId():
    '''returns long\n\n
    producerId()\n
    '''
def producerEpoch():
    '''returns short\n\n
    producerEpoch()\n
    '''
def coordinatorEpoch():
    '''returns int\n\n
    coordinatorEpoch()\n
    '''
def transactionResult():
    '''returns TransactionResult\n\n
    transactionResult()\n
    '''
def partitions():
    '''returns List<TopicPartition>\n\n
    partitions()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def build():
    '''returns WriteTxnMarkersRequest\n\n
    build(final short version)\n
    '''
