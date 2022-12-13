NO_CONTROLLER_ID = "int  -1"
def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def MetadataResponse():
    '''public MetadataResponse(final List<Node> brokers, final String clusterId, final int controllerId, final List<TopicMetadata> topicMetadata)
    public MetadataResponse(final int throttleTimeMs, final List<Node> brokers, final String clusterId, final int controllerId, final List<TopicMetadata> topicMetadata)
    public MetadataResponse(final Struct struct)
    '''
def throttleTimeMs():
    '''public int throttleTimeMs()
    '''
def errors():
    '''public Map<String, Errors> errors()
    '''
def errorCounts():
    '''public Map<Errors, Integer> errorCounts()
    '''
def topicsByError():
    '''public Set<String> topicsByError(final Errors error)
    '''
def unavailableTopics():
    '''public Set<String> unavailableTopics()
    '''
def cluster():
    '''public Cluster cluster()
    '''
def brokers():
    '''public Collection<Node> brokers()
    '''
def topicMetadata():
    '''public Collection<TopicMetadata> topicMetadata()
    '''
def controller():
    '''public Node controller()
    '''
def clusterId():
    '''public String clusterId()
    '''
def parse():
    '''public static MetadataResponse parse(final ByteBuffer buffer, final short version)
    '''
def TopicMetadata():
    '''public TopicMetadata(final Errors error, final String topic, final boolean isInternal, final List<PartitionMetadata> partitionMetadata)
    '''
def error():
    '''public Errors error()
    public Errors error()
    '''
def topic():
    '''public String topic()
    '''
def isInternal():
    '''public boolean isInternal()
    '''
def partitionMetadata():
    '''public List<PartitionMetadata> partitionMetadata()
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def PartitionMetadata():
    '''public PartitionMetadata(final Errors error, final int partition, final Node leader, final List<Node> replicas, final List<Node> isr, final List<Node> offlineReplicas)
    '''
def partition():
    '''public int partition()
    '''
def leaderId():
    '''public int leaderId()
    '''
def leader():
    '''public Node leader()
    '''
def replicas():
    '''public List<Node> replicas()
    '''
def isr():
    '''public List<Node> isr()
    '''
def offlineReplicas():
    '''public List<Node> offlineReplicas()
    '''
