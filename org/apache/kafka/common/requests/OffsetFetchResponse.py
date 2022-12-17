INVALID_OFFSET = "long  -1L"
NO_METADATA = "String  \"\""
def ():
    '''returns PartitionData\n\n
    (final Errors error, final Map<TopicPartition, PartitionData> responseData)\n
    (final int throttleTimeMs, final Errors error, final Map<TopicPartition, PartitionData> responseData)\n
    (final Struct struct)\n
    (final long offset, final String metadata, final Errors error)\n
    '''
def maybeThrowFirstPartitionError():
    '''returns None\n\n
    maybeThrowFirstPartitionError()\n
    '''
def throttleTimeMs():
    '''returns int\n\n
    throttleTimeMs()\n
    '''
def hasError():
    '''returns boolean\n\n
    hasError()\n
    hasError()\n
    '''
def error():
    '''returns Errors\n\n
    error()\n
    '''
