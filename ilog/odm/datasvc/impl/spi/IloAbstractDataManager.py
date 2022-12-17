COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
TEMP_DIR_PROPERTY = "String  \"TEMP_DIR\""
DERIVED_TABLE_ENABLED_PROPERTY = "String  \"DERIVED_TABLE_ENABLED\""
def ():
    '''returns IloAbstractDataManager\n\n
    (final IloApplicationContext context, final IloRepositoryAccessProfile repository_profile, final IloNameSpaceProfileManager app_profile, final String app_id, final String app_version, final IloSystemDataManager system_data_manager)\n
    (final IloApplicationContext context, final IloDataService.ConcurrencyMode concurrency_mode, final IloNameSpaceProfileManager app_profile, final String app_id, final String app_version, final IloSystemDataManager system_data_manager)\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def getCacheManager():
    '''returns IloCacheManager\n\n
    getCacheManager()\n
    '''
def getApplicationTempDir():
    '''returns File\n\n
    getApplicationTempDir()\n
    '''
def getRepositoryManagerProperties():
    '''returns Properties\n\n
    getRepositoryManagerProperties()\n
    '''
def getSystemSchemaCatalog():
    '''returns IloSchemaCatalog\n\n
    getSystemSchemaCatalog()\n
    '''
def getApplicationSchemaCatalog():
    '''returns IloSchemaCatalog\n\n
    getApplicationSchemaCatalog()\n
    '''
def getApplicationId():
    '''returns String\n\n
    getApplicationId()\n
    '''
def getApplicationVersion():
    '''returns String\n\n
    getApplicationVersion()\n
    '''
def getSystemModel():
    '''returns IloSystemModel\n\n
    getSystemModel()\n
    '''
def getLockManager():
    '''returns IloDataLockManager\n\n
    getLockManager()\n
    '''
def getUser():
    '''returns IloUser\n\n
    getUser(final Long user_id, final boolean refresh)\n
    '''
def createTempScenario():
    '''returns IloScenario\n\n
    createTempScenario()\n
    createTempScenario(final IloScenario source)\n
    '''
def setThreadSession():
    '''returns None\n\n
    setThreadSession(final boolean thread_session)\n
    '''
def getUserSession():
    '''returns IloODMSession\n\n
    getUserSession()\n
    getUserSession(final Long session_id)\n
    '''
def getUserSessionId():
    '''returns Long\n\n
    getUserSessionId()\n
    '''
def getSessionAsUserId():
    '''returns Long[]\n\n
    getSessionAsUserId()\n
    '''
def setUserSessionId():
    '''returns None\n\n
    setUserSessionId(final Long session_id)\n
    '''
def getRecycleBin():
    '''returns IloRecycleBinImpl\n\n
    getRecycleBin(final boolean refresh)\n
    '''
def createWorkspace():
    '''returns IloWorkspace\n\n
    createWorkspace()\n
    '''
def getWorkspace():
    '''returns IloWorkspace\n\n
    getWorkspace(final String persistent_id)\n
    '''
def getScenario():
    '''returns IloScenario\n\n
    getScenario(final String persistent_id)\n
    '''
def getScenarioMigrator():
    '''returns IloScenarioMigrator\n\n
    getScenarioMigrator()\n
    '''
def setScenarioMigrator():
    '''returns None\n\n
    setScenarioMigrator(final IloScenarioMigrator scenario_migrator)\n
    '''
def isDerivedTableEnabled():
    '''returns boolean\n\n
    isDerivedTableEnabled()\n
    '''
def login():
    '''returns IloODMSession\n\n
    login(final IloCredential credential, final X509TrustManager manager, final boolean force, final boolean admin)\n
    '''
def openSession():
    '''returns IloODMSession\n\n
    openSession(final String username, final boolean force)\n
    '''
