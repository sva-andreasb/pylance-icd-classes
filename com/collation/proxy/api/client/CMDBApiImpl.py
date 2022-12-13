def CMDBApiImpl():
'''public CMDBApiImpl(final ApiSession session)
'''
pass
def find():
'''public ModelObject[] find(final String query, final int depth, final Guid mss, final String[] permissions)
public ModelObject find(final Guid Guid, final int depth, final String[] permissions)
public ModelObject find(final Guid guid, final int depth, final Guid mss, final String[] permissions)
'''
pass
def findJDO():
'''public ModelObject[] findJDO(final String root, final String jdoQuery, final String jdoVarDecl, final int depth, final Guid mss, final String[] permissions)
'''
pass
def findXML():
'''public String findXML(final String query, final int depth, final int indent, final Guid mss, final String[] permissions)
public String findXML(final Guid Guid, final int indent, final int depth, final String[] permissions)
public void findXML(final String query, final int depth, final int indent, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions, final String suppressList, final OutputStream out)
public String findXML(final String query, final int depth, final int indent, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions, final String suppressList, final String outFile, final long maxFileSize)
'''
pass
def join():
'''public ModelObject[] join(final String query, final int depth, final Guid mss, final String[] permissions)
'''
pass
def executeQuery():
'''public DataResultSet executeQuery(final String query, final Guid mss, final String[] permissions)
'''
pass
def getMetaData():
'''public ObjectClass getMetaData(final String className)
public ObjectClass getMetaData(final String className, final Locale locale)
public ObjectClass getMetaData(final String className, final boolean flatten)
public ObjectClass getMetaData(final String className, final boolean flatten, final Locale locale)
'''
pass
def getAllMetaData():
'''public ObjectClass[] getAllMetaData()
public ObjectClass[] getAllMetaData(final Locale locale)
public ObjectClass[] getAllMetaData(final boolean flatten)
public ObjectClass[] getAllMetaData(final boolean flatten, final Locale locale)
'''
pass
def getClassNames():
'''public String[] getClassNames()
'''
pass
def registerManagementSoftwareSystem():
'''public Guid registerManagementSoftwareSystem(final ManagementSoftwareSystem mss)
'''
pass
def updateManagementSoftwareSystem():
'''public Guid updateManagementSoftwareSystem(final ManagementSoftwareSystem mss)
'''
pass
def deleteManagementSoftwareSystem():
'''public void deleteManagementSoftwareSystem(final Guid guid)
'''
pass
def getManagementSoftwareSystemLinks():
'''public MSSObjectLink[] getManagementSoftwareSystemLinks(final Guid guid, final Guid mss, final String[] permissions)
'''
pass
def getManagementSoftwareSystems():
'''public ManagementSoftwareSystem[] getManagementSoftwareSystems(final Guid guid, final String[] permissions)
'''
pass
def addRelationships():
'''public Guid[] addRelationships(final Relationship[] relationships, final Guid mss)
'''
pass
def deleteRelationships():
'''public void deleteRelationships(final Guid[] guids, final Guid mss)
public void deleteRelationships(final String type, final Guid source, final Guid target, final Guid mss)
'''
pass
def findRelationships():
'''public Relationship[] findRelationships(final Guid managedElementGuid, final int direction, final String type, final int scope, final String[] permissions)
'''
pass
def deleteStale():
'''public void deleteStale(final Guid mss, final long date)
'''
pass
def addCollectionMembers():
'''public void addCollectionMembers(final Guid collectionGuid, final Guid[] guids)
'''
pass
def removeCollectionMembers():
'''public void removeCollectionMembers(final Guid collectionGuid, final Guid[] guids)
'''
pass
def findCollections():
'''public Collection[] findCollections(final Guid guid, final String[] permissions)
'''
pass
def delete():
'''public int delete(final Guid[] guids, final Guid mss)
public int delete(final ModelObject[] obj, final Guid mss)
'''
pass
def findChanges():
'''public ModelObject[] findChanges(final String query, final int depth, final long start, final long end, final int changeType)
'''
pass
def getChangeHistory():
'''public ChangeHistory[] getChangeHistory(final Guid[] Guids, final long start, final long end)
public ChangeHistory[] getChangeHistory(final Guid[] guids, final long start, final long end, final int offset, final int nextBatch)
public ChangeHistory[] getChangeHistory(final Guid Guid, final long start, final long end)
public ChangeHistory[] getChangeHistory(final Guid[] Guids, final long start, final long end, final int filterType)
'''
pass
def getNumberOfChanges():
'''public int getNumberOfChanges(final Guid[] guids, final long start, final long end)
'''
pass
def getChangeHistoryFlat():
'''public ChangeHistory[] getChangeHistoryFlat(final Guid[] Guids, final long start, final long end)
public ChangeHistory[] getChangeHistoryFlat(final Guid Guid, final long start, final long end)
public ChangeHistory[] getChangeHistoryFlat(final Guid[] Guids, final long start, final long end, final int filterType)
'''
pass
def getPropagatedChanges():
'''public ChangeHistory[] getPropagatedChanges(final long primaryKey)
'''
pass
def getChangeHistoryInXML():
'''public String getChangeHistoryInXML(final Guid[] Guids, final long start, final long end)
public String getChangeHistoryInXML(final Guid Guid, final long start, final long end)
public String getChangeHistoryInXML(final Guid[] Guids, final long start, final long end, final int filterType)
'''
pass
def getChangeHistoryFlatInXML():
'''public String getChangeHistoryFlatInXML(final Guid[] Guids, final long start, final long end)
public String getChangeHistoryFlatInXML(final Guid Guid, final long start, final long end)
public String getChangeHistoryFlatInXML(final Guid[] Guids, final long start, final long end, final int filterType)
'''
pass
def getPropagatedChangesInXML():
'''public String getPropagatedChangesInXML(final long primaryKey)
'''
pass
def getVersion():
'''public TopologyVersion getVersion()
'''
pass
def update():
'''public Guid update(final ModelObject obj, final Guid mss)
public Guid[] update(final ModelObject[] obj, final Guid mss)
public Guid update(final ModelObject obj, final Guid mss, final String bidiFormat, final int bidiFlag)
public Guid update(final ModelObject obj, final Guid mss, final BidiProfile profile, final int bidiFlag)
public Guid[] update(final ModelObject[] objs, final Guid mss, final BidiProfile[] profile, final int[] bidiFlag)
public Guid[] update(final ModelObject[] objs, final Guid mss, final String[] bidiFormat, final int[] bidiFlag)
'''
pass
def updateXML():
'''public Guid[] updateXML(final String xml, final Guid mss)
'''
pass
def add():
'''public Guid[] add(final ModelObject[] obj, final Guid mss)
'''
pass
def beginTransaction():
'''public void beginTransaction(final int timeout)
public void beginTransaction()
'''
pass
def commitTransaction():
'''public void commitTransaction()
'''
pass
def rollback():
'''public void rollback()
'''
pass
def getConnection():
'''public ApiConnection getConnection()
'''
pass
def getSession():
'''public ApiSession getSession()
'''
pass
def release():
'''public void release()
'''
pass
def close():
'''public void close()
'''
pass
def addArrayElements():
'''public void addArrayElements(final Guid object, final String attrName, final Guid[] elements, final Guid mss)
'''
pass
def removeArrayElements():
'''public void removeArrayElements(final Guid object, final String attrName, final Guid[] elements, final Guid mss)
'''
pass
def importData():
'''public void importData(final URI source, final boolean rebuildTopo, final Guid mss)
'''
pass
def exportData():
'''public void exportData(final File directoryToWriteTo, final long maxFileSize, final Guid mss)
'''
pass
def defineExtendedAttributeMeta():
'''public void defineExtendedAttributeMeta(final UserDataMeta udm)
'''
pass
def getExtendedAttributeMeta():
'''public UserDataMeta[] getExtendedAttributeMeta(final String classname)
'''
pass
def setExtendedAttributes():
'''public void setExtendedAttributes(final Guid objGuid, final AttrNameValue[] attrNameVal)
'''
pass
def getExtendedAttributes():
'''public AttrNameValue[] getExtendedAttributes(final Guid objGuid)
'''
pass
def removeExtendedAttributeMeta():
'''public void removeExtendedAttributeMeta(final String classname, final Guid acct)
'''
pass
def findChangesInXml():
'''public String findChangesInXml(final String query, final int depth, final long start, final long end, final int changeType)
'''
pass
def getInventorySummary():
'''public String getInventorySummary(final boolean cached, final String fileName)
'''
pass
def getDetailsPanel():
'''public DetailPanelModel getDetailsPanel(final ObjectRef ref)
public DetailPanelModel getDetailsPanel(final ObjectRef ref, final Locale locale)
'''
pass
def getGraphView():
'''public TopologyGraphModel getGraphView(final ViewDefiner graphView)
'''
pass
def getGraphViewImage():
'''public ImageStream getGraphViewImage(final ViewDefiner graphView)
'''
pass
def getTreeView():
'''public TopologyTreeModel getTreeView(final ViewDefiner treeView)
'''
pass
def getNodeInfoMap():
'''public Map getNodeInfoMap()
'''
pass
def compare():
'''public ComparisonResult compare(final ObjectRef obj1, final ObjectRef[] objs, final CompareOptions opts)
public ComparisonResult compare(final ModelObject left, final ModelObject[] right, final CompareOptions opts)
'''
pass
def findImpactedBusinessApplications():
'''public Application[] findImpactedBusinessApplications(final Guid[] objects)
'''
pass
def findImpactedBusinessServices():
'''public BusinessSystem[] findImpactedBusinessServices(final Guid[] objects)
'''
pass
def startDiscovery():
'''public void startDiscovery(final String[] scope, final String runName)
public void startDiscovery(final RunDefinition runDef, final String runName)
public void startDiscovery(final Guid[] guidList, final String runName)
'''
pass
def abortDiscovery():
'''public void abortDiscovery()
'''
pass
def getStatus():
'''public String getStatus()
'''
pass
def rebuildTopology():
'''public void rebuildTopology()
'''
pass
def gcTopology():
'''public void gcTopology()
'''
pass
def clearTopology():
'''public void clearTopology()
'''
pass
def synchScopes():
'''public void synchScopes()
'''
pass
def setAnchorHosts():
'''public void setAnchorHosts(final String[] hosts)
'''
pass
def setAnchorPort():
'''public void setAnchorPort(final int port)
'''
pass
def getAnchorHosts():
'''public String[] getAnchorHosts()
'''
pass
def getAnchorPort():
'''public int getAnchorPort()
'''
pass
def createVersion():
'''public long createVersion(final String name, final String description)
'''
pass
def createEmptyVersion():
'''public long createEmptyVersion(final String name, final String description)
'''
pass
def deleteVersion():
'''public void deleteVersion(final long versionID)
'''
pass
def getAllVersions():
'''public TopologyVersion[] getAllVersions()
'''
pass
def disableDiscovery():
'''public void disableDiscovery()
'''
pass
def disableEvents():
'''public void disableEvents()
'''
pass
def enableDiscovery():
'''public void enableDiscovery()
'''
pass
def enableEvents():
'''public void enableEvents()
'''
pass
def addAccess():
'''public void addAccess(final Principal user, final Resource resource, final String role, final String[] permissions)
public void addAccess(final Principal user, final AccessDefinition[] accessDefinitions)
'''
pass
def deleteAccess():
'''public void deleteAccess(final Principal user, final Resource resource, final String role, final String[] permissions)
'''
pass
def getEntitlements():
'''public Resource[] getEntitlements(final Principal user, final String[] permissions)
'''
pass
def getEntitlementsForRole():
'''public Resource[] getEntitlementsForRole(final Principal user, final String role)
'''
pass
def addRuntimeAccess():
'''public void addRuntimeAccess(final Principal user, final String role, final String[] permissions)
'''
pass
def deleteRuntimeAccess():
'''public void deleteRuntimeAccess(final Principal user, final String role, final String[] permissions)
'''
pass
def getRuntimeAccess():
'''public String[] getRuntimeAccess(final Principal user)
'''
pass
def getRuntimeAccessDecisions():
'''public RuntimeAccessDecision[] getRuntimeAccessDecisions(final Principal user, final String[] permissions)
'''
pass
def assignPersonInRoleToAccessCollection():
'''public void assignPersonInRoleToAccessCollection(final Person user, final Role role, final Guid[] guids, final long[] versionId)
'''
pass
def removePersonInRoleToAccessCollection():
'''public void removePersonInRoleToAccessCollection(final Person user, final Role role, final Guid[] guids, final long[] versionId)
'''
pass
def getAccessDecisions():
'''public AccessDecision[] getAccessDecisions(final Principal user, final Resource[] resources, final String[] permissions)
'''
pass
def getDataPermissions():
'''public String[] getDataPermissions(final Principal user, final Resource[] resources)
'''
pass
def getRoles():
'''public String[] getRoles(final Principal user)
'''
pass
def deleteRole():
'''public void deleteRole(final String role)
'''
pass
def deletePermission():
'''public void deletePermission(final String permission)
'''
pass
def deletePermissionFromRole():
'''public void deletePermissionFromRole(final String role, final String permission)
'''
pass
def addDataPermissionToRole():
'''public void addDataPermissionToRole(final String role, final String permission)
'''
pass
def addRuntimePermissionToRole():
'''public void addRuntimePermissionToRole(final String role, final String permission)
'''
pass
def processChanges():
'''public void processChanges()
'''
pass
def startBulkload():
'''public long startBulkload(final long timeOutInSeconds)
'''
pass
def endBulkload():
'''public void endBulkload(final long transactionId)
'''
pass
def getDomain():
'''public CMDBDomain getDomain(final Guid obj)
'''
pass
def isECMDB():
'''public boolean isECMDB()
'''
pass
def getAttributesWithReplacementValues():
'''public String[] getAttributesWithReplacementValues(final String fqModelObjectClass)
'''
pass
def getReplacementValues():
'''public String[] getReplacementValues(final String fqModelObjectClass, final String attribute)
'''
pass
def updateMerge():
'''public Map updateMerge(final ModelObject[] objs, final Guid mss)
'''
pass
def getValidRelationshipTypes():
'''public RelationshipType[] getValidRelationshipTypes(final String sourceClass, final String targetClass)
'''
pass
def registerLocale():
'''public void registerLocale(final Locale locale)
'''
pass
def unregisterLocale():
'''public void unregisterLocale()
'''
pass
def getResultMetaData():
'''public ResultMetaData getResultMetaData(final String string, final String[] strings)
'''
pass
def getEDM():
'''public EDMInterface getEDM()
'''
pass
def evaluateGuids():
'''public GuidResult[] evaluateGuids(final ModelObject mo)
'''
pass
def getGuidAliases():
'''public Guid[] getGuidAliases(final Guid guid)
'''
pass
def getChangedClasses():
'''public String[] getChangedClasses(final long l, final long l1, final int i)
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
'''public ArrayList getDataSources()
'''
pass
def setDataSources():
'''public Guid[] setDataSources(final ArrayList dataSources)
'''
pass
def removeDataSources():
'''public void removeDataSources(final ArrayList dataSources)
'''
pass
def getPriorityRules():
'''public ArrayList getPriorityRules()
'''
pass
def setPriorityRules():
'''public Guid[] setPriorityRules(final ArrayList priorityRules)
'''
pass
def removePriorityRules():
'''public void removePriorityRules(final ArrayList priorityRules)
'''
pass
def mergeObjects():
'''public int mergeObjects(final Guid durableGuid, final Guid transientGuid, final int mergeType)
'''
pass
def assignMssToDataSource():
'''public boolean assignMssToDataSource(final Guid mssGuid, final AttributePrioDataSources apds)
'''
pass
def validateBidiFormat():
'''public boolean validateBidiFormat(final String bFormat)
'''
pass
def createBidiProfile():
'''public BidiProfile createBidiProfile(final String name, final String desc, final String format)
'''
pass
