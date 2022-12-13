def MetadataService():
'''public MetadataService()
'''
pass
def fetchCdmVersionInfo():
'''public ConnectionInfo fetchCdmVersionInfo(final Connection conn)
'''
pass
def init():
'''public void init(final Connection connection, final String jdbcDriver, final String databaseURL, final String userID, final String userPassword)
'''
pass
def shutdown():
'''public void shutdown()
'''
pass
def getNamingPolicies():
'''public HashMap getNamingPolicies(final String classType)
'''
pass
def getAllNamingPolicies():
'''public Map<String, Map<String, Guid>> getAllNamingPolicies()
'''
pass
def getAllNamingRules():
'''public Map<Guid, List<Map<String, Object>>> getAllNamingRules()
'''
pass
def getAllNamingRuleIdentifiers():
'''public Map<Guid, List<Map<String, Object>>> getAllNamingRuleIdentifiers()
'''
pass
def getModelLevel():
'''public String getModelLevel()
'''
pass
def getDerivedClasses():
'''public String[] getDerivedClasses(final String className)
public Guid[] getDerivedClasses(final Guid classGuid)
'''
pass
def isRelated():
'''public int isRelated(final Guid class1, final Guid class2)
public int isRelated(final String class1, final String class2)
'''
pass
def isDesiredClass():
'''public boolean isDesiredClass(final String className)
'''
pass
def registerDesiredRelationships():
'''public void registerDesiredRelationships(Guid mssGUID, final String[] desiredRelationships)
'''
pass
def isDesiredRelationship():
'''public boolean isDesiredRelationship(final String relType, final String sourceClass, final String targetClass)
'''
pass
def registerDesiredClasses():
'''public void registerDesiredClasses(Guid mssGUID, final String[] desiredClasses)
'''
pass
def registerFederatedClasses():
'''public void registerFederatedClasses(final Guid mssGUID, final String[] federatedClasses)
'''
pass
def registerFederatedAttributes():
'''public void registerFederatedAttributes(final Guid mssGUID, final String[] federatedAttributes, final String nameSpace)
'''
pass
def registerFederatedRelationships():
'''public void registerFederatedRelationships(final Guid mssGUID, final String[] federatedRelationships)
'''
pass
def getFederatedClasses():
'''public HashMap getFederatedClasses(final Guid mssGUID)
'''
pass
def getFederatedAttributes():
'''public HashMap getFederatedAttributes(final Guid mssGuid)
'''
pass
def getFederatedRelationships():
'''public HashMap getFederatedRelationships(final Guid mssGuid)
'''
pass
def registerDesiredAttributes():
'''public void registerDesiredAttributes(Guid mssGUID, final String[] desiredAttributes, final String nameSpace)
'''
pass
def isDesiredAttribute():
'''public boolean isDesiredAttribute(final String className, final String attributeName)
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
def getParentClasses():
'''public Guid[] getParentClasses(final Guid classGuid)
public String[] getParentClasses(final String className)
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
def getEnumerations():
'''public HashMap getEnumerations(final String[] enumNames)
'''
pass
def getValidRelationships():
'''public HashMap[] getValidRelationships(final String relType, final String sourceClass, final String targetClass)
'''
pass
def getDesiredClasses():
'''public HashMap getDesiredClasses(Guid mssGuid)
'''
pass
def getDesiredAttributes():
'''public HashMap getDesiredAttributes(Guid mssGuid, final String className)
'''
pass
def getDesiredRelationships():
'''public HashMap getDesiredRelationships(Guid mssGuid, final String relType, final String sourceClass, final String targetClass)
'''
pass
def getNamingContexts():
'''public HashMap getNamingContexts(final String[] classTypes)
'''
pass
def isDerivedFromClass():
'''public boolean isDerivedFromClass(final Guid class1Guid, final Guid class2Guid)
'''
pass
def isDerivedClass():
'''public boolean isDerivedClass(final String class1, final String class2)
'''
pass
def lockCache():
'''public void lockCache(final DisReadWriteLock.Usage usage)
'''
pass
def unlockCache():
'''public void unlockCache(final DisReadWriteLock.Usage usage)
'''
pass
def refreshCache():
'''public void refreshCache()
'''
pass
def hasMetadataChanged():
'''public boolean hasMetadataChanged(final Date since)
'''
pass
def buildShortName():
'''public String buildShortName(final String className)
'''
pass
def isDuplicateClass():
'''public boolean isDuplicateClass(final String className)
'''
pass
