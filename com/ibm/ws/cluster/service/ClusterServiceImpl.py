def ClusterServiceImpl():
    '''public ClusterServiceImpl()
    '''
def getCoidentifiers():
    '''public Map getCoidentifiers()
    '''
def getIdentity():
    '''public Identity getIdentity(final Map nameValuePairs)
    '''
def getClusterScopedData():
    '''public byte[] getClusterScopedData(final Identity clusterIdentity, final Identity dataIdentity)
    '''
def getMemberScopedData():
    '''public byte[] getMemberScopedData(final Identity memberIdentity, final Identity dataIdentity)
    '''
def getClientClusterContextListener():
    '''public ClientClusterContext getClientClusterContextListener(final List clusters)
    '''
def registerInterest():
    '''public void registerInterest(final ClusterObserver observer, final Identity identifier, final String type)
    '''
def deregisterInterest():
    '''public void deregisterInterest(final ClusterObserver observer, final Identity identifier, final String type)
    '''
def getMemberIdentities():
    '''public Identity[] getMemberIdentities(final Identity clusterIdentity)
    '''
def handleNotification():
    '''public void handleNotification(final DescriptionKey key, String type, Object data, final Object handback)
    '''
def matchEndPoints():
    '''public EndPoint[] matchEndPoints(final Identity owningIdentity, final Map matchProperties)
    public EndPoint[] matchEndPoints(final Map endPoints, final Map propertyNames)
    '''
def identityToString():
    '''public String identityToString(final Identity identity)
    '''
def stringToIdentity():
    '''public Identity stringToIdentity(final String identityString)
    '''
def getActiveClusterSet():
    '''public Set getActiveClusterSet()
    public Set getActiveClusterSet(final String cellName)
    '''
def ClusterObserverWeakReference():
    '''public ClusterObserverWeakReference(final Object obj)
    public ClusterObserverWeakReference(final Object obj, final ReferenceQueue refQ)
    '''
def equals():
    '''public boolean equals(final Object b)
    '''
def hashCode():
    '''public int hashCode()
    '''
