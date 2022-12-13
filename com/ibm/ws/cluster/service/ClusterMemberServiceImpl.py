def ClusterMemberServiceImpl():
    '''public ClusterMemberServiceImpl()
    '''
def initialize():
    '''public void initialize(final Object config)
    '''
def start():
    '''public void start()
    '''
def defineLocalScopedData():
    '''public EndPoint defineLocalScopedData(final Identity dataIdentity, final byte[] data)
    '''
def defineMemberScopedData():
    '''public EndPoint defineMemberScopedData(final Identity dataIdentity, final byte[] data)
    '''
def undefineMemberScopedData():
    '''public byte[] undefineMemberScopedData(final EndPoint endpoint)
    '''
def undefineLocalScopedData():
    '''public byte[] undefineLocalScopedData(final EndPoint endpoint)
    '''
def joinCluster():
    '''public void joinCluster(final Identity clusterIdentity)
    public void joinCluster(final Identity[] hierarchicalClusterIdentities)
    '''
def disjoinCluster():
    '''public void disjoinCluster(final Identity clusterIdentity)
    public void disjoinCluster(final Identity[] hierarchicalClusterIdentities)
    '''
def getServerClusterContextListener():
    '''public ServerClusterContext getServerClusterContextListener()
    '''
def registerDistributor():
    '''public void registerDistributor(final ClusterContextDistributor distributor, final Identity identity)
    '''
def defineAttribute():
    '''public void defineAttribute(final String attribute)
    '''
def undefineAttribute():
    '''public void undefineAttribute(final String attribute)
    '''
def getIdentity():
    '''public Identity getIdentity()
    '''
def getActiveClusterSetKey():
    '''public DescriptionKey getActiveClusterSetKey()
    '''
def setACSWaitTime():
    '''public void setACSWaitTime(final int time)
    '''
def setupForUT():
    '''public IdentityMap setupForUT()
    '''
