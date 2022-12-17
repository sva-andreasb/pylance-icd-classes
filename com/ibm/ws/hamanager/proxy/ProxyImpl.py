def start():
    '''returns None\n\n
    start()\n
    '''
def getCoreStackFactory():
    '''returns CoreStackFactory\n\n
    getCoreStackFactory()\n
    '''
def getBulletinboardFactory():
    '''returns BulletinBoardFactory\n\n
    getBulletinboardFactory()\n
    '''
def getGroupManager():
    '''returns GroupManager\n\n
    getGroupManager()\n
    '''
def getAgentClassFactory():
    '''returns AgentClassFactory\n\n
    getAgentClassFactory()\n
    '''
def getManagedGroupDataFactory():
    '''returns ManagedGroupDataFactory\n\n
    getManagedGroupDataFactory()\n
    '''
def addBulletinBoardListener():
    '''returns None\n\n
    addBulletinBoardListener(final BulletinBoardListener listener)\n
    '''
def removeBulletinBoardListener():
    '''returns None\n\n
    removeBulletinBoardListener(final BulletinBoardListener listener)\n
    '''
def addDefined():
    '''returns int\n\n
    addDefined(final CoreStackMemberInfo member, final int context)\n
    '''
def removeDefined():
    '''returns int\n\n
    removeDefined(final String memberName, final int context)\n
    '''
def updateCoreStackMembers():
    '''returns int\n\n
    updateCoreStackMembers(final CoreStackMemberInfo[] members, final int context)\n
    '''
def updateProtocolVersions():
    '''returns None\n\n
    updateProtocolVersions(final Map map)\n
    '''
def bridgeStateUnsychronized():
    '''returns None\n\n
    bridgeStateUnsychronized(final Set bridgesRunningInLocalAPG)\n
    '''
def bridgeStateSynchronized():
    '''returns None\n\n
    bridgeStateSynchronized(final Set subjectsCurrentlyOwned)\n
    '''
def transparentBridgeFailoverEnabled():
    '''returns boolean\n\n
    transparentBridgeFailoverEnabled()\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
