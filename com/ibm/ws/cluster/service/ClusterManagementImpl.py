def ClusterManagementImpl():
    '''public ClusterManagementImpl(final boolean distribute)
    '''
def createClusterMember():
    '''public Identity createClusterMember(final String cellName, final String nodeName, String hostName, final String memberName)
    '''
def joinCluster():
    '''public void joinCluster(final Identity clusterIdentity, final Identity[] memberIdentities)
    public void joinCluster(final Identity[] clusterIdentities, final Identity[] memberIdentities)
    '''
def disjoinCluster():
    '''public synchronized void disjoinCluster(final Identity clusterIdentity, final Identity[] memberIdentities)
    public void disjoinCluster(final Identity[] clusterIdentities, final Identity[] memberIdentities)
    '''
def defineClusterScopedData():
    '''public EndPoint defineClusterScopedData(final Identity clusterIdentity, final Identity dataIdentity, final byte[] data)
    '''
def defineMemberScopedData():
    '''public EndPoint defineMemberScopedData(final Identity memberIdentity, final Identity dataIdentity, final byte[] data)
    '''
def undefineClusterScopedData():
    '''public synchronized void undefineClusterScopedData(final Identity clusterIdentity, final EndPoint data)
    '''
def undefineMemberScopedData():
    '''public synchronized void undefineMemberScopedData(final Identity memberIdentity, final EndPoint data)
    '''
def getDesiredWeight():
    '''public int getDesiredWeight(final Identity cluster, final Identity member)
    '''
def setDesiredWeight():
    '''public void setDesiredWeight(final Identity clusterIdentity, final Identity memberIdentity, final int weight)
    '''
def defineAttribute():
    '''public void defineAttribute(final Identity identity, final String attribute)
    '''
def undefineAttribute():
    '''public void undefineAttribute(final Identity identity, final String attribute)
    '''
def getAttributes():
    '''public Set getAttributes(final Identity identity)
    '''
def setClusterAssociation():
    '''public void setClusterAssociation(final Identity cluster, final Identity member)
    '''
def setCARWaitTime():
    '''public void setCARWaitTime(final int time)
    '''
