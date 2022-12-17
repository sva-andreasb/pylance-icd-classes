def close():
    '''returns None\n\n
    close(final long duration, final TimeUnit unit)\n
    '''
def createTopics():
    '''returns CreateTopicsResult\n\n
    createTopics(final Collection<NewTopic> newTopics, final CreateTopicsOptions options)\n
    '''
def handleResponse():
    '''returns None\n\n
    handleResponse(final AbstractResponse abstractResponse)\n
    handleResponse(final AbstractResponse abstractResponse)\n
    handleResponse(final AbstractResponse abstractResponse)\n
    handleResponse(final AbstractResponse abstractResponse)\n
    handleResponse(final AbstractResponse abstractResponse)\n
    handleResponse(final AbstractResponse abstractResponse)\n
    '''
def deleteTopics():
    '''returns DeleteTopicsResult\n\n
    deleteTopics(final Collection<String> topicNames, final DeleteTopicsOptions options)\n
    '''
def listTopics():
    '''returns ListTopicsResult\n\n
    listTopics(final ListTopicsOptions options)\n
    '''
def describeTopics():
    '''returns DescribeTopicsResult\n\n
    describeTopics(final Collection<String> topicNames, final DescribeTopicsOptions options)\n
    '''
def compare():
    '''returns int\n\n
    compare(final TopicPartitionInfo tp1, final TopicPartitionInfo tp2)\n
    '''
def describeCluster():
    '''returns DescribeClusterResult\n\n
    describeCluster(final DescribeClusterOptions options)\n
    '''
def describeAcls():
    '''returns DescribeAclsResult\n\n
    describeAcls(final AclBindingFilter filter, final DescribeAclsOptions options)\n
    '''
def createAcls():
    '''returns CreateAclsResult\n\n
    createAcls(final Collection<AclBinding> acls, final CreateAclsOptions options)\n
    '''
def deleteAcls():
    '''returns DeleteAclsResult\n\n
    deleteAcls(final Collection<AclBindingFilter> filters, final DeleteAclsOptions options)\n
    '''
def describeConfigs():
    '''returns DescribeConfigsResult\n\n
    describeConfigs(final Collection<ConfigResource> configResources, final DescribeConfigsOptions options)\n
    '''
def alterConfigs():
    '''returns AlterConfigsResult\n\n
    alterConfigs(final Map<ConfigResource, Config> configs, final AlterConfigsOptions options)\n
    '''
def alterReplicaLogDirs():
    '''returns AlterReplicaLogDirsResult\n\n
    alterReplicaLogDirs(final Map<TopicPartitionReplica, String> replicaAssignment, final AlterReplicaLogDirsOptions options)\n
    '''
def describeLogDirs():
    '''returns DescribeLogDirsResult\n\n
    describeLogDirs(final Collection<Integer> brokers, final DescribeLogDirsOptions options)\n
    '''
def describeReplicaLogDirs():
    '''returns DescribeReplicaLogDirsResult\n\n
    describeReplicaLogDirs(final Collection<TopicPartitionReplica> replicas, final DescribeReplicaLogDirsOptions options)\n
    '''
def createPartitions():
    '''returns CreatePartitionsResult\n\n
    createPartitions(final Map<String, NewPartitions> newPartitions, final CreatePartitionsOptions options)\n
    '''
def deleteRecords():
    '''returns DeleteRecordsResult\n\n
    deleteRecords(final Map<TopicPartition, RecordsToDelete> recordsToDelete, final DeleteRecordsOptions options)\n
    '''
def provide():
    '''returns Node\n\n
    provide()\n
    provide()\n
    provide()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
