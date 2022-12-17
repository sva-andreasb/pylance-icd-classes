COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloDeleteScenarioTablesQuery\n\n
    ()\n
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
def setDataTableMapping():
    '''returns None\n\n
    setDataTableMapping(final IloDataTableMapping data_table_mapping)\n
    '''
def getRestrictedSchemaIds():
    '''returns Collection<String>\n\n
    getRestrictedSchemaIds()\n
    '''
def setRestrictedSchemaIds():
    '''returns None\n\n
    setRestrictedSchemaIds(final Collection<String> restricted_schema_id)\n
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
