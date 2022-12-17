def init():
    '''returns None\n\n
    init(final Connection connection, final String jdbcDriver, final String databaseUrl, final String userId, final String userPassword)\n
    '''
def initConnection():
    '''returns None\n\n
    initConnection(final String jdbcDriver, final String databaseUrl, final String schema, final String userId, final String userPassword)\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def getModelLevel():
    '''returns String\n\n
    getModelLevel()\n
    '''
def getClassTypes():
    '''returns HashMap[]\n\n
    getClassTypes(final String className)\n
    getClassTypes(final Guid classGuid)\n
    '''
def getAttributeTypes():
    '''returns HashMap[]\n\n
    getAttributeTypes(final int type, final String name)\n
    '''
def getEnumerations():
    '''returns HashMap\n\n
    getEnumerations(final String[] enumNames)\n
    '''
def getValidRelationships():
    '''returns HashMap[]\n\n
    getValidRelationships(final String relType, final String sourceClass, final String targetClass)\n
    '''
def registerFederatedAttributes():
    '''returns None\n\n
    registerFederatedAttributes(final Guid mssGUID, final String[] federatedAttributes, final String namespace)\n
    '''
def registerFederatedClasses():
    '''returns None\n\n
    registerFederatedClasses(final Guid mssGUID, final String[] federatedClasses)\n
    '''
def registerFederatedRelationships():
    '''returns None\n\n
    registerFederatedRelationships(final Guid mssGUID, final String[] federatedRelationships)\n
    '''
def getFederatedAttributes():
    '''returns HashMap\n\n
    getFederatedAttributes(final Guid mssGUID)\n
    '''
def getFederatedClasses():
    '''returns HashMap\n\n
    getFederatedClasses(final Guid mssGUID)\n
    '''
def getFederatedRelationships():
    '''returns HashMap\n\n
    getFederatedRelationships(final Guid mssGUID)\n
    '''
def setAttributePriorities():
    '''returns None\n\n
    setAttributePriorities(final HashMap attributePriorities, final Guid[] mssGuids)\n
    '''
def getAttributePriorities():
    '''returns HashMap\n\n
    getAttributePriorities(final String[] attributeTypes)\n
    '''
def getParentClasses():
    '''returns String[]\n\n
    getParentClasses(final Guid classGuid)\n
    getParentClasses(final String className)\n
    '''
def hasMetadataChanged():
    '''returns boolean\n\n
    hasMetadataChanged(final Date since)\n
    '''
def register():
    '''returns Guid[]\n\n
    register(final Guid mssGuid, final HashMap[] attributeMaps)\n
    '''
def convergeMasters():
    '''returns None\n\n
    convergeMasters(final Guid masterGuid1, final Guid masterGuid2)\n
    '''
def isMatch():
    '''returns boolean\n\n
    isMatch(final String nameUri)\n
    isMatch(final Guid guid1, final Guid guid2)\n
    '''
def getAliases():
    '''returns Guid[]\n\n
    getAliases(final Guid masterGuid)\n
    getAliases(final String masterNameUri)\n
    '''
def getMaster():
    '''returns Guid\n\n
    getMaster(final Guid aliasGuid)\n
    getMaster(final String aliasNameUri)\n
    '''
def getMasterAndAliases():
    '''returns Guid[]\n\n
    getMasterAndAliases(final Guid guid)\n
    getMasterAndAliases(final String masterNameUri)\n
    '''
def getNames():
    '''returns NrsMasterAliasInfo[]\n\n
    getNames(final Guid[] guids)\n
    '''
def getDuplicates():
    '''returns NrsDuplicateInfo[]\n\n
    getDuplicates(final String classType, final Date date)\n
    '''
def deleteDuplicates():
    '''returns None\n\n
    deleteDuplicates(final String classType, final Date date)\n
    '''
def registerMSS():
    '''returns Guid\n\n
    registerMSS(final HashMap mss)\n
    '''
def addRelationships():
    '''returns int[]\n\n
    addRelationships(final Guid mssGuid, final HashMap[] relationships)\n
    '''
def registerRelationships():
    '''returns Guid[]\n\n
    registerRelationships(final Guid mssGuid, final HashMap[] relationships)\n
    '''
def getGuid():
    '''returns Guid\n\n
    getGuid(final Guid mssGuid, final String sourceToken)\n
    '''
def getMSS():
    '''returns HashMap[]\n\n
    getMSS(final Date date)\n
    '''
def get():
    '''returns HashMap[][]\n\n
    get(final String mssName, final HashMap resourceFilter, final int scope)\n
    get(final Guid mssGuid, final HashMap resourceFilter, final int scope)\n
    get(final String mssName, final HashMap[] resourceFilters, final int scope)\n
    get(final Guid mssGuid, final HashMap[] resourceFilters, final int scope)\n
    '''
def getManagedElements():
    '''returns HashMap[]\n\n
    getManagedElements(final String classType, final Date date)\n
    '''
def getSourceToken():
    '''returns String\n\n
    getSourceToken(final Guid mssGuid, final Guid meGuid)\n
    '''
def getSourceTokens():
    '''returns HashMap[]\n\n
    getSourceTokens(final Guid mssGuid, final Date date)\n
    '''
def getRelationships():
    '''returns HashMap[]\n\n
    getRelationships(final String relationshipType, final String sourceClass, final String targetClass, final Date date)\n
    '''
def delete():
    '''returns None\n\n
    delete(final Guid mssGuid, final Guid[] guids)\n
    '''
def deleteMSS():
    '''returns None\n\n
    deleteMSS(final Guid mssGuid)\n
    '''
def getDeleted():
    '''returns Guid[]\n\n
    getDeleted(final String classType, final Date date)\n
    '''
def removeStale():
    '''returns None\n\n
    removeStale(final Guid mssGuid, final Date date)\n
    '''
def update():
    '''returns None\n\n
    update(final Guid mssGuid, final HashMap[] attributeMaps)\n
    '''
def updateMSS():
    '''returns None\n\n
    updateMSS(final HashMap mss)\n
    '''
def deleteRelationships():
    '''returns None\n\n
    deleteRelationships(final Guid mssGuid, final HashMap filter)\n
    deleteRelationships(final Guid mssGuid, final HashMap[] relationships)\n
    '''
def registerAbstractResources():
    '''returns Guid[]\n\n
    registerAbstractResources(final String mssName, final Map<String, Object>[] attributeMaps)\n
    registerAbstractResources(final Guid mssGuid, final Map<String, Object>[] attributeMaps)\n
    '''
