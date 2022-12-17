COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloSystemDataMigratorRebuild\n\n
    (final IloSystemModel system_model)\n
    '''
def migrate():
    '''returns None\n\n
    migrate(final IloRepositoryManager repository_manager)\n
    '''
def migrateSchemaCatalog():
    '''returns None\n\n
    migrateSchemaCatalog(final IloRepositoryManager repository_manager, final Map<String, IloSchemaCatalog> source_catalog_map, final Map<String, IloSchemaCatalog> destination_catalog_map)\n
    '''
def migrateSystemCatalog():
    '''returns None\n\n
    migrateSystemCatalog(final IloRepositoryManager repository_manager, final Map<String, IloSchemaCatalog> source_catalog_map, final Map<String, IloSchemaCatalog> destination_catalog_map)\n
    '''
def migrateScenarioCatalog():
    '''returns None\n\n
    migrateScenarioCatalog(final IloRepositoryManager repository_manager, final Map<String, IloSchemaCatalog> source_catalog_map, final Map<String, IloSchemaCatalog> destination_catalog_map)\n
    '''
def migrateScenarioAndDataTables():
    '''returns None\n\n
    migrateScenarioAndDataTables(final IloRepositoryManager repository_manager, final Map<String, IloSchemaCatalog> source_catalog_map, final Map<String, IloSchemaCatalog> destination_catalog_map)\n
    '''
def getSourceVersion():
    '''returns String\n\n
    getSourceVersion()\n
    '''
def getTargetVersion():
    '''returns String\n\n
    getTargetVersion()\n
    '''
