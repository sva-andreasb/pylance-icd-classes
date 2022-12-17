def ():
    '''returns HAManagerImpl\n\n
    (final Coordinator coordinator, final String coreGroupName, final String serverName, final MessageCache cache, final int isAliveTime, final boolean defaultCoreStack)\n
    '''
def getCoordinator():
    '''returns Coordinator\n\n
    getCoordinator()\n
    '''
def joinGroup():
    '''returns HAGroup\n\n
    joinGroup(final GroupName groupName, final Map memberProps, final HAGroupCallback groupCallback)\n
    '''
def getServerID():
    '''returns String\n\n
    getServerID()\n
    '''
def getStateForAllGroups():
    '''returns None\n\n
    getStateForAllGroups(final ReportStateMsg[] messages)\n
    getStateForAllGroups(final ReportClusterProcessStateMsg[] messages)\n
    '''
def setPMI():
    '''returns None\n\n
    setPMI(final HAManagerPerf pmi)\n
    '''
def groupStateUpdate():
    '''returns None\n\n
    groupStateUpdate(final GroupMemberActivationCmdMsg msg)\n
    '''
def groupMembershipUpdate():
    '''returns None\n\n
    groupMembershipUpdate(final GroupUpdateMsg msg)\n
    '''
def onMessage():
    '''returns None\n\n
    onMessage(final String sender, final GroupLocalMessage msg)\n
    '''
def alarm():
    '''returns None\n\n
    alarm(final Object alarmContext)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
