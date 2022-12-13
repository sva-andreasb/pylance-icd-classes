def logError():
'''public static void logError(final String sourceMethod, final String msg, final Throwable cause)
'''
pass
def init():
'''public void init(final Connection connection, final String jdbcDriver, final String databaseUrl, final String userId, final String userPassword)
'''
pass
def initConnection():
'''public void initConnection(final String jdbcDriver, final String databaseUrl, final String schema, final String userId, final String userPassword)
'''
pass
def shutdown():
'''public void shutdown()
'''
pass
def getModelLevel():
'''public String getModelLevel()
'''
pass
def getClassTypes():
'''public HashMap[] getClassTypes(final String className)
public HashMap[] getClassTypes(final Guid classGuid)
'''
pass
def getAttributeTypes():
'''public HashMap[] getAttributeTypes(final int type, final String name)
'''
pass
def getEnumerations():
'''public HashMap getEnumerations(final String[] enumNames)
'''
pass
def getValidRelationships():
'''public HashMap[] getValidRelationships(final String relType, final String sourceClass, final String targetClass)
'''
pass
def registerFederatedAttributes():
'''public void registerFederatedAttributes(final Guid mssGUID, final String[] federatedAttributes, final String namespace)
'''
pass
def registerFederatedClasses():
'''public void registerFederatedClasses(final Guid mssGUID, final String[] federatedClasses)
'''
pass
def registerFederatedRelationships():
'''public void registerFederatedRelationships(final Guid mssGUID, final String[] federatedRelationships)
'''
pass
def getFederatedAttributes():
'''public HashMap getFederatedAttributes(final Guid mssGUID)
'''
pass
def getFederatedClasses():
'''public HashMap getFederatedClasses(final Guid mssGUID)
'''
pass
def getFederatedRelationships():
'''public HashMap getFederatedRelationships(final Guid mssGUID)
'''
pass
def setAttributePriorities():
'''public void setAttributePriorities(final HashMap attributePriorities, final Guid[] mssGuids)
'''
pass
def getAttributePriorities():
'''public HashMap getAttributePriorities(final String[] attributeTypes)
'''
pass
def getParentClasses():
'''public Guid[] getParentClasses(final Guid classGuid)
public String[] getParentClasses(final String className)
'''
pass
def hasMetadataChanged():
'''public boolean hasMetadataChanged(final Date since)
'''
pass
def register():
'''public Guid[] register(final Guid mssGuid, final HashMap[] attributeMaps)
'''
pass
def convergeMasters():
'''public void convergeMasters(final Guid masterGuid1, final Guid masterGuid2)
'''
pass
def isMatch():
'''public boolean isMatch(final String nameUri)
public boolean isMatch(final Guid guid1, final Guid guid2)
'''
pass
def getAliases():
'''public Guid[] getAliases(final Guid masterGuid)
public Map<Guid, List<Guid>> getAliases(final Guid[] masterGuids)
public Guid[] getAliases(final String masterNameUri)
'''
pass
def getMaster():
'''public Guid getMaster(final Guid aliasGuid)
public Guid getMaster(final String aliasNameUri)
'''
pass
def getMasterAndAliases():
'''public Guid[] getMasterAndAliases(final Guid guid)
public Guid[] getMasterAndAliases(final String masterNameUri)
'''
pass
def getNames():
'''public NrsMasterAliasInfo[] getNames(final Guid[] guids)
'''
pass
def getDuplicates():
'''public NrsDuplicateInfo[] getDuplicates(final String classType, final Date date)
'''
pass
def deleteDuplicates():
'''public void deleteDuplicates(final String classType, final Date date)
'''
pass
def registerMSS():
'''public Guid registerMSS(final HashMap mss)
'''
pass
def addRelationships():
'''public int[] addRelationships(final Guid mssGuid, final HashMap[] relationships)
'''
pass
def registerRelationships():
'''public Guid[] registerRelationships(final Guid mssGuid, final HashMap[] relationships)
'''
pass
def getGuid():
'''public Guid getGuid(final Guid mssGuid, final String sourceToken)
'''
pass
def getMSS():
'''public HashMap[] getMSS(final Date date)
'''
pass
def get():
'''public HashMap[] get(final String mssName, final HashMap resourceFilter, final int scope)
public HashMap[] get(final Guid mssGuid, final HashMap resourceFilter, final int scope)
public HashMap[][] get(final String mssName, final HashMap[] resourceFilters, final int scope)
public HashMap[][] get(final Guid mssGuid, final HashMap[] resourceFilters, final int scope)
'''
pass
def getManagedElements():
'''public HashMap[] getManagedElements(final String classType, final Date date)
'''
pass
def getSourceToken():
'''public String getSourceToken(final Guid mssGuid, final Guid meGuid)
'''
pass
def getSourceTokens():
'''public HashMap[] getSourceTokens(final Guid mssGuid, final Date date)
'''
pass
def getRelationships():
'''public HashMap[] getRelationships(final String relationshipType, final String sourceClass, final String targetClass, final Date date)
'''
pass
def delete():
'''public void delete(final Guid mssGuid, final Guid[] guids)
'''
pass
def deleteMSS():
'''public void deleteMSS(final Guid mssGuid)
'''
pass
def getDeleted():
'''public Guid[] getDeleted(final String classType, final Date date)
'''
pass
def removeStale():
'''public void removeStale(final Guid mssGuid, final Date date)
'''
pass
def update():
'''public void update(final Guid mssGuid, final HashMap[] attributeMaps)
'''
pass
def updateMSS():
'''public void updateMSS(final HashMap mss)
'''
pass
def deleteRelationships():
'''public void deleteRelationships(final Guid mssGuid, final HashMap filter)
public void deleteRelationships(final Guid mssGuid, final HashMap[] relationships)
'''
pass
def getAllNames():
'''public Map<Guid, Map<Guid, String>> getAllNames(final Guid[] guids)
'''
pass
def getAllGuids():
'''public Map<Guid, Set<Guid>> getAllGuids(final Guid[] guids)
'''
pass
def registerAbstractResources():
'''public Guid[] registerAbstractResources(final String mssName, final Map<String, Object>[] attributeMaps)
public Guid[] registerAbstractResources(final Guid mssGuid, final Map<String, Object>[] attributeMaps)
'''
pass
