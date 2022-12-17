def getClassIdentifier():
    '''returns Map\n\n
    getClassIdentifier()\n
    '''
def getInstanceIdentifier():
    '''returns Map\n\n
    getInstanceIdentifier()\n
    '''
def getHAGroup():
    '''returns HAGroup\n\n
    getHAGroup()\n
    '''
def getMemberName():
    '''returns GroupMemberId\n\n
    getMemberName()\n
    '''
def createInstance():
    '''returns Agent\n\n
    createInstance(final Map agentId, final String channelName)\n
    '''
def getClassMembers():
    '''returns GroupMemberId[]\n\n
    getClassMembers()\n
    '''
def sendMessage():
    '''returns None\n\n
    sendMessage(final MsgQoS qos, final GroupMemberId destination, final byte[] msg)\n
    sendMessage(final MsgQoS qos, final GroupMemberId[] destinations, final byte[] msg)\n
    sendMessage(final MsgQoS qos, final byte[] msg)\n
    '''
def isAlive():
    '''returns boolean\n\n
    isAlive(final GroupName gn)\n
    '''
def memberDeactivate():
    '''returns None\n\n
    memberDeactivate(final GroupName groupName, final AsynchOperationComplete callback, final Object callbackContext)\n
    '''
def memberIsActivated():
    '''returns None\n\n
    memberIsActivated(final GroupName groupName, final AsynchOperationComplete callback, final Object callbackContext)\n
    '''
def memberMayActivate():
    '''returns None\n\n
    memberMayActivate(final GroupName groupName)\n
    '''
def memberMayActivateCancelled():
    '''returns None\n\n
    memberMayActivateCancelled(final GroupName groupName)\n
    '''
def onMessage():
    '''returns None\n\n
    onMessage(final GroupMemberId sender, final byte[] msg)\n
    '''
def membershipChanged():
    '''returns None\n\n
    membershipChanged(final GroupName groupName, final GroupMemberId[] members)\n
    '''
def dataStackMessageReceived():
    '''returns None\n\n
    dataStackMessageReceived(final GroupMemberId sender, final String channel, final byte[] message)\n
    '''
def dataStackMembershipChanged():
    '''returns None\n\n
    dataStackMembershipChanged(final GroupMemberId[] members)\n
    '''
def dataStackTerminated():
    '''returns None\n\n
    dataStackTerminated()\n
    '''
def dataStackEvent():
    '''returns None\n\n
    dataStackEvent(final DataStackEvent event)\n
    '''
def dataStackViewAboutToChange():
    '''returns None\n\n
    dataStackViewAboutToChange()\n
    '''
def toString():
    '''returns String\n\n
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
