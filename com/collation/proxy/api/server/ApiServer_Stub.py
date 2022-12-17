def ():
    '''returns ApiServer_Stub\n\n
    (final RemoteRef ref)\n
    '''
def abortDiscovery():
    '''returns None\n\n
    abortDiscovery(final String s)\n
    '''
def add():
    '''returns Guid[]\n\n
    add(final String s, final ModelObject[] array, final Guid guid)\n
    '''
def addAccess():
    '''returns None\n\n
    addAccess(final String s, final Principal principal, final Resource resource, final String s2, final String[] array)\n
    addAccess(final String s, final Principal principal, final AccessDefinition[] array)\n
    '''
def addArrayElements():
    '''returns None\n\n
    addArrayElements(final String s, final Guid guid, final String s2, final Guid[] array, final Guid guid2)\n
    '''
def addDataPermissionToRole():
    '''returns None\n\n
    addDataPermissionToRole(final String s, final String s2, final String s3)\n
    '''
def addLookupAttributes():
    '''returns None\n\n
    addLookupAttributes(final Entry[] array)\n
    '''
def addLookupGroups():
    '''returns None\n\n
    addLookupGroups(final String[] array)\n
    '''
def addLookupLocators():
    '''returns None\n\n
    addLookupLocators(final LookupLocator[] array)\n
    '''
def addRemoteListener():
    '''returns EventRegistration\n\n
    addRemoteListener(final RemoteEventListener remoteEventListener)\n
    '''
def addRuntimeAccess():
    '''returns None\n\n
    addRuntimeAccess(final String s, final Principal principal, final String s2, final String[] array)\n
    '''
def addRuntimePermissionToRole():
    '''returns None\n\n
    addRuntimePermissionToRole(final String s, final String s2, final String s3)\n
    '''
def assignMssToDataSource():
    '''returns boolean\n\n
    assignMssToDataSource(final String s, final Guid guid, final AttributePrioDataSources attributePrioDataSources)\n
    '''
def assignPersonInRoleToAccessCollection():
    '''returns None\n\n
    assignPersonInRoleToAccessCollection(final String s, final Person person, final Role role, final Guid[] array)\n
    '''
def beginTransaction():
    '''returns None\n\n
    beginTransaction(final String s, final int value)\n
    '''
def clearTopology():
    '''returns None\n\n
    clearTopology(final String s)\n
    '''
def closeCursor():
    '''returns None\n\n
    closeCursor(final String s, final String s2)\n
    '''
def commitTransaction():
    '''returns None\n\n
    commitTransaction(final String s)\n
    '''
def compare():
    '''returns ComparisonResult\n\n
    compare(final String s, final ModelObject modelObject, final ModelObject[] array, final CompareOptions compareOptions)\n
    compare(final String s, final ObjectRef objectRef, final ObjectRef[] array, final CompareOptions compareOptions)\n
    '''
def createEmptyVersion():
    '''returns long\n\n
    createEmptyVersion(final String s, final String s2, final String s3)\n
    '''
def createVersion():
    '''returns long\n\n
    createVersion(final String s, final String s2, final String s3)\n
    '''
def cursorSize():
    '''returns int\n\n
    cursorSize(final String s, final String s2)\n
    '''
def defineExtendedAttributeMeta():
    '''returns None\n\n
    defineExtendedAttributeMeta(final long value, final UserDataMeta userDataMeta)\n
    '''
def deleteAccess():
    '''returns None\n\n
    deleteAccess(final String s, final Principal principal, final Resource resource, final String s2, final String[] array)\n
    '''
def deleteById():
    '''returns int\n\n
    deleteById(final String s, final Guid guid, final Guid guid2)\n
    '''
def deleteMssObjLink():
    '''returns None\n\n
    deleteMssObjLink(final String s, final Guid guid, final Guid guid2)\n
    '''
def deletePermission():
    '''returns None\n\n
    deletePermission(final String s, final String s2)\n
    '''
def deletePermissionFromRole():
    '''returns None\n\n
    deletePermissionFromRole(final String s, final String s2, final String s3)\n
    '''
def deleteRole():
    '''returns None\n\n
    deleteRole(final String s, final String s2)\n
    '''
def deleteRuntimeAccess():
    '''returns None\n\n
    deleteRuntimeAccess(final String s, final Principal principal, final String s2, final String[] array)\n
    '''
def deleteVersion():
    '''returns None\n\n
    deleteVersion(final long value, final String s)\n
    '''
def disableDiscovery():
    '''returns None\n\n
    disableDiscovery()\n
    '''
def enableDiscovery():
    '''returns None\n\n
    enableDiscovery()\n
    '''
def endBulkload():
    '''returns None\n\n
    endBulkload(final long value)\n
    '''
def evaluateGuids():
    '''returns List\n\n
    evaluateGuids(final String s, final ModelObject modelObject)\n
    '''
def find():
    '''returns ModelObject[]\n\n
    find(final String s, final Guid[] array, final String s2, final int value, final String s3, final String s4, final Guid guid, final String[] array2)\n
    '''
def findChangeInit():
    '''returns None\n\n
    findChangeInit(final String s, final String s2, final int value, final long value2, final long value3, final int value4, final int value5)\n
    '''
def findChanges():
    '''returns ModelObject[]\n\n
    findChanges(final String s, final String s2, final int value, final long value2, final long value3, final int value4)\n
    '''
def findImpactedBusinessApplications():
    '''returns Application[]\n\n
    findImpactedBusinessApplications(final String s, final Guid[] array, final long value)\n
    '''
def findImpactedBusinessServices():
    '''returns BusinessSystem[]\n\n
    findImpactedBusinessServices(final String s, final Guid[] array, final long value)\n
    '''
def findInitCursor():
    '''returns String\n\n
    findInitCursor(final String s, final String s2, final Guid guid, final String[] array)\n
    '''
def findInitData():
    '''returns None\n\n
    findInitData(final String s, final String s2, final Guid[] array, final String s3, final String s4, final Guid guid, final String[] array2)\n
    '''
def findInitXML():
    '''returns None\n\n
    findInitXML(final String s, final String s2, final Guid[] array, final int value, final int value2, final int value3, final String s3, final String s4, final Guid guid, final String[] array2, final String s5)\n
    '''
def findXML():
    '''returns String\n\n
    findXML(final String s, final Guid guid, final int value, final int value2, final Guid guid2, final String[] array)\n
    '''
def generateExplicitRelationships():
    '''returns None\n\n
    generateExplicitRelationships()\n
    '''
def getAccessDecisions():
    '''returns AccessDecision[]\n\n
    getAccessDecisions(final String s, final Principal principal, final Resource[] array, final String[] array2)\n
    '''
def getAdmin():
    '''returns Object\n\n
    getAdmin()\n
    '''
def getAllMeta():
    '''returns ObjectClass[]\n\n
    getAllMeta(final boolean value)\n
    '''
def getAllVersions():
    '''returns TopologyVersion[]\n\n
    getAllVersions(final String s)\n
    '''
def getAnchorHosts():
    '''returns String[]\n\n
    getAnchorHosts(final String s)\n
    '''
def getAnchorPort():
    '''returns int\n\n
    getAnchorPort(final String s)\n
    '''
def getAttrPrioClassMeta():
    '''returns String\n\n
    getAttrPrioClassMeta()\n
    '''
def getAttributesWithReplacementValues():
    '''returns String[]\n\n
    getAttributesWithReplacementValues(final String s, final String s2)\n
    '''
def getAuthMap():
    '''returns AuthMap\n\n
    getAuthMap(final String s)\n
    '''
def getAvailableProcessors():
    '''returns int\n\n
    getAvailableProcessors()\n
    '''
def getBlobInfo():
    '''returns HashMap\n\n
    getBlobInfo(final String s)\n
    '''
def getChangeHistory():
    '''returns ChangeHistory[]\n\n
    getChangeHistory(final String s, final Guid guid, final long value, final long value2, final boolean value3)\n
    getChangeHistory(final String s, final Guid[] array, final long value, final long value2, final int value3, final boolean value4)\n
    getChangeHistory(final String s, final Guid[] array, final long value, final long value2, final boolean value3)\n
    getChangeHistory(final String s, final Guid[] array, final long value, final long value2, final boolean value3, final int value4, final int value5)\n
    '''
def getChangeHistoryInJava():
    '''returns ChangeHistory[]\n\n
    getChangeHistoryInJava(final String s, final Guid guid, final long value, final long value2, final boolean value3)\n
    getChangeHistoryInJava(final String s, final Guid[] array, final long value, final long value2, final int value3, final boolean value4)\n
    getChangeHistoryInJava(final String s, final Guid[] array, final long value, final long value2, final boolean value3)\n
    '''
def getChangedClasses():
    '''returns String[]\n\n
    getChangedClasses(final long value, final long value2, final int value3)\n
    '''
def getClassNames():
    '''returns String[]\n\n
    getClassNames(final String s)\n
    '''
def getDataPermissions():
    '''returns String[]\n\n
    getDataPermissions(final String s, final Principal principal, final Resource[] array)\n
    '''
def getDataSources():
    '''returns ArrayList\n\n
    getDataSources(final String s)\n
    '''
def getDetailsPanel():
    '''returns DetailPanelModel\n\n
    getDetailsPanel(final String s, final Guid guid, final long value)\n
    getDetailsPanel(final String s, final Guid guid, final long value, final Locale locale)\n
    '''
def getEDM():
    '''returns EDMInterface\n\n
    getEDM(final String s)\n
    '''
def getEntitlements():
    '''returns Resource[]\n\n
    getEntitlements(final String s, final Principal principal, final String[] array)\n
    '''
def getEntitlementsForRole():
    '''returns Resource[]\n\n
    getEntitlementsForRole(final String s, final Principal principal, final String s2)\n
    '''
def getExtendedAttributeMeta():
    '''returns UserDataMeta[]\n\n
    getExtendedAttributeMeta(final long value, final String s)\n
    '''
def getExtendedAttributes():
    '''returns AttrNameValue[]\n\n
    getExtendedAttributes(final String s, final long value, final Guid guid)\n
    '''
def getFreeMemory():
    '''returns long\n\n
    getFreeMemory()\n
    '''
def getGraphView():
    '''returns TopologyGraphModel\n\n
    getGraphView(final String s, final ViewDefiner viewDefiner)\n
    '''
def getGraphViewImage():
    '''returns ImageStream\n\n
    getGraphViewImage(final String s, final ViewDefiner viewDefiner)\n
    '''
def getGuidAliases():
    '''returns List\n\n
    getGuidAliases(final String s, final Guid guid)\n
    '''
def getInventorySummary():
    '''returns String\n\n
    getInventorySummary(final boolean value, final String s)\n
    '''
def getLookupAttributes():
    '''returns Entry[]\n\n
    getLookupAttributes()\n
    '''
def getLookupGroups():
    '''returns String[]\n\n
    getLookupGroups()\n
    '''
def getLookupLocators():
    '''returns LookupLocator[]\n\n
    getLookupLocators()\n
    '''
def getMaxMemory():
    '''returns long\n\n
    getMaxMemory()\n
    '''
def getMetaData():
    '''returns ObjectClass\n\n
    getMetaData(final String s, final boolean value)\n
    '''
def getMetaInfo():
    '''returns HashMap\n\n
    getMetaInfo(final String s)\n
    '''
def getNodeInfoMap():
    '''returns Map\n\n
    getNodeInfoMap(final String s)\n
    '''
def getNumberOfChanges():
    '''returns int\n\n
    getNumberOfChanges(final String s, final Guid[] array, final long value, final long value2, final boolean value3)\n
    '''
def getPriorityRules():
    '''returns ArrayList\n\n
    getPriorityRules(final String s)\n
    '''
def getPropagatedChanges():
    '''returns String\n\n
    getPropagatedChanges(final String s, final long value)\n
    '''
def getPropagatedChangesInJava():
    '''returns ChangeHistory[]\n\n
    getPropagatedChangesInJava(final String s, final long value)\n
    '''
def getReplacementValues():
    '''returns String[]\n\n
    getReplacementValues(final String s, final String s2, final String s3)\n
    '''
def getResultMetaData():
    '''returns ResultMetaData\n\n
    getResultMetaData(final String s, final String s2)\n
    getResultMetaData(final String s, final String s2, final LinkedHashMap linkedHashMap)\n
    '''
def getRmiPort():
    '''returns int\n\n
    getRmiPort()\n
    '''
def getRoles():
    '''returns String[]\n\n
    getRoles(final String s, final Principal principal)\n
    '''
def getRuntimeAccess():
    '''returns String[]\n\n
    getRuntimeAccess(final String s, final Principal principal)\n
    '''
def getRuntimeAccessDecisions():
    '''returns RuntimeAccessDecision[]\n\n
    getRuntimeAccessDecisions(final String s, final Principal principal, final String[] array)\n
    '''
def getTopLevelClasses():
    '''returns ArrayList\n\n
    getTopLevelClasses(final String s)\n
    '''
def getTotalMemory():
    '''returns long\n\n
    getTotalMemory()\n
    '''
def getTreeView():
    '''returns TopologyTreeModel\n\n
    getTreeView(final String s, final ViewDefiner viewDefiner)\n
    '''
def getUser():
    '''returns String\n\n
    getUser(final String s)\n
    '''
def getWebPort():
    '''returns int\n\n
    getWebPort()\n
    '''
def getWebSslPort():
    '''returns int\n\n
    getWebSslPort()\n
    '''
def insert():
    '''returns Guid[]\n\n
    insert(final String s, final String s2, final boolean value, final Guid guid)\n
    '''
def isECMDB():
    '''returns boolean\n\n
    isECMDB(final String s)\n
    '''
def login():
    '''returns String\n\n
    login(final long value, final long value2)\n
    login(final ApiPrincipal apiPrincipal, final String s, final long value)\n
    login(final String s, final String s2, final String s3, final long value)\n
    '''
def logout():
    '''returns None\n\n
    logout(final String s)\n
    '''
def mergeObjects():
    '''returns int\n\n
    mergeObjects(final String s, final Guid guid, final Guid guid2, final int value)\n
    '''
def modifyLookupAttributes():
    '''returns None\n\n
    modifyLookupAttributes(final Entry[] array, final Entry[] array2)\n
    '''
def nextDataCursor():
    '''returns ModelObject[]\n\n
    nextDataCursor(final String s, final String s2, final int value, final int value2, final int value3)\n
    '''
def nextDataResult():
    '''returns ModelObject[]\n\n
    nextDataResult(final String s, final int value, final int value2, final int value3)\n
    '''
def nextXML():
    '''returns String\n\n
    nextXML(final String s)\n
    '''
def ping():
    '''returns boolean\n\n
    ping()\n
    '''
def processChanges():
    '''returns None\n\n
    processChanges()\n
    '''
def rebuildTopology():
    '''returns None\n\n
    rebuildTopology()\n
    '''
def registerLocale():
    '''returns None\n\n
    registerLocale(final String s, final Locale locale)\n
    '''
def removeArrayElements():
    '''returns None\n\n
    removeArrayElements(final String s, final Guid guid, final String s2, final Guid[] array, final Guid guid2)\n
    '''
def removeDataSources():
    '''returns None\n\n
    removeDataSources(final String s, final ArrayList list)\n
    '''
def removeExtendedAttributeMeta():
    '''returns None\n\n
    removeExtendedAttributeMeta(final String s, final long value, final String s2, final Guid guid)\n
    '''
def removeLookupGroups():
    '''returns None\n\n
    removeLookupGroups(final String[] array)\n
    '''
def removeLookupLocators():
    '''returns None\n\n
    removeLookupLocators(final LookupLocator[] array)\n
    '''
def removePersonInRoleToAccessCollection():
    '''returns None\n\n
    removePersonInRoleToAccessCollection(final String s, final Person person, final Role role, final Guid[] array)\n
    '''
def removePriorityRules():
    '''returns None\n\n
    removePriorityRules(final String s, final ArrayList list)\n
    '''
def removeRemoteListener():
    '''returns None\n\n
    removeRemoteListener(final RemoteEventListener remoteEventListener)\n
    '''
def restart():
    '''returns None\n\n
    restart()\n
    '''
def rollback():
    '''returns None\n\n
    rollback(final String s)\n
    '''
def setAnchorHosts():
    '''returns None\n\n
    setAnchorHosts(final String s, final String[] array)\n
    '''
def setAnchorPort():
    '''returns None\n\n
    setAnchorPort(final String s, final int value)\n
    '''
def setAuthMap():
    '''returns None\n\n
    setAuthMap(final String s, final AuthMap authMap)\n
    '''
def setDataSources():
    '''returns Guid[]\n\n
    setDataSources(final String s, final ArrayList list)\n
    '''
def setExtendedAttributes():
    '''returns None\n\n
    setExtendedAttributes(final String s, final long value, final Guid guid, final AttrNameValue[] array)\n
    '''
def setLookupGroups():
    '''returns None\n\n
    setLookupGroups(final String[] array)\n
    '''
def setLookupLocators():
    '''returns None\n\n
    setLookupLocators(final LookupLocator[] array)\n
    '''
def setPriorityRules():
    '''returns Guid[]\n\n
    setPriorityRules(final String s, final ArrayList list)\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def startBulkload():
    '''returns long\n\n
    startBulkload(final long value)\n
    '''
def startDiscovery():
    '''returns None\n\n
    startDiscovery(final String s, final RunDefinition runDefinition, final String s2)\n
    startDiscovery(final String s, final Guid[] array, final String s2)\n
    startDiscovery(final String s, final String[] array, final String s2)\n
    '''
def startExport():
    '''returns None\n\n
    startExport(final String s, final String s2)\n
    '''
def startImport():
    '''returns None\n\n
    startImport(final String s)\n
    '''
def status():
    '''returns String\n\n
    status(final String s)\n
    '''
def stopExport():
    '''returns None\n\n
    stopExport(final String s)\n
    '''
def stopImport():
    '''returns None\n\n
    stopImport(final String s, final boolean value)\n
    '''
def synchScopes():
    '''returns None\n\n
    synchScopes(final String s)\n
    '''
def unregisterLocale():
    '''returns None\n\n
    unregisterLocale(final String s)\n
    '''
def update():
    '''returns Guid[]\n\n
    update(final String s, final ModelObject[] array, final Guid guid)\n
    '''
def updateDomainPorts():
    '''returns CMDBDomain\n\n
    updateDomainPorts(final CMDBDomain cmdbDomain)\n
    '''
def updateMerge():
    '''returns Map\n\n
    updateMerge(final String s, final ModelObject[] array, final Guid guid)\n
    '''
