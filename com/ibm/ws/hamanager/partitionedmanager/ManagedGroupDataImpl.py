def ():
    '''returns ManagedGroupDataImpl\n\n
    (final String mgdName, final boolean manager, final boolean fixedManagers, final boolean restrictToPreferred, final int numberOfManagers, final String[] preferredManagers, final ManagedGroupCallback managerEvents)\n
    '''
def setPartitionedManagerGroupImpl():
    '''returns None\n\n
    setPartitionedManagerGroupImpl(final PartitionedManagerGroupImpl partitionedManagerGroupImpl)\n
    '''
def resetPartitionedManagerGroupImpl():
    '''returns None\n\n
    resetPartitionedManagerGroupImpl()\n
    '''
def attachedToAPartitionedManagerGroup():
    '''returns boolean\n\n
    attachedToAPartitionedManagerGroup()\n
    '''
def isManager():
    '''returns boolean\n\n
    isManager()\n
    '''
def isFixedManagers():
    '''returns boolean\n\n
    isFixedManagers()\n
    '''
def isRestrictToPreferred():
    '''returns boolean\n\n
    isRestrictToPreferred()\n
    '''
def getNumberOfManagers():
    '''returns int\n\n
    getNumberOfManagers()\n
    '''
def getManagerSetName():
    '''returns String\n\n
    getManagerSetName()\n
    '''
def getPreferredManagers():
    '''returns Map\n\n
    getPreferredManagers()\n
    '''
def getManagerEvents():
    '''returns ManagedGroupCallback\n\n
    getManagerEvents()\n
    '''
def isActive():
    '''returns boolean\n\n
    isActive()\n
    '''
def getState():
    '''returns MemberStateEnum\n\n
    getState()\n
    '''
def sendMessage():
    '''returns None\n\n
    sendMessage(final GroupMemberId destination, final byte[] message)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
