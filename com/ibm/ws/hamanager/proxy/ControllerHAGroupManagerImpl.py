def ():
    '''returns ControllerHAGroupManagerImpl\n\n
    (final CoreStack cs)\n
    '''
def getServerName():
    '''returns String\n\n
    getServerName()\n
    '''
def createGroupName():
    '''returns GroupName\n\n
    createGroupName(final Map groupProperties)\n
    '''
def getMemberName():
    '''returns GroupMemberId\n\n
    getMemberName(final GroupName groupName)\n
    '''
def getMemberState():
    '''returns GroupMemberState\n\n
    getMemberState(final GroupName groupName)\n
    '''
def setVersionString():
    '''returns None\n\n
    setVersionString(final GroupName groupName, final String version)\n
    '''
def getVersionString():
    '''returns String\n\n
    getVersionString(final GroupName groupName)\n
    '''
def enableMember():
    '''returns None\n\n
    enableMember(final GroupName groupName)\n
    '''
def disableMember():
    '''returns None\n\n
    disableMember(final GroupName groupName, final String reason)\n
    '''
def sendMessage():
    '''returns None\n\n
    sendMessage(final GroupName groupName, final MsgQoS qos, final GroupMemberId destination, final byte[] msg)\n
    sendMessage(final GroupName groupName, final MsgQoS qos, final GroupMemberId[] destinations, final byte[] msg)\n
    sendMessage(final GroupName groupName, final MsgQoS qos, final byte[] msg)\n
    '''
def isHardwareQuorumEnforced():
    '''returns boolean\n\n
    isHardwareQuorumEnforced(final GroupName groupName)\n
    '''
def success():
    '''returns None\n\n
    success(final GroupName groupName, final Object data, final int sequenceNumber)\n
    '''
def failed():
    '''returns None\n\n
    failed(final GroupName groupName, final String reason, final Object data, final int sequenceNumber)\n
    failed(final GroupName groupName, final String message, final Throwable t, final Object data, final int sequenceNumber)\n
    '''
