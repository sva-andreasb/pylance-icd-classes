def ApiServerBean():
'''public ApiServerBean(final TopologyManagerFactory factory, final TopologyBuilderFactory topobuilderFactory, final ApiProps props, final BulkloadInterface bulkloadHandler, final String loginImplClass, final String principalBasedLogins)
public ApiServerBean(final TopologyManagerFactory factory, final TopologyBuilderFactory topobuilderFactory, final ApiProps props, final BulkloadInterface bulkloadHandler, final String loginImplClass, final String principalBasedLogins, final boolean adapter)
public ApiServerBean()
'''
pass
def readAdapterFilesFromFS():
'''public static boolean readAdapterFilesFromFS()
'''
pass
def isAllowPrincipalBasedLogins():
'''public boolean isAllowPrincipalBasedLogins()
'''
pass
def getLoginClass():
'''public ApiLoginInterface getLoginClass()
'''
pass
def getBulkloadHandler():
'''public BulkloadInterface getBulkloadHandler()
'''
pass
def setBulkloadHandler():
'''public void setBulkloadHandler(final BulkloadInterface bulkloadHandler)
'''
pass
def getTopobuilderFactory():
'''public TopologyBuilderFactory getTopobuilderFactory()
'''
pass
def setTopobuilderFactory():
'''public void setTopobuilderFactory(final TopologyBuilderFactory topobuilderFactory)
'''
pass
def getFactory():
'''public TopologyManagerFactory getFactory()
'''
pass
def setFactory():
'''public void setFactory(final TopologyManagerFactory factory)
'''
pass
def getProps():
'''public ApiProps getProps()
'''
pass
def setProps():
'''public void setProps(final ApiProps props)
'''
pass
def findXML():
'''public String findXML(final String sessionId, final Guid object_id, final int depth, final int indent, final Guid mss, final String[] permissions)
'''
pass
def findInitXML():
'''public void findInitXML(final String sessionId, final String root, final Guid[] guids, final int depth, final int fetch_size, final int indent, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions, final String suppressList)
'''
pass
def findInitData():
'''public void findInitData(final String sessionId, final String root, final Guid[] guids, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions)
'''
pass
def nextXML():
'''public String nextXML(final String sessionId)
'''
pass
def nextDataResult():
'''public ModelObject[] nextDataResult(final String sessionId, final int start, final int size, final int depth)
'''
pass
def findInitCursor():
'''public String findInitCursor(final String sessionId, final String query, final Guid mss, final String[] permissions)
'''
pass
def nextDataCursor():
'''public ModelObject[] nextDataCursor(final String sessionId, final String cursorId, final int start, final int size, final int depth)
'''
pass
def cursorSize():
'''public int cursorSize(final String sessionId, final String cursorId)
'''
pass
def closeCursor():
'''public void closeCursor(final String sessionId, final String cursorId)
'''
pass
def getClassNames():
'''public String[] getClassNames(final String session_id)
'''
pass
def insert():
'''public Guid[] insert(final String sessionId, final String xml, final boolean isImport, final Guid mss)
'''
pass
def deleteById():
'''public int deleteById(final String sessionId, final Guid objectId, final Guid mss)
'''
pass
def deleteMssObjLink():
'''public void deleteMssObjLink(final String sessionId, final Guid objGuid, final Guid mssGuid)
'''
pass
def startImport():
'''public void startImport(final String sessionId)
'''
pass
def stopImport():
'''public void stopImport(final String sessionId, final boolean rebuildTopo)
'''
pass
def startExport():
'''public void startExport(final String sessionId, final String sourceName)
'''
pass
def stopExport():
'''public void stopExport(final String sessionId)
'''
pass
def getTopLevelClasses():
'''public ArrayList getTopLevelClasses(final String sessionId)
'''
pass
def findChangeInit():
'''public void findChangeInit(final String session_id, final String root, final int depth, final long start, final long end, final int changeType, final int fetch_size)
'''
pass
def getInventorySummary():
'''public String getInventorySummary(final boolean cached, final String fileName)
'''
pass
def createVersion():
'''public long createVersion(final String name, final String description, final String sessionId)
'''
pass
def createEmptyVersion():
'''public long createEmptyVersion(final String name, final String description, final String sessionId)
'''
pass
def deleteVersion():
'''public void deleteVersion(final long verisonID, final String sessionId)
'''
pass
def getAllVersions():
'''public TopologyVersion[] getAllVersions(final String sessionId)
'''
pass
def update():
'''public Guid[] update(final String sessionId, final ModelObject[] objs, final Guid mss)
'''
pass
def updateMerge():
'''public LinkedHashMap updateMerge(final String sessionId, final ModelObject[] objs, final Guid mss)
'''
pass
def add():
'''public Guid[] add(final String sessionId, final ModelObject[] objs, final Guid mss)
'''
pass
def getAllMeta():
'''public ObjectClass[] getAllMeta(final boolean flatten)
'''
pass
def getMetaData():
'''public ObjectClass getMetaData(final String className, final boolean flatten)
'''
pass
def getResultMetaData():
'''public ResultMetaData getResultMetaData(final String sessionId, final String className, final LinkedHashMap attribs)
public ResultMetaData getResultMetaData(final String sessionId, final String query)
'''
pass
def addArrayElements():
'''public void addArrayElements(final String sessionId, final Guid objectId, final String attrName, final Guid[] elements, final Guid mss)
'''
pass
def removeArrayElements():
'''public void removeArrayElements(final String sessionId, final Guid objectId, final String attrName, final Guid[] elements, final Guid mss)
'''
pass
def assignPersonInRoleToAccessCollection():
'''public void assignPersonInRoleToAccessCollection(final String sessionId, final Person user, final Role role, final Guid[] guids)
'''
pass
def removePersonInRoleToAccessCollection():
'''public void removePersonInRoleToAccessCollection(final String sessionId, final Person user, final Role role, final Guid[] guids)
'''
pass
def find():
'''public ModelObject[] find(final String sessionId, final Guid[] guids, final String query, final int depth, final String jdoQuery, final String jdoVardecl, final Guid mss, final String[] permissions)
'''
pass
def beginTransaction():
'''public void beginTransaction(final String sessionId, final int timeout)
'''
pass
def commitTransaction():
'''public void commitTransaction(final String sessionId)
'''
pass
def rollback():
'''public void rollback(final String sessionId)
'''
pass
def rebuildTopology():
'''public void rebuildTopology()
'''
pass
def findChanges():
'''public ModelObject[] findChanges(final String sessionId, final String query, final int depth, final long start, final long end, final int changeType)
'''
pass
def processChanges():
'''public void processChanges()
'''
pass
def startBulkload():
'''public long startBulkload(final long timeout)
'''
pass
def setBulkloadId():
'''public void setBulkloadId(final long bulkLoadId)
'''
pass
def endBulkload():
'''public void endBulkload(final long transactionId)
'''
pass
def isECMDB():
'''public boolean isECMDB(final String sessionId)
'''
pass
def login():
'''public String login(final String user, final String password, final String clientIp, final long version)
public String login(final ApiPrincipal pr, final String clientIp, final long version)
public String login(final long sessionId, final long version)
'''
pass
def logout():
'''public void logout(final String session_id)
'''
pass
def registerLocale():
'''public void registerLocale(final String sessionId, final Locale locale)
'''
pass
def unregisterLocale():
'''public void unregisterLocale(final String sessionId)
'''
pass
def getChangeHistoryInJava():
'''public ChangeHistory[] getChangeHistoryInJava(final String sessionId, final Guid[] objectIds, final long start, final long end, final boolean hierarchy)
public ChangeHistory[] getChangeHistoryInJava(final String sessionId, final Guid[] objectIds, final long start, final long end, final int filterType, final boolean hierarchy)
public ChangeHistory[] getChangeHistoryInJava(final String sessionId, final Guid objectId, final long start, final long end, final boolean hierarchy)
'''
pass
def getNumberOfChanges():
'''public int getNumberOfChanges(final String sessionId, final Guid[] Guids, final long start, final long end, final boolean hierarchy)
'''
pass
def getChangeHistory():
'''public ChangeHistory[] getChangeHistory(final String sessionId, final Guid[] Guids, final long start, final long end, final boolean hierarchy, final int offset, final int nextBatch)
public String getChangeHistory(final String sessionId, final Guid[] objectIds, final long start, final long end, final boolean hierarchy)
public String getChangeHistory(final String sessionId, final Guid[] objectIds, final long start, final long end, final int filterType, final boolean hierarchy)
public String getChangeHistory(final String sessionId, final Guid objectId, final long start, final long end, final boolean hierarchy)
'''
pass
def getPropagatedChangesInJava():
'''public ChangeHistory[] getPropagatedChangesInJava(final String sessionId, final long primaryKey)
'''
pass
def getEDM():
'''public EDMInterface getEDM(final String session_id)
'''
pass
def setExtendedAttributes():
'''public void setExtendedAttributes(final String sessionId, final long version, final Guid objGuid, final AttrNameValue[] attrNameVal)
'''
pass
def addAccess():
'''public void addAccess(final String sessionId, final Principal user, final Resource resource, final String role, final String[] permissions)
public void addAccess(final String sessionId, final Principal user, final AccessDefinition[] accessDefinitions)
'''
pass
def deleteAccess():
'''public void deleteAccess(final String sessionId, final Principal user, final Resource resource, final String role, final String[] permissions)
'''
pass
def getEntitlements():
'''public Resource[] getEntitlements(final String sessionId, final Principal user, final String[] permissions)
'''
pass
def getEntitlementsForRole():
'''public Resource[] getEntitlementsForRole(final String sessionId, final Principal user, final String role)
'''
pass
def getAccessDecisions():
'''public AccessDecision[] getAccessDecisions(final String sessionId, final Principal user, final Resource[] resources, final String[] permissions)
'''
pass
def getDataPermissions():
'''public String[] getDataPermissions(final String sessionId, final Principal user, final Resource[] resources)
'''
pass
def addRuntimeAccess():
'''public void addRuntimeAccess(final String sessionId, final Principal user, final String role, final String[] permissions)
public void addRuntimeAccess(final Principal user, final String role, final String[] permissions)
'''
pass
def deleteRuntimeAccess():
'''public void deleteRuntimeAccess(final String sessionId, final Principal user, final String role, final String[] permissions)
public void deleteRuntimeAccess(final Principal user, final String role, final String[] permissions)
'''
pass
def getRuntimeAccess():
'''public String[] getRuntimeAccess(final String sessionId, final Principal user)
public String[] getRuntimeAccess(final Principal user)
'''
pass
def getRuntimeAccessDecisions():
'''public RuntimeAccessDecision[] getRuntimeAccessDecisions(final String sessionId, final Principal user, final String[] permissions)
'''
pass
def getRoles():
'''public String[] getRoles(final String sessionId, final Principal user)
public String[] getRoles(final Principal user)
'''
pass
def deleteRole():
'''public void deleteRole(final String sessionId, final String role)
public void deleteRole(final String role)
'''
pass
def deletePermission():
'''public void deletePermission(final String sessionId, final String permission)
public void deletePermission(final String permission)
'''
pass
def deletePermissionFromRole():
'''public void deletePermissionFromRole(final String sessionId, final String role, final String permission)
public void deletePermissionFromRole(final String role, final String permission)
'''
pass
def addDataPermissionToRole():
'''public void addDataPermissionToRole(final String sessionId, final String role, final String permission)
public void addDataPermissionToRole(final String role, final String permission)
'''
pass
def addRuntimePermissionToRole():
'''public void addRuntimePermissionToRole(final String sessionId, final String role, final String permission)
public void addRuntimePermissionToRole(final String role, final String permission)
'''
pass
def getMetaInfo():
'''public HashMap getMetaInfo(final String sessionId)
'''
pass
def getBlobInfo():
'''public HashMap getBlobInfo(final String sessionId)
'''
pass
def getAttributesWithReplacementValues():
'''public String[] getAttributesWithReplacementValues(final String sessionId, final String fqModelObjectClass)
'''
pass
def getReplacementValues():
'''public String[] getReplacementValues(final String sessionId, final String fqModelObjectClass, final String attribute)
'''
pass
def startDiscovery():
'''public void startDiscovery(final String session_id, final String[] scope, final String runName)
'''
pass
def abortDiscovery():
'''public void abortDiscovery(final String session_id)
'''
pass
def clearTopology():
'''public void clearTopology(final String session_id)
'''
pass
def synchScopes():
'''public void synchScopes(final String session_id)
'''
pass
def status():
'''public String status(final String session_id)
'''
pass
def getAnchorHosts():
'''public String[] getAnchorHosts(final String sessionId)
'''
pass
def setAnchorHosts():
'''public void setAnchorHosts(final String sessionId, final String[] hosts)
'''
pass
def getAnchorPort():
'''public int getAnchorPort(final String sessionId)
'''
pass
def setAnchorPort():
'''public void setAnchorPort(final String sessionId, final int port)
'''
pass
def getPropagatedChanges():
'''public String getPropagatedChanges(final String sessionId, final long primaryKey)
'''
pass
def defineExtendedAttributeMeta():
'''public void defineExtendedAttributeMeta(final long version, final UserDataMeta udm)
'''
pass
def getExtendedAttributeMeta():
'''public UserDataMeta[] getExtendedAttributeMeta(final long version, final String classname)
'''
pass
def getExtendedAttributes():
'''public AttrNameValue[] getExtendedAttributes(final String sessionId, final long version, final Guid objGuid)
'''
pass
def removeExtendedAttributeMeta():
'''public void removeExtendedAttributeMeta(final String sessionId, final long version, final String classname, final Guid acct)
'''
pass
def disableDiscovery():
'''public void disableDiscovery()
'''
pass
def enableDiscovery():
'''public void enableDiscovery()
'''
pass
def getUser():
'''public String getUser(final String sessionId)
'''
pass
def evaluateGuids():
'''public List evaluateGuids(final String sessionId, final ModelObject mo)
'''
pass
def getGuidAliases():
'''public List getGuidAliases(final String sessionId, final Guid guid)
'''
pass
def getChangedClasses():
'''public String[] getChangedClasses(final long start, final long end, final int changeType)
'''
pass
def generateExplicitRelationships():
'''public void generateExplicitRelationships()
'''
pass
def getAttrPrioClassMeta():
'''public String getAttrPrioClassMeta()
'''
pass
def getDataSources():
'''public ArrayList getDataSources(final String sessionId)
'''
pass
def setDataSources():
'''public Guid[] setDataSources(final String sessionId, final ArrayList dataSources)
'''
pass
def removeDataSources():
'''public void removeDataSources(final String sessionId, final ArrayList dataSources)
'''
pass
def getPriorityRules():
'''public ArrayList getPriorityRules(final String sessionId)
'''
pass
def setPriorityRules():
'''public Guid[] setPriorityRules(final String sessionId, final ArrayList priorityRules)
'''
pass
def removePriorityRules():
'''public void removePriorityRules(final String sessionId, final ArrayList priorityRules)
'''
pass
def mergeObjects():
'''public int mergeObjects(final String sessionId, final Guid durableGuid, final Guid transientGuid, final int mergeType)
'''
pass
def assignMssToDataSource():
'''public boolean assignMssToDataSource(final String sessionId, final Guid mssGuid, final AttributePrioDataSources apds)
'''
pass
