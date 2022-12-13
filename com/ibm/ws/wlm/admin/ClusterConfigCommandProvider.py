CREATE_CLUSTER_TASK_NAME = "String  \"createCluster\""
CREATE_CLUSTER_MEMBER_TASK_NAME = "String  \"createClusterMember\""
DELETE_CLUSTER_TASK_NAME = "String  \"deleteCluster\""
DELETE_CLUSTER_MEMBER_TASK_NAME = "String  \"deleteClusterMember\""
LIST_CLUSTER_MEMBER_TEMPLATES_TASK_NAME = "String  \"listClusterMemberTemplates\""
UPDATE_CLUSTER_TASK_NAME = "String  \"updateCluster\""
UPDATE_CLUSTER_MEMBER_WEIGHTS_TASK_NAME = "String  \"updateClusterMemberWeights\""
CLUSTER_CONFIG_STEP_NAME = "String  \"clusterConfig\""
REPLICATION_DOMAIN_STEP_NAME = "String  \"replicationDomain\""
CONVERT_SERVER_STEP_NAME = "String  \"convertServer\""
MEMBER_CONFIG_STEP_NAME = "String  \"memberConfig\""
FIRST_MEMBER_STEP_NAME = "String  \"firstMember\""
REPLICATOR_ENTRY_STEP_NAME = "String  \"replicatorEntry\""
DELETE_REPLICATOR_ENTRY_STEP_NAME = "String  \"deleteRepEntry\""
REPLICATION_ENTRY_STEP_NAME = "String  \"replicatorEntry\""
PREFER_LOCAL_STEP_NAME = "String  \"preferLocal\""
TRANSACTION_LOG_RECOVERY_STEP_NAME = "String  \"transactionLogRecovery\""
BOUNDING_NODE_GROUP_NAME_STEP_NAME = "String  \"boundingNodeGroupName\""
MEMBERS_STEP_NAME = "String  \"members\""
def createCommand():
    '''    public AbstractAdminCommand createCommand(final CommandMetadata metadata)
    '''
def loadCommand():
    '''    public AbstractAdminCommand loadCommand(final CommandData cmdData)
    '''
def createCommandStep():
    '''    public AbstractCommandStep createCommandStep(final AbstractTaskCommand taskCmd, final String stepName)
    '''
def loadCommandStep():
    '''    public AbstractCommandStep loadCommandStep(final AbstractTaskCommand taskCmd, final CommandStepData stepData)
    '''
