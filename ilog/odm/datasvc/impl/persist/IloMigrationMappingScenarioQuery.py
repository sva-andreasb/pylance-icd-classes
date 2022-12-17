COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
MAPPING_TABLE_NAME = "String  \"MigrationOidMap\""
MAPPING_ID = "String  \"MappingId\""
def ():
    '''returns IloMigrationMappingScenarioQuery\n\n
    ()\n
    '''
def setMigrationCommands():
    '''returns None\n\n
    setMigrationCommands(final IloRepositoryScenarioMigrator.IloRepositoryMigrationCommands migration_commands)\n
    '''
def getSourceDataTableMapping():
    '''returns IloDataTableMapping\n\n
    getSourceDataTableMapping()\n
    '''
def setSourceDataTableMapping():
    '''returns None\n\n
    setSourceDataTableMapping(final IloDataTableMapping data_table_mapping)\n
    '''
def getTargetDataTableMapping():
    '''returns IloDataTableMapping\n\n
    getTargetDataTableMapping()\n
    '''
def setTargetDataTableMapping():
    '''returns None\n\n
    setTargetDataTableMapping(final IloDataTableMapping data_table_mapping)\n
    '''
def setAlreadyMigrated():
    '''returns None\n\n
    setAlreadyMigrated(final Collection<String> already_migrated)\n
    '''
def getInsertColumns():
    '''returns StringBuffer\n\n
    getInsertColumns(final IloTransactionalSession session, final IloSchema target_schema, final List<IloColumn> target_columns, final List<IloColumn> default_columns)\n
    '''
def getSelectColumnCast():
    '''returns String\n\n
    getSelectColumnCast(final String column_physical_name, final IloColumn column, final IloColumn dest_column)\n
    '''
def getDefaultColumnCast():
    '''returns String\n\n
    getDefaultColumnCast(final String column_physical_name, final IloColumn dest_column)\n
    '''
def getSelectColumns():
    '''returns StringBuffer\n\n
    getSelectColumns(final IloTransactionalSession session, final IloSchema source_schema, final IloSchema target_schema, final List<IloColumn> source_columns, final List<IloColumn> target_columns, final List<IloColumn> default_columns)\n
    '''
def getMappingSelectColumns():
    '''returns StringBuffer\n\n
    getMappingSelectColumns(final IloTransactionalSession session, final IloSchema source_schema, final IloSchema target_schema, final List<IloColumn> source_columns, final List<IloColumn> target_columns, final List<IloColumn> default_columns)\n
    '''
def execute():
    '''returns Object\n\n
    execute(final IloTransactionalSession session)\n
    '''
def prepare():
    '''returns None\n\n
    prepare(final Properties properties)\n
    '''
