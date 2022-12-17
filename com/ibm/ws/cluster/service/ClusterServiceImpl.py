def ():
    '''returns ClusterObserverWeakReference\n\n
    ()\n
    (final Object obj)\n
    (final Object obj, final ReferenceQueue refQ)\n
    '''
def getCoidentifiers():
    '''returns Map\n\n
    getCoidentifiers()\n
    '''
def getIdentity():
    '''returns Identity\n\n
    getIdentity(final Map nameValuePairs)\n
    '''
def getClusterScopedData():
    '''returns byte[]\n\n
    getClusterScopedData(final Identity clusterIdentity, final Identity dataIdentity)\n
    '''
def getMemberScopedData():
    '''returns byte[]\n\n
    getMemberScopedData(final Identity memberIdentity, final Identity dataIdentity)\n
    '''
def getClientClusterContextListener():
    '''returns ClientClusterContext\n\n
    getClientClusterContextListener(final List clusters)\n
    '''
def registerInterest():
    '''returns None\n\n
    registerInterest(final ClusterObserver observer, final Identity identifier, final String type)\n
    '''
def deregisterInterest():
    '''returns None\n\n
    deregisterInterest(final ClusterObserver observer, final Identity identifier, final String type)\n
    '''
def getMemberIdentities():
    '''returns Identity[]\n\n
    getMemberIdentities(final Identity clusterIdentity)\n
    '''
def handleNotification():
    '''returns None\n\n
    handleNotification(final DescriptionKey key, String type, Object data, final Object handback)\n
    '''
def matchEndPoints():
    '''returns EndPoint[]\n\n
    matchEndPoints(final Identity owningIdentity, final Map matchProperties)\n
    matchEndPoints(final Map endPoints, final Map propertyNames)\n
    '''
def identityToString():
    '''returns String\n\n
    identityToString(final Identity identity)\n
    '''
def stringToIdentity():
    '''returns Identity\n\n
    stringToIdentity(final String identityString)\n
    '''
def getActiveClusterSet():
    '''returns Set\n\n
    getActiveClusterSet()\n
    getActiveClusterSet(final String cellName)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object b)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
