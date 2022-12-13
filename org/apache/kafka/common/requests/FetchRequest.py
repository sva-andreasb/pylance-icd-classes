CONSUMER_REPLICA_ID = "int  -1"
DEFAULT_RESPONSE_MAX_BYTES = "int  Integer.MAX_VALUE"
INVALID_LOG_START_OFFSET = "long  -1L"
def schemaVersions():
    '''    public static Schema[] schemaVersions()
    '''
def FetchRequest():
    '''    public FetchRequest(final Struct struct, final short version)
    '''
def getErrorResponse():
    '''    public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def replicaId():
    '''    public int replicaId()
    '''
def maxWait():
    '''    public int maxWait()
    '''
def minBytes():
    '''    public int minBytes()
    '''
def maxBytes():
    '''    public int maxBytes()
    '''
def fetchData():
    '''    public Map<TopicPartition, PartitionData> fetchData()
    public Map<TopicPartition, PartitionData> fetchData()
    '''
def toForget():
    '''    public List<TopicPartition> toForget()
    public List<TopicPartition> toForget()
    public Builder toForget(final List<TopicPartition> toForget)
    '''
def isFromFollower():
    '''    public boolean isFromFollower()
    '''
def isolationLevel():
    '''    public IsolationLevel isolationLevel()
    public Builder isolationLevel(final IsolationLevel isolationLevel)
    '''
def metadata():
    '''    public FetchMetadata metadata()
    public Builder metadata(final FetchMetadata metadata)
    '''
def parse():
    '''    public static FetchRequest parse(final ByteBuffer buffer, final short version)
    '''
def PartitionData():
    '''    public PartitionData(final long fetchOffset, final long logStartOffset, final int maxBytes)
    '''
def toString():
    '''    public String toString()
    public String toString()
    '''
def hashCode():
    '''    public int hashCode()
    '''
def equals():
    '''    public boolean equals(final Object o)
    '''
def TopicAndPartitionData():
    '''    public TopicAndPartitionData(final String topic)
    '''
def batchByTopic():
    '''    public static <T> List<TopicAndPartitionData<T>> batchByTopic(final Iterator<Map.Entry<TopicPartition, T>> iter)
    '''
def forConsumer():
    '''    public static Builder forConsumer(final int maxWait, final int minBytes, final Map<TopicPartition, PartitionData> fetchData)
    '''
def forReplica():
    '''    public static Builder forReplica(final short allowedVersion, final int replicaId, final int maxWait, final int minBytes, final Map<TopicPartition, PartitionData> fetchData)
    '''
def Builder():
    '''    public Builder(final short minVersion, final short maxVersion, final int replicaId, final int maxWait, final int minBytes, final Map<TopicPartition, PartitionData> fetchData)
    '''
def setMaxBytes():
    '''    public Builder setMaxBytes(final int maxBytes)
    '''
def build():
    '''    public FetchRequest build(final short version)
    '''
