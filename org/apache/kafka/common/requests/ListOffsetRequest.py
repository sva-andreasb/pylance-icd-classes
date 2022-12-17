EARLIEST_TIMESTAMP = "long  -2L"
LATEST_TIMESTAMP = "long  -1L"
CONSUMER_REPLICA_ID = "int  -1"
DEBUGGING_REPLICA_ID = "int  -2"
def ():
    '''returns PartitionData\n\n
    (final Struct struct, final short version)\n
    (final long timestamp, final int maxNumOffsets)\n
    '''
def getErrorResponse():
    '''returns AbstractResponse\n\n
    getErrorResponse(final int throttleTimeMs, final Throwable e)\n
    '''
def replicaId():
    '''returns int\n\n
    replicaId()\n
    '''
def isolationLevel():
    '''returns IsolationLevel\n\n
    isolationLevel()\n
    '''
def duplicatePartitions():
    '''returns Set<TopicPartition>\n\n
    duplicatePartitions()\n
    '''
def setOffsetData():
    '''returns Builder\n\n
    setOffsetData(final Map<TopicPartition, PartitionData> offsetData)\n
    '''
def setTargetTimes():
    '''returns Builder\n\n
    setTargetTimes(final Map<TopicPartition, Long> partitionTimestamps)\n
    '''
def build():
    '''returns ListOffsetRequest\n\n
    build(final short version)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
