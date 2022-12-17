COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def getFieldConformity():
    '''returns String\n\n
    getFieldConformity(final String type)\n
    '''
def isSingleUserMode():
    '''returns boolean\n\n
    isSingleUserMode()\n
    '''
def getDBConnectionProfile():
    '''returns IloDBConnectionProfile\n\n
    getDBConnectionProfile()\n
    '''
def validate():
    '''returns None\n\n
    validate()\n
    '''
def getRepositoryManagerClass():
    '''returns Class\n\n
    getRepositoryManagerClass()\n
    '''
def getApplicationSchemaName():
    '''returns String\n\n
    getApplicationSchemaName()\n
    '''
def isMultiUserMode():
    '''returns boolean\n\n
    isMultiUserMode()\n
    '''
def setConcurrencyMode():
    '''returns None\n\n
    setConcurrencyMode(final IloDataService.ConcurrencyMode value)\n
    '''
def useSingleUserMode():
    '''returns None\n\n
    useSingleUserMode()\n
    '''
def useMultiUserMode():
    '''returns None\n\n
    useMultiUserMode()\n
    '''
def useDefaultSchemaAndUser():
    '''returns None\n\n
    useDefaultSchemaAndUser()\n
    '''
def useCustomSchemaAndUser():
    '''returns None\n\n
    useCustomSchemaAndUser()\n
    '''
def isUsingDefaultSchemaAndUser():
    '''returns boolean\n\n
    isUsingDefaultSchemaAndUser()\n
    '''
def setManagerClassname():
    '''returns None\n\n
    setManagerClassname(final String managerClassname)\n
    '''
def useDefaultManagerConfig():
    '''returns None\n\n
    useDefaultManagerConfig()\n
    '''
def getManagerClassname():
    '''returns String\n\n
    getManagerClassname()\n
    getManagerClassname()\n
    getManagerClassname()\n
    getManagerClassname()\n
    getManagerClassname()\n
    getManagerClassname()\n
    getManagerClassname()\n
    '''
def getAuthenticationManagerClassName():
    '''returns String\n\n
    getAuthenticationManagerClassName()\n
    '''
def getRepositoryManagerProperties():
    '''returns Properties\n\n
    getRepositoryManagerProperties()\n
    '''
def setRepositoryManagerProperties():
    '''returns None\n\n
    setRepositoryManagerProperties(final Properties props)\n
    '''
def isCustomDatabaseType():
    '''returns boolean\n\n
    isCustomDatabaseType()\n
    '''
def setServerHostname():
    '''returns None\n\n
    setServerHostname(final String hostname)\n
    '''
def getServerHostname():
    '''returns String\n\n
    getServerHostname()\n
    '''
def setInMemory():
    '''returns None\n\n
    setInMemory(final boolean in_memory)\n
    '''
def setServerPort():
    '''returns None\n\n
    setServerPort(final int port)\n
    '''
def getServerPort():
    '''returns int\n\n
    getServerPort()\n
    '''
def setInstanceName():
    '''returns None\n\n
    setInstanceName(final String instanceName)\n
    '''
def getInstanceName():
    '''returns String\n\n
    getInstanceName()\n
    '''
def setDatabaseSchema():
    '''returns None\n\n
    setDatabaseSchema(final String databaseSchema)\n
    '''
def getDatabaseSchema():
    '''returns String\n\n
    getDatabaseSchema()\n
    '''
def setDatabaseUser():
    '''returns None\n\n
    setDatabaseUser(final String databaseUser)\n
    '''
def getDatabaseUser():
    '''returns String\n\n
    getDatabaseUser()\n
    '''
def setDatabasePassword():
    '''returns None\n\n
    setDatabasePassword(final String databasePassword)\n
    '''
def getDatabasePassword():
    '''returns String\n\n
    getDatabasePassword()\n
    '''
def setRepositoryLocationType():
    '''returns None\n\n
    setRepositoryLocationType(final RepositoryLocationType value)\n
    '''
def getRepositoryLocationType():
    '''returns RepositoryLocationType\n\n
    getRepositoryLocationType()\n
    '''
def setRepositoryRelativeLocation():
    '''returns None\n\n
    setRepositoryRelativeLocation(final String value)\n
    '''
def getRepositoryRelativeLocation():
    '''returns String\n\n
    getRepositoryRelativeLocation()\n
    '''
def makeAbsoluteLocation():
    '''returns String\n\n
    makeAbsoluteLocation(final String odmAppDeployDir, final String relativeRepositoryPath)\n
    '''
def makeRelativeLocation():
    '''returns String\n\n
    makeRelativeLocation(final String odmAppDeployDir, String absoluteRepositoryPath)\n
    '''
def getConnection():
    '''returns IloDBConnectionProfileImpl\n\n
    getConnection()\n
    '''
def getHelper():
    '''returns RepositoryManagerHelper\n\n
    getHelper()\n
    '''
def migrateOnOpen():
    '''returns None\n\n
    migrateOnOpen()\n
    '''
def ():
    '''returns MissingRepositoryManagerTagException\n\n
    (final String message)\n
    '''
def createDatabase():
    '''returns None\n\n
    createDatabase(final String appID, final File odmAppDir, final IloRepositoryAccessProfileImpl profile, final String adminLogin, final String adminPassword)\n
    '''
def deleteDatabase():
    '''returns None\n\n
    deleteDatabase(final String appID, final File odmAppDir, final IloRepositoryAccessProfileImpl profile, final String adminLogin, final String adminPassword)\n
    deleteDatabase(final String appID, final File odmAppDir, final IloRepositoryAccessProfileImpl profile, final String adminLogin, final String adminPassword)\n
    '''
def call():
    '''returns Void\n\n
    call()\n
    '''
def testUserConnection():
    '''returns Future<Void>\n\n
    testUserConnection(final String appID, final File odmAppDir, final IloRepositoryAccessProfileImpl profile, final boolean createSchema)\n
    '''
def testAdminConnection():
    '''returns Future<Void>\n\n
    testAdminConnection(final String appID, final File odmAppDir, final IloRepositoryAccessProfileImpl profile, final String adminLogin, final String adminPassword)\n
    '''
def getRepositoryManager():
    '''returns IloRepositoryManager\n\n
    getRepositoryManager(final IloRepositoryManagerFactory factory)\n
    '''
def getRepositoryManagerFactory():
    '''returns IloRepositoryManagerFactory\n\n
    getRepositoryManagerFactory(final String appID, final File odmAppDir, final IloRepositoryAccessProfileImpl profile, final String adminLogin, final String adminPassword)\n
    '''
def isCustom():
    '''returns boolean\n\n
    isCustom()\n
    isCustom()\n
    '''
def isMultiUser():
    '''returns boolean\n\n
    isMultiUser()\n
    isMultiUser()\n
    isMultiUser()\n
    isMultiUser()\n
    isMultiUser()\n
    '''
def getTrustedUserPassword():
    '''returns String\n\n
    getTrustedUserPassword(final String name)\n
    '''
def getTrustedSchemaName():
    '''returns String\n\n
    getTrustedSchemaName(final String name)\n
    '''
def getDisplayName():
    '''returns String\n\n
    getDisplayName()\n
    getDisplayName()\n
    getDisplayName()\n
    getDisplayName()\n
    getDisplayName()\n
    '''
def newDefaultRepositoryManagerFactory():
    '''returns IloRepositoryManagerFactory\n\n
    newDefaultRepositoryManagerFactory()\n
    newDefaultRepositoryManagerFactory()\n
    newDefaultRepositoryManagerFactory()\n
    newDefaultRepositoryManagerFactory()\n
    newDefaultRepositoryManagerFactory()\n
    newDefaultRepositoryManagerFactory()\n
    '''
def usesDatabaseSchema():
    '''returns boolean\n\n
    usesDatabaseSchema()\n
    usesDatabaseSchema()\n
    usesDatabaseSchema()\n
    usesDatabaseSchema()\n
    usesDatabaseSchema()\n
    '''
def extractParameters():
    '''returns boolean\n\n
    extractParameters(final IloRepositoryAccessProfileImpl profile)\n
    extractParameters(final IloRepositoryAccessProfileImpl profile)\n
    extractParameters(final IloRepositoryAccessProfileImpl profile)\n
    extractParameters(final IloRepositoryAccessProfileImpl profile)\n
    extractParameters(final IloRepositoryAccessProfileImpl profile)\n
    extractParameters(final IloRepositoryAccessProfileImpl profile)\n
    '''
def getJdbcUrl():
    '''returns String\n\n
    getJdbcUrl(final IloRepositoryAccessProfileImpl profile)\n
    getJdbcUrl(final IloRepositoryAccessProfileImpl profile)\n
    getJdbcUrl(final IloRepositoryAccessProfileImpl profile)\n
    getJdbcUrl(final IloRepositoryAccessProfileImpl profile)\n
    getJdbcUrl(final IloRepositoryAccessProfileImpl profile)\n
    getJdbcUrl(final IloRepositoryAccessProfileImpl profile)\n
    '''
def canCreateUser():
    '''returns boolean\n\n
    canCreateUser()\n
    canCreateUser()\n
    canCreateUser()\n
    canCreateUser()\n
    canCreateUser()\n
    canCreateUser()\n
    '''
def getDatabaseLocation():
    '''returns File\n\n
    getDatabaseLocation(final String appID, final File odmAppDir, final IloRepositoryAccessProfileImpl profile)\n
    '''
