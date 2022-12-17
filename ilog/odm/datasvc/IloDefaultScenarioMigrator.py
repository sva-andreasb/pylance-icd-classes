COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def getMigrationCommands():
    '''returns IloMigrationCommands\n\n
    getMigrationCommands(final IloScenario scenario, final IloTableContainer target, final IloDataServiceContext dataService)\n
    getMigrationCommands(final IloScenario scenario, final IloTableContainer target)\n
    '''
def migrate():
    '''returns None\n\n
    migrate(final IloScenario scenario, final IloTableContainer outputTables, final IloDataServiceContext dataService)\n
    migrate(final IloScenario scenario, final IloTableContainer outputTables)\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def getSourceSchema():
    '''returns IloSchema\n\n
    getSourceSchema()\n
    '''
def getSourceColumns():
    '''returns List<IloColumn>\n\n
    getSourceColumns()\n
    '''
def getTargetSchema():
    '''returns IloSchema\n\n
    getTargetSchema()\n
    '''
def getTargetColumns():
    '''returns List<IloColumn>\n\n
    getTargetColumns()\n
    '''
def addColumnMapping():
    '''returns None\n\n
    addColumnMapping(final IloColumn source_column, final IloColumn target_column)\n
    '''
def getDefaultValueColumns():
    '''returns List<IloColumn>\n\n
    getDefaultValueColumns()\n
    '''
def addDefaultValueColumn():
    '''returns None\n\n
    addDefaultValueColumn(final IloColumn target_column)\n
    '''
def removeDefaultValueColumn():
    '''returns None\n\n
    removeDefaultValueColumn(final IloColumn target_column)\n
    '''
def removeSourceColumn():
    '''returns None\n\n
    removeSourceColumn(final IloColumn column)\n
    '''
def removeTargetColumn():
    '''returns None\n\n
    removeTargetColumn(final IloColumn column)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def ():
    '''returns IloMigrationCommands\n\n
    ()\n
    '''
def addMapping():
    '''returns None\n\n
    addMapping(final IloSchema current_schema, final List<IloColumn> current_columns, final IloSchema target_schema, final List<IloColumn> target_columns)\n
    '''
def getMapping():
    '''returns IloMigrationMapping\n\n
    getMapping(final IloSchema current_schema, final IloSchema target_schema)\n
    '''
def removeMapping():
    '''returns None\n\n
    removeMapping(final IloMigrationMapping mapping)\n
    '''
def getRepositoryMappings():
    '''returns Collection<IloRepositoryMigrationMapping>\n\n
    getRepositoryMappings()\n
    '''
def getMappings():
    '''returns Collection<IloMigrationMapping>\n\n
    getMappings()\n
    '''
