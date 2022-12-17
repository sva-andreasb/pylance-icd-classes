def ():
    '''returns CoordinatorJMXImpl\n\n
    (final CoordinatorImpl coordinator, final CoordinatorComponentImpl coordinatorComponent, final boolean singleServerMode)\n
    '''
def supportsDynamicCGReload():
    '''returns boolean\n\n
    supportsDynamicCGReload()\n
    '''
def isInSingleServerMode():
    '''returns boolean\n\n
    isInSingleServerMode()\n
    '''
def getCoreGroupInfo():
    '''returns CoreGroupInfo\n\n
    getCoreGroupInfo()\n
    '''
def queryGroupState():
    '''returns GroupData[]\n\n
    queryGroupState(final String groupNameProps, final Integer maxGroupsPerCoordinator, final Boolean includeMemberData)\n
    '''
def retrieveGroupMembers():
    '''returns GroupMemberData[]\n\n
    retrieveGroupMembers(final GroupName groupName)\n
    '''
def queryCountActiveGroupsOnServers():
    '''returns ServerWithActiveGroups[]\n\n
    queryCountActiveGroupsOnServers(final String groupNameProps, final Integer maxGroupsPerCoordinator)\n
    '''
def enableMember():
    '''returns None\n\n
    enableMember(final GroupName groupName, final String nodeName, final String serverName)\n
    '''
def disableMember():
    '''returns None\n\n
    disableMember(final GroupName groupName, final String nodeName, final String serverName)\n
    '''
def activateMember():
    '''returns None\n\n
    activateMember(final GroupName groupName, final String nodeName, final String serverName)\n
    '''
def deactivateMember():
    '''returns None\n\n
    deactivateMember(final GroupName groupName, final String nodeName, final String serverName)\n
    '''
def enableGroup():
    '''returns None\n\n
    enableGroup(final GroupName groupName)\n
    '''
def disableGroup():
    '''returns None\n\n
    disableGroup(final GroupName groupName)\n
    '''
def createGroupName():
    '''returns GroupName\n\n
    createGroupName(final String groupNameProps)\n
    '''
def migrateActiveMember():
    '''returns None\n\n
    migrateActiveMember(final GroupName groupName, final String currActiveMemberNodeName, final String currActiveMemberServerName, final String futureActiveMemberNodeName, final String futureActiveMemberServerName)\n
    '''
def resolvePolicyForGroup():
    '''returns String[]\n\n
    resolvePolicyForGroup(final GroupName groupName)\n
    '''
def runPolicy():
    '''returns None\n\n
    runPolicy(final GroupName groupName)\n
    '''
def resetQuorumProviders():
    '''returns None\n\n
    resetQuorumProviders()\n
    '''
def updateRuntimeConfig():
    '''returns None\n\n
    updateRuntimeConfig(final Serializable state)\n
    '''
def getCoreGroupConfig():
    '''returns Serializable\n\n
    getCoreGroupConfig(final String coreGroupName)\n
    '''
