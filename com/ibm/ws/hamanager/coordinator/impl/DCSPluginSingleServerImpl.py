def getViewId():
    '''returns Comparable\n\n
    getViewId()\n
    '''
def setStateExchangeBlob():
    '''returns None\n\n
    setStateExchangeBlob(final StateBlob blob)\n
    '''
def addDefined():
    '''returns int\n\n
    addDefined(final CoreStackMemberInfo member, final int context)\n
    '''
def removeDefined():
    '''returns int\n\n
    removeDefined(final String memberName, final int context)\n
    '''
def updateCoreStackMembership():
    '''returns int\n\n
    updateCoreStackMembership(final CoreStackMemberInfo[] members, final int context)\n
    '''
def updateProtocolVersion():
    '''returns None\n\n
    updateProtocolVersion(final String version)\n
    '''
def getCoreGroupMembers():
    '''returns Set\n\n
    getCoreGroupMembers()\n
    '''
def setSharedSecret():
    '''returns None\n\n
    setSharedSecret(final String updatedSecret)\n
    '''
def sendGroupMessage():
    '''returns None\n\n
    sendGroupMessage(final MsgQoS qos, final String[] destinations, final GroupLocalMessage msg)\n
    '''
def terminateCoreStack():
    '''returns None\n\n
    terminateCoreStack()\n
    '''
def getMemberProvider():
    '''returns MemberInfoManager\n\n
    getMemberProvider()\n
    '''
def createDataStack():
    '''returns DataStack\n\n
    createDataStack(final String name, final boolean usesVS, final HAGroupImpl haGroup, final DataStackCallback callback, final SyncDataReqCallback sdrcallback, final String[] members)\n
    '''
def deleteDataStack():
    '''returns None\n\n
    deleteDataStack(final String name)\n
    '''
def sendAttentionReqMsg():
    '''returns None\n\n
    sendAttentionReqMsg(final String msgID)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
