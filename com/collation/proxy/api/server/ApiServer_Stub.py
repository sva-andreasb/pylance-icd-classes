def ApiServer_Stub():
'''public ApiServer_Stub(final RemoteRef ref)
'''
pass
def abortDiscovery():
'''public void abortDiscovery(final String s)
'''
pass
def add():
'''public Guid[] add(final String s, final ModelObject[] array, final Guid guid)
'''
pass
def addAccess():
'''public void addAccess(final String s, final Principal principal, final Resource resource, final String s2, final String[] array)
public void addAccess(final String s, final Principal principal, final AccessDefinition[] array)
'''
pass
def addArrayElements():
'''public void addArrayElements(final String s, final Guid guid, final String s2, final Guid[] array, final Guid guid2)
'''
pass
def addDataPermissionToRole():
'''public void addDataPermissionToRole(final String s, final String s2, final String s3)
'''
pass
def addLookupAttributes():
'''public void addLookupAttributes(final Entry[] array)
'''
pass
def addLookupGroups():
'''public void addLookupGroups(final String[] array)
'''
pass
def addLookupLocators():
'''public void addLookupLocators(final LookupLocator[] array)
'''
pass
def addRemoteListener():
'''public EventRegistration addRemoteListener(final RemoteEventListener remoteEventListener)
'''
pass
def addRuntimeAccess():
'''public void addRuntimeAccess(final String s, final Principal principal, final String s2, final String[] array)
'''
pass
def addRuntimePermissionToRole():
'''public void addRuntimePermissionToRole(final String s, final String s2, final String s3)
'''
pass
def assignMssToDataSource():
'''public boolean assignMssToDataSource(final String s, final Guid guid, final AttributePrioDataSources attributePrioDataSources)
'''
pass
def assignPersonInRoleToAccessCollection():
'''public void assignPersonInRoleToAccessCollection(final String s, final Person person, final Role role, final Guid[] array)
'''
pass
def beginTransaction():
'''public void beginTransaction(final String s, final int value)
'''
pass
def clearTopology():
'''public void clearTopology(final String s)
'''
pass
def closeCursor():
'''public void closeCursor(final String s, final String s2)
'''
pass
def commitTransaction():
'''public void commitTransaction(final String s)
'''
pass
def compare():
'''public ComparisonResult compare(final String s, final ModelObject modelObject, final ModelObject[] array, final CompareOptions compareOptions)
public ComparisonResult compare(final String s, final ObjectRef objectRef, final ObjectRef[] array, final CompareOptions compareOptions)
'''
pass
def createEmptyVersion():
'''public long createEmptyVersion(final String s, final String s2, final String s3)
'''
pass
def createVersion():
'''public long createVersion(final String s, final String s2, final String s3)
'''
pass
def cursorSize():
'''public int cursorSize(final String s, final String s2)
'''
pass
def defineExtendedAttributeMeta():
'''public void defineExtendedAttributeMeta(final long value, final UserDataMeta userDataMeta)
'''
pass
def deleteAccess():
'''public void deleteAccess(final String s, final Principal principal, final Resource resource, final String s2, final String[] array)
'''
pass
def deleteById():
'''public int deleteById(final String s, final Guid guid, final Guid guid2)
'''
pass
def deleteMssObjLink():
'''public void deleteMssObjLink(final String s, final Guid guid, final Guid guid2)
'''
pass
def deletePermission():
'''public void deletePermission(final String s, final String s2)
'''
pass
def deletePermissionFromRole():
'''public void deletePermissionFromRole(final String s, final String s2, final String s3)
'''
pass
def deleteRole():
'''public void deleteRole(final String s, final String s2)
'''
pass
def deleteRuntimeAccess():
'''public void deleteRuntimeAccess(final String s, final Principal principal, final String s2, final String[] array)
'''
pass
def deleteVersion():
'''public void deleteVersion(final long value, final String s)
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
def endBulkload():
'''public void endBulkload(final long value)
'''
pass
def evaluateGuids():
'''public List evaluateGuids(final String s, final ModelObject modelObject)
'''
pass
def find():
'''public ModelObject[] find(final String s, final Guid[] array, final String s2, final int value, final String s3, final String s4, final Guid guid, final String[] array2)
'''
pass
def findChangeInit():
'''public void findChangeInit(final String s, final String s2, final int value, final long value2, final long value3, final int value4, final int value5)
'''
pass
def findChanges():
'''public ModelObject[] findChanges(final String s, final String s2, final int value, final long value2, final long value3, final int value4)
'''
pass
def findImpactedBusinessApplications():
'''public Application[] findImpactedBusinessApplications(final String s, final Guid[] array, final long value)
'''
pass
def findImpactedBusinessServices():
'''public BusinessSystem[] findImpactedBusinessServices(final String s, final Guid[] array, final long value)
'''
pass
def findInitCursor():
'''public String findInitCursor(final String s, final String s2, final Guid guid, final String[] array)
'''
pass
def findInitData():
'''public void findInitData(final String s, final String s2, final Guid[] array, final String s3, final String s4, final Guid guid, final String[] array2)
'''
pass
def findInitXML():
'''public void findInitXML(final String s, final String s2, final Guid[] array, final int value, final int value2, final int value3, final String s3, final String s4, final Guid guid, final String[] array2, final String s5)
'''
pass
def findXML():
'''public String findXML(final String s, final Guid guid, final int value, final int value2, final Guid guid2, final String[] array)
'''
pass
def generateExplicitRelationships():
'''public void generateExplicitRelationships()
'''
pass
def getAccessDecisions():
'''public AccessDecision[] getAccessDecisions(final String s, final Principal principal, final Resource[] array, final String[] array2)
'''
pass
def getAdmin():
'''public Object getAdmin()
'''
pass
def getAllMeta():
'''public ObjectClass[] getAllMeta(final boolean value)
'''
pass
def getAllVersions():
'''public TopologyVersion[] getAllVersions(final String s)
'''
pass
def getAnchorHosts():
'''public String[] getAnchorHosts(final String s)
'''
pass
def getAnchorPort():
'''public int getAnchorPort(final String s)
'''
pass
def getAttrPrioClassMeta():
'''public String getAttrPrioClassMeta()
'''
pass
def getAttributesWithReplacementValues():
'''public String[] getAttributesWithReplacementValues(final String s, final String s2)
'''
pass
def getAuthMap():
'''public AuthMap getAuthMap(final String s)
'''
pass
def getAvailableProcessors():
'''public int getAvailableProcessors()
'''
pass
def getBlobInfo():
'''public HashMap getBlobInfo(final String s)
'''
pass
def getChangeHistory():
'''public String getChangeHistory(final String s, final Guid guid, final long value, final long value2, final boolean value3)
public String getChangeHistory(final String s, final Guid[] array, final long value, final long value2, final int value3, final boolean value4)
public String getChangeHistory(final String s, final Guid[] array, final long value, final long value2, final boolean value3)
public ChangeHistory[] getChangeHistory(final String s, final Guid[] array, final long value, final long value2, final boolean value3, final int value4, final int value5)
'''
pass
def getChangeHistoryInJava():
'''public ChangeHistory[] getChangeHistoryInJava(final String s, final Guid guid, final long value, final long value2, final boolean value3)
public ChangeHistory[] getChangeHistoryInJava(final String s, final Guid[] array, final long value, final long value2, final int value3, final boolean value4)
public ChangeHistory[] getChangeHistoryInJava(final String s, final Guid[] array, final long value, final long value2, final boolean value3)
'''
pass
def getChangedClasses():
'''public String[] getChangedClasses(final long value, final long value2, final int value3)
'''
pass
def getClassNames():
'''public String[] getClassNames(final String s)
'''
pass
def getDataPermissions():
'''public String[] getDataPermissions(final String s, final Principal principal, final Resource[] array)
'''
pass
def getDataSources():
'''public ArrayList getDataSources(final String s)
'''
pass
def getDetailsPanel():
'''public DetailPanelModel getDetailsPanel(final String s, final Guid guid, final long value)
public DetailPanelModel getDetailsPanel(final String s, final Guid guid, final long value, final Locale locale)
'''
pass
def getEDM():
'''public EDMInterface getEDM(final String s)
'''
pass
def getEntitlements():
'''public Resource[] getEntitlements(final String s, final Principal principal, final String[] array)
'''
pass
def getEntitlementsForRole():
'''public Resource[] getEntitlementsForRole(final String s, final Principal principal, final String s2)
'''
pass
def getExtendedAttributeMeta():
'''public UserDataMeta[] getExtendedAttributeMeta(final long value, final String s)
'''
pass
def getExtendedAttributes():
'''public AttrNameValue[] getExtendedAttributes(final String s, final long value, final Guid guid)
'''
pass
def getFreeMemory():
'''public long getFreeMemory()
'''
pass
def getGraphView():
'''public TopologyGraphModel getGraphView(final String s, final ViewDefiner viewDefiner)
'''
pass
def getGraphViewImage():
'''public ImageStream getGraphViewImage(final String s, final ViewDefiner viewDefiner)
'''
pass
def getGuidAliases():
'''public List getGuidAliases(final String s, final Guid guid)
'''
pass
def getInventorySummary():
'''public String getInventorySummary(final boolean value, final String s)
'''
pass
def getLookupAttributes():
'''public Entry[] getLookupAttributes()
'''
pass
def getLookupGroups():
'''public String[] getLookupGroups()
'''
pass
def getLookupLocators():
'''public LookupLocator[] getLookupLocators()
'''
pass
def getMaxMemory():
'''public long getMaxMemory()
'''
pass
def getMetaData():
'''public ObjectClass getMetaData(final String s, final boolean value)
'''
pass
def getMetaInfo():
'''public HashMap getMetaInfo(final String s)
'''
pass
def getNodeInfoMap():
'''public Map getNodeInfoMap(final String s)
'''
pass
def getNumberOfChanges():
'''public int getNumberOfChanges(final String s, final Guid[] array, final long value, final long value2, final boolean value3)
'''
pass
def getPriorityRules():
'''public ArrayList getPriorityRules(final String s)
'''
pass
def getPropagatedChanges():
'''public String getPropagatedChanges(final String s, final long value)
'''
pass
def getPropagatedChangesInJava():
'''public ChangeHistory[] getPropagatedChangesInJava(final String s, final long value)
'''
pass
def getReplacementValues():
'''public String[] getReplacementValues(final String s, final String s2, final String s3)
'''
pass
def getResultMetaData():
'''public ResultMetaData getResultMetaData(final String s, final String s2)
public ResultMetaData getResultMetaData(final String s, final String s2, final LinkedHashMap linkedHashMap)
'''
pass
def getRmiPort():
'''public int getRmiPort()
'''
pass
def getRoles():
'''public String[] getRoles(final String s, final Principal principal)
'''
pass
def getRuntimeAccess():
'''public String[] getRuntimeAccess(final String s, final Principal principal)
'''
pass
def getRuntimeAccessDecisions():
'''public RuntimeAccessDecision[] getRuntimeAccessDecisions(final String s, final Principal principal, final String[] array)
'''
pass
def getTopLevelClasses():
'''public ArrayList getTopLevelClasses(final String s)
'''
pass
def getTotalMemory():
'''public long getTotalMemory()
'''
pass
def getTreeView():
'''public TopologyTreeModel getTreeView(final String s, final ViewDefiner viewDefiner)
'''
pass
def getUser():
'''public String getUser(final String s)
'''
pass
def getWebPort():
'''public int getWebPort()
'''
pass
def getWebSslPort():
'''public int getWebSslPort()
'''
pass
def insert():
'''public Guid[] insert(final String s, final String s2, final boolean value, final Guid guid)
'''
pass
def isECMDB():
'''public boolean isECMDB(final String s)
'''
pass
def login():
'''public String login(final long value, final long value2)
public String login(final ApiPrincipal apiPrincipal, final String s, final long value)
public String login(final String s, final String s2, final String s3, final long value)
'''
pass
def logout():
'''public void logout(final String s)
'''
pass
def mergeObjects():
'''public int mergeObjects(final String s, final Guid guid, final Guid guid2, final int value)
'''
pass
def modifyLookupAttributes():
'''public void modifyLookupAttributes(final Entry[] array, final Entry[] array2)
'''
pass
def nextDataCursor():
'''public ModelObject[] nextDataCursor(final String s, final String s2, final int value, final int value2, final int value3)
'''
pass
def nextDataResult():
'''public ModelObject[] nextDataResult(final String s, final int value, final int value2, final int value3)
'''
pass
def nextXML():
'''public String nextXML(final String s)
'''
pass
def ping():
'''public boolean ping()
'''
pass
def processChanges():
'''public void processChanges()
'''
pass
def rebuildTopology():
'''public void rebuildTopology()
'''
pass
def registerLocale():
'''public void registerLocale(final String s, final Locale locale)
'''
pass
def removeArrayElements():
'''public void removeArrayElements(final String s, final Guid guid, final String s2, final Guid[] array, final Guid guid2)
'''
pass
def removeDataSources():
'''public void removeDataSources(final String s, final ArrayList list)
'''
pass
def removeExtendedAttributeMeta():
'''public void removeExtendedAttributeMeta(final String s, final long value, final String s2, final Guid guid)
'''
pass
def removeLookupGroups():
'''public void removeLookupGroups(final String[] array)
'''
pass
def removeLookupLocators():
'''public void removeLookupLocators(final LookupLocator[] array)
'''
pass
def removePersonInRoleToAccessCollection():
'''public void removePersonInRoleToAccessCollection(final String s, final Person person, final Role role, final Guid[] array)
'''
pass
def removePriorityRules():
'''public void removePriorityRules(final String s, final ArrayList list)
'''
pass
def removeRemoteListener():
'''public void removeRemoteListener(final RemoteEventListener remoteEventListener)
'''
pass
def restart():
'''public void restart()
'''
pass
def rollback():
'''public void rollback(final String s)
'''
pass
def setAnchorHosts():
'''public void setAnchorHosts(final String s, final String[] array)
'''
pass
def setAnchorPort():
'''public void setAnchorPort(final String s, final int value)
'''
pass
def setAuthMap():
'''public void setAuthMap(final String s, final AuthMap authMap)
'''
pass
def setDataSources():
'''public Guid[] setDataSources(final String s, final ArrayList list)
'''
pass
def setExtendedAttributes():
'''public void setExtendedAttributes(final String s, final long value, final Guid guid, final AttrNameValue[] array)
'''
pass
def setLookupGroups():
'''public void setLookupGroups(final String[] array)
'''
pass
def setLookupLocators():
'''public void setLookupLocators(final LookupLocator[] array)
'''
pass
def setPriorityRules():
'''public Guid[] setPriorityRules(final String s, final ArrayList list)
'''
pass
def shutdown():
'''public void shutdown()
'''
pass
def startBulkload():
'''public long startBulkload(final long value)
'''
pass
def startDiscovery():
'''public void startDiscovery(final String s, final RunDefinition runDefinition, final String s2)
public void startDiscovery(final String s, final Guid[] array, final String s2)
public void startDiscovery(final String s, final String[] array, final String s2)
'''
pass
def startExport():
'''public void startExport(final String s, final String s2)
'''
pass
def startImport():
'''public void startImport(final String s)
'''
pass
def status():
'''public String status(final String s)
'''
pass
def stopExport():
'''public void stopExport(final String s)
'''
pass
def stopImport():
'''public void stopImport(final String s, final boolean value)
'''
pass
def synchScopes():
'''public void synchScopes(final String s)
'''
pass
def unregisterLocale():
'''public void unregisterLocale(final String s)
'''
pass
def update():
'''public Guid[] update(final String s, final ModelObject[] array, final Guid guid)
'''
pass
def updateDomainPorts():
'''public CMDBDomain updateDomainPorts(final CMDBDomain cmdbDomain)
'''
pass
def updateMerge():
'''public Map updateMerge(final String s, final ModelObject[] array, final Guid guid)
'''
pass
