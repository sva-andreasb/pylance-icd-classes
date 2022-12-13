NO_CONTROLLER_ID = "int  -1"
def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def MetadataResponse():
'''public MetadataResponse(final List<Node> brokers, final String clusterId, final int controllerId, final List<TopicMetadata> topicMetadata)
public MetadataResponse(final int throttleTimeMs, final List<Node> brokers, final String clusterId, final int controllerId, final List<TopicMetadata> topicMetadata)
public MetadataResponse(final Struct struct)
'''
pass
def throttleTimeMs():
'''public int throttleTimeMs()
'''
pass
def errors():
'''public Map<String, Errors> errors()
'''
pass
def errorCounts():
'''public Map<Errors, Integer> errorCounts()
'''
pass
def topicsByError():
'''public Set<String> topicsByError(final Errors error)
'''
pass
def unavailableTopics():
'''public Set<String> unavailableTopics()
'''
pass
def cluster():
'''public Cluster cluster()
'''
pass
def brokers():
'''public Collection<Node> brokers()
'''
pass
def topicMetadata():
'''public Collection<TopicMetadata> topicMetadata()
'''
pass
def controller():
'''public Node controller()
'''
pass
def clusterId():
'''public String clusterId()
'''
pass
def parse():
'''public static MetadataResponse parse(final ByteBuffer buffer, final short version)
'''
pass
def TopicMetadata():
'''public TopicMetadata(final Errors error, final String topic, final boolean isInternal, final List<PartitionMetadata> partitionMetadata)
'''
pass
def error():
'''public Errors error()
public Errors error()
'''
pass
def topic():
'''public String topic()
'''
pass
def isInternal():
'''public boolean isInternal()
'''
pass
def partitionMetadata():
'''public List<PartitionMetadata> partitionMetadata()
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def PartitionMetadata():
'''public PartitionMetadata(final Errors error, final int partition, final Node leader, final List<Node> replicas, final List<Node> isr, final List<Node> offlineReplicas)
'''
pass
def partition():
'''public int partition()
'''
pass
def leaderId():
'''public int leaderId()
'''
pass
def leader():
'''public Node leader()
'''
pass
def replicas():
'''public List<Node> replicas()
'''
pass
def isr():
'''public List<Node> isr()
'''
pass
def offlineReplicas():
'''public List<Node> offlineReplicas()
'''
pass
