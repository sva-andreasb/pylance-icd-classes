def ():
    '''returns ClusterDescriptionImpl\n\n
    (final DescriptionKey key)\n
    '''
def getDefinitionKey():
    '''returns String\n\n
    getDefinitionKey()\n
    '''
def setClusterScopedData():
    '''returns None\n\n
    setClusterScopedData(final DescriptionKey dataKey, final byte[] data)\n
    '''
def setClusterWeightTable():
    '''returns None\n\n
    setClusterWeightTable(final Map weightTable)\n
    '''
def setClusterWeightTableEntry():
    '''returns None\n\n
    setClusterWeightTableEntry(final DescriptionKey memberKey, final Integer weight)\n
    '''
def setClusterIdentityForWeightTable():
    '''returns None\n\n
    setClusterIdentityForWeightTable(final Identity parentClusterIdentity)\n
    '''
def removeClusterScopedData():
    '''returns None\n\n
    removeClusterScopedData(final DescriptionKey dataKey)\n
    '''
def addMember():
    '''returns None\n\n
    addMember(final ClusterMemberDescription member)\n
    addMember(final ClusterMemberDescription member, final int delay)\n
    '''
def removeMember():
    '''returns None\n\n
    removeMember(final ClusterMemberDescription member)\n
    removeMember(final ClusterMemberDescription member, final int delay)\n
    '''
def handleNotification():
    '''returns None\n\n
    handleNotification(final DescriptionKey key, final String type, final Object data, final Object handback)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def setMemento():
    '''returns None\n\n
    setMemento(final Description.Memento memento)\n
    '''
def setQuiesce():
    '''returns None\n\n
    setQuiesce(final Identity member)\n
    '''
def unsetQuiesce():
    '''returns None\n\n
    unsetQuiesce(final Identity member)\n
    '''
def getStructuralEpoch():
    '''returns long\n\n
    getStructuralEpoch()\n
    '''
def getClusterMembers():
    '''returns Iterator\n\n
    getClusterMembers()\n
    '''
def getMembers():
    '''returns Map\n\n
    getMembers()\n
    '''
def getMemberEntrySet():
    '''returns Set\n\n
    getMemberEntrySet()\n
    '''
def getWeightTable():
    '''returns Map\n\n
    getWeightTable()\n
    '''
def getWeightTableEntry():
    '''returns int\n\n
    getWeightTableEntry(final DescriptionKey memberKey)\n
    '''
def getBackupCluster():
    '''returns ClusterDescription\n\n
    getBackupCluster()\n
    '''
def getSelectionDescription():
    '''returns SelectionDescription\n\n
    getSelectionDescription()\n
    '''
def getInfluentialEpoch():
    '''returns long\n\n
    getInfluentialEpoch()\n
    '''
def getClusterScopedData():
    '''returns Set\n\n
    getClusterScopedData(final DescriptionKey dataKey)\n
    getClusterScopedData()\n
    '''
def isQuiesced():
    '''returns boolean\n\n
    isQuiesced(final Identity member)\n
    '''
def getQuiesceState():
    '''returns Map\n\n
    getQuiesceState()\n
    '''
def getState():
    '''returns byte\n\n
    getState()\n
    '''
def isLeaf():
    '''returns boolean\n\n
    isLeaf()\n
    '''
