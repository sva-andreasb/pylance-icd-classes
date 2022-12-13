def ClusterManagementImpl():
'''public ClusterManagementImpl(final boolean distribute)
'''
pass
def createClusterMember():
'''public Identity createClusterMember(final String cellName, final String nodeName, String hostName, final String memberName)
'''
pass
def joinCluster():
'''public void joinCluster(final Identity clusterIdentity, final Identity[] memberIdentities)
public void joinCluster(final Identity[] clusterIdentities, final Identity[] memberIdentities)
'''
pass
def disjoinCluster():
'''public synchronized void disjoinCluster(final Identity clusterIdentity, final Identity[] memberIdentities)
public void disjoinCluster(final Identity[] clusterIdentities, final Identity[] memberIdentities)
'''
pass
def defineClusterScopedData():
'''public EndPoint defineClusterScopedData(final Identity clusterIdentity, final Identity dataIdentity, final byte[] data)
'''
pass
def defineMemberScopedData():
'''public EndPoint defineMemberScopedData(final Identity memberIdentity, final Identity dataIdentity, final byte[] data)
'''
pass
def undefineClusterScopedData():
'''public synchronized void undefineClusterScopedData(final Identity clusterIdentity, final EndPoint data)
'''
pass
def undefineMemberScopedData():
'''public synchronized void undefineMemberScopedData(final Identity memberIdentity, final EndPoint data)
'''
pass
def getDesiredWeight():
'''public int getDesiredWeight(final Identity cluster, final Identity member)
'''
pass
def setDesiredWeight():
'''public void setDesiredWeight(final Identity clusterIdentity, final Identity memberIdentity, final int weight)
'''
pass
def defineAttribute():
'''public void defineAttribute(final Identity identity, final String attribute)
'''
pass
def undefineAttribute():
'''public void undefineAttribute(final Identity identity, final String attribute)
'''
pass
def getAttributes():
'''public Set getAttributes(final Identity identity)
'''
pass
def setClusterAssociation():
'''public void setClusterAssociation(final Identity cluster, final Identity member)
'''
pass
def setCARWaitTime():
'''public void setCARWaitTime(final int time)
'''
pass
