def ClusterServiceImpl():
'''public ClusterServiceImpl()
'''
pass
def getCoidentifiers():
'''public Map getCoidentifiers()
'''
pass
def getIdentity():
'''public Identity getIdentity(final Map nameValuePairs)
'''
pass
def getClusterScopedData():
'''public byte[] getClusterScopedData(final Identity clusterIdentity, final Identity dataIdentity)
'''
pass
def getMemberScopedData():
'''public byte[] getMemberScopedData(final Identity memberIdentity, final Identity dataIdentity)
'''
pass
def getClientClusterContextListener():
'''public ClientClusterContext getClientClusterContextListener(final List clusters)
'''
pass
def registerInterest():
'''public void registerInterest(final ClusterObserver observer, final Identity identifier, final String type)
'''
pass
def deregisterInterest():
'''public void deregisterInterest(final ClusterObserver observer, final Identity identifier, final String type)
'''
pass
def getMemberIdentities():
'''public Identity[] getMemberIdentities(final Identity clusterIdentity)
'''
pass
def handleNotification():
'''public void handleNotification(final DescriptionKey key, String type, Object data, final Object handback)
'''
pass
def matchEndPoints():
'''public EndPoint[] matchEndPoints(final Identity owningIdentity, final Map matchProperties)
public EndPoint[] matchEndPoints(final Map endPoints, final Map propertyNames)
'''
pass
def identityToString():
'''public String identityToString(final Identity identity)
'''
pass
def stringToIdentity():
'''public Identity stringToIdentity(final String identityString)
'''
pass
def getActiveClusterSet():
'''public Set getActiveClusterSet()
public Set getActiveClusterSet(final String cellName)
'''
pass
def ClusterObserverWeakReference():
'''public ClusterObserverWeakReference(final Object obj)
public ClusterObserverWeakReference(final Object obj, final ReferenceQueue refQ)
'''
pass
def equals():
'''public boolean equals(final Object b)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
