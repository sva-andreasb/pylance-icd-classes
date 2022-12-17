def ():
    '''returns ViewSynchronousHAGroup\n\n
    (final GroupManager groupManager, final GroupName groupName, final Map memberProperties, final String dataStackName, final HAGroupCallback haGroupCallback)\n
    '''
def getGroupName():
    '''returns GroupName\n\n
    getGroupName()\n
    '''
def getMemberName():
    '''returns GroupMemberId\n\n
    getMemberName()\n
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
    sendMessage(final MsgQoS msgQos, final GroupMemberId destination, final byte[] message)\n
    sendMessage(final MsgQoS msgQos, final GroupMemberId[] destinations, final byte[] message)\n
    sendMessage(final MsgQoS msgQos, final byte[] message)\n
    '''
def isHardwareQuorumEnforced():
    '''returns boolean\n\n
    isHardwareQuorumEnforced()\n
    '''
def memberMayActivate():
    '''returns None\n\n
    memberMayActivate(final GroupName groupName)\n
    '''
def memberMayActivateCancelled():
    '''returns None\n\n
    memberMayActivateCancelled(final GroupName groupName)\n
    '''
def memberIsActivated():
    '''returns None\n\n
    memberIsActivated(final GroupName groupName, final AsynchOperationComplete callback, final Object callbackContext)\n
    '''
def memberDeactivate():
    '''returns None\n\n
    memberDeactivate(final GroupName groupName, final AsynchOperationComplete callback, final Object callbackContext)\n
    '''
def membershipChanged():
    '''returns None\n\n
    membershipChanged(final GroupName groupName, final GroupMemberId[] members)\n
    '''
def isAlive():
    '''returns boolean\n\n
    isAlive(final GroupName groupName)\n
    '''
def onMessage():
    '''returns None\n\n
    onMessage(final GroupMemberId sender, final byte[] message)\n
    '''
def dataStackMessageReceived():
    '''returns None\n\n
    dataStackMessageReceived(final GroupMemberId sender, final String channel, final byte[] message)\n
    '''
def dataStackMembershipChanged():
    '''returns None\n\n
    dataStackMembershipChanged(final GroupMemberId[] members)\n
    '''
def dataStackEvent():
    '''returns None\n\n
    dataStackEvent(final DataStackEvent dataStackEvent)\n
    '''
def dataStackViewAboutToChange():
    '''returns None\n\n
    dataStackViewAboutToChange()\n
    '''
