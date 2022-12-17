def close():
    '''returns None\n\n
    close()\n
    '''
def createTopics():
    '''returns CreateTopicsResult\n\n
    createTopics(final Collection<NewTopic> newTopics)\n
    '''
def deleteTopics():
    '''returns DeleteTopicsResult\n\n
    deleteTopics(final Collection<String> topics)\n
    '''
def listTopics():
    '''returns ListTopicsResult\n\n
    listTopics()\n
    '''
def describeTopics():
    '''returns DescribeTopicsResult\n\n
    describeTopics(final Collection<String> topicNames)\n
    '''
def describeCluster():
    '''returns DescribeClusterResult\n\n
    describeCluster()\n
    '''
def describeAcls():
    '''returns DescribeAclsResult\n\n
    describeAcls(final AclBindingFilter filter)\n
    '''
def createAcls():
    '''returns CreateAclsResult\n\n
    createAcls(final Collection<AclBinding> acls)\n
    '''
def deleteAcls():
    '''returns DeleteAclsResult\n\n
    deleteAcls(final Collection<AclBindingFilter> filters)\n
    '''
def describeConfigs():
    '''returns DescribeConfigsResult\n\n
    describeConfigs(final Collection<ConfigResource> resources)\n
    '''
def alterConfigs():
    '''returns AlterConfigsResult\n\n
    alterConfigs(final Map<ConfigResource, Config> configs)\n
    '''
def alterReplicaLogDirs():
    '''returns AlterReplicaLogDirsResult\n\n
    alterReplicaLogDirs(final Map<TopicPartitionReplica, String> replicaAssignment)\n
    '''
def describeLogDirs():
    '''returns DescribeLogDirsResult\n\n
    describeLogDirs(final Collection<Integer> brokers)\n
    '''
def describeReplicaLogDirs():
    '''returns DescribeReplicaLogDirsResult\n\n
    describeReplicaLogDirs(final Collection<TopicPartitionReplica> replicas)\n
    '''
def createPartitions():
    '''returns CreatePartitionsResult\n\n
    createPartitions(final Map<String, NewPartitions> newPartitions)\n
    '''
def deleteRecords():
    '''returns DeleteRecordsResult\n\n
    deleteRecords(final Map<TopicPartition, RecordsToDelete> recordsToDelete)\n
    '''
