def ClusterMemberServiceImpl():
'''public ClusterMemberServiceImpl()
'''
pass
def initialize():
'''public void initialize(final Object config)
'''
pass
def start():
'''public void start()
'''
pass
def defineLocalScopedData():
'''public EndPoint defineLocalScopedData(final Identity dataIdentity, final byte[] data)
'''
pass
def defineMemberScopedData():
'''public EndPoint defineMemberScopedData(final Identity dataIdentity, final byte[] data)
'''
pass
def undefineMemberScopedData():
'''public byte[] undefineMemberScopedData(final EndPoint endpoint)
'''
pass
def undefineLocalScopedData():
'''public byte[] undefineLocalScopedData(final EndPoint endpoint)
'''
pass
def joinCluster():
'''public void joinCluster(final Identity clusterIdentity)
public void joinCluster(final Identity[] hierarchicalClusterIdentities)
'''
pass
def disjoinCluster():
'''public void disjoinCluster(final Identity clusterIdentity)
public void disjoinCluster(final Identity[] hierarchicalClusterIdentities)
'''
pass
def getServerClusterContextListener():
'''public ServerClusterContext getServerClusterContextListener()
'''
pass
def registerDistributor():
'''public void registerDistributor(final ClusterContextDistributor distributor, final Identity identity)
'''
pass
def defineAttribute():
'''public void defineAttribute(final String attribute)
'''
pass
def undefineAttribute():
'''public void undefineAttribute(final String attribute)
'''
pass
def getIdentity():
'''public Identity getIdentity()
'''
pass
def getActiveClusterSetKey():
'''public DescriptionKey getActiveClusterSetKey()
'''
pass
def setACSWaitTime():
'''public void setACSWaitTime(final int time)
'''
pass
def setupForUT():
'''public IdentityMap setupForUT()
'''
pass
