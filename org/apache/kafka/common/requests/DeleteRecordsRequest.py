HIGH_WATERMARK = "long  -1L"
def ():
    '''returns Builder\n\n
    (final Struct struct, final short version)\n
    (final int timeout, final Map<TopicPartition, Long> partitionOffsets, final short version)\n
    (final int timeout, final Map<TopicPartition, Long> partitionOffsets)\n
    '''
def getErrorResponse():
    '''returns AbstractResponse\n\n
    getErrorResponse(final int throttleTimeMs, final Throwable e)\n
    '''
def timeout():
    '''returns int\n\n
    timeout()\n
    '''
def build():
    '''returns DeleteRecordsRequest\n\n
    build(final short version)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
