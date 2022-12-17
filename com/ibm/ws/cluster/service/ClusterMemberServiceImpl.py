def ():
    '''returns ClusterMemberServiceImpl\n\n
    ()\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final Object config)\n
    '''
def start():
    '''returns None\n\n
    start()\n
    '''
def defineLocalScopedData():
    '''returns EndPoint\n\n
    defineLocalScopedData(final Identity dataIdentity, final byte[] data)\n
    '''
def defineMemberScopedData():
    '''returns EndPoint\n\n
    defineMemberScopedData(final Identity dataIdentity, final byte[] data)\n
    '''
def undefineMemberScopedData():
    '''returns byte[]\n\n
    undefineMemberScopedData(final EndPoint endpoint)\n
    '''
def undefineLocalScopedData():
    '''returns byte[]\n\n
    undefineLocalScopedData(final EndPoint endpoint)\n
    '''
def joinCluster():
    '''returns None\n\n
    joinCluster(final Identity clusterIdentity)\n
    joinCluster(final Identity[] hierarchicalClusterIdentities)\n
    '''
def disjoinCluster():
    '''returns None\n\n
    disjoinCluster(final Identity clusterIdentity)\n
    disjoinCluster(final Identity[] hierarchicalClusterIdentities)\n
    '''
def getServerClusterContextListener():
    '''returns ServerClusterContext\n\n
    getServerClusterContextListener()\n
    '''
def registerDistributor():
    '''returns None\n\n
    registerDistributor(final ClusterContextDistributor distributor, final Identity identity)\n
    '''
def defineAttribute():
    '''returns None\n\n
    defineAttribute(final String attribute)\n
    '''
def undefineAttribute():
    '''returns None\n\n
    undefineAttribute(final String attribute)\n
    '''
def getIdentity():
    '''returns Identity\n\n
    getIdentity()\n
    '''
def getActiveClusterSetKey():
    '''returns DescriptionKey\n\n
    getActiveClusterSetKey()\n
    '''
def setACSWaitTime():
    '''returns None\n\n
    setACSWaitTime(final int time)\n
    '''
def setupForUT():
    '''returns IdentityMap\n\n
    setupForUT()\n
    '''
