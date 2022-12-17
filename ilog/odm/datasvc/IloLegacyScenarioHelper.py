COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
CONNECTOR_PROPERTY = "String  \"RequirementConnector\""
def ():
    '''returns LegacySchemaProviderAdapter\n\n
    (final ilog.odm.scenario.IloScenario scenario)\n
    (final IloSchemaProvider provider)\n
    '''
def getInput():
    '''returns IloScenarioInput\n\n
    getInput()\n
    '''
def getGoalBoundsReport():
    '''returns IloGoalBoundsReport\n\n
    getGoalBoundsReport()\n
    '''
def getNameSpaceProfileManager():
    '''returns IloNameSpaceProfileManager\n\n
    getNameSpaceProfileManager()\n
    '''
def getOutput():
    '''returns IloSolutionReport\n\n
    getOutput()\n
    '''
def getSchema():
    '''returns IloSchema\n\n
    getSchema(final String tableId)\n
    getSchema(final IloTableId tableId)\n
    '''
def getLegacyTable():
    '''returns IloTable\n\n
    getLegacyTable(final String tableId)\n
    '''
def makeNewRow():
    '''returns IloRow\n\n
    makeNewRow(final String tableId)\n
    makeNewRow(final IloTableId tableId)\n
    '''
def setTable():
    '''returns None\n\n
    setTable(final String tableId, final IloTable table)\n
    '''
def tableIdsIterator():
    '''returns Iterator\n\n
    tableIdsIterator()\n
    tableIdsIterator()\n
    '''
def isInBulkModifications():
    '''returns boolean\n\n
    isInBulkModifications()\n
    '''
def hasErrors():
    '''returns boolean\n\n
    hasErrors()\n
    '''
def hasWarnings():
    '''returns boolean\n\n
    hasWarnings()\n
    '''
def getIssuesReport():
    '''returns IloIssuesReport\n\n
    getIssuesReport()\n
    '''
def getTables():
    '''returns Collection\n\n
    getTables()\n
    '''
def clearOutput():
    '''returns None\n\n
    clearOutput()\n
    '''
def refreshSharableInfos():
    '''returns None\n\n
    refreshSharableInfos()\n
    '''
def transferLockOwnership():
    '''returns None\n\n
    transferLockOwnership(final IloLock lock, final IloUser otherUser)\n
    '''
def getSchemaCatalog():
    '''returns IloSchemaCatalog\n\n
    getSchemaCatalog()\n
    '''
def removeLock():
    '''returns None\n\n
    removeLock(final ilog.odm.datasvc.IloLock lock)\n
    '''
def addLock():
    '''returns IloLock\n\n
    addLock(final int type)\n
    addLock(final int type, final int description_code)\n
    addLock(final int type, final boolean persistent)\n
    addLock(final int type, final int description_code, final boolean persistent)\n
    '''
def isUsed():
    '''returns boolean\n\n
    isUsed()\n
    '''
def getLocks():
    '''returns Collection\n\n
    getLocks()\n
    '''
def getLastModifier():
    '''returns IloUser\n\n
    getLastModifier()\n
    '''
def getLastModificationDate():
    '''returns Date\n\n
    getLastModificationDate()\n
    '''
def getPersistentID():
    '''returns String\n\n
    getPersistentID()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def isModified():
    '''returns boolean\n\n
    isModified()\n
    '''
def getScenarioExtensionContext():
    '''returns IloScenarioExtensionContext\n\n
    getScenarioExtensionContext()\n
    '''
def registerScenarioListener():
    '''returns None\n\n
    registerScenarioListener(final IloScenarioListener listener)\n
    '''
def refresh():
    '''returns None\n\n
    refresh()\n
    '''
def beginModifications():
    '''returns None\n\n
    beginModifications()\n
    beginModifications(final Object userData)\n
    '''
def endModifications():
    '''returns None\n\n
    endModifications()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def isDeleted():
    '''returns boolean\n\n
    isDeleted()\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final IloScenarioListener listener)\n
    '''
def startInSyncNotifier():
    '''returns None\n\n
    startInSyncNotifier(final long checkingPeriod)\n
    '''
def stopInSyncNotifier():
    '''returns None\n\n
    stopInSyncNotifier()\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final IloScenarioListener listener)\n
    '''
def isInSync():
    '''returns boolean\n\n
    isInSync()\n
    '''
def acknowledgeUpdates():
    '''returns None\n\n
    acknowledgeUpdates()\n
    '''
def getConcurrentChangeConflicts():
    '''returns IloConcurrentChangeConflictsSet\n\n
    getConcurrentChangeConflicts()\n
    '''
def getConcurrentChangeUpdates():
    '''returns IloConcurrentChangeUpdatesSet\n\n
    getConcurrentChangeUpdates()\n
    '''
def getScenarioDiff():
    '''returns IloDifferencesSet\n\n
    getScenarioDiff(final IloScenario scenario)\n
    '''
def revertFromRepository():
    '''returns None\n\n
    revertFromRepository()\n
    revertFromRepository(final IloScenario source_scenario, final Collection<ilog.odm.datasvc.IloSchema> schemas)\n
    '''
def updateFromRepository():
    '''returns boolean\n\n
    updateFromRepository()\n
    '''
def addRepositoryChangeListener():
    '''returns None\n\n
    addRepositoryChangeListener(final IloRepositoryChangeListener listener)\n
    '''
def removeRepositoryChangeListener():
    '''returns None\n\n
    removeRepositoryChangeListener(final IloRepositoryChangeListener listener)\n
    '''
def refreshLocks():
    '''returns None\n\n
    refreshLocks()\n
    '''
def checkInSync():
    '''returns boolean\n\n
    checkInSync()\n
    '''
def areDataInSync():
    '''returns boolean\n\n
    areDataInSync()\n
    '''
def areDataLoaded():
    '''returns boolean\n\n
    areDataLoaded()\n
    '''
def areLocksInSync():
    '''returns boolean\n\n
    areLocksInSync()\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def getModificationUserData():
    '''returns Object\n\n
    getModificationUserData()\n
    '''
def getLockVersion():
    '''returns Long\n\n
    getLockVersion()\n
    '''
def getVersion():
    '''returns Long\n\n
    getVersion()\n
    '''
def getTablesVersion():
    '''returns Long\n\n
    getTablesVersion()\n
    '''
def getTableVersion():
    '''returns Long\n\n
    getTableVersion(final String id)\n
    '''
def exportAsScenarioSet():
    '''returns None\n\n
    exportAsScenarioSet(final File destination)\n
    '''
def makeTableId():
    '''returns IloTableId\n\n
    makeTableId(final String id)\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
