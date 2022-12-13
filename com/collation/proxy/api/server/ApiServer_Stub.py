def ApiServer_Stub():
    '''public ApiServer_Stub(final RemoteRef ref)
    '''
def abortDiscovery():
    '''public void abortDiscovery(final String s)
    '''
def add():
    '''public Guid[] add(final String s, final ModelObject[] array, final Guid guid)
    '''
def addAccess():
    '''public void addAccess(final String s, final Principal principal, final Resource resource, final String s2, final String[] array)
    public void addAccess(final String s, final Principal principal, final AccessDefinition[] array)
    '''
def addArrayElements():
    '''public void addArrayElements(final String s, final Guid guid, final String s2, final Guid[] array, final Guid guid2)
    '''
def addDataPermissionToRole():
    '''public void addDataPermissionToRole(final String s, final String s2, final String s3)
    '''
def addLookupAttributes():
    '''public void addLookupAttributes(final Entry[] array)
    '''
def addLookupGroups():
    '''public void addLookupGroups(final String[] array)
    '''
def addLookupLocators():
    '''public void addLookupLocators(final LookupLocator[] array)
    '''
def addRemoteListener():
    '''public EventRegistration addRemoteListener(final RemoteEventListener remoteEventListener)
    '''
def addRuntimeAccess():
    '''public void addRuntimeAccess(final String s, final Principal principal, final String s2, final String[] array)
    '''
def addRuntimePermissionToRole():
    '''public void addRuntimePermissionToRole(final String s, final String s2, final String s3)
    '''
def assignMssToDataSource():
    '''public boolean assignMssToDataSource(final String s, final Guid guid, final AttributePrioDataSources attributePrioDataSources)
    '''
def assignPersonInRoleToAccessCollection():
    '''public void assignPersonInRoleToAccessCollection(final String s, final Person person, final Role role, final Guid[] array)
    '''
def beginTransaction():
    '''public void beginTransaction(final String s, final int value)
    '''
def clearTopology():
    '''public void clearTopology(final String s)
    '''
def closeCursor():
    '''public void closeCursor(final String s, final String s2)
    '''
def commitTransaction():
    '''public void commitTransaction(final String s)
    '''
def compare():
    '''public ComparisonResult compare(final String s, final ModelObject modelObject, final ModelObject[] array, final CompareOptions compareOptions)
    public ComparisonResult compare(final String s, final ObjectRef objectRef, final ObjectRef[] array, final CompareOptions compareOptions)
    '''
def createEmptyVersion():
    '''public long createEmptyVersion(final String s, final String s2, final String s3)
    '''
def createVersion():
    '''public long createVersion(final String s, final String s2, final String s3)
    '''
def cursorSize():
    '''public int cursorSize(final String s, final String s2)
    '''
def defineExtendedAttributeMeta():
    '''public void defineExtendedAttributeMeta(final long value, final UserDataMeta userDataMeta)
    '''
def deleteAccess():
    '''public void deleteAccess(final String s, final Principal principal, final Resource resource, final String s2, final String[] array)
    '''
def deleteById():
    '''public int deleteById(final String s, final Guid guid, final Guid guid2)
    '''
def deleteMssObjLink():
    '''public void deleteMssObjLink(final String s, final Guid guid, final Guid guid2)
    '''
def deletePermission():
    '''public void deletePermission(final String s, final String s2)
    '''
def deletePermissionFromRole():
    '''public void deletePermissionFromRole(final String s, final String s2, final String s3)
    '''
def deleteRole():
    '''public void deleteRole(final String s, final String s2)
    '''
def deleteRuntimeAccess():
    '''public void deleteRuntimeAccess(final String s, final Principal principal, final String s2, final String[] array)
    '''
def deleteVersion():
    '''public void deleteVersion(final long value, final String s)
    '''
def disableDiscovery():
    '''public void disableDiscovery()
    '''
def enableDiscovery():
    '''public void enableDiscovery()
    '''
def endBulkload():
    '''public void endBulkload(final long value)
    '''
def evaluateGuids():
    '''public List evaluateGuids(final String s, final ModelObject modelObject)
    '''
def find():
    '''public ModelObject[] find(final String s, final Guid[] array, final String s2, final int value, final String s3, final String s4, final Guid guid, final String[] array2)
    '''
def findChangeInit():
    '''public void findChangeInit(final String s, final String s2, final int value, final long value2, final long value3, final int value4, final int value5)
    '''
def findChanges():
    '''public ModelObject[] findChanges(final String s, final String s2, final int value, final long value2, final long value3, final int value4)
    '''
def findImpactedBusinessApplications():
    '''public Application[] findImpactedBusinessApplications(final String s, final Guid[] array, final long value)
    '''
def findImpactedBusinessServices():
    '''public BusinessSystem[] findImpactedBusinessServices(final String s, final Guid[] array, final long value)
    '''
def findInitCursor():
    '''public String findInitCursor(final String s, final String s2, final Guid guid, final String[] array)
    '''
def findInitData():
    '''public void findInitData(final String s, final String s2, final Guid[] array, final String s3, final String s4, final Guid guid, final String[] array2)
    '''
def findInitXML():
    '''public void findInitXML(final String s, final String s2, final Guid[] array, final int value, final int value2, final int value3, final String s3, final String s4, final Guid guid, final String[] array2, final String s5)
    '''
def findXML():
    '''public String findXML(final String s, final Guid guid, final int value, final int value2, final Guid guid2, final String[] array)
    '''
def generateExplicitRelationships():
    '''public void generateExplicitRelationships()
    '''
def getAccessDecisions():
    '''public AccessDecision[] getAccessDecisions(final String s, final Principal principal, final Resource[] array, final String[] array2)
    '''
def getAdmin():
    '''public Object getAdmin()
    '''
def getAllMeta():
    '''public ObjectClass[] getAllMeta(final boolean value)
    '''
def getAllVersions():
    '''public TopologyVersion[] getAllVersions(final String s)
    '''
def getAnchorHosts():
    '''public String[] getAnchorHosts(final String s)
    '''
def getAnchorPort():
    '''public int getAnchorPort(final String s)
    '''
def getAttrPrioClassMeta():
    '''public String getAttrPrioClassMeta()
    '''
def getAttributesWithReplacementValues():
    '''public String[] getAttributesWithReplacementValues(final String s, final String s2)
    '''
def getAuthMap():
    '''public AuthMap getAuthMap(final String s)
    '''
def getAvailableProcessors():
    '''public int getAvailableProcessors()
    '''
def getBlobInfo():
    '''public HashMap getBlobInfo(final String s)
    '''
def getChangeHistory():
    '''public String getChangeHistory(final String s, final Guid guid, final long value, final long value2, final boolean value3)
    public String getChangeHistory(final String s, final Guid[] array, final long value, final long value2, final int value3, final boolean value4)
    public String getChangeHistory(final String s, final Guid[] array, final long value, final long value2, final boolean value3)
    public ChangeHistory[] getChangeHistory(final String s, final Guid[] array, final long value, final long value2, final boolean value3, final int value4, final int value5)
    '''
def getChangeHistoryInJava():
    '''public ChangeHistory[] getChangeHistoryInJava(final String s, final Guid guid, final long value, final long value2, final boolean value3)
    public ChangeHistory[] getChangeHistoryInJava(final String s, final Guid[] array, final long value, final long value2, final int value3, final boolean value4)
    public ChangeHistory[] getChangeHistoryInJava(final String s, final Guid[] array, final long value, final long value2, final boolean value3)
    '''
def getChangedClasses():
    '''public String[] getChangedClasses(final long value, final long value2, final int value3)
    '''
def getClassNames():
    '''public String[] getClassNames(final String s)
    '''
def getDataPermissions():
    '''public String[] getDataPermissions(final String s, final Principal principal, final Resource[] array)
    '''
def getDataSources():
    '''public ArrayList getDataSources(final String s)
    '''
def getDetailsPanel():
    '''public DetailPanelModel getDetailsPanel(final String s, final Guid guid, final long value)
    public DetailPanelModel getDetailsPanel(final String s, final Guid guid, final long value, final Locale locale)
    '''
def getEDM():
    '''public EDMInterface getEDM(final String s)
    '''
def getEntitlements():
    '''public Resource[] getEntitlements(final String s, final Principal principal, final String[] array)
    '''
def getEntitlementsForRole():
    '''public Resource[] getEntitlementsForRole(final String s, final Principal principal, final String s2)
    '''
def getExtendedAttributeMeta():
    '''public UserDataMeta[] getExtendedAttributeMeta(final long value, final String s)
    '''
def getExtendedAttributes():
    '''public AttrNameValue[] getExtendedAttributes(final String s, final long value, final Guid guid)
    '''
def getFreeMemory():
    '''public long getFreeMemory()
    '''
def getGraphView():
    '''public TopologyGraphModel getGraphView(final String s, final ViewDefiner viewDefiner)
    '''
def getGraphViewImage():
    '''public ImageStream getGraphViewImage(final String s, final ViewDefiner viewDefiner)
    '''
def getGuidAliases():
    '''public List getGuidAliases(final String s, final Guid guid)
    '''
def getInventorySummary():
    '''public String getInventorySummary(final boolean value, final String s)
    '''
def getLookupAttributes():
    '''public Entry[] getLookupAttributes()
    '''
def getLookupGroups():
    '''public String[] getLookupGroups()
    '''
def getLookupLocators():
    '''public LookupLocator[] getLookupLocators()
    '''
def getMaxMemory():
    '''public long getMaxMemory()
    '''
def getMetaData():
    '''public ObjectClass getMetaData(final String s, final boolean value)
    '''
def getMetaInfo():
    '''public HashMap getMetaInfo(final String s)
    '''
def getNodeInfoMap():
    '''public Map getNodeInfoMap(final String s)
    '''
def getNumberOfChanges():
    '''public int getNumberOfChanges(final String s, final Guid[] array, final long value, final long value2, final boolean value3)
    '''
def getPriorityRules():
    '''public ArrayList getPriorityRules(final String s)
    '''
def getPropagatedChanges():
    '''public String getPropagatedChanges(final String s, final long value)
    '''
def getPropagatedChangesInJava():
    '''public ChangeHistory[] getPropagatedChangesInJava(final String s, final long value)
    '''
def getReplacementValues():
    '''public String[] getReplacementValues(final String s, final String s2, final String s3)
    '''
def getResultMetaData():
    '''public ResultMetaData getResultMetaData(final String s, final String s2)
    public ResultMetaData getResultMetaData(final String s, final String s2, final LinkedHashMap linkedHashMap)
    '''
def getRmiPort():
    '''public int getRmiPort()
    '''
def getRoles():
    '''public String[] getRoles(final String s, final Principal principal)
    '''
def getRuntimeAccess():
    '''public String[] getRuntimeAccess(final String s, final Principal principal)
    '''
def getRuntimeAccessDecisions():
    '''public RuntimeAccessDecision[] getRuntimeAccessDecisions(final String s, final Principal principal, final String[] array)
    '''
def getTopLevelClasses():
    '''public ArrayList getTopLevelClasses(final String s)
    '''
def getTotalMemory():
    '''public long getTotalMemory()
    '''
def getTreeView():
    '''public TopologyTreeModel getTreeView(final String s, final ViewDefiner viewDefiner)
    '''
def getUser():
    '''public String getUser(final String s)
    '''
def getWebPort():
    '''public int getWebPort()
    '''
def getWebSslPort():
    '''public int getWebSslPort()
    '''
def insert():
    '''public Guid[] insert(final String s, final String s2, final boolean value, final Guid guid)
    '''
def isECMDB():
    '''public boolean isECMDB(final String s)
    '''
def login():
    '''public String login(final long value, final long value2)
    public String login(final ApiPrincipal apiPrincipal, final String s, final long value)
    public String login(final String s, final String s2, final String s3, final long value)
    '''
def logout():
    '''public void logout(final String s)
    '''
def mergeObjects():
    '''public int mergeObjects(final String s, final Guid guid, final Guid guid2, final int value)
    '''
def modifyLookupAttributes():
    '''public void modifyLookupAttributes(final Entry[] array, final Entry[] array2)
    '''
def nextDataCursor():
    '''public ModelObject[] nextDataCursor(final String s, final String s2, final int value, final int value2, final int value3)
    '''
def nextDataResult():
    '''public ModelObject[] nextDataResult(final String s, final int value, final int value2, final int value3)
    '''
def nextXML():
    '''public String nextXML(final String s)
    '''
def ping():
    '''public boolean ping()
    '''
def processChanges():
    '''public void processChanges()
    '''
def rebuildTopology():
    '''public void rebuildTopology()
    '''
def registerLocale():
    '''public void registerLocale(final String s, final Locale locale)
    '''
def removeArrayElements():
    '''public void removeArrayElements(final String s, final Guid guid, final String s2, final Guid[] array, final Guid guid2)
    '''
def removeDataSources():
    '''public void removeDataSources(final String s, final ArrayList list)
    '''
def removeExtendedAttributeMeta():
    '''public void removeExtendedAttributeMeta(final String s, final long value, final String s2, final Guid guid)
    '''
def removeLookupGroups():
    '''public void removeLookupGroups(final String[] array)
    '''
def removeLookupLocators():
    '''public void removeLookupLocators(final LookupLocator[] array)
    '''
def removePersonInRoleToAccessCollection():
    '''public void removePersonInRoleToAccessCollection(final String s, final Person person, final Role role, final Guid[] array)
    '''
def removePriorityRules():
    '''public void removePriorityRules(final String s, final ArrayList list)
    '''
def removeRemoteListener():
    '''public void removeRemoteListener(final RemoteEventListener remoteEventListener)
    '''
def restart():
    '''public void restart()
    '''
def rollback():
    '''public void rollback(final String s)
    '''
def setAnchorHosts():
    '''public void setAnchorHosts(final String s, final String[] array)
    '''
def setAnchorPort():
    '''public void setAnchorPort(final String s, final int value)
    '''
def setAuthMap():
    '''public void setAuthMap(final String s, final AuthMap authMap)
    '''
def setDataSources():
    '''public Guid[] setDataSources(final String s, final ArrayList list)
    '''
def setExtendedAttributes():
    '''public void setExtendedAttributes(final String s, final long value, final Guid guid, final AttrNameValue[] array)
    '''
def setLookupGroups():
    '''public void setLookupGroups(final String[] array)
    '''
def setLookupLocators():
    '''public void setLookupLocators(final LookupLocator[] array)
    '''
def setPriorityRules():
    '''public Guid[] setPriorityRules(final String s, final ArrayList list)
    '''
def shutdown():
    '''public void shutdown()
    '''
def startBulkload():
    '''public long startBulkload(final long value)
    '''
def startDiscovery():
    '''public void startDiscovery(final String s, final RunDefinition runDefinition, final String s2)
    public void startDiscovery(final String s, final Guid[] array, final String s2)
    public void startDiscovery(final String s, final String[] array, final String s2)
    '''
def startExport():
    '''public void startExport(final String s, final String s2)
    '''
def startImport():
    '''public void startImport(final String s)
    '''
def status():
    '''public String status(final String s)
    '''
def stopExport():
    '''public void stopExport(final String s)
    '''
def stopImport():
    '''public void stopImport(final String s, final boolean value)
    '''
def synchScopes():
    '''public void synchScopes(final String s)
    '''
def unregisterLocale():
    '''public void unregisterLocale(final String s)
    '''
def update():
    '''public Guid[] update(final String s, final ModelObject[] array, final Guid guid)
    '''
def updateDomainPorts():
    '''public CMDBDomain updateDomainPorts(final CMDBDomain cmdbDomain)
    '''
def updateMerge():
    '''public Map updateMerge(final String s, final ModelObject[] array, final Guid guid)
    '''
