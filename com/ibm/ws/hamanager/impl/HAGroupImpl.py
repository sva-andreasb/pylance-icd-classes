def ():
    '''returns HAGroupImpl\n\n
    (final HAManagerImpl hAManagerImpl, final GroupName groupName, final HAPolicyRule rule, final MemberDataImpl memberData, final HAGroupCallback groupCallback)\n
    '''
def deleteDataStack():
    '''returns None\n\n
    deleteDataStack()\n
    '''
def success():
    '''returns None\n\n
    success(final Object callbackContext, final Object data)\n
    '''
def failed():
    '''returns None\n\n
    failed(final Object callbackContext, final String reason, final Object data)\n
    failed(final Object callbackContext, final String reason, final Throwable t, final Object data)\n
    '''
def getGroupName():
    '''returns GroupName\n\n
    getGroupName()\n
    '''
def getMemberName():
    '''returns GroupMemberId\n\n
    getMemberName()\n
    '''
def getVersionString():
    '''returns String\n\n
    getVersionString()\n
    '''
def setVersionString():
    '''returns None\n\n
    setVersionString(final String v)\n
    '''
def leave():
    '''returns None\n\n
    leave()\n
    '''
def enableMember():
    '''returns None\n\n
    enableMember()\n
    '''
def disableMember():
    '''returns None\n\n
    disableMember(final String reason)\n
    '''
def createDataStack():
    '''returns DataStack\n\n
    createDataStack(final String name, final boolean usesVS, final DataStackCallback callback)\n
    '''
def createSyncDataStack():
    '''returns SyncDataStack\n\n
    createSyncDataStack(final String name, final boolean usesVS, final DataStackCallback callback, final SyncDataReqCallback sdrcallback)\n
    '''
def sendMessage():
    '''returns None\n\n
    sendMessage(final MsgQoS qos, final GroupMemberId destination, final byte[] msg)\n
    sendMessage(final MsgQoS qos, final GroupMemberId[] destinations, final byte[] msg)\n
    sendMessage(final MsgQoS qos, final byte[] msg)\n
    '''
def isHardwareQuorumEnforced():
    '''returns boolean\n\n
    isHardwareQuorumEnforced()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def doCallback():
    '''returns None\n\n
    doCallback()\n
    '''
def getQueue():
    '''returns int\n\n
    getQueue(final int numberOfQueues)\n
    '''
def getUserClassName():
    '''returns String\n\n
    getUserClassName()\n
    '''
