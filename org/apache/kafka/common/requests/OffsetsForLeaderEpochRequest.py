def schemaVersions():
    '''    public static Schema[] schemaVersions()
    '''
def epochsByTopicPartition():
    '''    public Map<TopicPartition, Integer> epochsByTopicPartition()
    '''
def OffsetsForLeaderEpochRequest():
    '''    public OffsetsForLeaderEpochRequest(final Map<TopicPartition, Integer> epochsByPartition, final short version)
    public OffsetsForLeaderEpochRequest(final Struct struct, final short version)
    '''
def parse():
    '''    public static OffsetsForLeaderEpochRequest parse(final ByteBuffer buffer, final short versionId)
    public static OffsetsForLeaderEpochRequest parse(final ByteBuffer buffer, final short version)
    '''
def getErrorResponse():
    '''    public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def Builder():
    '''    public Builder()
    public Builder(final Map<TopicPartition, Integer> epochsByPartition)
    '''
def add():
    '''    public Builder add(final TopicPartition topicPartition, final Integer epoch)
    '''
def build():
    '''    public OffsetsForLeaderEpochRequest build(final short version)
    '''
def toString():
    '''    public String toString()
    '''
