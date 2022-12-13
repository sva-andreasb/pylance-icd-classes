def CMDBApiImpl():
    '''public CMDBApiImpl(final ApiSession session)
    '''
def find():
    '''public ModelObject[] find(final String query, final int depth, final Guid mss, final String[] permissions)
    public ModelObject find(final Guid Guid, final int depth, final String[] permissions)
    public ModelObject find(final Guid guid, final int depth, final Guid mss, final String[] permissions)
    '''
def findJDO():
    '''public ModelObject[] findJDO(final String root, final String jdoQuery, final String jdoVarDecl, final int depth, final Guid mss, final String[] permissions)
    '''
def findXML():
    '''public String findXML(final String query, final int depth, final int indent, final Guid mss, final String[] permissions)
    public String findXML(final Guid Guid, final int indent, final int depth, final String[] permissions)
    public void findXML(final String query, final int depth, final int indent, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions, final String suppressList, final OutputStream out)
    public String findXML(final String query, final int depth, final int indent, final String jdoQuery, final String jdoVarDecl, final Guid mss, final String[] permissions, final String suppressList, final String outFile, final long maxFileSize)
    '''
def join():
    '''public ModelObject[] join(final String query, final int depth, final Guid mss, final String[] permissions)
    '''
def executeQuery():
    '''public DataResultSet executeQuery(final String query, final Guid mss, final String[] permissions)
    '''
def getMetaData():
    '''public ObjectClass getMetaData(final String className)
    public ObjectClass getMetaData(final String className, final Locale locale)
    public ObjectClass getMetaData(final String className, final boolean flatten)
    public ObjectClass getMetaData(final String className, final boolean flatten, final Locale locale)
    '''
def getAllMetaData():
    '''public ObjectClass[] getAllMetaData()
    public ObjectClass[] getAllMetaData(final Locale locale)
    public ObjectClass[] getAllMetaData(final boolean flatten)
    public ObjectClass[] getAllMetaData(final boolean flatten, final Locale locale)
    '''
def getClassNames():
    '''public String[] getClassNames()
    '''
def registerManagementSoftwareSystem():
    '''public Guid registerManagementSoftwareSystem(final ManagementSoftwareSystem mss)
    '''
def updateManagementSoftwareSystem():
    '''public Guid updateManagementSoftwareSystem(final ManagementSoftwareSystem mss)
    '''
def deleteManagementSoftwareSystem():
    '''public void deleteManagementSoftwareSystem(final Guid guid)
    '''
def getManagementSoftwareSystemLinks():
    '''public MSSObjectLink[] getManagementSoftwareSystemLinks(final Guid guid, final Guid mss, final String[] permissions)
    '''
def getManagementSoftwareSystems():
    '''public ManagementSoftwareSystem[] getManagementSoftwareSystems(final Guid guid, final String[] permissions)
    '''
def addRelationships():
    '''public Guid[] addRelationships(final Relationship[] relationships, final Guid mss)
    '''
def deleteRelationships():
    '''public void deleteRelationships(final Guid[] guids, final Guid mss)
    public void deleteRelationships(final String type, final Guid source, final Guid target, final Guid mss)
    '''
def findRelationships():
    '''public Relationship[] findRelationships(final Guid managedElementGuid, final int direction, final String type, final int scope, final String[] permissions)
    '''
def deleteStale():
    '''public void deleteStale(final Guid mss, final long date)
    '''
def addCollectionMembers():
    '''public void addCollectionMembers(final Guid collectionGuid, final Guid[] guids)
    '''
def removeCollectionMembers():
    '''public void removeCollectionMembers(final Guid collectionGuid, final Guid[] guids)
    '''
def findCollections():
    '''public Collection[] findCollections(final Guid guid, final String[] permissions)
    '''
def delete():
    '''public int delete(final Guid[] guids, final Guid mss)
    public int delete(final ModelObject[] obj, final Guid mss)
    '''
def findChanges():
    '''public ModelObject[] findChanges(final String query, final int depth, final long start, final long end, final int changeType)
    '''
def getChangeHistory():
    '''public ChangeHistory[] getChangeHistory(final Guid[] Guids, final long start, final long end)
    public ChangeHistory[] getChangeHistory(final Guid[] guids, final long start, final long end, final int offset, final int nextBatch)
    public ChangeHistory[] getChangeHistory(final Guid Guid, final long start, final long end)
    public ChangeHistory[] getChangeHistory(final Guid[] Guids, final long start, final long end, final int filterType)
    '''
def getNumberOfChanges():
    '''public int getNumberOfChanges(final Guid[] guids, final long start, final long end)
    '''
def getChangeHistoryFlat():
    '''public ChangeHistory[] getChangeHistoryFlat(final Guid[] Guids, final long start, final long end)
    public ChangeHistory[] getChangeHistoryFlat(final Guid Guid, final long start, final long end)
    public ChangeHistory[] getChangeHistoryFlat(final Guid[] Guids, final long start, final long end, final int filterType)
    '''
def getPropagatedChanges():
    '''public ChangeHistory[] getPropagatedChanges(final long primaryKey)
    '''
def getChangeHistoryInXML():
    '''public String getChangeHistoryInXML(final Guid[] Guids, final long start, final long end)
    public String getChangeHistoryInXML(final Guid Guid, final long start, final long end)
    public String getChangeHistoryInXML(final Guid[] Guids, final long start, final long end, final int filterType)
    '''
def getChangeHistoryFlatInXML():
    '''public String getChangeHistoryFlatInXML(final Guid[] Guids, final long start, final long end)
    public String getChangeHistoryFlatInXML(final Guid Guid, final long start, final long end)
    public String getChangeHistoryFlatInXML(final Guid[] Guids, final long start, final long end, final int filterType)
    '''
def getPropagatedChangesInXML():
    '''public String getPropagatedChangesInXML(final long primaryKey)
    '''
def getVersion():
    '''public TopologyVersion getVersion()
    '''
def update():
    '''public Guid update(final ModelObject obj, final Guid mss)
    public Guid[] update(final ModelObject[] obj, final Guid mss)
    public Guid update(final ModelObject obj, final Guid mss, final String bidiFormat, final int bidiFlag)
    public Guid update(final ModelObject obj, final Guid mss, final BidiProfile profile, final int bidiFlag)
    public Guid[] update(final ModelObject[] objs, final Guid mss, final BidiProfile[] profile, final int[] bidiFlag)
    public Guid[] update(final ModelObject[] objs, final Guid mss, final String[] bidiFormat, final int[] bidiFlag)
    '''
def updateXML():
    '''public Guid[] updateXML(final String xml, final Guid mss)
    '''
def add():
    '''public Guid[] add(final ModelObject[] obj, final Guid mss)
    '''
def beginTransaction():
    '''public void beginTransaction(final int timeout)
    public void beginTransaction()
    '''
def commitTransaction():
    '''public void commitTransaction()
    '''
def rollback():
    '''public void rollback()
    '''
def getConnection():
    '''public ApiConnection getConnection()
    '''
def getSession():
    '''public ApiSession getSession()
    '''
def release():
    '''public void release()
    '''
def close():
    '''public void close()
    '''
def addArrayElements():
    '''public void addArrayElements(final Guid object, final String attrName, final Guid[] elements, final Guid mss)
    '''
def removeArrayElements():
    '''public void removeArrayElements(final Guid object, final String attrName, final Guid[] elements, final Guid mss)
    '''
def importData():
    '''public void importData(final URI source, final boolean rebuildTopo, final Guid mss)
    '''
def exportData():
    '''public void exportData(final File directoryToWriteTo, final long maxFileSize, final Guid mss)
    '''
def defineExtendedAttributeMeta():
    '''public void defineExtendedAttributeMeta(final UserDataMeta udm)
    '''
def getExtendedAttributeMeta():
    '''public UserDataMeta[] getExtendedAttributeMeta(final String classname)
    '''
def setExtendedAttributes():
    '''public void setExtendedAttributes(final Guid objGuid, final AttrNameValue[] attrNameVal)
    '''
def getExtendedAttributes():
    '''public AttrNameValue[] getExtendedAttributes(final Guid objGuid)
    '''
def removeExtendedAttributeMeta():
    '''public void removeExtendedAttributeMeta(final String classname, final Guid acct)
    '''
def findChangesInXml():
    '''public String findChangesInXml(final String query, final int depth, final long start, final long end, final int changeType)
    '''
def getInventorySummary():
    '''public String getInventorySummary(final boolean cached, final String fileName)
    '''
def getDetailsPanel():
    '''public DetailPanelModel getDetailsPanel(final ObjectRef ref)
    public DetailPanelModel getDetailsPanel(final ObjectRef ref, final Locale locale)
    '''
def getGraphView():
    '''public TopologyGraphModel getGraphView(final ViewDefiner graphView)
    '''
def getGraphViewImage():
    '''public ImageStream getGraphViewImage(final ViewDefiner graphView)
    '''
def getTreeView():
    '''public TopologyTreeModel getTreeView(final ViewDefiner treeView)
    '''
def getNodeInfoMap():
    '''public Map getNodeInfoMap()
    '''
def compare():
    '''public ComparisonResult compare(final ObjectRef obj1, final ObjectRef[] objs, final CompareOptions opts)
    public ComparisonResult compare(final ModelObject left, final ModelObject[] right, final CompareOptions opts)
    '''
def findImpactedBusinessApplications():
    '''public Application[] findImpactedBusinessApplications(final Guid[] objects)
    '''
def findImpactedBusinessServices():
    '''public BusinessSystem[] findImpactedBusinessServices(final Guid[] objects)
    '''
def startDiscovery():
    '''public void startDiscovery(final String[] scope, final String runName)
    public void startDiscovery(final RunDefinition runDef, final String runName)
    public void startDiscovery(final Guid[] guidList, final String runName)
    '''
def abortDiscovery():
    '''public void abortDiscovery()
    '''
def getStatus():
    '''public String getStatus()
    '''
def rebuildTopology():
    '''public void rebuildTopology()
    '''
def gcTopology():
    '''public void gcTopology()
    '''
def clearTopology():
    '''public void clearTopology()
    '''
def synchScopes():
    '''public void synchScopes()
    '''
def setAnchorHosts():
    '''public void setAnchorHosts(final String[] hosts)
    '''
def setAnchorPort():
    '''public void setAnchorPort(final int port)
    '''
def getAnchorHosts():
    '''public String[] getAnchorHosts()
    '''
def getAnchorPort():
    '''public int getAnchorPort()
    '''
def createVersion():
    '''public long createVersion(final String name, final String description)
    '''
def createEmptyVersion():
    '''public long createEmptyVersion(final String name, final String description)
    '''
def deleteVersion():
    '''public void deleteVersion(final long versionID)
    '''
def getAllVersions():
    '''public TopologyVersion[] getAllVersions()
    '''
def disableDiscovery():
    '''public void disableDiscovery()
    '''
def disableEvents():
    '''public void disableEvents()
    '''
def enableDiscovery():
    '''public void enableDiscovery()
    '''
def enableEvents():
    '''public void enableEvents()
    '''
def addAccess():
    '''public void addAccess(final Principal user, final Resource resource, final String role, final String[] permissions)
    public void addAccess(final Principal user, final AccessDefinition[] accessDefinitions)
    '''
def deleteAccess():
    '''public void deleteAccess(final Principal user, final Resource resource, final String role, final String[] permissions)
    '''
def getEntitlements():
    '''public Resource[] getEntitlements(final Principal user, final String[] permissions)
    '''
def getEntitlementsForRole():
    '''public Resource[] getEntitlementsForRole(final Principal user, final String role)
    '''
def addRuntimeAccess():
    '''public void addRuntimeAccess(final Principal user, final String role, final String[] permissions)
    '''
def deleteRuntimeAccess():
    '''public void deleteRuntimeAccess(final Principal user, final String role, final String[] permissions)
    '''
def getRuntimeAccess():
    '''public String[] getRuntimeAccess(final Principal user)
    '''
def getRuntimeAccessDecisions():
    '''public RuntimeAccessDecision[] getRuntimeAccessDecisions(final Principal user, final String[] permissions)
    '''
def assignPersonInRoleToAccessCollection():
    '''public void assignPersonInRoleToAccessCollection(final Person user, final Role role, final Guid[] guids, final long[] versionId)
    '''
def removePersonInRoleToAccessCollection():
    '''public void removePersonInRoleToAccessCollection(final Person user, final Role role, final Guid[] guids, final long[] versionId)
    '''
def getAccessDecisions():
    '''public AccessDecision[] getAccessDecisions(final Principal user, final Resource[] resources, final String[] permissions)
    '''
def getDataPermissions():
    '''public String[] getDataPermissions(final Principal user, final Resource[] resources)
    '''
def getRoles():
    '''public String[] getRoles(final Principal user)
    '''
def deleteRole():
    '''public void deleteRole(final String role)
    '''
def deletePermission():
    '''public void deletePermission(final String permission)
    '''
def deletePermissionFromRole():
    '''public void deletePermissionFromRole(final String role, final String permission)
    '''
def addDataPermissionToRole():
    '''public void addDataPermissionToRole(final String role, final String permission)
    '''
def addRuntimePermissionToRole():
    '''public void addRuntimePermissionToRole(final String role, final String permission)
    '''
def processChanges():
    '''public void processChanges()
    '''
def startBulkload():
    '''public long startBulkload(final long timeOutInSeconds)
    '''
def endBulkload():
    '''public void endBulkload(final long transactionId)
    '''
def getDomain():
    '''public CMDBDomain getDomain(final Guid obj)
    '''
def isECMDB():
    '''public boolean isECMDB()
    '''
def getAttributesWithReplacementValues():
    '''public String[] getAttributesWithReplacementValues(final String fqModelObjectClass)
    '''
def getReplacementValues():
    '''public String[] getReplacementValues(final String fqModelObjectClass, final String attribute)
    '''
def updateMerge():
    '''public Map updateMerge(final ModelObject[] objs, final Guid mss)
    '''
def getValidRelationshipTypes():
    '''public RelationshipType[] getValidRelationshipTypes(final String sourceClass, final String targetClass)
    '''
def registerLocale():
    '''public void registerLocale(final Locale locale)
    '''
def unregisterLocale():
    '''public void unregisterLocale()
    '''
def getResultMetaData():
    '''public ResultMetaData getResultMetaData(final String string, final String[] strings)
    '''
def getEDM():
    '''public EDMInterface getEDM()
    '''
def evaluateGuids():
    '''public GuidResult[] evaluateGuids(final ModelObject mo)
    '''
def getGuidAliases():
    '''public Guid[] getGuidAliases(final Guid guid)
    '''
def getChangedClasses():
    '''public String[] getChangedClasses(final long l, final long l1, final int i)
    '''
def generateExplicitRelationships():
    '''public void generateExplicitRelationships()
    '''
def getAttrPrioClassMeta():
    '''public String getAttrPrioClassMeta()
    '''
def getDataSources():
    '''public ArrayList getDataSources()
    '''
def setDataSources():
    '''public Guid[] setDataSources(final ArrayList dataSources)
    '''
def removeDataSources():
    '''public void removeDataSources(final ArrayList dataSources)
    '''
def getPriorityRules():
    '''public ArrayList getPriorityRules()
    '''
def setPriorityRules():
    '''public Guid[] setPriorityRules(final ArrayList priorityRules)
    '''
def removePriorityRules():
    '''public void removePriorityRules(final ArrayList priorityRules)
    '''
def mergeObjects():
    '''public int mergeObjects(final Guid durableGuid, final Guid transientGuid, final int mergeType)
    '''
def assignMssToDataSource():
    '''public boolean assignMssToDataSource(final Guid mssGuid, final AttributePrioDataSources apds)
    '''
def validateBidiFormat():
    '''public boolean validateBidiFormat(final String bFormat)
    '''
def createBidiProfile():
    '''public BidiProfile createBidiProfile(final String name, final String desc, final String format)
    '''
