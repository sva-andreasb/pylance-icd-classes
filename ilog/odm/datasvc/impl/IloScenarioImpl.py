COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
REPOSITORY_CHANGE_POLLING_TIMER = "String  \"ilog.edi.scenario.refreshtimer\""
SCENARIO_READ = "String  \"Read\""
SCENARIO_WRITE = "String  \"Write\""
_SCENARIO_EDIT_TABLE = "String  \"EditTable\""
SCENARIO_LOCK = "String  \"Lock\""
STATE_NORMAL = "int  0"
def getCurrentUser():
    '''returns IloUser\n\n
    getCurrentUser()\n
    '''
def createTempScenarioCopy():
    '''returns IloScenarioImpl\n\n
    createTempScenarioCopy()\n
    '''
def call():
    '''returns IloNameSpaceProfileManager\n\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    '''
def getPo():
    '''returns IloPersistentRow\n\n
    getPo()\n
    '''
def getPersistentLockable():
    '''returns IloPersistentRow\n\n
    getPersistentLockable(final IloTransactionalSession session, final boolean lock)\n
    '''
def getPersistentScenario():
    '''returns IloPersistentRow\n\n
    getPersistentScenario(final IloTransactionalSession session, final boolean lock)\n
    '''
def setDisableMigration():
    '''returns None\n\n
    setDisableMigration(final boolean migration)\n
    '''
def delete():
    '''returns None\n\n
    delete(final boolean check_temporary)\n
    delete()\n
    delete()\n
    delete(final boolean moveToRecycleBin)\n
    '''
def importData():
    '''returns None\n\n
    importData(final File scenario_file, final Map<String, String> schemaMapping)\n
    '''
def getTable():
    '''returns IloTableImpl\n\n
    getTable(final String tableId)\n
    '''
def getTables():
    '''returns Collection<IloTable>\n\n
    getTables()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def beginModifications():
    '''returns None\n\n
    beginModifications()\n
    beginModifications(final Object userData)\n
    '''
def getModificationUserData():
    '''returns Object\n\n
    getModificationUserData()\n
    '''
def endModifications():
    '''returns None\n\n
    endModifications()\n
    '''
def isInBulkModifications():
    '''returns boolean\n\n
    isInBulkModifications()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    save(final IloScenarioTableContainer table_container, final boolean has_errors, final boolean has_warnings)\n
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
def revertFromRepository():
    '''returns None\n\n
    revertFromRepository()\n
    revertFromRepository(final ilog.odm.datasvc.IloScenario source_scenario, final Collection<IloSchema> schemas)\n
    '''
def updateFromRepository():
    '''returns boolean\n\n
    updateFromRepository()\n
    '''
def getConcurrentChangeConflicts():
    '''returns IloConcurrentChangeConflictsSet\n\n
    getConcurrentChangeConflicts()\n
    '''
def getConcurrentChangeUpdates():
    '''returns IloConcurrentChangeUpdatesSet\n\n
    getConcurrentChangeUpdates()\n
    '''
def acknowledgeUpdates():
    '''returns None\n\n
    acknowledgeUpdates()\n
    '''
def getScenarioDiff():
    '''returns IloDifferencesSet\n\n
    getScenarioDiff(final ilog.odm.datasvc.IloScenario scenario)\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final IloScenarioListener listener)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final IloScenarioListener listener)\n
    '''
def getScenarioExtensionContext():
    '''returns IloScenarioExtensionContext\n\n
    getScenarioExtensionContext()\n
    '''
def isDeleted():
    '''returns boolean\n\n
    isDeleted()\n
    isDeleted(final boolean deleted)\n
    isDeleted()\n
    '''
def getPersistentID():
    '''returns String\n\n
    getPersistentID()\n
    '''
def getIssuesReport():
    '''returns IloIssuesReportImpl\n\n
    getIssuesReport()\n
    '''
def areInfosInSync():
    '''returns boolean\n\n
    areInfosInSync()\n
    '''
def checkInSync():
    '''returns boolean\n\n
    checkInSync()\n
    '''
def addRepositoryChangeListener():
    '''returns None\n\n
    addRepositoryChangeListener(final IloRepositoryChangeListener listener)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def getSource():
    '''returns IloSharable\n\n
    getSource()\n
    '''
def removeRepositoryChangeListener():
    '''returns None\n\n
    removeRepositoryChangeListener(final IloRepositoryChangeListener listener)\n
    '''
def getLastModifier():
    '''returns IloUser\n\n
    getLastModifier()\n
    '''
def getLastModificationDate():
    '''returns Date\n\n
    getLastModificationDate()\n
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
def addLock():
    '''returns IloLock\n\n
    addLock(final int type)\n
    addLock(final int type, final int action_code)\n
    addLock(final int type, final boolean persistent)\n
    addLock(final int type, final int action_code, final boolean persistent)\n
    '''
def transferLockOwnership():
    '''returns None\n\n
    transferLockOwnership(final IloLock lock, final IloUser otherUser)\n
    '''
def areLocksInSync():
    '''returns boolean\n\n
    areLocksInSync()\n
    '''
def isUsed():
    '''returns boolean\n\n
    isUsed()\n
    '''
def refreshLocks():
    '''returns None\n\n
    refreshLocks()\n
    '''
def removeLock():
    '''returns None\n\n
    removeLock(final ilog.odm.datasvc.IloLock lock)\n
    '''
def getNamespaceView():
    '''returns IloNamespaceView\n\n
    getNamespaceView()\n
    '''
def getNameSpaceProfileManager():
    '''returns IloNameSpaceProfileManager\n\n
    getNameSpaceProfileManager()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
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
def getLockVersion():
    '''returns Long\n\n
    getLockVersion()\n
    '''
def exportAsScenarioSet():
    '''returns None\n\n
    exportAsScenarioSet(final File destination)\n
    exportAsScenarioSet(final File destination)\n
    '''
def getParentFolder():
    '''returns IloWorkspaceFolder\n\n
    getParentFolder()\n
    '''
def getWorkspace():
    '''returns IloWorkspace\n\n
    getWorkspace()\n
    '''
def markChanged():
    '''returns None\n\n
    markChanged(final IloPersistentRow po)\n
    '''
def unmarkChanged():
    '''returns None\n\n
    unmarkChanged(final IloPersistentRow po)\n
    '''
def markDeleted():
    '''returns None\n\n
    markDeleted(final IloPersistentRow po)\n
    '''
def markNew():
    '''returns None\n\n
    markNew(final IloPersistentRow po)\n
    '''
def markAllDeleted():
    '''returns None\n\n
    markAllDeleted(final IloSchema schema)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def get():
    '''returns IloPersistentRow\n\n
    get(final IloSchema schema, final Long row_id)\n
    '''
def remove():
    '''returns IloPersistentRow\n\n
    remove(final IloSchema schema, final Long row_id)\n
    '''
def removeAll():
    '''returns None\n\n
    removeAll()\n
    '''
def values():
    '''returns Collection<IloPersistentRow>\n\n
    values()\n
    values(final IloSchema schema)\n
    '''
def keySet():
    '''returns Collection<Long>\n\n
    keySet(final IloSchema schema)\n
    '''
def add():
    '''returns None\n\n
    add(final IloPersistentRow po)\n
    add(final IloSessionSchemaRowMap row_collection)\n
    add(final IloSchema schema, final Map<Long, IloPersistentRow> rows)\n
    '''
def getSchemas():
    '''returns Collection<IloSchema>\n\n
    getSchemas()\n
    '''
