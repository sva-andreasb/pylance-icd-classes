def MetadataService():
    '''public MetadataService()
    '''
def fetchCdmVersionInfo():
    '''public ConnectionInfo fetchCdmVersionInfo(final Connection conn)
    '''
def init():
    '''public void init(final Connection connection, final String jdbcDriver, final String databaseURL, final String userID, final String userPassword)
    '''
def shutdown():
    '''public void shutdown()
    '''
def getNamingPolicies():
    '''public HashMap getNamingPolicies(final String classType)
    '''
def getAllNamingPolicies():
    '''public Map<String, Map<String, Guid>> getAllNamingPolicies()
    '''
def getAllNamingRules():
    '''public Map<Guid, List<Map<String, Object>>> getAllNamingRules()
    '''
def getAllNamingRuleIdentifiers():
    '''public Map<Guid, List<Map<String, Object>>> getAllNamingRuleIdentifiers()
    '''
def getModelLevel():
    '''public String getModelLevel()
    '''
def getDerivedClasses():
    '''public String[] getDerivedClasses(final String className)
    public Guid[] getDerivedClasses(final Guid classGuid)
    '''
def isRelated():
    '''public int isRelated(final Guid class1, final Guid class2)
    public int isRelated(final String class1, final String class2)
    '''
def isDesiredClass():
    '''public boolean isDesiredClass(final String className)
    '''
def registerDesiredRelationships():
    '''public void registerDesiredRelationships(Guid mssGUID, final String[] desiredRelationships)
    '''
def isDesiredRelationship():
    '''public boolean isDesiredRelationship(final String relType, final String sourceClass, final String targetClass)
    '''
def registerDesiredClasses():
    '''public void registerDesiredClasses(Guid mssGUID, final String[] desiredClasses)
    '''
def registerFederatedClasses():
    '''public void registerFederatedClasses(final Guid mssGUID, final String[] federatedClasses)
    '''
def registerFederatedAttributes():
    '''public void registerFederatedAttributes(final Guid mssGUID, final String[] federatedAttributes, final String nameSpace)
    '''
def registerFederatedRelationships():
    '''public void registerFederatedRelationships(final Guid mssGUID, final String[] federatedRelationships)
    '''
def getFederatedClasses():
    '''public HashMap getFederatedClasses(final Guid mssGUID)
    '''
def getFederatedAttributes():
    '''public HashMap getFederatedAttributes(final Guid mssGuid)
    '''
def getFederatedRelationships():
    '''public HashMap getFederatedRelationships(final Guid mssGuid)
    '''
def registerDesiredAttributes():
    '''public void registerDesiredAttributes(Guid mssGUID, final String[] desiredAttributes, final String nameSpace)
    '''
def isDesiredAttribute():
    '''public boolean isDesiredAttribute(final String className, final String attributeName)
    '''
def getClassTypes():
    '''public HashMap[] getClassTypes(final String className)
    public HashMap[] getClassTypes(final Guid classGuid)
    '''
def getAttributeTypes():
    '''public HashMap[] getAttributeTypes(final int type, final String name)
    '''
def getParentClasses():
    '''public Guid[] getParentClasses(final Guid classGuid)
    public String[] getParentClasses(final String className)
    '''
def setAttributePriorities():
    '''public void setAttributePriorities(final HashMap attributePriorities, final Guid[] mssGuids)
    '''
def getAttributePriorities():
    '''public HashMap getAttributePriorities(final String[] attributeTypes)
    '''
def getEnumerations():
    '''public HashMap getEnumerations(final String[] enumNames)
    '''
def getValidRelationships():
    '''public HashMap[] getValidRelationships(final String relType, final String sourceClass, final String targetClass)
    '''
def getDesiredClasses():
    '''public HashMap getDesiredClasses(Guid mssGuid)
    '''
def getDesiredAttributes():
    '''public HashMap getDesiredAttributes(Guid mssGuid, final String className)
    '''
def getDesiredRelationships():
    '''public HashMap getDesiredRelationships(Guid mssGuid, final String relType, final String sourceClass, final String targetClass)
    '''
def getNamingContexts():
    '''public HashMap getNamingContexts(final String[] classTypes)
    '''
def isDerivedFromClass():
    '''public boolean isDerivedFromClass(final Guid class1Guid, final Guid class2Guid)
    '''
def isDerivedClass():
    '''public boolean isDerivedClass(final String class1, final String class2)
    '''
def lockCache():
    '''public void lockCache(final DisReadWriteLock.Usage usage)
    '''
def unlockCache():
    '''public void unlockCache(final DisReadWriteLock.Usage usage)
    '''
def refreshCache():
    '''public void refreshCache()
    '''
def hasMetadataChanged():
    '''public boolean hasMetadataChanged(final Date since)
    '''
def buildShortName():
    '''public String buildShortName(final String className)
    '''
def isDuplicateClass():
    '''public boolean isDuplicateClass(final String className)
    '''
