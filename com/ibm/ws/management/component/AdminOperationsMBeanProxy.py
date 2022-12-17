def ():
    '''returns AdminOperationsMBeanProxy\n\n
    ()\n
    (final String profileKey)\n
    '''
def renameNodeOnDmgr():
    '''returns None\n\n
    renameNodeOnDmgr(final String oldNode, final String newNode, final String shortName)\n
    '''
def checkNodeAndDmgrCompatibility():
    '''returns None\n\n
    checkNodeAndDmgrCompatibility(final Properties nodeMetadataProp)\n
    '''
def mergeConfigDataOnDmgr():
    '''returns None\n\n
    mergeConfigDataOnDmgr(final Properties nodeProperties, final Properties adminProperties)\n
    '''
def doUnMergeConfigDataOnDmgr():
    '''returns None\n\n
    doUnMergeConfigDataOnDmgr(final Properties nodeProperties)\n
    '''
def addNode():
    '''returns None\n\n
    addNode(final String cellHost, final String cellPort)\n
    '''
def addNodeWithOptions():
    '''returns None\n\n
    addNodeWithOptions(final String cellHost, final String cellPort, final String options)\n
    '''
def removeNode():
    '''returns None\n\n
    removeNode()\n
    '''
def removeNodeWithOptions():
    '''returns None\n\n
    removeNodeWithOptions(final String options)\n
    '''
def expandVariable():
    '''returns String\n\n
    expandVariable(final String variable)\n
    '''
def getResourceAdapterFromRAR():
    '''returns AttributeList\n\n
    getResourceAdapterFromRAR(final String rarPath, final Hashtable props)\n
    '''
def extractArchive():
    '''returns None\n\n
    extractArchive(final String archivePath, final String dest, final int flag)\n
    '''
def configChanged():
    '''returns None\n\n
    configChanged(final ConfigRepositoryEvent e)\n
    '''
def updateMetadataForNode():
    '''returns None\n\n
    updateMetadataForNode(final String nodeName, final Properties nodeMetadata)\n
    '''
def collectMetadataForThisNode():
    '''returns Properties\n\n
    collectMetadataForThisNode()\n
    '''
def _getAppDistributionStatus():
    '''returns Hashtable\n\n
    _getAppDistributionStatus(final String appName, final Hashtable options)\n
    '''
def getRARInfo():
    '''returns Hashtable\n\n
    getRARInfo(final String name, final Hashtable props)\n
    '''
