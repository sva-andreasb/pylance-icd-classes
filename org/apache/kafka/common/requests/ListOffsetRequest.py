EARLIEST_TIMESTAMP = "long  -2L"
LATEST_TIMESTAMP = "long  -1L"
CONSUMER_REPLICA_ID = "int  -1"
DEBUGGING_REPLICA_ID = "int  -2"
def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def ListOffsetRequest():
    '''public ListOffsetRequest(final Struct struct, final short version)
    '''
def getErrorResponse():
    '''public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def replicaId():
    '''public int replicaId()
    '''
def isolationLevel():
    '''public IsolationLevel isolationLevel()
    '''
def offsetData():
    '''public Map<TopicPartition, PartitionData> offsetData()
    '''
def partitionTimestamps():
    '''public Map<TopicPartition, Long> partitionTimestamps()
    '''
def duplicatePartitions():
    '''public Set<TopicPartition> duplicatePartitions()
    '''
def parse():
    '''public static ListOffsetRequest parse(final ByteBuffer buffer, final short version)
    '''
def forReplica():
    '''public static Builder forReplica(final short allowedVersion, final int replicaId)
    '''
def forConsumer():
    '''public static Builder forConsumer(final boolean requireTimestamp, final IsolationLevel isolationLevel)
    '''
def setOffsetData():
    '''public Builder setOffsetData(final Map<TopicPartition, PartitionData> offsetData)
    '''
def setTargetTimes():
    '''public Builder setTargetTimes(final Map<TopicPartition, Long> partitionTimestamps)
    '''
def build():
    '''public ListOffsetRequest build(final short version)
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def PartitionData():
    '''public PartitionData(final long timestamp, final int maxNumOffsets)
    '''
