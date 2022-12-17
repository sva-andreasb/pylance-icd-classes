COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
SAVE_CHECK_ORDER_PROPERTY = "String  \"SAVE_CHECK_ORDER\""
SAVE_CHECK_ORDER_DEFAULT = "String  \"true\""
def ():
    '''returns IloSaveScenarioTablesQuery\n\n
    ()\n
    '''
def prepare():
    '''returns None\n\n
    prepare(final Properties properties)\n
    '''
def getScenarioSystemId():
    '''returns Long\n\n
    getScenarioSystemId()\n
    '''
def setScenarioSystemId():
    '''returns None\n\n
    setScenarioSystemId(final Long id)\n
    '''
def getSystemCatalog():
    '''returns IloSchemaCatalog\n\n
    getSystemCatalog()\n
    '''
def setSystemCatalog():
    '''returns None\n\n
    setSystemCatalog(final IloSchemaCatalog system_catalog)\n
    '''
def getScenarioCatalog():
    '''returns IloSchemaCatalog\n\n
    getScenarioCatalog()\n
    '''
def setScenarioCatalog():
    '''returns None\n\n
    setScenarioCatalog(final IloSchemaCatalog scenario_catalog)\n
    '''
def setTxnRow():
    '''returns None\n\n
    setTxnRow(final IloPersistentRow txn_row)\n
    '''
def getInitialDataTableMapping():
    '''returns IloDataTableMapping\n\n
    getInitialDataTableMapping()\n
    '''
def setInitialDataTableMapping():
    '''returns None\n\n
    setInitialDataTableMapping(final IloDataTableMapping data_table_mapping)\n
    '''
def getTargetDataTableMapping():
    '''returns IloDataTableMapping\n\n
    getTargetDataTableMapping()\n
    '''
def setTableUpdate():
    '''returns None\n\n
    setTableUpdate(final IloTableUpdate table_update)\n
    '''
def execute():
    '''returns Object\n\n
    execute(final IloTransactionalSession session)\n
    '''
def process():
    '''returns None\n\n
    process(final IloTransactionalSession session)\n
    '''
def materializeTables():
    '''returns None\n\n
    materializeTables(final IloTransactionalSession session, final Set<IloSchema> modified_schemas, final Map<Long, IloSchema> shared_data_tables_map)\n
    '''
def createOwnedTables():
    '''returns None\n\n
    createOwnedTables(final IloTransactionalSession session, final Map<Long, IloSchema> shared_data_tables_map)\n
    '''
def copyToOwnedTables():
    '''returns Set<IloSchema>\n\n
    copyToOwnedTables(final IloTransactionalSession session)\n
    '''
def preCommit():
    '''returns None\n\n
    preCommit(final IloTransactionalSession session)\n
    '''
def postCommit():
    '''returns None\n\n
    postCommit(final IloTransactionalSession session, final boolean error)\n
    '''
def rollback():
    '''returns None\n\n
    rollback(final IloTransactionalSession session, final boolean error)\n
    '''
def end():
    '''returns None\n\n
    end(final IloRepositoryManager manager, final boolean committed, final boolean error)\n
    '''
def getReport():
    '''returns String\n\n
    getReport()\n
    '''
