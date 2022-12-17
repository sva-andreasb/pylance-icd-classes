COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloSystemDataManager\n\n
    (final IloApplicationContext application_context, final IloScenarioSourceProvider scen_src_provider, final File odm_app_dir, final IloNameSpaceProfileManager app_profile, final String data_server_url, final boolean in_data_server_context)\n
    (final IloApplicationContext application_context, final IloScenarioSourceProvider scen_src_provider, final File odm_app_dir, final IloNameSpaceProfileManager app_profile, final String data_server_url)\n
    (final IloApplicationContext application_context, final IloRepositoryAccessProfile repository_profile, final IloNameSpaceProfileManager app_profile, final File odmAppDir, final String app_id, final String app_version, final String data_server_url, final String archiveChecksum)\n
    '''
def login():
    '''returns IloODMSession\n\n
    login(final IloCredential credential, final boolean force, final boolean admin)\n
    login(final IloCredential credential, final X509TrustManager manager, final boolean force, final boolean admin)\n
    '''
def openSession():
    '''returns IloODMSession\n\n
    openSession(final String username, final boolean force)\n
    '''
def logout():
    '''returns None\n\n
    logout()\n
    '''
def getSessionTimeout():
    '''returns long\n\n
    getSessionTimeout()\n
    '''
def setMigrationConfiguration():
    '''returns None\n\n
    setMigrationConfiguration(final IloScenarioMigrator scenario_migrator)\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def getApplicationContext():
    '''returns IloApplicationContext\n\n
    getApplicationContext()\n
    '''
def getSystemModel():
    '''returns IloSystemModel\n\n
    getSystemModel()\n
    '''
def getUserManager():
    '''returns IloUserManager\n\n
    getUserManager()\n
    '''
def getWorkspaceManager():
    '''returns IloWorkspaceManager\n\n
    getWorkspaceManager()\n
    '''
def getScenarioManager():
    '''returns IloScenarioManager\n\n
    getScenarioManager()\n
    '''
def getDataManager():
    '''returns IloDataManager\n\n
    getDataManager()\n
    '''
def getApplicationSchemaCatalog():
    '''returns IloSchemaCatalog\n\n
    getApplicationSchemaCatalog()\n
    '''
def getScenarioExtensionContext():
    '''returns IloScenarioExtensionContext\n\n
    getScenarioExtensionContext()\n
    '''
def setScenarioExtensionContext():
    '''returns None\n\n
    setScenarioExtensionContext(final IloScenarioExtensionContext extension_context)\n
    '''
def createWorkspace():
    '''returns IloWorkspace\n\n
    createWorkspace()\n
    '''
def createTempScenario():
    '''returns IloScenario\n\n
    createTempScenario()\n
    createTempScenario(final IloScenario source)\n
    '''
def getWorkspace():
    '''returns IloWorkspace\n\n
    getWorkspace(final String persistent_id)\n
    '''
def getScenario():
    '''returns IloScenario\n\n
    getScenario(final String persistent_id)\n
    '''
def checkSession():
    '''returns None\n\n
    checkSession(final IloODMSession odm_session)\n
    '''
def getUser():
    '''returns IloUser\n\n
    getUser(final String name)\n
    '''
def createUser():
    '''returns IloUser\n\n
    createUser(final String name)\n
    '''
def getAnonymousUser():
    '''returns String\n\n
    getAnonymousUser()\n
    '''
def getUserSession():
    '''returns IloODMSession\n\n
    getUserSession()\n
    '''
def isInDataServerContext():
    '''returns boolean\n\n
    isInDataServerContext()\n
    '''
