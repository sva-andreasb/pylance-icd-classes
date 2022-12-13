def ApiServerBean():
    '''    public ApiServerBean(final TopologyManagerFactory factory, final TopologyBuilderFactory topobuilderFactory, final ApiProps props, final BulkloadInterface bulkloadHandler, final String loginImplClass, final String principalBasedLogins)
    public ApiServerBean(final TopologyManagerFactory factory, final TopologyBuilderFactory topobuilderFactory, final ApiProps props, final BulkloadInterface bulkloadHandler, final String loginImplClass, final String principalBasedLogins, final boolean adapter)
    public ApiServerBean()
    '''
def readAdapterFilesFromFS():
    '''    public static boolean readAdapterFilesFromFS()
    '''
def isAllowPrincipalBasedLogins():
    '''    public boolean isAllowPrincipalBasedLogins()
    '''
def getLoginClass():
    '''    public ApiLoginInterface getLoginClass()
    '''
def getBulkloadHandler():
    '''    public BulkloadInterface getBulkloadHandler()
    '''
def setBulkloadHandler():
    '''    public void setBulkloadHandler(final BulkloadInterface bulkloadHandler)
    '''
def getTopobuilderFactory():
    '''    public TopologyBuilderFactory getTopobuilderFactory()
    '''
def setTopobuilderFactory():
    '''    public void setTopobuilderFactory(final TopologyBuilderFactory topobuilderFactory)
    '''
def getFactory():
    '''    public TopologyManagerFactory getFactory()
    '''
def setFactory():
    '''    public void setFactory(final TopologyManagerFactory factory)
    '''
def getProps():
    '''    public ApiProps getProps()
    '''
def setProps():
    '''    public void setProps(final ApiProps props)
    '''
def findXML():
    '''    public String findXML(final String sessionId, final Guid object_id, final int depth, final int indent, final Guid mss, final String[] permissions)
    '''
def findInitXML():
    '''    public void findInitXML(final String sessionId, final String root, final Guid[] guids, final int depth, final int fetch_size, final int indent, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions, final String suppressList)
    '''
def findInitData():
    '''    public void findInitData(final String sessionId, final String root, final Guid[] guids, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions)
    '''
def nextXML():
    '''    public String nextXML(final String sessionId)
    '''
def nextDataResult():
    '''    public ModelObject[] nextDataResult(final String sessionId, final int start, final int size, final int depth)
    '''
def findInitCursor():
    '''    public String findInitCursor(final String sessionId, final String query, final Guid mss, final String[] permissions)
    '''
def nextDataCursor():
    '''    public ModelObject[] nextDataCursor(final String sessionId, final String cursorId, final int start, final int size, final int depth)
    '''
def cursorSize():
    '''    public int cursorSize(final String sessionId, final String cursorId)
    '''
def closeCursor():
    '''    public void closeCursor(final String sessionId, final String cursorId)
    '''
def getClassNames():
    '''    public String[] getClassNames(final String session_id)
    '''
def insert():
    '''    public Guid[] insert(final String sessionId, final String xml, final boolean isImport, final Guid mss)
    '''
def deleteById():
    '''    public int deleteById(final String sessionId, final Guid objectId, final Guid mss)
    '''
def deleteMssObjLink():
    '''    public void deleteMssObjLink(final String sessionId, final Guid objGuid, final Guid mssGuid)
    '''
def startImport():
    '''    public void startImport(final String sessionId)
    '''
def stopImport():
    '''    public void stopImport(final String sessionId, final boolean rebuildTopo)
    '''
def startExport():
    '''    public void startExport(final String sessionId, final String sourceName)
    '''
def stopExport():
    '''    public void stopExport(final String sessionId)
    '''
def getTopLevelClasses():
    '''    public ArrayList getTopLevelClasses(final String sessionId)
    '''
def findChangeInit():
    '''    public void findChangeInit(final String session_id, final String root, final int depth, final long start, final long end, final int changeType, final int fetch_size)
    '''
def getInventorySummary():
    '''    public String getInventorySummary(final boolean cached, final String fileName)
    '''
def createVersion():
    '''    public long createVersion(final String name, final String description, final String sessionId)
    '''
def createEmptyVersion():
    '''    public long createEmptyVersion(final String name, final String description, final String sessionId)
    '''
def deleteVersion():
    '''    public void deleteVersion(final long verisonID, final String sessionId)
    '''
def getAllVersions():
    '''    public TopologyVersion[] getAllVersions(final String sessionId)
    '''
def update():
    '''    public Guid[] update(final String sessionId, final ModelObject[] objs, final Guid mss)
    '''
def updateMerge():
    '''    public LinkedHashMap updateMerge(final String sessionId, final ModelObject[] objs, final Guid mss)
    '''
def add():
    '''    public Guid[] add(final String sessionId, final ModelObject[] objs, final Guid mss)
    '''
def getAllMeta():
    '''    public ObjectClass[] getAllMeta(final boolean flatten)
    '''
def getMetaData():
    '''    public ObjectClass getMetaData(final String className, final boolean flatten)
    '''
def getResultMetaData():
    '''    public ResultMetaData getResultMetaData(final String sessionId, final String className, final LinkedHashMap attribs)
    public ResultMetaData getResultMetaData(final String sessionId, final String query)
    '''
def addArrayElements():
    '''    public void addArrayElements(final String sessionId, final Guid objectId, final String attrName, final Guid[] elements, final Guid mss)
    '''
def removeArrayElements():
    '''    public void removeArrayElements(final String sessionId, final Guid objectId, final String attrName, final Guid[] elements, final Guid mss)
    '''
def assignPersonInRoleToAccessCollection():
    '''    public void assignPersonInRoleToAccessCollection(final String sessionId, final Person user, final Role role, final Guid[] guids)
    '''
def removePersonInRoleToAccessCollection():
    '''    public void removePersonInRoleToAccessCollection(final String sessionId, final Person user, final Role role, final Guid[] guids)
    '''
def find():
    '''    public ModelObject[] find(final String sessionId, final Guid[] guids, final String query, final int depth, final String jdoQuery, final String jdoVardecl, final Guid mss, final String[] permissions)
    '''
def beginTransaction():
    '''    public void beginTransaction(final String sessionId, final int timeout)
    '''
def commitTransaction():
    '''    public void commitTransaction(final String sessionId)
    '''
def rollback():
    '''    public void rollback(final String sessionId)
    '''
def rebuildTopology():
    '''    public void rebuildTopology()
    '''
def findChanges():
    '''    public ModelObject[] findChanges(final String sessionId, final String query, final int depth, final long start, final long end, final int changeType)
    '''
def processChanges():
    '''    public void processChanges()
    '''
def startBulkload():
    '''    public long startBulkload(final long timeout)
    '''
def setBulkloadId():
    '''    public void setBulkloadId(final long bulkLoadId)
    '''
def endBulkload():
    '''    public void endBulkload(final long transactionId)
    '''
def isECMDB():
    '''    public boolean isECMDB(final String sessionId)
    '''
def login():
    '''    public String login(final String user, final String password, final String clientIp, final long version)
    public String login(final ApiPrincipal pr, final String clientIp, final long version)
    public String login(final long sessionId, final long version)
    '''
def logout():
    '''    public void logout(final String session_id)
    '''
def registerLocale():
    '''    public void registerLocale(final String sessionId, final Locale locale)
    '''
def unregisterLocale():
    '''    public void unregisterLocale(final String sessionId)
    '''
def getChangeHistoryInJava():
    '''    public ChangeHistory[] getChangeHistoryInJava(final String sessionId, final Guid[] objectIds, final long start, final long end, final boolean hierarchy)
    public ChangeHistory[] getChangeHistoryInJava(final String sessionId, final Guid[] objectIds, final long start, final long end, final int filterType, final boolean hierarchy)
    public ChangeHistory[] getChangeHistoryInJava(final String sessionId, final Guid objectId, final long start, final long end, final boolean hierarchy)
    '''
def getNumberOfChanges():
    '''    public int getNumberOfChanges(final String sessionId, final Guid[] Guids, final long start, final long end, final boolean hierarchy)
    '''
def getChangeHistory():
    '''    public ChangeHistory[] getChangeHistory(final String sessionId, final Guid[] Guids, final long start, final long end, final boolean hierarchy, final int offset, final int nextBatch)
    public String getChangeHistory(final String sessionId, final Guid[] objectIds, final long start, final long end, final boolean hierarchy)
    public String getChangeHistory(final String sessionId, final Guid[] objectIds, final long start, final long end, final int filterType, final boolean hierarchy)
    public String getChangeHistory(final String sessionId, final Guid objectId, final long start, final long end, final boolean hierarchy)
    '''
def getPropagatedChangesInJava():
    '''    public ChangeHistory[] getPropagatedChangesInJava(final String sessionId, final long primaryKey)
    '''
def getEDM():
    '''    public EDMInterface getEDM(final String session_id)
    '''
def setExtendedAttributes():
    '''    public void setExtendedAttributes(final String sessionId, final long version, final Guid objGuid, final AttrNameValue[] attrNameVal)
    '''
def addAccess():
    '''    public void addAccess(final String sessionId, final Principal user, final Resource resource, final String role, final String[] permissions)
    public void addAccess(final String sessionId, final Principal user, final AccessDefinition[] accessDefinitions)
    '''
def deleteAccess():
    '''    public void deleteAccess(final String sessionId, final Principal user, final Resource resource, final String role, final String[] permissions)
    '''
def getEntitlements():
    '''    public Resource[] getEntitlements(final String sessionId, final Principal user, final String[] permissions)
    '''
def getEntitlementsForRole():
    '''    public Resource[] getEntitlementsForRole(final String sessionId, final Principal user, final String role)
    '''
def getAccessDecisions():
    '''    public AccessDecision[] getAccessDecisions(final String sessionId, final Principal user, final Resource[] resources, final String[] permissions)
    '''
def getDataPermissions():
    '''    public String[] getDataPermissions(final String sessionId, final Principal user, final Resource[] resources)
    '''
def addRuntimeAccess():
    '''    public void addRuntimeAccess(final String sessionId, final Principal user, final String role, final String[] permissions)
    public void addRuntimeAccess(final Principal user, final String role, final String[] permissions)
    '''
def deleteRuntimeAccess():
    '''    public void deleteRuntimeAccess(final String sessionId, final Principal user, final String role, final String[] permissions)
    public void deleteRuntimeAccess(final Principal user, final String role, final String[] permissions)
    '''
def getRuntimeAccess():
    '''    public String[] getRuntimeAccess(final String sessionId, final Principal user)
    public String[] getRuntimeAccess(final Principal user)
    '''
def getRuntimeAccessDecisions():
    '''    public RuntimeAccessDecision[] getRuntimeAccessDecisions(final String sessionId, final Principal user, final String[] permissions)
    '''
def getRoles():
    '''    public String[] getRoles(final String sessionId, final Principal user)
    public String[] getRoles(final Principal user)
    '''
def deleteRole():
    '''    public void deleteRole(final String sessionId, final String role)
    public void deleteRole(final String role)
    '''
def deletePermission():
    '''    public void deletePermission(final String sessionId, final String permission)
    public void deletePermission(final String permission)
    '''
def deletePermissionFromRole():
    '''    public void deletePermissionFromRole(final String sessionId, final String role, final String permission)
    public void deletePermissionFromRole(final String role, final String permission)
    '''
def addDataPermissionToRole():
    '''    public void addDataPermissionToRole(final String sessionId, final String role, final String permission)
    public void addDataPermissionToRole(final String role, final String permission)
    '''
def addRuntimePermissionToRole():
    '''    public void addRuntimePermissionToRole(final String sessionId, final String role, final String permission)
    public void addRuntimePermissionToRole(final String role, final String permission)
    '''
def getMetaInfo():
    '''    public HashMap getMetaInfo(final String sessionId)
    '''
def getBlobInfo():
    '''    public HashMap getBlobInfo(final String sessionId)
    '''
def getAttributesWithReplacementValues():
    '''    public String[] getAttributesWithReplacementValues(final String sessionId, final String fqModelObjectClass)
    '''
def getReplacementValues():
    '''    public String[] getReplacementValues(final String sessionId, final String fqModelObjectClass, final String attribute)
    '''
def startDiscovery():
    '''    public void startDiscovery(final String session_id, final String[] scope, final String runName)
    '''
def abortDiscovery():
    '''    public void abortDiscovery(final String session_id)
    '''
def clearTopology():
    '''    public void clearTopology(final String session_id)
    '''
def synchScopes():
    '''    public void synchScopes(final String session_id)
    '''
def status():
    '''    public String status(final String session_id)
    '''
def getAnchorHosts():
    '''    public String[] getAnchorHosts(final String sessionId)
    '''
def setAnchorHosts():
    '''    public void setAnchorHosts(final String sessionId, final String[] hosts)
    '''
def getAnchorPort():
    '''    public int getAnchorPort(final String sessionId)
    '''
def setAnchorPort():
    '''    public void setAnchorPort(final String sessionId, final int port)
    '''
def getPropagatedChanges():
    '''    public String getPropagatedChanges(final String sessionId, final long primaryKey)
    '''
def defineExtendedAttributeMeta():
    '''    public void defineExtendedAttributeMeta(final long version, final UserDataMeta udm)
    '''
def getExtendedAttributeMeta():
    '''    public UserDataMeta[] getExtendedAttributeMeta(final long version, final String classname)
    '''
def getExtendedAttributes():
    '''    public AttrNameValue[] getExtendedAttributes(final String sessionId, final long version, final Guid objGuid)
    '''
def removeExtendedAttributeMeta():
    '''    public void removeExtendedAttributeMeta(final String sessionId, final long version, final String classname, final Guid acct)
    '''
def disableDiscovery():
    '''    public void disableDiscovery()
    '''
def enableDiscovery():
    '''    public void enableDiscovery()
    '''
def getUser():
    '''    public String getUser(final String sessionId)
    '''
def evaluateGuids():
    '''    public List evaluateGuids(final String sessionId, final ModelObject mo)
    '''
def getGuidAliases():
    '''    public List getGuidAliases(final String sessionId, final Guid guid)
    '''
def getChangedClasses():
    '''    public String[] getChangedClasses(final long start, final long end, final int changeType)
    '''
def generateExplicitRelationships():
    '''    public void generateExplicitRelationships()
    '''
def getAttrPrioClassMeta():
    '''    public String getAttrPrioClassMeta()
    '''
def getDataSources():
    '''    public ArrayList getDataSources(final String sessionId)
    '''
def setDataSources():
    '''    public Guid[] setDataSources(final String sessionId, final ArrayList dataSources)
    '''
def removeDataSources():
    '''    public void removeDataSources(final String sessionId, final ArrayList dataSources)
    '''
def getPriorityRules():
    '''    public ArrayList getPriorityRules(final String sessionId)
    '''
def setPriorityRules():
    '''    public Guid[] setPriorityRules(final String sessionId, final ArrayList priorityRules)
    '''
def removePriorityRules():
    '''    public void removePriorityRules(final String sessionId, final ArrayList priorityRules)
    '''
def mergeObjects():
    '''    public int mergeObjects(final String sessionId, final Guid durableGuid, final Guid transientGuid, final int mergeType)
    '''
def assignMssToDataSource():
    '''    public boolean assignMssToDataSource(final String sessionId, final Guid mssGuid, final AttributePrioDataSources apds)
    '''
