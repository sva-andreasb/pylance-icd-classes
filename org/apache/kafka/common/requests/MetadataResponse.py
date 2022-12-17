NO_CONTROLLER_ID = "int  -1"
def ():
    '''returns PartitionMetadata\n\n
    (final List<Node> brokers, final String clusterId, final int controllerId, final List<TopicMetadata> topicMetadata)\n
    (final int throttleTimeMs, final List<Node> brokers, final String clusterId, final int controllerId, final List<TopicMetadata> topicMetadata)\n
    (final Struct struct)\n
    (final Errors error, final String topic, final boolean isInternal, final List<PartitionMetadata> partitionMetadata)\n
    (final Errors error, final int partition, final Node leader, final List<Node> replicas, final List<Node> isr, final List<Node> offlineReplicas)\n
    '''
def throttleTimeMs():
    '''returns int\n\n
    throttleTimeMs()\n
    '''
def topicsByError():
    '''returns Set<String>\n\n
    topicsByError(final Errors error)\n
    '''
def unavailableTopics():
    '''returns Set<String>\n\n
    unavailableTopics()\n
    '''
def cluster():
    '''returns Cluster\n\n
    cluster()\n
    '''
def brokers():
    '''returns Collection<Node>\n\n
    brokers()\n
    '''
def topicMetadata():
    '''returns Collection<TopicMetadata>\n\n
    topicMetadata()\n
    '''
def controller():
    '''returns Node\n\n
    controller()\n
    '''
def clusterId():
    '''returns String\n\n
    clusterId()\n
    '''
def error():
    '''returns Errors\n\n
    error()\n
    error()\n
    '''
def topic():
    '''returns String\n\n
    topic()\n
    '''
def isInternal():
    '''returns boolean\n\n
    isInternal()\n
    '''
def partitionMetadata():
    '''returns List<PartitionMetadata>\n\n
    partitionMetadata()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def partition():
    '''returns int\n\n
    partition()\n
    '''
def leaderId():
    '''returns int\n\n
    leaderId()\n
    '''
def leader():
    '''returns Node\n\n
    leader()\n
    '''
def replicas():
    '''returns List<Node>\n\n
    replicas()\n
    '''
def isr():
    '''returns List<Node>\n\n
    isr()\n
    '''
def offlineReplicas():
    '''returns List<Node>\n\n
    offlineReplicas()\n
    '''
