def ():
    '''returns ApplicationMessage\n\n
    (final GroupManager groupManager, final GroupName groupName, final Map memberProps, final ManagedGroupData[] managedGroupDataArray)\n
    (final ManagedGroupData managedGroupData, final String isManagerKey)\n
    (final String mgdName, final byte[] message)\n
    (final GroupMemberId sender, final byte[] message)\n
    '''
def getGroupName():
    '''returns GroupName\n\n
    getGroupName()\n
    '''
def getMemberName():
    '''returns GroupMemberId\n\n
    getMemberName()\n
    '''
def isActive():
    '''returns boolean\n\n
    isActive(final String mgdName)\n
    '''
def getState():
    '''returns MemberStateEnum\n\n
    getState(final String mgdName)\n
    '''
def stop():
    '''returns None\n\n
    stop()\n
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
def isAlive():
    '''returns boolean\n\n
    isAlive(final GroupName groupName)\n
    '''
def membershipChanged():
    '''returns None\n\n
    membershipChanged(final GroupName groupName, final GroupMemberId[] members)\n
    '''
def onMessage():
    '''returns None\n\n
    onMessage(final GroupMemberId sender, final byte[] msg)\n
    '''
def viewAboutToChange():
    '''returns None\n\n
    viewAboutToChange()\n
    '''
def sendMessage():
    '''returns None\n\n
    sendMessage(final String mgdName, final GroupMemberId destination, final byte[] message)\n
    sendMessage(final String mgdName, final byte[] message)\n
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
