EARLIEST_TIMESTAMP = "long  -2L"
LATEST_TIMESTAMP = "long  -1L"
CONSUMER_REPLICA_ID = "int  -1"
DEBUGGING_REPLICA_ID = "int  -2"
def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def ListOffsetRequest():
'''public ListOffsetRequest(final Struct struct, final short version)
'''
pass
def getErrorResponse():
'''public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
'''
pass
def replicaId():
'''public int replicaId()
'''
pass
def isolationLevel():
'''public IsolationLevel isolationLevel()
'''
pass
def offsetData():
'''public Map<TopicPartition, PartitionData> offsetData()
'''
pass
def partitionTimestamps():
'''public Map<TopicPartition, Long> partitionTimestamps()
'''
pass
def duplicatePartitions():
'''public Set<TopicPartition> duplicatePartitions()
'''
pass
def parse():
'''public static ListOffsetRequest parse(final ByteBuffer buffer, final short version)
'''
pass
def forReplica():
'''public static Builder forReplica(final short allowedVersion, final int replicaId)
'''
pass
def forConsumer():
'''public static Builder forConsumer(final boolean requireTimestamp, final IsolationLevel isolationLevel)
'''
pass
def setOffsetData():
'''public Builder setOffsetData(final Map<TopicPartition, PartitionData> offsetData)
'''
pass
def setTargetTimes():
'''public Builder setTargetTimes(final Map<TopicPartition, Long> partitionTimestamps)
'''
pass
def build():
'''public ListOffsetRequest build(final short version)
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def PartitionData():
'''public PartitionData(final long timestamp, final int maxNumOffsets)
'''
pass
