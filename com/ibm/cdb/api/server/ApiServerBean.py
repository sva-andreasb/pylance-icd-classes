def ():
    '''returns ApiServerBean\n\n
    (final TopologyManagerFactory factory, final TopologyBuilderFactory topobuilderFactory, final ApiProps props, final BulkloadInterface bulkloadHandler, final String loginImplClass, final String principalBasedLogins)\n
    (final TopologyManagerFactory factory, final TopologyBuilderFactory topobuilderFactory, final ApiProps props, final BulkloadInterface bulkloadHandler, final String loginImplClass, final String principalBasedLogins, final boolean adapter)\n
    ()\n
    '''
def isAllowPrincipalBasedLogins():
    '''returns boolean\n\n
    isAllowPrincipalBasedLogins()\n
    '''
def getLoginClass():
    '''returns ApiLoginInterface\n\n
    getLoginClass()\n
    '''
def getBulkloadHandler():
    '''returns BulkloadInterface\n\n
    getBulkloadHandler()\n
    '''
def setBulkloadHandler():
    '''returns None\n\n
    setBulkloadHandler(final BulkloadInterface bulkloadHandler)\n
    '''
def getTopobuilderFactory():
    '''returns TopologyBuilderFactory\n\n
    getTopobuilderFactory()\n
    '''
def setTopobuilderFactory():
    '''returns None\n\n
    setTopobuilderFactory(final TopologyBuilderFactory topobuilderFactory)\n
    '''
def getFactory():
    '''returns TopologyManagerFactory\n\n
    getFactory()\n
    '''
def setFactory():
    '''returns None\n\n
    setFactory(final TopologyManagerFactory factory)\n
    '''
def getProps():
    '''returns ApiProps\n\n
    getProps()\n
    '''
def setProps():
    '''returns None\n\n
    setProps(final ApiProps props)\n
    '''
def findXML():
    '''returns String\n\n
    findXML(final String sessionId, final Guid object_id, final int depth, final int indent, final Guid mss, final String[] permissions)\n
    '''
def findInitXML():
    '''returns None\n\n
    findInitXML(final String sessionId, final String root, final Guid[] guids, final int depth, final int fetch_size, final int indent, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions, final String suppressList)\n
    '''
def findInitData():
    '''returns None\n\n
    findInitData(final String sessionId, final String root, final Guid[] guids, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions)\n
    '''
def nextXML():
    '''returns String\n\n
    nextXML(final String sessionId)\n
    '''
def nextDataResult():
    '''returns ModelObject[]\n\n
    nextDataResult(final String sessionId, final int start, final int size, final int depth)\n
    '''
def findInitCursor():
    '''returns String\n\n
    findInitCursor(final String sessionId, final String query, final Guid mss, final String[] permissions)\n
    '''
def nextDataCursor():
    '''returns ModelObject[]\n\n
    nextDataCursor(final String sessionId, final String cursorId, final int start, final int size, final int depth)\n
    '''
def cursorSize():
    '''returns int\n\n
    cursorSize(final String sessionId, final String cursorId)\n
    '''
def closeCursor():
    '''returns None\n\n
    closeCursor(final String sessionId, final String cursorId)\n
    '''
def getClassNames():
    '''returns String[]\n\n
    getClassNames(final String session_id)\n
    '''
def insert():
    '''returns Guid[]\n\n
    insert(final String sessionId, final String xml, final boolean isImport, final Guid mss)\n
    '''
def deleteById():
    '''returns int\n\n
    deleteById(final String sessionId, final Guid objectId, final Guid mss)\n
    '''
def deleteMssObjLink():
    '''returns None\n\n
    deleteMssObjLink(final String sessionId, final Guid objGuid, final Guid mssGuid)\n
    '''
def startImport():
    '''returns None\n\n
    startImport(final String sessionId)\n
    '''
def stopImport():
    '''returns None\n\n
    stopImport(final String sessionId, final boolean rebuildTopo)\n
    '''
def startExport():
    '''returns None\n\n
    startExport(final String sessionId, final String sourceName)\n
    '''
def stopExport():
    '''returns None\n\n
    stopExport(final String sessionId)\n
    '''
def getTopLevelClasses():
    '''returns ArrayList\n\n
    getTopLevelClasses(final String sessionId)\n
    '''
def findChangeInit():
    '''returns None\n\n
    findChangeInit(final String session_id, final String root, final int depth, final long start, final long end, final int changeType, final int fetch_size)\n
    '''
def getInventorySummary():
    '''returns String\n\n
    getInventorySummary(final boolean cached, final String fileName)\n
    '''
def createVersion():
    '''returns long\n\n
    createVersion(final String name, final String description, final String sessionId)\n
    '''
def createEmptyVersion():
    '''returns long\n\n
    createEmptyVersion(final String name, final String description, final String sessionId)\n
    '''
def deleteVersion():
    '''returns None\n\n
    deleteVersion(final long verisonID, final String sessionId)\n
    '''
def getAllVersions():
    '''returns TopologyVersion[]\n\n
    getAllVersions(final String sessionId)\n
    '''
def update():
    '''returns Guid[]\n\n
    update(final String sessionId, final ModelObject[] objs, final Guid mss)\n
    '''
def updateMerge():
    '''returns LinkedHashMap\n\n
    updateMerge(final String sessionId, final ModelObject[] objs, final Guid mss)\n
    '''
def add():
    '''returns Guid[]\n\n
    add(final String sessionId, final ModelObject[] objs, final Guid mss)\n
    '''
def getAllMeta():
    '''returns ObjectClass[]\n\n
    getAllMeta(final boolean flatten)\n
    '''
def getMetaData():
    '''returns ObjectClass\n\n
    getMetaData(final String className, final boolean flatten)\n
    '''
def getResultMetaData():
    '''returns ResultMetaData\n\n
    getResultMetaData(final String sessionId, final String className, final LinkedHashMap attribs)\n
    getResultMetaData(final String sessionId, final String query)\n
    '''
def addArrayElements():
    '''returns None\n\n
    addArrayElements(final String sessionId, final Guid objectId, final String attrName, final Guid[] elements, final Guid mss)\n
    '''
def removeArrayElements():
    '''returns None\n\n
    removeArrayElements(final String sessionId, final Guid objectId, final String attrName, final Guid[] elements, final Guid mss)\n
    '''
def assignPersonInRoleToAccessCollection():
    '''returns None\n\n
    assignPersonInRoleToAccessCollection(final String sessionId, final Person user, final Role role, final Guid[] guids)\n
    '''
def removePersonInRoleToAccessCollection():
    '''returns None\n\n
    removePersonInRoleToAccessCollection(final String sessionId, final Person user, final Role role, final Guid[] guids)\n
    '''
def find():
    '''returns ModelObject[]\n\n
    find(final String sessionId, final Guid[] guids, final String query, final int depth, final String jdoQuery, final String jdoVardecl, final Guid mss, final String[] permissions)\n
    '''
def beginTransaction():
    '''returns None\n\n
    beginTransaction(final String sessionId, final int timeout)\n
    '''
def commitTransaction():
    '''returns None\n\n
    commitTransaction(final String sessionId)\n
    '''
def rollback():
    '''returns None\n\n
    rollback(final String sessionId)\n
    '''
def rebuildTopology():
    '''returns None\n\n
    rebuildTopology()\n
    '''
def findChanges():
    '''returns ModelObject[]\n\n
    findChanges(final String sessionId, final String query, final int depth, final long start, final long end, final int changeType)\n
    '''
def processChanges():
    '''returns None\n\n
    processChanges()\n
    '''
def startBulkload():
    '''returns long\n\n
    startBulkload(final long timeout)\n
    '''
def setBulkloadId():
    '''returns None\n\n
    setBulkloadId(final long bulkLoadId)\n
    '''
def endBulkload():
    '''returns None\n\n
    endBulkload(final long transactionId)\n
    '''
def isECMDB():
    '''returns boolean\n\n
    isECMDB(final String sessionId)\n
    '''
def login():
    '''returns String\n\n
    login(final String user, final String password, final String clientIp, final long version)\n
    login(final ApiPrincipal pr, final String clientIp, final long version)\n
    login(final long sessionId, final long version)\n
    '''
def logout():
    '''returns None\n\n
    logout(final String session_id)\n
    '''
def registerLocale():
    '''returns None\n\n
    registerLocale(final String sessionId, final Locale locale)\n
    '''
def unregisterLocale():
    '''returns None\n\n
    unregisterLocale(final String sessionId)\n
    '''
def getChangeHistoryInJava():
    '''returns ChangeHistory[]\n\n
    getChangeHistoryInJava(final String sessionId, final Guid[] objectIds, final long start, final long end, final boolean hierarchy)\n
    getChangeHistoryInJava(final String sessionId, final Guid[] objectIds, final long start, final long end, final int filterType, final boolean hierarchy)\n
    getChangeHistoryInJava(final String sessionId, final Guid objectId, final long start, final long end, final boolean hierarchy)\n
    '''
def getNumberOfChanges():
    '''returns int\n\n
    getNumberOfChanges(final String sessionId, final Guid[] Guids, final long start, final long end, final boolean hierarchy)\n
    '''
def getChangeHistory():
    '''returns String\n\n
    getChangeHistory(final String sessionId, final Guid[] Guids, final long start, final long end, final boolean hierarchy, final int offset, final int nextBatch)\n
    getChangeHistory(final String sessionId, final Guid[] objectIds, final long start, final long end, final boolean hierarchy)\n
    getChangeHistory(final String sessionId, final Guid[] objectIds, final long start, final long end, final int filterType, final boolean hierarchy)\n
    getChangeHistory(final String sessionId, final Guid objectId, final long start, final long end, final boolean hierarchy)\n
    '''
def getPropagatedChangesInJava():
    '''returns ChangeHistory[]\n\n
    getPropagatedChangesInJava(final String sessionId, final long primaryKey)\n
    '''
def getEDM():
    '''returns EDMInterface\n\n
    getEDM(final String session_id)\n
    '''
def setExtendedAttributes():
    '''returns None\n\n
    setExtendedAttributes(final String sessionId, final long version, final Guid objGuid, final AttrNameValue[] attrNameVal)\n
    '''
def addAccess():
    '''returns None\n\n
    addAccess(final String sessionId, final Principal user, final Resource resource, final String role, final String[] permissions)\n
    addAccess(final String sessionId, final Principal user, final AccessDefinition[] accessDefinitions)\n
    '''
def deleteAccess():
    '''returns None\n\n
    deleteAccess(final String sessionId, final Principal user, final Resource resource, final String role, final String[] permissions)\n
    '''
def getEntitlements():
    '''returns Resource[]\n\n
    getEntitlements(final String sessionId, final Principal user, final String[] permissions)\n
    '''
def getEntitlementsForRole():
    '''returns Resource[]\n\n
    getEntitlementsForRole(final String sessionId, final Principal user, final String role)\n
    '''
def getAccessDecisions():
    '''returns AccessDecision[]\n\n
    getAccessDecisions(final String sessionId, final Principal user, final Resource[] resources, final String[] permissions)\n
    '''
def getDataPermissions():
    '''returns String[]\n\n
    getDataPermissions(final String sessionId, final Principal user, final Resource[] resources)\n
    '''
def addRuntimeAccess():
    '''returns None\n\n
    addRuntimeAccess(final String sessionId, final Principal user, final String role, final String[] permissions)\n
    addRuntimeAccess(final Principal user, final String role, final String[] permissions)\n
    '''
def deleteRuntimeAccess():
    '''returns None\n\n
    deleteRuntimeAccess(final String sessionId, final Principal user, final String role, final String[] permissions)\n
    deleteRuntimeAccess(final Principal user, final String role, final String[] permissions)\n
    '''
def getRuntimeAccess():
    '''returns String[]\n\n
    getRuntimeAccess(final String sessionId, final Principal user)\n
    getRuntimeAccess(final Principal user)\n
    '''
def getRuntimeAccessDecisions():
    '''returns RuntimeAccessDecision[]\n\n
    getRuntimeAccessDecisions(final String sessionId, final Principal user, final String[] permissions)\n
    '''
def getRoles():
    '''returns String[]\n\n
    getRoles(final String sessionId, final Principal user)\n
    getRoles(final Principal user)\n
    '''
def deleteRole():
    '''returns None\n\n
    deleteRole(final String sessionId, final String role)\n
    deleteRole(final String role)\n
    '''
def deletePermission():
    '''returns None\n\n
    deletePermission(final String sessionId, final String permission)\n
    deletePermission(final String permission)\n
    '''
def deletePermissionFromRole():
    '''returns None\n\n
    deletePermissionFromRole(final String sessionId, final String role, final String permission)\n
    deletePermissionFromRole(final String role, final String permission)\n
    '''
def addDataPermissionToRole():
    '''returns None\n\n
    addDataPermissionToRole(final String sessionId, final String role, final String permission)\n
    addDataPermissionToRole(final String role, final String permission)\n
    '''
def addRuntimePermissionToRole():
    '''returns None\n\n
    addRuntimePermissionToRole(final String sessionId, final String role, final String permission)\n
    addRuntimePermissionToRole(final String role, final String permission)\n
    '''
def getMetaInfo():
    '''returns HashMap\n\n
    getMetaInfo(final String sessionId)\n
    '''
def getBlobInfo():
    '''returns HashMap\n\n
    getBlobInfo(final String sessionId)\n
    '''
def getAttributesWithReplacementValues():
    '''returns String[]\n\n
    getAttributesWithReplacementValues(final String sessionId, final String fqModelObjectClass)\n
    '''
def getReplacementValues():
    '''returns String[]\n\n
    getReplacementValues(final String sessionId, final String fqModelObjectClass, final String attribute)\n
    '''
def startDiscovery():
    '''returns None\n\n
    startDiscovery(final String session_id, final String[] scope, final String runName)\n
    '''
def abortDiscovery():
    '''returns None\n\n
    abortDiscovery(final String session_id)\n
    '''
def clearTopology():
    '''returns None\n\n
    clearTopology(final String session_id)\n
    '''
def synchScopes():
    '''returns None\n\n
    synchScopes(final String session_id)\n
    '''
def status():
    '''returns String\n\n
    status(final String session_id)\n
    '''
def getAnchorHosts():
    '''returns String[]\n\n
    getAnchorHosts(final String sessionId)\n
    '''
def setAnchorHosts():
    '''returns None\n\n
    setAnchorHosts(final String sessionId, final String[] hosts)\n
    '''
def getAnchorPort():
    '''returns int\n\n
    getAnchorPort(final String sessionId)\n
    '''
def setAnchorPort():
    '''returns None\n\n
    setAnchorPort(final String sessionId, final int port)\n
    '''
def getPropagatedChanges():
    '''returns String\n\n
    getPropagatedChanges(final String sessionId, final long primaryKey)\n
    '''
def defineExtendedAttributeMeta():
    '''returns None\n\n
    defineExtendedAttributeMeta(final long version, final UserDataMeta udm)\n
    '''
def getExtendedAttributeMeta():
    '''returns UserDataMeta[]\n\n
    getExtendedAttributeMeta(final long version, final String classname)\n
    '''
def getExtendedAttributes():
    '''returns AttrNameValue[]\n\n
    getExtendedAttributes(final String sessionId, final long version, final Guid objGuid)\n
    '''
def removeExtendedAttributeMeta():
    '''returns None\n\n
    removeExtendedAttributeMeta(final String sessionId, final long version, final String classname, final Guid acct)\n
    '''
def disableDiscovery():
    '''returns None\n\n
    disableDiscovery()\n
    '''
def enableDiscovery():
    '''returns None\n\n
    enableDiscovery()\n
    '''
def getUser():
    '''returns String\n\n
    getUser(final String sessionId)\n
    '''
def evaluateGuids():
    '''returns List\n\n
    evaluateGuids(final String sessionId, final ModelObject mo)\n
    '''
def getGuidAliases():
    '''returns List\n\n
    getGuidAliases(final String sessionId, final Guid guid)\n
    '''
def getChangedClasses():
    '''returns String[]\n\n
    getChangedClasses(final long start, final long end, final int changeType)\n
    '''
def generateExplicitRelationships():
    '''returns None\n\n
    generateExplicitRelationships()\n
    '''
def getAttrPrioClassMeta():
    '''returns String\n\n
    getAttrPrioClassMeta()\n
    '''
def getDataSources():
    '''returns ArrayList\n\n
    getDataSources(final String sessionId)\n
    '''
def setDataSources():
    '''returns Guid[]\n\n
    setDataSources(final String sessionId, final ArrayList dataSources)\n
    '''
def removeDataSources():
    '''returns None\n\n
    removeDataSources(final String sessionId, final ArrayList dataSources)\n
    '''
def getPriorityRules():
    '''returns ArrayList\n\n
    getPriorityRules(final String sessionId)\n
    '''
def setPriorityRules():
    '''returns Guid[]\n\n
    setPriorityRules(final String sessionId, final ArrayList priorityRules)\n
    '''
def removePriorityRules():
    '''returns None\n\n
    removePriorityRules(final String sessionId, final ArrayList priorityRules)\n
    '''
def mergeObjects():
    '''returns int\n\n
    mergeObjects(final String sessionId, final Guid durableGuid, final Guid transientGuid, final int mergeType)\n
    '''
def assignMssToDataSource():
    '''returns boolean\n\n
    assignMssToDataSource(final String sessionId, final Guid mssGuid, final AttributePrioDataSources apds)\n
    '''
