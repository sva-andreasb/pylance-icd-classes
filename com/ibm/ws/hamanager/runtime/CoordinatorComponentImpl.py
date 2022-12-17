def ():
    '''returns CoordinatorComponentImpl\n\n
    ()\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final Object cfg)\n
    '''
def start():
    '''returns None\n\n
    start()\n
    '''
def stop():
    '''returns None\n\n
    stop()\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def getCoreStackFactory():
    '''returns CoreStackFactory\n\n
    getCoreStackFactory()\n
    '''
def getAgentClassFactory():
    '''returns AgentClassFactory\n\n
    getAgentClassFactory()\n
    '''
def getBulletinboardFactory():
    '''returns BulletinBoardFactory\n\n
    getBulletinboardFactory()\n
    '''
def addBulletinBoardListener():
    '''returns None\n\n
    addBulletinBoardListener(final BulletinBoardListener listener)\n
    '''
def removeBulletinBoardListener():
    '''returns None\n\n
    removeBulletinBoardListener(final BulletinBoardListener listener)\n
    '''
def getManagedGroupDataFactory():
    '''returns ManagedGroupDataFactory\n\n
    getManagedGroupDataFactory()\n
    '''
def getGroupManager():
    '''returns GroupManager\n\n
    getGroupManager()\n
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
def bridgeStateSynchronized():
    '''returns None\n\n
    bridgeStateSynchronized(final Set subjectsCurrentlyOwned)\n
    '''
def bridgeStateUnsychronized():
    '''returns None\n\n
    bridgeStateUnsychronized(final Set bridgesRunningInLocalAPG)\n
    '''
def transparentBridgeFailoverEnabled():
    '''returns boolean\n\n
    transparentBridgeFailoverEnabled()\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def viewAboutToChange():
    '''returns None\n\n
    viewAboutToChange()\n
    '''
def viewChangeCompleted():
    '''returns None\n\n
    viewChangeCompleted(final String[] members)\n
    '''
def changeDefinedCompleted():
    '''returns None\n\n
    changeDefinedCompleted(final int context)\n
    '''
def terminated():
    '''returns None\n\n
    terminated(final int reason)\n
    '''
def stateReceived():
    '''returns None\n\n
    stateReceived(final StateBlob blob)\n
    '''
def getServerProperty():
    '''returns String\n\n
    getServerProperty(final String serverName, final String name)\n
    '''
def getCoreGroupProperty():
    '''returns String\n\n
    getCoreGroupProperty(final String name)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
