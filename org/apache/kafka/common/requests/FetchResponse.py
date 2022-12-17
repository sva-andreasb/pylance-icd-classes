INVALID_HIGHWATERMARK = "long  -1L"
INVALID_LAST_STABLE_OFFSET = "long  -1L"
INVALID_LOG_START_OFFSET = "long  -1L"
def ():
    '''returns PartitionData\n\n
    (final Errors error, final LinkedHashMap<TopicPartition, PartitionData> responseData, final int throttleTimeMs, final int sessionId)\n
    (final Struct struct)\n
    (final long producerId, final long firstOffset)\n
    (final Errors error, final long highWatermark, final long lastStableOffset, final long logStartOffset, final List<AbortedTransaction> abortedTransactions, final Records records)\n
    '''
def toStruct():
    '''returns Struct\n\n
    toStruct(final short version)\n
    '''
def error():
    '''returns Errors\n\n
    error()\n
    '''
def throttleTimeMs():
    '''returns int\n\n
    throttleTimeMs()\n
    '''
def sessionId():
    '''returns int\n\n
    sessionId()\n
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
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
