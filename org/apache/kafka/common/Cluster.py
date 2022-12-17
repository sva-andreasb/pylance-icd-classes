def ():
    '''returns Cluster\n\n
    (final String clusterId, final Collection<Node> nodes, final Collection<PartitionInfo> partitions, final Set<String> unauthorizedTopics, final Set<String> internalTopics)\n
    (final String clusterId, final Collection<Node> nodes, final Collection<PartitionInfo> partitions, final Set<String> unauthorizedTopics, final Set<String> internalTopics, final Node controller)\n
    '''
def withPartitions():
    '''returns Cluster\n\n
    withPartitions(final Map<TopicPartition, PartitionInfo> partitions)\n
    '''
def nodes():
    '''returns List<Node>\n\n
    nodes()\n
    '''
def nodeById():
    '''returns Node\n\n
    nodeById(final int id)\n
    '''
def leaderFor():
    '''returns Node\n\n
    leaderFor(final TopicPartition topicPartition)\n
    '''
def partition():
    '''returns PartitionInfo\n\n
    partition(final TopicPartition topicPartition)\n
    '''
def partitionsForTopic():
    '''returns List<PartitionInfo>\n\n
    partitionsForTopic(final String topic)\n
    '''
def partitionCountForTopic():
    '''returns Integer\n\n
    partitionCountForTopic(final String topic)\n
    '''
def availablePartitionsForTopic():
    '''returns List<PartitionInfo>\n\n
    availablePartitionsForTopic(final String topic)\n
    '''
def partitionsForNode():
    '''returns List<PartitionInfo>\n\n
    partitionsForNode(final int nodeId)\n
    '''
def topics():
    '''returns Set<String>\n\n
    topics()\n
    '''
def unauthorizedTopics():
    '''returns Set<String>\n\n
    unauthorizedTopics()\n
    '''
def internalTopics():
    '''returns Set<String>\n\n
    internalTopics()\n
    '''
def isBootstrapConfigured():
    '''returns boolean\n\n
    isBootstrapConfigured()\n
    '''
def clusterResource():
    '''returns ClusterResource\n\n
    clusterResource()\n
    '''
def controller():
    '''returns Node\n\n
    controller()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
