def ():
    '''returns ClusterManagementImpl\n\n
    (final boolean distribute)\n
    '''
def createClusterMember():
    '''returns Identity\n\n
    createClusterMember(final String cellName, final String nodeName, String hostName, final String memberName)\n
    '''
def joinCluster():
    '''returns None\n\n
    joinCluster(final Identity clusterIdentity, final Identity[] memberIdentities)\n
    joinCluster(final Identity[] clusterIdentities, final Identity[] memberIdentities)\n
    '''
def disjoinCluster():
    '''returns None\n\n
    disjoinCluster(final Identity[] clusterIdentities, final Identity[] memberIdentities)\n
    '''
def defineClusterScopedData():
    '''returns EndPoint\n\n
    defineClusterScopedData(final Identity clusterIdentity, final Identity dataIdentity, final byte[] data)\n
    '''
def defineMemberScopedData():
    '''returns EndPoint\n\n
    defineMemberScopedData(final Identity memberIdentity, final Identity dataIdentity, final byte[] data)\n
    '''
def getDesiredWeight():
    '''returns int\n\n
    getDesiredWeight(final Identity cluster, final Identity member)\n
    '''
def setDesiredWeight():
    '''returns None\n\n
    setDesiredWeight(final Identity clusterIdentity, final Identity memberIdentity, final int weight)\n
    '''
def defineAttribute():
    '''returns None\n\n
    defineAttribute(final Identity identity, final String attribute)\n
    '''
def undefineAttribute():
    '''returns None\n\n
    undefineAttribute(final Identity identity, final String attribute)\n
    '''
def getAttributes():
    '''returns Set\n\n
    getAttributes(final Identity identity)\n
    '''
def setClusterAssociation():
    '''returns None\n\n
    setClusterAssociation(final Identity cluster, final Identity member)\n
    '''
def setCARWaitTime():
    '''returns None\n\n
    setCARWaitTime(final int time)\n
    '''
