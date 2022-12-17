wlmID = "String  \"com.ibm.ws.wlm.clusterMgr\""
ClusterMgrMBeanType = "String  \"ClusterMgr\""
ServerMBeanType = "String  \"Server\""
TYPE_ACTIVATE_CLUSTER = "String  \"cluster.changed.activate\""
TYPE_DEACTIVATE_CLUSTER = "String  \"cluster.changed.deactivate\""
TYPE_MEMBER_ADDED = "String  \"cluster.member.added\""
TYPE_MEMBER_REMOVED = "String  \"cluster.member.removed\""
KEY_CLUSTER_NAME = "String  \"clusterName\""
def ():
    '''returns ClusterMgr\n\n
    ()\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def retrieveClusters():
    '''returns ClusterData[]\n\n
    retrieveClusters()\n
    '''
def retrieveCluster():
    '''returns ClusterData\n\n
    retrieveCluster(final String clusterName)\n
    '''
def retrieveClusterByMember():
    '''returns ClusterData\n\n
    retrieveClusterByMember(final String memberName, final String nodeName)\n
    '''
def getServerState():
    '''returns String\n\n
    getServerState(final String memberName, final String nodeName)\n
    '''
def getClusterState():
    '''returns String\n\n
    getClusterState(final String clusterName)\n
    '''
def configChanged():
    '''returns None\n\n
    configChanged(final ConfigRepositoryEvent event)\n
    '''
def handleNotification():
    '''returns None\n\n
    handleNotification(final Notification notification, final Object handback)\n
    '''
