def startDiscovery():
    '''returns None\n\n
    startDiscovery(final RunDefinition runDef, final String runName)\n
    startDiscovery(final Guid[] guidList, final String runName)\n
    startDiscovery(final String[] scope, final String runName)\n
    '''
def ():
    '''returns OalApiImpl\n\n
    (final ApiSession apiSession)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def find():
    '''returns ModelObject\n\n
    find(final String query, final int depth, final Guid mss, final String[] permissions)\n
    find(final Guid Guid, final int depth, final String[] permissions)\n
    find(final Guid guid, final int depth, final Guid mss, final String[] permissions)\n
    '''
def findJDO():
    '''returns ModelObject[]\n\n
    findJDO(final String root, final String jdoQuery, final String jdoVarDecl, final int depth, final Guid mss, final String[] permissions)\n
    '''
def findXML():
    '''returns String\n\n
    findXML(final String query, final int depth, final int indent, final Guid mss, final String[] permissions)\n
    findXML(final String query, final int depth, final int indent, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions, final String suppressList, final String outFile, final long maxFileSize)\n
    findXML(final String query, final int depth, final int indent, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions, final String suppressList, final OutputStream out)\n
    findXML(final Guid Guid, final int indent, final int depth, final String[] permissions)\n
    '''
def join():
    '''returns ModelObject[]\n\n
    join(final String query, final int depth, final Guid mss, final String[] permissions)\n
    '''
def executeQuery():
    '''returns DataResultSet\n\n
    executeQuery(final String query, final Guid mss, final String[] permissions)\n
    '''
def getMetaData():
    '''returns ObjectClass\n\n
    getMetaData(final String className)\n
    getMetaData(final String className, final Locale locale)\n
    getMetaData(final String className, final boolean flatten)\n
    getMetaData(final String className, final boolean flatten, final Locale locale)\n
    '''
def getAllMetaData():
    '''returns ObjectClass[]\n\n
    getAllMetaData()\n
    getAllMetaData(final Locale locale)\n
    getAllMetaData(final boolean flatten)\n
    getAllMetaData(final boolean flatten, final Locale locale)\n
    '''
def getClassNames():
    '''returns String[]\n\n
    getClassNames()\n
    '''
def delete():
    '''returns int\n\n
    delete(final Guid[] guids, final Guid mss)\n
    delete(final ModelObject[] obj, final Guid mss)\n
    '''
def findChanges():
    '''returns ModelObject[]\n\n
    findChanges(final String query, final int depth, final long start, final long end, final int changeType)\n
    '''
def findChangesInXml():
    '''returns String\n\n
    findChangesInXml(final String query, final int depth, final long start, final long end, final int changeType)\n
    '''
def getChangeHistory():
    '''returns ChangeHistory[]\n\n
    getChangeHistory(final Guid[] Guids, final long start, final long end)\n
    getChangeHistory(final Guid[] Guids, final long start, final long end, final int offset, final int nextBatch)\n
    getChangeHistory(final Guid Guid, final long start, final long end)\n
    getChangeHistory(final Guid[] Guids, final long start, final long end, final int filterType)\n
    '''
def getChangeHistoryFlat():
    '''returns ChangeHistory[]\n\n
    getChangeHistoryFlat(final Guid[] Guids, final long start, final long end)\n
    getChangeHistoryFlat(final Guid Guid, final long start, final long end)\n
    getChangeHistoryFlat(final Guid[] Guids, final long start, final long end, final int filterType)\n
    '''
def getNumberOfChanges():
    '''returns int\n\n
    getNumberOfChanges(final Guid[] Guids, final long start, final long end)\n
    '''
def getPropagatedChanges():
    '''returns ChangeHistory[]\n\n
    getPropagatedChanges(final long primaryKey)\n
    '''
def getChangeHistoryInXML():
    '''returns String\n\n
    getChangeHistoryInXML(final Guid[] Guids, final long start, final long end)\n
    getChangeHistoryInXML(final Guid Guid, final long start, final long end)\n
    getChangeHistoryInXML(final Guid[] Guids, final long start, final long end, final int filterType)\n
    '''
def getChangeHistoryFlatInXML():
    '''returns String\n\n
    getChangeHistoryFlatInXML(final Guid[] Guids, final long start, final long end)\n
    getChangeHistoryFlatInXML(final Guid Guid, final long start, final long end)\n
    getChangeHistoryFlatInXML(final Guid[] Guids, final long start, final long end, final int filterType)\n
    '''
def getPropagatedChangesInXML():
    '''returns String\n\n
    getPropagatedChangesInXML(final long primaryKey)\n
    '''
def getVersion():
    '''returns TopologyVersion\n\n
    getVersion()\n
    '''
def update():
    '''returns Guid[]\n\n
    update(final ModelObject obj, final Guid mss)\n
    update(final ModelObject[] obj, final Guid mss)\n
    update(final ModelObject obj, final Guid mss, final BidiProfile profile, final int bidiFlag)\n
    update(final ModelObject obj, final Guid mss, final String bidiFormat, final int bidiFlag)\n
    update(final ModelObject[] objs, final Guid mss, final BidiProfile[] profile, final int[] bidiFlag)\n
    update(final ModelObject[] objs, final Guid mss, final String[] bidiFormat, final int[] bidiFlag)\n
    '''
def updateMerge():
    '''returns LinkedHashMap\n\n
    updateMerge(final ModelObject[] objs, final Guid mss)\n
    '''
def updateXML():
    '''returns Guid[]\n\n
    updateXML(final String xml, final Guid mss)\n
    '''
def add():
    '''returns Guid[]\n\n
    add(final ModelObject[] obj, final Guid mss)\n
    '''
def beginTransaction():
    '''returns None\n\n
    beginTransaction(final int timeout)\n
    beginTransaction()\n
    '''
def commitTransaction():
    '''returns None\n\n
    commitTransaction()\n
    '''
def rollback():
    '''returns None\n\n
    rollback()\n
    '''
def getConnection():
    '''returns ApiConnection\n\n
    getConnection()\n
    '''
def getSession():
    '''returns ApiSession\n\n
    getSession()\n
    '''
def release():
    '''returns None\n\n
    release()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def addArrayElements():
    '''returns None\n\n
    addArrayElements(final Guid object, final String attrName, final Guid[] elements, final Guid mss)\n
    '''
def removeArrayElements():
    '''returns None\n\n
    removeArrayElements(final Guid object, final String attrName, final Guid[] elements, final Guid mss)\n
    '''
def importData():
    '''returns None\n\n
    importData(final URI source, final boolean rebuildTopo, final Guid mss)\n
    '''
def exportData():
    '''returns None\n\n
    exportData(final File directoryToWriteTo, final long maxFileSize, final Guid mss)\n
    '''
def defineExtendedAttributeMeta():
    '''returns None\n\n
    defineExtendedAttributeMeta(final UserDataMeta udm)\n
    '''
def getExtendedAttributeMeta():
    '''returns UserDataMeta[]\n\n
    getExtendedAttributeMeta(final String classname)\n
    '''
def setExtendedAttributes():
    '''returns None\n\n
    setExtendedAttributes(final Guid objGuid, final AttrNameValue[] attrNameVal)\n
    '''
def getExtendedAttributes():
    '''returns AttrNameValue[]\n\n
    getExtendedAttributes(final Guid objGuid)\n
    '''
def removeExtendedAttributeMeta():
    '''returns None\n\n
    removeExtendedAttributeMeta(final String classname, final Guid acct)\n
    '''
def getInventorySummary():
    '''returns String\n\n
    getInventorySummary(final boolean cached, final String fileName)\n
    '''
def getDomain():
    '''returns CMDBDomain\n\n
    getDomain(final Guid obj)\n
    '''
def isECMDB():
    '''returns boolean\n\n
    isECMDB()\n
    '''
def getDetailsPanel():
    '''returns DetailPanelModel\n\n
    getDetailsPanel(final ObjectRef ref)\n
    getDetailsPanel(final ObjectRef ref, final Locale locale)\n
    '''
def getGraphViewImage():
    '''returns ImageStream\n\n
    getGraphViewImage(final ViewDefiner graphView)\n
    '''
def getGraphView():
    '''returns TopologyGraphModel\n\n
    getGraphView(final ViewDefiner graphView)\n
    '''
def getTreeView():
    '''returns TopologyTreeModel\n\n
    getTreeView(final ViewDefiner treeView)\n
    '''
def getNodeInfoMap():
    '''returns Map\n\n
    getNodeInfoMap()\n
    '''
def compare():
    '''returns ComparisonResult\n\n
    compare(final ObjectRef obj1, final ObjectRef[] objs, final CompareOptions opts)\n
    compare(final ModelObject left, final ModelObject[] right, final CompareOptions opts)\n
    '''
def findImpactedBusinessApplications():
    '''returns Application[]\n\n
    findImpactedBusinessApplications(final Guid[] objects)\n
    '''
def findImpactedBusinessServices():
    '''returns BusinessSystem[]\n\n
    findImpactedBusinessServices(final Guid[] objects)\n
    '''
def registerManagementSoftwareSystem():
    '''returns Guid\n\n
    registerManagementSoftwareSystem(final ManagementSoftwareSystem mss)\n
    '''
def updateManagementSoftwareSystem():
    '''returns Guid\n\n
    updateManagementSoftwareSystem(final ManagementSoftwareSystem mss)\n
    '''
def deleteManagementSoftwareSystem():
    '''returns None\n\n
    deleteManagementSoftwareSystem(final Guid guid)\n
    '''
def getManagementSoftwareSystemLinks():
    '''returns MSSObjectLink[]\n\n
    getManagementSoftwareSystemLinks(final Guid guid, final Guid mss, final String[] permissions)\n
    '''
def getManagementSoftwareSystems():
    '''returns ManagementSoftwareSystem[]\n\n
    getManagementSoftwareSystems(final Guid guid, final String[] permissions)\n
    '''
def addRelationships():
    '''returns Guid[]\n\n
    addRelationships(final Relationship[] relationships, final Guid mss)\n
    '''
def deleteRelationships():
    '''returns None\n\n
    deleteRelationships(final Guid[] guids, final Guid mss)\n
    deleteRelationships(final String type, final Guid source, final Guid target, final Guid mss)\n
    '''
def findRelationships():
    '''returns Relationship[]\n\n
    findRelationships(final Guid managedElementGuid, final int direction, final String type, final int scope, final String[] permissions)\n
    '''
def deleteStale():
    '''returns None\n\n
    deleteStale(final Guid mss, final long date)\n
    '''
def addCollectionMembers():
    '''returns None\n\n
    addCollectionMembers(final Guid collectionGuid, final Guid[] guids)\n
    '''
def removeCollectionMembers():
    '''returns None\n\n
    removeCollectionMembers(final Guid collectionGuid, final Guid[] guids)\n
    '''
def findCollections():
    '''returns Collection[]\n\n
    findCollections(final Guid guid, final String[] permissions)\n
    '''
def getValidRelationshipTypes():
    '''returns RelationshipType[]\n\n
    getValidRelationshipTypes(final String sourceClass, final String targetClass)\n
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
    endBulkload(final long bulkloadId)\n
    '''
def registerLocale():
    '''returns None\n\n
    registerLocale(final Locale locale)\n
    '''
def unregisterLocale():
    '''returns None\n\n
    unregisterLocale()\n
    '''
def addAccess():
    '''returns None\n\n
    addAccess(final Principal user, final Resource resource, final String role, final String[] permissions)\n
    addAccess(final Principal user, final AccessDefinition[] accessDefinitions)\n
    '''
def deleteAccess():
    '''returns None\n\n
    deleteAccess(final Principal user, final Resource resource, final String role, final String[] permissions)\n
    '''
def getEntitlements():
    '''returns Resource[]\n\n
    getEntitlements(final Principal user, final String[] permissions)\n
    '''
def getEntitlementsForRole():
    '''returns Resource[]\n\n
    getEntitlementsForRole(final Principal user, final String role)\n
    '''
def getAccessDecisions():
    '''returns AccessDecision[]\n\n
    getAccessDecisions(final Principal user, final Resource[] resources, final String[] permissions)\n
    '''
def getDataPermissions():
    '''returns String[]\n\n
    getDataPermissions(final Principal user, final Resource[] resources)\n
    '''
def addRuntimeAccess():
    '''returns None\n\n
    addRuntimeAccess(final Principal user, final String role, final String[] permissions)\n
    '''
def deleteRuntimeAccess():
    '''returns None\n\n
    deleteRuntimeAccess(final Principal user, final String role, final String[] permissions)\n
    '''
def getRuntimeAccess():
    '''returns String[]\n\n
    getRuntimeAccess(final Principal user)\n
    '''
def getRuntimeAccessDecisions():
    '''returns RuntimeAccessDecision[]\n\n
    getRuntimeAccessDecisions(final Principal user, final String[] permissions)\n
    '''
def getRoles():
    '''returns String[]\n\n
    getRoles(final Principal user)\n
    '''
def assignPersonInRoleToAccessCollection():
    '''returns None\n\n
    assignPersonInRoleToAccessCollection(final Person user, final Role role, final Guid[] guids, final long[] versionId)\n
    '''
def removePersonInRoleToAccessCollection():
    '''returns None\n\n
    removePersonInRoleToAccessCollection(final Person user, final Role role, final Guid[] guids, final long[] versionId)\n
    '''
def deleteRole():
    '''returns None\n\n
    deleteRole(final String role)\n
    '''
def deletePermission():
    '''returns None\n\n
    deletePermission(final String permission)\n
    '''
def deletePermissionFromRole():
    '''returns None\n\n
    deletePermissionFromRole(final String role, final String permission)\n
    '''
def addDataPermissionToRole():
    '''returns None\n\n
    addDataPermissionToRole(final String role, final String permission)\n
    '''
def addRuntimePermissionToRole():
    '''returns None\n\n
    addRuntimePermissionToRole(final String role, final String permission)\n
    '''
def getAttributesWithReplacementValues():
    '''returns String[]\n\n
    getAttributesWithReplacementValues(final String fqModelObjectClass)\n
    '''
def getReplacementValues():
    '''returns String[]\n\n
    getReplacementValues(final String fqModelObjectClass, final String attribute)\n
    '''
def getResultMetaData():
    '''returns ResultMetaData\n\n
    getResultMetaData(final String className, final String[] attribs)\n
    '''
def getEDM():
    '''returns EDMInterface\n\n
    getEDM()\n
    '''
def evaluateGuids():
    '''returns GuidResult[]\n\n
    evaluateGuids(final ModelObject mo)\n
    '''
def getGuidAliases():
    '''returns Guid[]\n\n
    getGuidAliases(final Guid guid)\n
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
    getDataSources()\n
    '''
def setDataSources():
    '''returns Guid[]\n\n
    setDataSources(final ArrayList dataSources)\n
    '''
def removeDataSources():
    '''returns None\n\n
    removeDataSources(final ArrayList dataSources)\n
    '''
def getPriorityRules():
    '''returns ArrayList\n\n
    getPriorityRules()\n
    '''
def setPriorityRules():
    '''returns Guid[]\n\n
    setPriorityRules(final ArrayList priorityRules)\n
    '''
def removePriorityRules():
    '''returns None\n\n
    removePriorityRules(final ArrayList priorityRules)\n
    '''
def mergeObjects():
    '''returns int\n\n
    mergeObjects(final Guid durableGuid, final Guid transientGuid, final int mergeType)\n
    '''
def assignMssToDataSource():
    '''returns boolean\n\n
    assignMssToDataSource(final Guid mssGuid, final AttributePrioDataSources apds)\n
    '''
def createBidiProfile():
    '''returns BidiProfile\n\n
    createBidiProfile(final String name, final String desc, final String format)\n
    '''
def validateBidiFormat():
    '''returns boolean\n\n
    validateBidiFormat(final String bFormat)\n
    '''
