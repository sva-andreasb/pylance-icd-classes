COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
MATERIALIZE_TABLE_LAZY = "String  \"MATERIALIZE_TABLE_LAZY\""
DEFAULT_MATERIALIZE_TABLE_LAZY = "String  \"true\""
def ():
    '''returns IloCreateScenarioTablesQuery\n\n
    ()\n
    '''
def setCreateSingleRows():
    '''returns None\n\n
    setCreateSingleRows(final boolean create_single_rows)\n
    '''
def setDeferRowCreation():
    '''returns None\n\n
    setDeferRowCreation(final boolean defer_row_creation)\n
    '''
def getDeferedRowCreated():
    '''returns List<IloPersistentRow>\n\n
    getDeferedRowCreated()\n
    '''
def getDeferedSingleRowCreated():
    '''returns List<IloPersistentRow>\n\n
    getDeferedSingleRowCreated()\n
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
def getCreatedDataTableMapping():
    '''returns IloDataTableMapping\n\n
    getCreatedDataTableMapping()\n
    '''
def setExcludedSchemaIds():
    '''returns None\n\n
    setExcludedSchemaIds(final Collection<String> excluded_schema_ids)\n
    '''
def setLazyCreationMode():
    '''returns None\n\n
    setLazyCreationMode(final boolean lazy_creation_mode)\n
    '''
def setTxnRow():
    '''returns None\n\n
    setTxnRow(final IloPersistentRow txn_row)\n
    '''
def execute():
    '''returns Object\n\n
    execute(final IloTransactionalSession session)\n
    '''
def process():
    '''returns None\n\n
    process(final IloTransactionalSession session)\n
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
