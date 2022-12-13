CONSUMER_REPLICA_ID = "int  -1"
DEFAULT_RESPONSE_MAX_BYTES = "int  Integer.MAX_VALUE"
INVALID_LOG_START_OFFSET = "long  -1L"
def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def FetchRequest():
'''public FetchRequest(final Struct struct, final short version)
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
def maxWait():
'''public int maxWait()
'''
pass
def minBytes():
'''public int minBytes()
'''
pass
def maxBytes():
'''public int maxBytes()
'''
pass
def fetchData():
'''public Map<TopicPartition, PartitionData> fetchData()
public Map<TopicPartition, PartitionData> fetchData()
'''
pass
def toForget():
'''public List<TopicPartition> toForget()
public List<TopicPartition> toForget()
public Builder toForget(final List<TopicPartition> toForget)
'''
pass
def isFromFollower():
'''public boolean isFromFollower()
'''
pass
def isolationLevel():
'''public IsolationLevel isolationLevel()
public Builder isolationLevel(final IsolationLevel isolationLevel)
'''
pass
def metadata():
'''public FetchMetadata metadata()
public Builder metadata(final FetchMetadata metadata)
'''
pass
def parse():
'''public static FetchRequest parse(final ByteBuffer buffer, final short version)
'''
pass
def PartitionData():
'''public PartitionData(final long fetchOffset, final long logStartOffset, final int maxBytes)
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
def TopicAndPartitionData():
'''public TopicAndPartitionData(final String topic)
'''
pass
def batchByTopic():
'''public static <T> List<TopicAndPartitionData<T>> batchByTopic(final Iterator<Map.Entry<TopicPartition, T>> iter)
'''
pass
def forConsumer():
'''public static Builder forConsumer(final int maxWait, final int minBytes, final Map<TopicPartition, PartitionData> fetchData)
'''
pass
def forReplica():
'''public static Builder forReplica(final short allowedVersion, final int replicaId, final int maxWait, final int minBytes, final Map<TopicPartition, PartitionData> fetchData)
'''
pass
def Builder():
'''public Builder(final short minVersion, final short maxVersion, final int replicaId, final int maxWait, final int minBytes, final Map<TopicPartition, PartitionData> fetchData)
'''
pass
def setMaxBytes():
'''public Builder setMaxBytes(final int maxBytes)
'''
pass
def build():
'''public FetchRequest build(final short version)
'''
pass
