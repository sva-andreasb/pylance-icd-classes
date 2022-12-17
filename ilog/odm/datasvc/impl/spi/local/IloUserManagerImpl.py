COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
SESSION_TIMEOUT_PROPERTY = "String  \"session_timeout\""
CLEAN_DATA_ENABLED_PROPERTY = "String  \"CLEAN_DATA_ENABLED\""
DEFAULT_CLEAN_DATA_ENABLED = "boolean  true"
HOSTNAME_PROPERTY = "String  \"HOST\""
ODM_VERSION = "String  \"ODMVER\""
ODM_SERVER_CONTEXT = "String  \"ODMCTX\""
APPLICATION_VERSION = "String  \"APPVER\""
ODME_ADMIN_ROLE = "String  \"HAS_ADMIN_ROLE\""
HOSTIP_PROPERTY = "String  \"IP\""
APPCHKSUM_PROPERTY = "String  \"CHECKSUM\""
OPTIMIZATION_SERVICE_USER = "String  \"__optimservice\""
PASSWORD_ENCRYPTED_PROPERTY = "String  \"ilog.edi.password_encrypted\""
AUTOMATIC_USER_MAPPING = "String  \"AUTOMATIC_USER_MAPPING\""
VERIFY_CHECKSUM = "String  \"VERIFY_CHECKSUM\""
def ():
    '''returns IloUserManagerImpl\n\n
    (final IloApplicationContext context, final IloDataManagerImpl data_manager, final IloRepositoryAccessProfile repository_profile)\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def getRepositoryManager():
    '''returns IloRepositoryManager\n\n
    getRepositoryManager()\n
    '''
def getSystemSchemaCatalog():
    '''returns IloSchemaCatalog\n\n
    getSystemSchemaCatalog()\n
    '''
def getApplicationSchemaCatalog():
    '''returns IloSchemaCatalog\n\n
    getApplicationSchemaCatalog()\n
    '''
def addRight():
    '''returns int\n\n
    addRight(final Long user_id, String right)\n
    '''
def getRoles():
    '''returns Set<String>\n\n
    getRoles(final Long user_id)\n
    '''
def addRole():
    '''returns None\n\n
    addRole(final Long user_id, final String role)\n
    '''
def removeRole():
    '''returns None\n\n
    removeRole(final Long user_id, final String role)\n
    '''
def addPossibleUserRight():
    '''returns None\n\n
    addPossibleUserRight(final String rightId)\n
    '''
def checkSession():
    '''returns None\n\n
    checkSession(final Long session_id)\n
    '''
def getSession():
    '''returns IloRow\n\n
    getSession(final Long session_id)\n
    '''
def closeSession():
    '''returns None\n\n
    closeSession(final Long session_id)\n
    '''
def cleanSessions():
    '''returns None\n\n
    cleanSessions()\n
    '''
def createUser():
    '''returns IloRow\n\n
    createUser(final String name)\n
    '''
def removeUser():
    '''returns None\n\n
    removeUser(final Long user_id)\n
    '''
def getUserById():
    '''returns IloRow\n\n
    getUserById(final Long user_id)\n
    '''
def getUserByName():
    '''returns IloRow\n\n
    getUserByName(final String name)\n
    '''
def getUsers():
    '''returns IloSchemaRowMap\n\n
    getUsers()\n
    '''
def removeRight():
    '''returns int\n\n
    removeRight(final Long user_id, String right)\n
    '''
def updateRights():
    '''returns int\n\n
    updateRights(final Long user_id, final IloUser.RIGHTS[] newRights)\n
    '''
def setUserName():
    '''returns None\n\n
    setUserName(final Long user_id, final String name)\n
    '''
def getUserSessions():
    '''returns Collection<IloRow>\n\n
    getUserSessions(final Long user_id)\n
    '''
def getSessionTimeout():
    '''returns long\n\n
    getSessionTimeout()\n
    '''
def setSessionTimeout():
    '''returns None\n\n
    setSessionTimeout(final long session_timeout)\n
    '''
def getTransactions():
    '''returns IloSchemaRowMap\n\n
    getTransactions(final Collection<Long> transaction_ids)\n
    '''
def hasRight():
    '''returns boolean\n\n
    hasRight(final Long user_id, final String right)\n
    '''
def getRights():
    '''returns Collection<String>\n\n
    getRights()\n
    '''
def openSession():
    '''returns IloRow\n\n
    openSession(String username, final String type, final boolean unique, final Properties props, final boolean force)\n
    '''
