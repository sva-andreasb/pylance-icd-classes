def logError():
    '''public static void logError(final String sourceMethod, final String msg, final Throwable cause)
    '''
def init():
    '''public void init(final Connection connection, final String jdbcDriver, final String databaseUrl, final String userId, final String userPassword)
    '''
def initConnection():
    '''public void initConnection(final String jdbcDriver, final String databaseUrl, final String schema, final String userId, final String userPassword)
    '''
def shutdown():
    '''public void shutdown()
    '''
def getModelLevel():
    '''public String getModelLevel()
    '''
def getClassTypes():
    '''public HashMap[] getClassTypes(final String className)
    public HashMap[] getClassTypes(final Guid classGuid)
    '''
def getAttributeTypes():
    '''public HashMap[] getAttributeTypes(final int type, final String name)
    '''
def getEnumerations():
    '''public HashMap getEnumerations(final String[] enumNames)
    '''
def getValidRelationships():
    '''public HashMap[] getValidRelationships(final String relType, final String sourceClass, final String targetClass)
    '''
def registerFederatedAttributes():
    '''public void registerFederatedAttributes(final Guid mssGUID, final String[] federatedAttributes, final String namespace)
    '''
def registerFederatedClasses():
    '''public void registerFederatedClasses(final Guid mssGUID, final String[] federatedClasses)
    '''
def registerFederatedRelationships():
    '''public void registerFederatedRelationships(final Guid mssGUID, final String[] federatedRelationships)
    '''
def getFederatedAttributes():
    '''public HashMap getFederatedAttributes(final Guid mssGUID)
    '''
def getFederatedClasses():
    '''public HashMap getFederatedClasses(final Guid mssGUID)
    '''
def getFederatedRelationships():
    '''public HashMap getFederatedRelationships(final Guid mssGUID)
    '''
def setAttributePriorities():
    '''public void setAttributePriorities(final HashMap attributePriorities, final Guid[] mssGuids)
    '''
def getAttributePriorities():
    '''public HashMap getAttributePriorities(final String[] attributeTypes)
    '''
def getParentClasses():
    '''public Guid[] getParentClasses(final Guid classGuid)
    public String[] getParentClasses(final String className)
    '''
def hasMetadataChanged():
    '''public boolean hasMetadataChanged(final Date since)
    '''
def register():
    '''public Guid[] register(final Guid mssGuid, final HashMap[] attributeMaps)
    '''
def convergeMasters():
    '''public void convergeMasters(final Guid masterGuid1, final Guid masterGuid2)
    '''
def isMatch():
    '''public boolean isMatch(final String nameUri)
    public boolean isMatch(final Guid guid1, final Guid guid2)
    '''
def getAliases():
    '''public Guid[] getAliases(final Guid masterGuid)
    public Map<Guid, List<Guid>> getAliases(final Guid[] masterGuids)
    public Guid[] getAliases(final String masterNameUri)
    '''
def getMaster():
    '''public Guid getMaster(final Guid aliasGuid)
    public Guid getMaster(final String aliasNameUri)
    '''
def getMasterAndAliases():
    '''public Guid[] getMasterAndAliases(final Guid guid)
    public Guid[] getMasterAndAliases(final String masterNameUri)
    '''
def getNames():
    '''public NrsMasterAliasInfo[] getNames(final Guid[] guids)
    '''
def getDuplicates():
    '''public NrsDuplicateInfo[] getDuplicates(final String classType, final Date date)
    '''
def deleteDuplicates():
    '''public void deleteDuplicates(final String classType, final Date date)
    '''
def registerMSS():
    '''public Guid registerMSS(final HashMap mss)
    '''
def addRelationships():
    '''public int[] addRelationships(final Guid mssGuid, final HashMap[] relationships)
    '''
def registerRelationships():
    '''public Guid[] registerRelationships(final Guid mssGuid, final HashMap[] relationships)
    '''
def getGuid():
    '''public Guid getGuid(final Guid mssGuid, final String sourceToken)
    '''
def getMSS():
    '''public HashMap[] getMSS(final Date date)
    '''
def get():
    '''public HashMap[] get(final String mssName, final HashMap resourceFilter, final int scope)
    public HashMap[] get(final Guid mssGuid, final HashMap resourceFilter, final int scope)
    public HashMap[][] get(final String mssName, final HashMap[] resourceFilters, final int scope)
    public HashMap[][] get(final Guid mssGuid, final HashMap[] resourceFilters, final int scope)
    '''
def getManagedElements():
    '''public HashMap[] getManagedElements(final String classType, final Date date)
    '''
def getSourceToken():
    '''public String getSourceToken(final Guid mssGuid, final Guid meGuid)
    '''
def getSourceTokens():
    '''public HashMap[] getSourceTokens(final Guid mssGuid, final Date date)
    '''
def getRelationships():
    '''public HashMap[] getRelationships(final String relationshipType, final String sourceClass, final String targetClass, final Date date)
    '''
def delete():
    '''public void delete(final Guid mssGuid, final Guid[] guids)
    '''
def deleteMSS():
    '''public void deleteMSS(final Guid mssGuid)
    '''
def getDeleted():
    '''public Guid[] getDeleted(final String classType, final Date date)
    '''
def removeStale():
    '''public void removeStale(final Guid mssGuid, final Date date)
    '''
def update():
    '''public void update(final Guid mssGuid, final HashMap[] attributeMaps)
    '''
def updateMSS():
    '''public void updateMSS(final HashMap mss)
    '''
def deleteRelationships():
    '''public void deleteRelationships(final Guid mssGuid, final HashMap filter)
    public void deleteRelationships(final Guid mssGuid, final HashMap[] relationships)
    '''
def getAllNames():
    '''public Map<Guid, Map<Guid, String>> getAllNames(final Guid[] guids)
    '''
def getAllGuids():
    '''public Map<Guid, Set<Guid>> getAllGuids(final Guid[] guids)
    '''
def registerAbstractResources():
    '''public Guid[] registerAbstractResources(final String mssName, final Map<String, Object>[] attributeMaps)
    public Guid[] registerAbstractResources(final Guid mssGuid, final Map<String, Object>[] attributeMaps)
    '''
