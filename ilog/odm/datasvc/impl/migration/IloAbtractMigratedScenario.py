COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloAbtractMigratedScenario\n\n
    (final IloScenarioImpl scenario, final IloTableContainer container)\n
    '''
def getScenario():
    '''returns IloScenarioImpl\n\n
    getScenario()\n
    '''
def getTableContainer():
    '''returns IloTableContainer\n\n
    getTableContainer()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getScenarioExtensionContext():
    '''returns IloScenarioExtensionContext\n\n
    getScenarioExtensionContext()\n
    '''
def getSchemaCatalog():
    '''returns IloSchemaCatalog\n\n
    getSchemaCatalog()\n
    '''
def isDeleted():
    '''returns boolean\n\n
    isDeleted()\n
    '''
def isModified():
    '''returns boolean\n\n
    isModified()\n
    '''
def hasErrors():
    '''returns boolean\n\n
    hasErrors()\n
    '''
def hasWarnings():
    '''returns boolean\n\n
    hasWarnings()\n
    '''
def getLastModificationDate():
    '''returns Date\n\n
    getLastModificationDate()\n
    '''
def getLastModifier():
    '''returns IloUser\n\n
    getLastModifier()\n
    '''
def getPersistentID():
    '''returns String\n\n
    getPersistentID()\n
    '''
def getIssuesReport():
    '''returns IloIssuesReport\n\n
    getIssuesReport()\n
    '''
def getLocks():
    '''returns Collection<IloLock>\n\n
    getLocks()\n
    '''
def isUsed():
    '''returns boolean\n\n
    isUsed()\n
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
def getModificationUserData():
    '''returns Object\n\n
    getModificationUserData()\n
    '''
def isInBulkModifications():
    '''returns boolean\n\n
    isInBulkModifications()\n
    '''
def getTable():
    '''returns IloTable\n\n
    getTable(final String tableId)\n
    '''
def acknowledgeUpdates():
    '''returns None\n\n
    acknowledgeUpdates()\n
    '''
def clearOutput():
    '''returns None\n\n
    clearOutput()\n
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
    getScenarioDiff(final ilog.odm.datasvc.IloScenario scenario)\n
    '''
def isInSync():
    '''returns boolean\n\n
    isInSync()\n
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
def refresh():
    '''returns None\n\n
    refresh()\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final IloScenarioListener listener)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final IloScenarioListener listener)\n
    '''
def revertFromRepository():
    '''returns None\n\n
    revertFromRepository()\n
    revertFromRepository(final ilog.odm.datasvc.IloScenario scenario, final Collection<IloSchema> schemas)\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
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
def transferLockOwnership():
    '''returns None\n\n
    transferLockOwnership(final ilog.odm.datasvc.internal.IloLock lock, final IloUser otherUser)\n
    '''
def refreshLocks():
    '''returns None\n\n
    refreshLocks()\n
    '''
def removeLock():
    '''returns None\n\n
    removeLock(final IloLock lock)\n
    '''
def checkInSync():
    '''returns boolean\n\n
    checkInSync()\n
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
