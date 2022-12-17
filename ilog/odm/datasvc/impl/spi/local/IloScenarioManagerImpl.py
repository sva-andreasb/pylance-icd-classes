COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
STATE_NORMAL = "int  0"
def ():
    '''returns IloTargetScenario\n\n
    (final IloApplicationContext context, final IloDataManagerImpl data_manager)\n
    (final IloScenarioImpl scenario, final IloScenarioTableContainer source, final IloTableContainer target)\n
    (final IloScenarioImpl scenario, final IloScenarioTableContainer container, final Collection<String> already_migrated_schema_ids)\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def createScenario():
    '''returns IloRow\n\n
    createScenario(final String catalog_id)\n
    '''
def createScenarioCopy():
    '''returns IloRow\n\n
    createScenarioCopy(final Long source_id, final Long source_version)\n
    '''
def delete():
    '''returns None\n\n
    delete(final Long scenario_id, final boolean temporary_check)\n
    delete()\n
    delete()\n
    '''
def getDataTableMapping():
    '''returns IloSchemaRowMap\n\n
    getDataTableMapping(final Long scenario_id, final String schema_restriction, final boolean disable_migration)\n
    '''
def migrate():
    '''returns None\n\n
    migrate(final IloTransactionalSession session, final Long scenario_id)\n
    '''
def revertFromRepository():
    '''returns None\n\n
    revertFromRepository(final Long scenario_id, final Long source_id, final Set<String> schema_ids)\n
    '''
def getRows():
    '''returns IloSchemaRowMap\n\n
    getRows(final Long scenario_id, final String catalog_id, final String table_name, final Long table_id, final Long minTcn, final Long maxTcn, final boolean load_deleted, final Long min_range, final Long max_range, final boolean check_table_id, final IloSessionQueryFilter filter)\n
    '''
def countRows():
    '''returns int\n\n
    countRows(final Long scenario_id, final String catalog_id, final String table_name, final Long table_id, final Long minTcn, final Long maxTcn, final boolean load_deleted, final Long min_range, final Long max_range, final boolean check_table_id, final IloSessionQueryFilter filter)\n
    '''
def getScenario():
    '''returns IloRow\n\n
    getScenario(final Long scenario_id)\n
    '''
def save():
    '''returns None\n\n
    save(final Long scenario_id, final Long scenario_version, final IloTableUpdate table_update, final boolean hasErrors, final boolean hasWarnings)\n
    save()\n
    save()\n
    '''
def patch():
    '''returns IloSchemaRowMap\n\n
    patch(final Long scenario_id, final IloScenarioUpdateSession session)\n
    '''
def setName():
    '''returns IloRow\n\n
    setName(final Long scenario_id, final String name)\n
    '''
def addLock():
    '''returns IloRow\n\n
    addLock(final Long scenario_id, final int type, final int description, final boolean persistent)\n
    '''
def tranfertLock():
    '''returns IloRow\n\n
    tranfertLock(final Long scenario_id, final Long lock_id, final Long user_id)\n
    '''
def removeLock():
    '''returns None\n\n
    removeLock(final Long scenario_id, final Long lock_id)\n
    '''
def getLocks():
    '''returns IloSchemaRowMap\n\n
    getLocks(final Long scenario_id, final Long current_version)\n
    '''
def getBulkLocks():
    '''returns IloSchemaRowMap\n\n
    getBulkLocks(final Long[] scenario_ids, final Long[] current_versions)\n
    '''
def getLockVersion():
    '''returns Long\n\n
    getLockVersion(final Long scenario_id)\n
    '''
def checkIntegrity():
    '''returns IloSchemaRowMap\n\n
    checkIntegrity(final Long scenario_id, final Collection<String> table_names, final int overflow)\n
    '''
def getSchemaRowIds():
    '''returns IloLongCollection\n\n
    getSchemaRowIds(final String catalog_id, final String table_name, final int size)\n
    '''
def getNotEnoughResourceErrors():
    '''returns long\n\n
    getNotEnoughResourceErrors()\n
    '''
def getIssuesReport():
    '''returns IloIssuesReportImpl\n\n
    getIssuesReport()\n
    '''
def setLoadingDisabled():
    '''returns None\n\n
    setLoadingDisabled(final boolean loading_disabled)\n
    setLoadingDisabled(final boolean loading_disabled)\n
    '''
def beginModifications():
    '''returns None\n\n
    beginModifications(final Object userData)\n
    '''
def getModificationUserData():
    '''returns Object\n\n
    getModificationUserData()\n
    '''
def getAlreadyMigrated():
    '''returns Collection<String>\n\n
    getAlreadyMigrated()\n
    '''
def isAlreadyMigrated():
    '''returns boolean\n\n
    isAlreadyMigrated(final String schema_id)\n
    '''
