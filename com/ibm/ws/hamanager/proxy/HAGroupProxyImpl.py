def getGroupName():
    '''returns GroupName\n\n
    getGroupName()\n
    '''
def getMemberName():
    '''returns GroupMemberId\n\n
    getMemberName()\n
    '''
def getMemberState():
    '''returns GroupMemberState\n\n
    getMemberState()\n
    '''
def leave():
    '''returns None\n\n
    leave()\n
    '''
def setVersionString():
    '''returns None\n\n
    setVersionString(final String version)\n
    '''
def getVersionString():
    '''returns String\n\n
    getVersionString()\n
    '''
def enableMember():
    '''returns None\n\n
    enableMember()\n
    '''
def disableMember():
    '''returns None\n\n
    disableMember(final String reason)\n
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
