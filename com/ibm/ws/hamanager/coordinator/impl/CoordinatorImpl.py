def ():
    '''returns RebuildTimeoutAction\n\n
    (final CoreStackInfo csInfo, final CoreStackMemberInfo[] csMembers, final CoreStackListener csl, final StateExchangeListener sel, final StateBlob blob, final boolean defaultCoreStack, final Set bridgeMembers)\n
    ()\n
    '''
def getCoreStackFactory():
    '''returns CoreStackFactory\n\n
    getCoreStackFactory()\n
    '''
def getAgentClassFactory():
    '''returns AgentClassFactory\n\n
    getAgentClassFactory()\n
    '''
def getManagedGroupDataFactory():
    '''returns ManagedGroupDataFactory\n\n
    getManagedGroupDataFactory()\n
    '''
def getBulletinboardFactory():
    '''returns BulletinBoardFactory\n\n
    getBulletinboardFactory()\n
    '''
def getGroupManager():
    '''returns GroupManager\n\n
    getGroupManager()\n
    '''
def addBulletinBoardListener():
    '''returns None\n\n
    addBulletinBoardListener(final BulletinBoardListener listener)\n
    '''
def removeBulletinBoardListener():
    '''returns None\n\n
    removeBulletinBoardListener(final BulletinBoardListener listener)\n
    '''
def updateCoreStackMembers():
    '''returns int\n\n
    updateCoreStackMembers(final CoreStackMemberInfo[] members, final int context)\n
    '''
def addDefined():
    '''returns int\n\n
    addDefined(final CoreStackMemberInfo member, final int context)\n
    '''
def removeDefined():
    '''returns int\n\n
    removeDefined(final String memberName, final int context)\n
    '''
def updateProtocolVersions():
    '''returns None\n\n
    updateProtocolVersions(final Map protocols)\n
    '''
def transparentBridgeFailoverEnabled():
    '''returns boolean\n\n
    transparentBridgeFailoverEnabled()\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def getCoreStackPropertyProvider():
    '''returns CoreStackPropertyProvider\n\n
    getCoreStackPropertyProvider()\n
    '''
def getQuorumProviderFactory():
    '''returns QuorumProviderFactory\n\n
    getQuorumProviderFactory()\n
    '''
def disableQuorumDetection():
    '''returns None\n\n
    disableQuorumDetection()\n
    '''
def requestCheckGroup():
    '''returns None\n\n
    requestCheckGroup(final GroupName groupName)\n
    '''
def setClusterStateHolder():
    '''returns None\n\n
    setClusterStateHolder(final RPCResponseCollector holder)\n
    '''
def setPMI():
    '''returns None\n\n
    setPMI(final HAManagerPerf pmi)\n
    '''
def getPMI():
    '''returns HAManagerPerf\n\n
    getPMI()\n
    '''
def getCoreGroupName():
    '''returns String\n\n
    getCoreGroupName()\n
    '''
def getServerName():
    '''returns String\n\n
    getServerName()\n
    '''
def getPolicyManager():
    '''returns HAPolicyManager\n\n
    getPolicyManager()\n
    '''
def getWLMProvider():
    '''returns WorkloadManagementProvider\n\n
    getWLMProvider()\n
    '''
def setHAManagerCallback():
    '''returns None\n\n
    setHAManagerCallback(final HAManagerCoordinatorCallback callback)\n
    '''
def getJVMController():
    '''returns JVMController\n\n
    getJVMController()\n
    '''
def sendMessage():
    '''returns None\n\n
    sendMessage(final String destination, final HAMMessage msg)\n
    sendMessage(final String[] destinations, final HAMMessage msg)\n
    '''
def sendGroupMessage():
    '''returns None\n\n
    sendGroupMessage(final MsgQoS qos, final String[] destinations, final GroupLocalMessage msg)\n
    '''
def isHardwareQuorumEnforced():
    '''returns boolean\n\n
    isHardwareQuorumEnforced(final GroupName gn)\n
    '''
def createDataStack():
    '''returns DataStack\n\n
    createDataStack(final String name, final boolean usesVS, final HAGroupImpl haGroup, final DataStackCallback callback, final SyncDataReqCallback sdrcallback, final String[] members)\n
    '''
def getCurrentViewMembers():
    '''returns String[]\n\n
    getCurrentViewMembers()\n
    '''
def isDefaultCoreStack():
    '''returns boolean\n\n
    isDefaultCoreStack()\n
    '''
def stopDefaultCoreStack():
    '''returns None\n\n
    stopDefaultCoreStack()\n
    '''
def distributeDefaultCoreStackConfiguration():
    '''returns None\n\n
    distributeDefaultCoreStackConfiguration(final StateBlob config)\n
    '''
def alarm():
    '''returns None\n\n
    alarm(final Object alarmContext)\n
    '''
