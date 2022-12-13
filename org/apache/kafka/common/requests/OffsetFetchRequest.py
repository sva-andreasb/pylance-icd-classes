def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def forAllPartitions():
    '''public static OffsetFetchRequest forAllPartitions(final String groupId)
    '''
def OffsetFetchRequest():
    '''public OffsetFetchRequest(final Struct struct, final short version)
    '''
def getErrorResponse():
    '''public OffsetFetchResponse getErrorResponse(final Errors error)
    public OffsetFetchResponse getErrorResponse(final int throttleTimeMs, final Errors error)
    public OffsetFetchResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def groupId():
    '''public String groupId()
    '''
def partitions():
    '''public List<TopicPartition> partitions()
    '''
def parse():
    '''public static OffsetFetchRequest parse(final ByteBuffer buffer, final short version)
    '''
def isAllPartitions():
    '''public boolean isAllPartitions()
    '''
def Builder():
    '''public Builder(final String groupId, final List<TopicPartition> partitions)
    '''
def allTopicPartitions():
    '''public static Builder allTopicPartitions(final String groupId)
    '''
def isAllTopicPartitions():
    '''public boolean isAllTopicPartitions()
    '''
def build():
    '''public OffsetFetchRequest build(final short version)
    '''
def toString():
    '''public String toString()
    '''
