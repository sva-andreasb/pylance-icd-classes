def startDiscovery():
    '''returns None\n\n
    startDiscovery(final RunDefinition runDef, final String runName)\n
    startDiscovery(final Guid[] guidList, final String runName)\n
    startDiscovery(final String[] scope, final String runName)\n
    '''
def abortDiscovery():
    '''returns None\n\n
    abortDiscovery()\n
    '''
def getStatus():
    '''returns String\n\n
    getStatus()\n
    '''
def rebuildTopology():
    '''returns None\n\n
    rebuildTopology()\n
    '''
def gcTopology():
    '''returns None\n\n
    gcTopology()\n
    '''
def clearTopology():
    '''returns None\n\n
    clearTopology()\n
    '''
def synchScopes():
    '''returns None\n\n
    synchScopes()\n
    '''
def setAnchorHosts():
    '''returns None\n\n
    setAnchorHosts(final String[] hosts)\n
    '''
def setAnchorPort():
    '''returns None\n\n
    setAnchorPort(final int port)\n
    '''
def getAnchorHosts():
    '''returns String[]\n\n
    getAnchorHosts()\n
    '''
def getAnchorPort():
    '''returns int\n\n
    getAnchorPort()\n
    '''
def createVersion():
    '''returns long\n\n
    createVersion(final String name, final String description)\n
    '''
def createEmptyVersion():
    '''returns long\n\n
    createEmptyVersion(final String name, final String description)\n
    '''
def deleteVersion():
    '''returns None\n\n
    deleteVersion(final long versionID)\n
    '''
def getAllVersions():
    '''returns TopologyVersion[]\n\n
    getAllVersions()\n
    '''
def disableDiscovery():
    '''returns None\n\n
    disableDiscovery()\n
    '''
def disableEvents():
    '''returns None\n\n
    disableEvents()\n
    '''
def enableDiscovery():
    '''returns None\n\n
    enableDiscovery()\n
    '''
def enableEvents():
    '''returns None\n\n
    enableEvents()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def processChanges():
    '''returns None\n\n
    processChanges()\n
    '''
def startBulkload():
    '''returns long\n\n
    startBulkload(final long timeoutInSeconds)\n
    '''
def endBulkload():
    '''returns None\n\n
    endBulkload(final long transactionId)\n
    '''
def registerLocale():
    '''returns None\n\n
    registerLocale(final Locale locale)\n
    '''
def unregisterLocale():
    '''returns None\n\n
    unregisterLocale()\n
    '''
