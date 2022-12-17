COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloScenarioTableContainer\n\n
    (final IloScenarioImpl scenario, final Long scenario_system_id, final IloSchemaCatalog catalog, final IloAbstractDataManager data_manager, final IloScenarioUpdateSession update_session, final IloDataTableMapping data_table_mapping)\n
    '''
def getMigration():
    '''returns boolean\n\n
    getMigration()\n
    '''
def setDisableMigration():
    '''returns None\n\n
    setDisableMigration(final boolean migration)\n
    '''
def getScenarioSystemId():
    '''returns Long\n\n
    getScenarioSystemId()\n
    '''
def getUpdateSession():
    '''returns IloScenarioUpdateSession\n\n
    getUpdateSession()\n
    '''
def getDataTableMapping():
    '''returns IloDataTableMapping\n\n
    getDataTableMapping()\n
    '''
def setDataTableMapping():
    '''returns None\n\n
    setDataTableMapping(final IloDataTableMapping data_table_mapping)\n
    '''
def getLastSyncDataTableMapping():
    '''returns IloDataTableMapping\n\n
    getLastSyncDataTableMapping()\n
    '''
def setLastSyncDataTableMapping():
    '''returns None\n\n
    setLastSyncDataTableMapping(final IloDataTableMapping data_table_mapping)\n
    '''
def loadRows():
    '''returns List<IloRow>\n\n
    loadRows(final IloPersistentTable table)\n
    '''
def getRowFactory():
    '''returns IloRowFactory\n\n
    getRowFactory()\n
    '''
def revertedFromRepository():
    '''returns List<IloTable>\n\n
    revertedFromRepository(final IloDataTableMapping refreshed_mapping)\n
    '''
def updatedFromRepository():
    '''returns List<IloTable>\n\n
    updatedFromRepository(final IloDataTableMapping refreshed_mapping, final IloConcurrentChangeUpdatesSetImpl updates, final IloConcurrentChangeConflictsSetImpl conflicts)\n
    '''
def getDataManager():
    '''returns IloAbstractDataManager\n\n
    getDataManager()\n
    '''
def isLoadingDisabled():
    '''returns boolean\n\n
    isLoadingDisabled()\n
    '''
def setLoadingDisabled():
    '''returns None\n\n
    setLoadingDisabled(final boolean loading_disabled)\n
    '''
