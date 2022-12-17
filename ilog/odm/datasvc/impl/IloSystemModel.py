COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
SCENARIO_CATALOG_PREFIX = "String  \"v\""
ODM2_5_VERSION = "String  \"2.5.0\""
ODM2_5_SYSTEM_DATA_VERSION = "String  \"0\""
ODM3_0_SYSTEM_DATA_VERSION = "String  \"1\""
ODM3_1_SYSTEM_DATA_VERSION = "String  \"2\""
ODM3_1_1_SYSTEM_DATA_VERSION_V1 = "String  \"3\""
ODM3_1_1_SYSTEM_DATA_VERSION_V2 = "String  \"4\""
ODM3_3_SYSTEM_DATA_VERSION = "String  \"7\""
ODM3_4_SYSTEM_DATA_VERSION = "String  \"8\""
ODM3_5_SYSTEM_DATA_VERSION = "String  \"9\""
ODM3_8_SYSTEM_DATA_VERSION = "String  \"14\""
CURRENT_SYSTEM_DATA_VERSION = "String  \"14\""
ODM2_5_SCENARIO_DATA_VERSION = "String  \"0\""
ODM3_0_SCENARIO_DATA_VERSION = "String  \"1\""
ODM3_1_SCENARIO_DATA_VERSION = "String  \"3\""
ODM3_3_SCENARIO_DATA_VERSION = "String  \"5\""
CURRENT_SCENARIO_DATA_VERSION = "String  \"5\""
SCENARIOTABLES_DELETE = "String  \"__DELETED\""
SCENARIOTABLES_TCN = "String  \"__TCN\""
SCENARIOTABLES_EOV = "String  \"__EOV\""
SCENARIOTABLES_PREVIOUS = "String  \"__PREVIOUS\""
SCENARIOTABLES_NEXT = "String  \"__NEXT\""
SYSTEM_MANAGEMENT_CATALOG_NAME = "String  \"SYS\""
DATA_TABLE_NAME = "String  \"DataTable\""
DATA_NAME = "String  \"name\""
DATA_TCN = "String  \"TCN\""
DATA_USER_ID = "String  \"USER_ID\""
DATA_UPDATE_DATE = "String  \"update_date\""
DATA_DELETED = "String  \"deleted\""
DATACLEAN_TABLE_NAME = "String  \"DataClean\""
DATACLEAN_TABLE_ID = "String  \"TABLE_ID\""
DATACLEAN_NAME = "String  \"name\""
DATACLEAN_TCN = "String  \"CLEAN_TCN\""
DATACLEAN_DATE = "String  \"CLEAN_DATE\""
FOLDERITEM_TABLE_NAME = "String  \"FolderItem\""
FOLDERITEM_WORKSPACE_ID = "String  \"WORKSPACE_ID\""
FOLDERITEM_PARENT_ID = "String  \"PARENT_ID\""
FOLDERITEM_ORDER = "String  \"order\""
FOLDERITEM_REFERENCE_TYPE = "String  \"type\""
FOLDERITEM_REFERENCE_ID = "String  \"reference\""
FOLDERITEM_NAME = "String  \"name\""
FOLDERITEM_TCN = "String  \"tcn\""
FOLDERITEM_REFERENCE_TYPE_FOLDER = "int  0"
FOLDERITEM_REFERENCE_TYPE_SCENARIOREFERENCE = "int  1"
LOCK_REFERENCE_TYPE_WORKSPACE = "int  0"
LOCK_REFERENCE_TYPE_SCENARIO = "int  1"
LOCKABLE_REFERENCE_ID = "String  \"REFERENCE_ID\""
LOCKABLE_LOCK_TCN = "String  \"LOCK_TCN\""
WORKSPACE_LOCKABLE_TABLE_NAME = "String  \"WorkspaceLockable\""
SCENARIO_LOCKABLE_TABLE_NAME = "String  \"ScenarioLockable\""
LOCK_TABLE_NAME = "String  \"Lock\""
LOCK_SESSION_ID = "String  \"SESSION_ID\""
LOCK_REFERENCE_ID = "String  \"REFERENCE_ID\""
LOCK_REFERENCE_TYPE = "String  \"REFERENCE_TYPE\""
LOCK_USER_ID = "String  \"USER_ID\""
LOCK_INITIAL_USER_ID = "String  \"INITIAL_USER_ID\""
LOCK_TYPE = "String  \"type\""
LOCK_DESCRIPTION_CODE = "String  \"desc_code\""
LOCK_DATE = "String  \"lock_date\""
MIGRATED_TABLE_NAME = "String  \"MigratedDataTable\""
MIGRATED_SOURCE_ID = "String  \"SOURCE_TABLE_ID\""
MIGRATED_TARGET_ID = "String  \"TARGET_TABLE_ID\""
MIGRATED_CATALOG_ID = "String  \"CATALOG_ID\""
SCENARIO_TABLE_NAME = "String  \"Scenario\""
SCENARIO_SESSION_ID = "String  \"SESSION_ID\""
SCENARIO_NAME = "String  \"name\""
SCENARIO_STATE = "String  \"state\""
SCENARIO_CATALOG_ID = "String  \"catalog_id\""
SCENARIO_UPDATE_USER_ID = "String  \"USER_ID\""
SCENARIO_UPDATE_DATE = "String  \"update_date\""
SCENARIO_UPDATE_COUNTER = "String  \"update_counter\""
SCENARIO_DATA_TCN = "String  \"DATA_TCN\""
SCENARIO_DATA_TABLE_NAME = "String  \"ScenarioDataTable\""
SCENARIO_DATA_SCENARIO_ID = "String  \"SCENARIO_ID\""
SCENARIO_DATA_TABLE_ID = "String  \"TABLE_ID\""
SESSION_TABLE_NAME = "String  \"Session\""
SESSION_USER_ID = "String  \"user_id\""
SESSION_OPEN_HOST = "String  \"open_host\""
SESSION_OPEN_DATE = "String  \"open_date\""
SESSION_CHECK_DATE = "String  \"check_date\""
SESSION_TYPE = "String  \"type\""
SESSION_UNIQUE = "String  \"unique\""
SCENARIO_TXN_TABLE_NAME = "String  \"ScenarioTransactionDesc\""
SCENARIO_TXN_SCENARIO_ID = "String  \"SCENARIO_ID\""
SCENARIO_TXN_TXNDESC_ID = "String  \"TXNDESC_ID\""
TXNDESC_TABLE_NAME = "String  \"TransactionDesc\""
TXNDESC_USER_ID = "String  \"TransactionUserId\""
TXNDESC_DATE = "String  \"TransactionDate\""
USER_TABLE_NAME = "String  \"User\""
USER_PRINCIPAL = "String  \"principal\""
USER_PASSWORD = "String  \"password\""
USER_RIGHTS = "String  \"rights\""
USERROLE_TABLE_NAME = "String  \"UserRole\""
USERROLE_USER_ID = "String  \"USER_ID\""
USERROLE_ROLE_ID = "String  \"ROLE_ID\""
ROLE_TABLE_NAME = "String  \"Role\""
ROLE_NAME = "String  \"Name\""
WORKSPACE_TABLE_NAME = "String  \"Workspace\""
WORKSPACE_NAME = "String  \"name\""
WORKSPACE_UPDATE_USER_ID = "String  \"USER_ID\""
WORKSPACE_UPDATE_DATE = "String  \"update_date\""
WORKSPACE_UPDATE_COUNTER = "String  \"update_counter\""
WORKSPACE_TCN = "String  \"tcn\""
def ():
    '''returns IloSystemModel\n\n
    ()\n
    '''
def createSystemSchemaCatalog():
    '''returns IloSchemaCatalog\n\n
    createSystemSchemaCatalog()\n
    createSystemSchemaCatalog(final String system_data_version)\n
    '''
def adaptApplicationSchemaCatalog():
    '''returns None\n\n
    adaptApplicationSchemaCatalog(final IloSchemaCatalog app_catalog)\n
    adaptApplicationSchemaCatalog(final String system_data_version, final IloSchemaCatalog app_catalog)\n
    '''
def addCheckDataPattern():
    '''returns None\n\n
    addCheckDataPattern(final Pattern pattern)\n
    '''
def getCheckDataPatterns():
    '''returns Collection<Pattern>\n\n
    getCheckDataPatterns()\n
    '''
def matchCheckDataPatterns():
    '''returns boolean\n\n
    matchCheckDataPatterns(final IloSchema schema)\n
    '''
def getTruncateOnMigrationIds():
    '''returns List<String>\n\n
    getTruncateOnMigrationIds()\n
    '''
