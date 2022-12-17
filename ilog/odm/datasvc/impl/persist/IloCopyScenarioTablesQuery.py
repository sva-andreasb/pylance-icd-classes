COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloCopyScenarioTablesQuery\n\n
    ()\n
    '''
def getScenarioCatalog():
    '''returns IloSchemaCatalog\n\n
    getScenarioCatalog()\n
    '''
def setScenarioCatalog():
    '''returns None\n\n
    setScenarioCatalog(final IloSchemaCatalog scenario_catalog)\n
    '''
def setSourceDataTableMapping():
    '''returns None\n\n
    setSourceDataTableMapping(final IloDataTableMapping data_table_mapping)\n
    '''
def setTargetDataTableMapping():
    '''returns None\n\n
    setTargetDataTableMapping(final IloDataTableMapping target_data_table_mapping)\n
    '''
def setAllDeleted():
    '''returns None\n\n
    setAllDeleted(final Collection<IloSchema> all_deleted, final Long scenario_eov)\n
    '''
def prepare():
    '''returns None\n\n
    prepare(final Properties properties)\n
    '''
def execute():
    '''returns Object\n\n
    execute(final IloTransactionalSession session)\n
    '''
