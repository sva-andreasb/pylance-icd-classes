COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
DATASVC_PROPERTY_PREFIX = "String  \"ilog.edi.datasvc.\""
ERROR_OVERFLOW_PROPERTY = "String  \"error_overflow\""
def ():
    '''returns IloCheckDataScenarioWrapper\n\n
    (final File odmAppDir, final IloNameSpaceProfileManager relationalModelDesc, final IloScenarioSourceProvider deploymentDesc, final IloApplicationContext applicationContext)\n
    (final IloSystemDataManager system_data_manager, final IloScenarioSourceProvider deploymentDesc)\n
    (final ilog.odm.datasvc.IloScenario scenario, final String category)\n
    (final IloScenario scenario, final IloScenario scenario_copy)\n
    '''
def setScenarioExtensionContext():
    '''returns None\n\n
    setScenarioExtensionContext(final IloScenarioExtensionContext value)\n
    '''
def getRepositoryProfile():
    '''returns IloRepositoryAccessProfile\n\n
    getRepositoryProfile()\n
    '''
def enableIntegrityCheckForTable():
    '''returns None\n\n
    enableIntegrityCheckForTable(final String tableId)\n
    '''
def getResourcesEstimationProfile():
    '''returns IloResourcesEstimationProfile\n\n
    getResourcesEstimationProfile()\n
    '''
def getOdmAppDir():
    '''returns File\n\n
    getOdmAppDir()\n
    '''
def loginAsAnonymous():
    '''returns None\n\n
    loginAsAnonymous(final boolean force)\n
    '''
def login():
    '''returns None\n\n
    login(final IloCredential credential, final boolean force)\n
    login(final IloCredential credential, final X509TrustManager manager, final boolean force)\n
    '''
def logout():
    '''returns None\n\n
    logout()\n
    '''
def getCurrentSession():
    '''returns IloODMSession\n\n
    getCurrentSession()\n
    '''
def getCurrentUser():
    '''returns IloUser\n\n
    getCurrentUser()\n
    getCurrentUser()\n
    '''
def isMultiUserMode():
    '''returns boolean\n\n
    isMultiUserMode()\n
    isMultiUserMode()\n
    '''
def checkSession():
    '''returns None\n\n
    checkSession()\n
    '''
def getAppDataId():
    '''returns String\n\n
    getAppDataId()\n
    '''
def getAppDataVersion():
    '''returns String\n\n
    getAppDataVersion()\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def getCredentialPrompter():
    '''returns IloCredentialPrompter\n\n
    getCredentialPrompter()\n
    '''
def getCredentialManager():
    '''returns IloCredentialManager\n\n
    getCredentialManager()\n
    getCredentialManager()\n
    '''
def setCredentialPrompter():
    '''returns None\n\n
    setCredentialPrompter(final IloCredentialPrompter credentialPrompter)\n
    '''
def getReportHandler():
    '''returns IloIssueReporter\n\n
    getReportHandler()\n
    '''
def setReportHandler():
    '''returns None\n\n
    setReportHandler(final IloIssueReporter reportHandler)\n
    '''
def visit():
    '''returns None\n\n
    visit(final IloScenarioSourceProvider.Visitor v)\n
    '''
def getScenarioUpdaterTemplates():
    '''returns Collection<IloScenarioSourceTemplate>\n\n
    getScenarioUpdaterTemplates()\n
    '''
def getScenarioExporterTemplates():
    '''returns Collection<IloFormTemplate>\n\n
    getScenarioExporterTemplates()\n
    '''
def invoke():
    '''returns Object\n\n
    invoke(final Object proxy, final Method method, final Object[] args)\n
    '''
def call():
    '''returns Boolean\n\n
    call()\n
    call()\n
    '''
def getScenarioExporterIds():
    '''returns Collection<String>\n\n
    getScenarioExporterIds()\n
    getScenarioExporterIds()\n
    '''
def getScenarioExporterInstance():
    '''returns IloTemplateInstance\n\n
    getScenarioExporterInstance(final String exporterId)\n
    getScenarioExporterInstance(final String exporterId)\n
    '''
def getScenarioUpdaterIds():
    '''returns Collection<String>\n\n
    getScenarioUpdaterIds()\n
    getScenarioUpdaterIds()\n
    '''
def getScenarioUpdaterInstance():
    '''returns IloTemplateInstance\n\n
    getScenarioUpdaterInstance(final String updaterId)\n
    getScenarioUpdaterInstance(final String updaterId)\n
    '''
def checkData():
    '''returns boolean\n\n
    checkData(final ilog.odm.datasvc.IloScenario scenario)\n
    '''
def checkDataInternal():
    '''returns boolean\n\n
    checkDataInternal(final IloScenario scenario)\n
    '''
def createWorkspace():
    '''returns IloWorkspace\n\n
    createWorkspace()\n
    '''
def exportScenario():
    '''returns boolean\n\n
    exportScenario(final ilog.odm.datasvc.IloScenario scenario, final IloTemplateInstance exporterI)\n
    exportScenario(final ilog.odm.datasvc.IloScenario scenario, final IloTemplateInstance exporter)\n
    '''
def getSchemaCatalog():
    '''returns IloSchemaCatalog\n\n
    getSchemaCatalog()\n
    getSchemaCatalog()\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def getWorkspace():
    '''returns IloWorkspace\n\n
    getWorkspace(final String persistent_id)\n
    '''
def getScenario():
    '''returns IloScenario\n\n
    getScenario(final String persistent_id)\n
    '''
def getRecycleBin():
    '''returns IloRecycleBin\n\n
    getRecycleBin()\n
    '''
def visitScenarioUpdater():
    '''returns None\n\n
    visitScenarioUpdater(final IloScenarioUpdater updater)\n
    '''
def visitScenarioExporter():
    '''returns None\n\n
    visitScenarioExporter(final IloScenarioExporter exporter)\n
    '''
def updateScenario():
    '''returns boolean\n\n
    updateScenario(final ilog.odm.datasvc.IloScenario scenario, IloTemplateInstance updaterI)\n
    updateScenario(final ilog.odm.datasvc.IloScenario scenario, final IloTemplateInstance updater)\n
    '''
def getDBConnection():
    '''returns Connection\n\n
    getDBConnection(final String connectionId)\n
    getDBConnection(final String connectionId)\n
    '''
def releaseDBConnection():
    '''returns None\n\n
    releaseDBConnection(final Connection connection)\n
    releaseDBConnection(final String connectionId, final Connection connection)\n
    releaseDBConnection(final Connection connection)\n
    '''
def createNewResourcesSet():
    '''returns IloResourcesSet\n\n
    createNewResourcesSet()\n
    '''
def checkIfPossibleToUseResources():
    '''returns boolean\n\n
    checkIfPossibleToUseResources(final IloResourcesSet resources)\n
    '''
def checkIfPossibleToUseResourcesInternal():
    '''returns ResourcesCheckingResult\n\n
    checkIfPossibleToUseResourcesInternal(final IloResourcesSet resources)\n
    '''
def getDeploymentCustomProperties():
    '''returns Properties\n\n
    getDeploymentCustomProperties()\n
    getDeploymentCustomProperties()\n
    '''
def newDataServiceContext():
    '''returns IloDataServiceContext\n\n
    newDataServiceContext()\n
    '''
def getAdminService():
    '''returns IloDataAdminService\n\n
    getAdminService()\n
    getAdminService()\n
    '''
def createScenario():
    '''returns IloScenario\n\n
    createScenario()\n
    createScenario(final ilog.odm.datasvc.IloScenario source)\n
    '''
def findCorrespondingScenarioLinks():
    '''returns Collection<IloScenarioLink>\n\n
    findCorrespondingScenarioLinks(final ilog.odm.datasvc.IloScenario scenario, final IloWorkspaceFolder folder, final boolean stopAtFirstFound)\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final IloDataServiceListener listener)\n
    addListener(final IloScenarioListener listener)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final IloDataServiceListener listener)\n
    removeListener(final IloScenarioListener listener)\n
    '''
def notifyScenarioCreated():
    '''returns None\n\n
    notifyScenarioCreated(final IloScenario scenario)\n
    '''
def notifyScenarioMigrated():
    '''returns None\n\n
    notifyScenarioMigrated(final IloScenario scenario)\n
    '''
def notifyScenarioUpdated():
    '''returns None\n\n
    notifyScenarioUpdated(final IloScenario scenario)\n
    '''
def notifyScenarioChecked():
    '''returns None\n\n
    notifyScenarioChecked(final IloScenario scenario)\n
    '''
def getLogger():
    '''returns Logger\n\n
    getLogger()\n
    '''
def getErrorOverflow():
    '''returns int\n\n
    getErrorOverflow()\n
    '''
def getDeploymentProfile():
    '''returns IloDeploymentProfile\n\n
    getDeploymentProfile()\n
    '''
def getErrorReporter():
    '''returns IloErrorReporter\n\n
    getErrorReporter()\n
    '''
def isServerContext():
    '''returns boolean\n\n
    isServerContext()\n
    '''
def addErrorMessage():
    '''returns None\n\n
    addErrorMessage(final ilog.odm.datasvc.IloRow row, final String message)\n
    addErrorMessage(final ilog.odm.datasvc.IloRow row, final int columnIndex, final String message)\n
    addErrorMessage(final IloTable table, final String message)\n
    '''
def addWarningMessage():
    '''returns None\n\n
    addWarningMessage(final ilog.odm.datasvc.IloRow row, final String message)\n
    addWarningMessage(final ilog.odm.datasvc.IloRow row, final int columnIndex, final String message)\n
    addWarningMessage(final IloTable table, final String message)\n
    '''
def setErrorMessage():
    '''returns None\n\n
    setErrorMessage(final String msg)\n
    '''
def isPossible():
    '''returns boolean\n\n
    isPossible()\n
    '''
def getTotalNeededMemory():
    '''returns long\n\n
    getTotalNeededMemory()\n
    '''
def getAdditionalNeededMemory():
    '''returns long\n\n
    getAdditionalNeededMemory()\n
    '''
def getAlreadyLoadedMemory():
    '''returns long\n\n
    getAlreadyLoadedMemory()\n
    '''
def getTotalAvailableMemory():
    '''returns long\n\n
    getTotalAvailableMemory()\n
    '''
def getFreeMemory():
    '''returns long\n\n
    getFreeMemory()\n
    '''
def getFreeableMemory():
    '''returns long\n\n
    getFreeableMemory()\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def acknowledgeUpdates():
    '''returns None\n\n
    acknowledgeUpdates()\n
    '''
def addRepositoryChangeListener():
    '''returns None\n\n
    addRepositoryChangeListener(final IloRepositoryChangeListener listener)\n
    '''
def areDataInSync():
    '''returns boolean\n\n
    areDataInSync()\n
    '''
def areDataLoaded():
    '''returns boolean\n\n
    areDataLoaded()\n
    '''
def beginModifications():
    '''returns None\n\n
    beginModifications()\n
    beginModifications(final Object userData)\n
    '''
def checkInSync():
    '''returns boolean\n\n
    checkInSync()\n
    '''
def endModifications():
    '''returns None\n\n
    endModifications()\n
    '''
def getConcurrencyMode():
    '''returns ConcurrencyMode\n\n
    getConcurrencyMode()\n
    '''
def getConcurrentChangeConflicts():
    '''returns IloConcurrentChangeConflictsSet\n\n
    getConcurrentChangeConflicts()\n
    '''
def getConcurrentChangeUpdates():
    '''returns IloConcurrentChangeUpdatesSet\n\n
    getConcurrentChangeUpdates()\n
    '''
def getIssuesReport():
    '''returns IloIssuesReport\n\n
    getIssuesReport()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getPersistentID():
    '''returns String\n\n
    getPersistentID()\n
    '''
def getScenarioDiff():
    '''returns IloDifferencesSet\n\n
    getScenarioDiff(final ilog.odm.datasvc.IloScenario scenario)\n
    '''
def getScenarioExtensionContext():
    '''returns IloScenarioExtensionContext\n\n
    getScenarioExtensionContext()\n
    '''
def hasErrors():
    '''returns boolean\n\n
    hasErrors()\n
    '''
def hasWarnings():
    '''returns boolean\n\n
    hasWarnings()\n
    '''
def isDeleted():
    '''returns boolean\n\n
    isDeleted()\n
    '''
def isInBulkModifications():
    '''returns boolean\n\n
    isInBulkModifications()\n
    '''
def isInSync():
    '''returns boolean\n\n
    isInSync()\n
    '''
def isModified():
    '''returns boolean\n\n
    isModified()\n
    '''
def removeRepositoryChangeListener():
    '''returns None\n\n
    removeRepositoryChangeListener(final IloRepositoryChangeListener listener)\n
    '''
def revertFromRepository():
    '''returns None\n\n
    revertFromRepository()\n
    revertFromRepository(final ilog.odm.datasvc.IloScenario source_scenario, final Collection<IloSchema> schemas)\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def updateFromRepository():
    '''returns boolean\n\n
    updateFromRepository()\n
    '''
def getLastModificationDate():
    '''returns Date\n\n
    getLastModificationDate()\n
    '''
def areLocksInSync():
    '''returns boolean\n\n
    areLocksInSync()\n
    '''
def getLocks():
    '''returns Collection<IloLock>\n\n
    getLocks()\n
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
    removeLock(final IloLock lock)\n
    '''
def getTables():
    '''returns Collection<IloTable>\n\n
    getTables()\n
    '''
def transferLockOwnership():
    '''returns None\n\n
    transferLockOwnership(final ilog.odm.datasvc.internal.IloLock lock, final ilog.odm.datasvc.internal.IloUser otherUser)\n
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
