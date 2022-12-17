def getAgentClass():
    '''returns AgentClass\n\n
    getAgentClass()\n
    '''
def getInstanceId():
    '''returns Map\n\n
    getInstanceId()\n
    '''
def getPrimaryId():
    '''returns GroupMemberId\n\n
    getPrimaryId()\n
    '''
def getHAGroup():
    '''returns HAGroup\n\n
    getHAGroup()\n
    '''
def getMemberName():
    '''returns GroupMemberId\n\n
    getMemberName()\n
    '''
def isPrimary():
    '''returns boolean\n\n
    isPrimary()\n
    '''
def getMembers():
    '''returns GroupMemberId[]\n\n
    getMembers()\n
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
def membershipChanged():
    '''returns None\n\n
    membershipChanged(final GroupName groupName, final GroupMemberId[] members)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
