def _ids():
    '''returns String[]\n\n
    _ids()\n
    '''
def createGroupName():
    '''returns GroupName\n\n
    createGroupName(final Map map)\n
    '''
def disableMember():
    '''returns None\n\n
    disableMember(final GroupName groupName, final String s)\n
    '''
def enableMember():
    '''returns None\n\n
    enableMember(final GroupName groupName)\n
    '''
def failed():
    '''returns None\n\n
    failed(final GroupName groupName, final String s, final Object o, final int n)\n
    failed(final GroupName groupName, final String s, final Throwable t, final Object o, final int n)\n
    '''
def getMemberName():
    '''returns GroupMemberId\n\n
    getMemberName(final GroupName groupName)\n
    '''
def getMemberState():
    '''returns GroupMemberState\n\n
    getMemberState(final GroupName groupName)\n
    '''
def getServerName():
    '''returns String\n\n
    getServerName()\n
    '''
def getVersionString():
    '''returns String\n\n
    getVersionString(final GroupName groupName)\n
    '''
def isHardwareQuorumEnforced():
    '''returns boolean\n\n
    isHardwareQuorumEnforced(final GroupName groupName)\n
    '''
def joinGroup():
    '''returns None\n\n
    joinGroup(final String s, final GroupName groupName, final Map map, final boolean b, final int n)\n
    '''
def leave():
    '''returns None\n\n
    leave(final String s, final GroupName groupName)\n
    '''
def sendMessage():
    '''returns None\n\n
    sendMessage(final GroupName groupName, final MsgQoS msgQoS, final GroupMemberId groupMemberId, final byte[] array)\n
    sendMessage(final GroupName groupName, final MsgQoS msgQoS, final byte[] array)\n
    sendMessage(final GroupName groupName, final MsgQoS msgQoS, final GroupMemberId[] array, final byte[] array2)\n
    '''
def servantInitialized():
    '''returns None\n\n
    servantInitialized(final String s)\n
    '''
def setVersionString():
    '''returns None\n\n
    setVersionString(final GroupName groupName, final String s)\n
    '''
def success():
    '''returns None\n\n
    success(final GroupName groupName, final Object o, final int n)\n
    '''
