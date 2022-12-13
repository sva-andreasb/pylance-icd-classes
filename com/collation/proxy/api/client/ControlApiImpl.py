def startDiscovery():
    '''    public void startDiscovery(final String[] scope, final String runName)
    public void startDiscovery(final RunDefinition runDef, final String runName)
    public void startDiscovery(final Guid[] guidList, final String runName)
    '''
def abortDiscovery():
    '''    public void abortDiscovery()
    '''
def getStatus():
    '''    public String getStatus()
    '''
def rebuildTopology():
    '''    public void rebuildTopology()
    '''
def gcTopology():
    '''    public void gcTopology()
    '''
def clearTopology():
    '''    public void clearTopology()
    '''
def synchScopes():
    '''    public void synchScopes()
    '''
def setAnchorHosts():
    '''    public void setAnchorHosts(final String[] hosts)
    '''
def setAnchorPort():
    '''    public void setAnchorPort(final int port)
    '''
def getAnchorHosts():
    '''    public String[] getAnchorHosts()
    '''
def getAnchorPort():
    '''    public int getAnchorPort()
    '''
def createVersion():
    '''    public long createVersion(final String name, final String description)
    '''
def createEmptyVersion():
    '''    public long createEmptyVersion(final String name, final String description)
    '''
def deleteVersion():
    '''    public void deleteVersion(final long versionID)
    '''
def getAllVersions():
    '''    public TopologyVersion[] getAllVersions()
    '''
def disableDiscovery():
    '''    public void disableDiscovery()
    '''
def disableEvents():
    '''    public void disableEvents()
    '''
def enableDiscovery():
    '''    public void enableDiscovery()
    '''
def enableEvents():
    '''    public void enableEvents()
    '''
def toString():
    '''    public String toString()
    '''
def processChanges():
    '''    public void processChanges()
    '''
def startBulkload():
    '''    public long startBulkload(final long timeoutInSeconds)
    '''
def endBulkload():
    '''    public void endBulkload(final long transactionId)
    '''
def registerLocale():
    '''    public void registerLocale(final Locale locale)
    '''
def unregisterLocale():
    '''    public void unregisterLocale()
    '''
