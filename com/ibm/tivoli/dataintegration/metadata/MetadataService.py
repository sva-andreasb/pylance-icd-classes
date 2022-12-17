def ():
    '''returns MetadataService\n\n
    ()\n
    '''
def fetchCdmVersionInfo():
    '''returns ConnectionInfo\n\n
    fetchCdmVersionInfo(final Connection conn)\n
    '''
def init():
    '''returns None\n\n
    init(final Connection connection, final String jdbcDriver, final String databaseURL, final String userID, final String userPassword)\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def getNamingPolicies():
    '''returns HashMap\n\n
    getNamingPolicies(final String classType)\n
    '''
def getModelLevel():
    '''returns String\n\n
    getModelLevel()\n
    '''
def getDerivedClasses():
    '''returns Guid[]\n\n
    getDerivedClasses(final String className)\n
    getDerivedClasses(final Guid classGuid)\n
    '''
def isRelated():
    '''returns int\n\n
    isRelated(final Guid class1, final Guid class2)\n
    isRelated(final String class1, final String class2)\n
    '''
def isDesiredClass():
    '''returns boolean\n\n
    isDesiredClass(final String className)\n
    '''
def registerDesiredRelationships():
    '''returns None\n\n
    registerDesiredRelationships(Guid mssGUID, final String[] desiredRelationships)\n
    '''
def isDesiredRelationship():
    '''returns boolean\n\n
    isDesiredRelationship(final String relType, final String sourceClass, final String targetClass)\n
    '''
def registerDesiredClasses():
    '''returns None\n\n
    registerDesiredClasses(Guid mssGUID, final String[] desiredClasses)\n
    '''
def registerFederatedClasses():
    '''returns None\n\n
    registerFederatedClasses(final Guid mssGUID, final String[] federatedClasses)\n
    '''
def registerFederatedAttributes():
    '''returns None\n\n
    registerFederatedAttributes(final Guid mssGUID, final String[] federatedAttributes, final String nameSpace)\n
    '''
def registerFederatedRelationships():
    '''returns None\n\n
    registerFederatedRelationships(final Guid mssGUID, final String[] federatedRelationships)\n
    '''
def getFederatedClasses():
    '''returns HashMap\n\n
    getFederatedClasses(final Guid mssGUID)\n
    '''
def getFederatedAttributes():
    '''returns HashMap\n\n
    getFederatedAttributes(final Guid mssGuid)\n
    '''
def getFederatedRelationships():
    '''returns HashMap\n\n
    getFederatedRelationships(final Guid mssGuid)\n
    '''
def registerDesiredAttributes():
    '''returns None\n\n
    registerDesiredAttributes(Guid mssGUID, final String[] desiredAttributes, final String nameSpace)\n
    '''
def isDesiredAttribute():
    '''returns boolean\n\n
    isDesiredAttribute(final String className, final String attributeName)\n
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
def getParentClasses():
    '''returns String[]\n\n
    getParentClasses(final Guid classGuid)\n
    getParentClasses(final String className)\n
    '''
def setAttributePriorities():
    '''returns None\n\n
    setAttributePriorities(final HashMap attributePriorities, final Guid[] mssGuids)\n
    '''
def getAttributePriorities():
    '''returns HashMap\n\n
    getAttributePriorities(final String[] attributeTypes)\n
    '''
def getEnumerations():
    '''returns HashMap\n\n
    getEnumerations(final String[] enumNames)\n
    '''
def getValidRelationships():
    '''returns HashMap[]\n\n
    getValidRelationships(final String relType, final String sourceClass, final String targetClass)\n
    '''
def getDesiredClasses():
    '''returns HashMap\n\n
    getDesiredClasses(Guid mssGuid)\n
    '''
def getDesiredAttributes():
    '''returns HashMap\n\n
    getDesiredAttributes(Guid mssGuid, final String className)\n
    '''
def getDesiredRelationships():
    '''returns HashMap\n\n
    getDesiredRelationships(Guid mssGuid, final String relType, final String sourceClass, final String targetClass)\n
    '''
def getNamingContexts():
    '''returns HashMap\n\n
    getNamingContexts(final String[] classTypes)\n
    '''
def isDerivedFromClass():
    '''returns boolean\n\n
    isDerivedFromClass(final Guid class1Guid, final Guid class2Guid)\n
    '''
def isDerivedClass():
    '''returns boolean\n\n
    isDerivedClass(final String class1, final String class2)\n
    '''
def lockCache():
    '''returns None\n\n
    lockCache(final DisReadWriteLock.Usage usage)\n
    '''
def unlockCache():
    '''returns None\n\n
    unlockCache(final DisReadWriteLock.Usage usage)\n
    '''
def refreshCache():
    '''returns None\n\n
    refreshCache()\n
    '''
def hasMetadataChanged():
    '''returns boolean\n\n
    hasMetadataChanged(final Date since)\n
    '''
def buildShortName():
    '''returns String\n\n
    buildShortName(final String className)\n
    '''
def isDuplicateClass():
    '''returns boolean\n\n
    isDuplicateClass(final String className)\n
    '''
