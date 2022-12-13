NO_NUM_PARTITIONS = "int  -1"
NO_REPLICATION_FACTOR = "short  -1"
def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def CreateTopicsRequest():
    '''public CreateTopicsRequest(final Struct struct, final short version)
    '''
def getErrorResponse():
    '''public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def topics():
    '''public Map<String, TopicDetails> topics()
    '''
def timeout():
    '''public int timeout()
    '''
def validateOnly():
    '''public boolean validateOnly()
    '''
def duplicateTopics():
    '''public Set<String> duplicateTopics()
    '''
def parse():
    '''public static CreateTopicsRequest parse(final ByteBuffer buffer, final short version)
    '''
def toStruct():
    '''public Struct toStruct()
    '''
def TopicDetails():
    '''public TopicDetails(final int partitions, final short replicationFactor, final Map<String, String> configs)
    public TopicDetails(final int partitions, final short replicationFactor)
    public TopicDetails(final Map<Integer, List<Integer>> replicasAssignments, final Map<String, String> configs)
    public TopicDetails(final Map<Integer, List<Integer>> replicasAssignments)
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def Builder():
    '''public Builder(final Map<String, TopicDetails> topics, final int timeout)
    public Builder(final Map<String, TopicDetails> topics, final int timeout, final boolean validateOnly)
    '''
def build():
    '''public CreateTopicsRequest build(final short version)
    '''
