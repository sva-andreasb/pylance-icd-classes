COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloDataTableMapping\n\n
    ()\n
    (final Collection<IloRow> scenario_data_tables)\n
    (final IloDataTableMapping data_table_mapping)\n
    '''
def getDataTable():
    '''returns IloRow\n\n
    getDataTable(final String schema_id)\n
    '''
def getDataTables():
    '''returns Collection<IloRow>\n\n
    getDataTables()\n
    '''
def getDataTableId():
    '''returns Long\n\n
    getDataTableId(final String schema_id)\n
    '''
def getDataTableTcn():
    '''returns Long\n\n
    getDataTableTcn(final String schema_id)\n
    '''
def getDataTableLastModifier():
    '''returns Long\n\n
    getDataTableLastModifier(final String schema_id)\n
    '''
def diff():
    '''returns List<IloRow>\n\n
    diff(final IloDataTableMapping mapping)\n
    '''
def getDataTableLastModificationDate():
    '''returns Date\n\n
    getDataTableLastModificationDate(final String schema_id)\n
    '''
def getShemaId():
    '''returns String\n\n
    getShemaId(final Long table_id)\n
    '''
def getDataTableIds():
    '''returns List<Long>\n\n
    getDataTableIds()\n
    '''
def setDataTable():
    '''returns None\n\n
    setDataTable(final IloRow data_table)\n
    '''
def setDataTableTxn():
    '''returns IloRow\n\n
    setDataTableTxn(final String schema_id, final IloPersistentRow txn_row)\n
    '''
def removeDataTable():
    '''returns None\n\n
    removeDataTable(final String schema_id)\n
    '''
def getSchemaIds():
    '''returns Collection<String>\n\n
    getSchemaIds()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
