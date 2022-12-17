ClusterMBeanType = "String  \"Cluster\""
wlmID = "String  \"com.ibm.ws.wlm.cluster\""
TYPE_USABLE = "String  \"cluster.member.usable\""
TYPE_UNUSABLE = "String  \"cluster.member.unusable\""
TYPE_CLUSTER_CONTROLLER_REGISTERED = "String  \"websphere.cluster.controller.registered\""
TYPE_CLUSTER_BACKUP_SET = "String  \"websphere.cluster.backup.set\""
def ():
    '''returns Cluster\n\n
    ()\n
    (final ClusterData lwCluster)\n
    '''
def activate():
    '''returns None\n\n
    activate()\n
    '''
def deactivate():
    '''returns None\n\n
    deactivate()\n
    '''
def getClusterName():
    '''returns String\n\n
    getClusterName()\n
    '''
def getPreferLocal():
    '''returns Boolean\n\n
    getPreferLocal()\n
    '''
def getWLCid():
    '''returns String\n\n
    getWLCid()\n
    '''
def getClusterMembers():
    '''returns ClusterMemberData[]\n\n
    getClusterMembers()\n
    '''
def getClusterMember():
    '''returns ClusterMemberData\n\n
    getClusterMember(final String memberName, final String nodeName)\n
    '''
def getWeightTable():
    '''returns ClusterWeightTableEntry[]\n\n
    getWeightTable()\n
    '''
def getWeightTableEntry():
    '''returns ClusterWeightTableEntry\n\n
    getWeightTableEntry(final String memberName, final String nodeName)\n
    '''
def getClusterType():
    '''returns String\n\n
    getClusterType()\n
    '''
def register():
    '''returns Long\n\n
    register(final String wlcName)\n
    '''
def refresh():
    '''returns ClusterData\n\n
    refresh()\n
    '''
def getBackupName():
    '''returns String\n\n
    getBackupName()\n
    '''
def getBackupBootstrapHost():
    '''returns String\n\n
    getBackupBootstrapHost()\n
    '''
def getBackupBootstrapPort():
    '''returns Integer\n\n
    getBackupBootstrapPort()\n
    '''
def receiveClusterDescription():
    '''returns None\n\n
    receiveClusterDescription(final ClusterDescription cluster, final Object handBack)\n
    '''
def setAvailable():
    '''returns None\n\n
    setAvailable(final String memberName, final String nodeName)\n
    '''
def setUnavailable():
    '''returns None\n\n
    setUnavailable(final String memberName, final String nodeName)\n
    '''
def getAvailable():
    '''returns Boolean\n\n
    getAvailable(final String memberName, final String nodeName)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def receiveBackupCellName():
    '''returns None\n\n
    receiveBackupCellName(final String cellName)\n
    '''
def exportRouteTable():
    '''returns String\n\n
    exportRouteTable()\n
    '''
def removeRouteTable():
    '''returns boolean\n\n
    removeRouteTable()\n
    '''
def handleNotification():
    '''returns None\n\n
    handleNotification(final DescriptionKey deskey, final String type, final Object data, final Object handback)\n
    handleNotification(final Notification notification, final Object handback)\n
    '''
def getState():
    '''returns String\n\n
    getState()\n
    '''
def start():
    '''returns None\n\n
    start()\n
    '''
def stop():
    '''returns None\n\n
    stop()\n
    '''
def stopImmediate():
    '''returns None\n\n
    stopImmediate()\n
    '''
def rippleStart():
    '''returns None\n\n
    rippleStart()\n
    '''
def dumpClusterInfo():
    '''returns String\n\n
    dumpClusterInfo()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
