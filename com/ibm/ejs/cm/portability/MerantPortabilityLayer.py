def translateException():
    '''returns SQLException\n\n
    translateException(final SQLException e, final Hashtable customMap)\n
    '''
def createTable():
    '''returns None\n\n
    createTable(final Connection connection, final String schema, final String name, final String sql)\n
    createTable(final Connection connection, final String schema, final String sql)\n
    '''
def createTableForPersister():
    '''returns None\n\n
    createTableForPersister(final Connection connection, final String schema, final String name, final String sql)\n
    '''
def addRowLockHint():
    '''returns String\n\n
    addRowLockHint(final String sql)\n
    '''
def supportsRowLockHint():
    '''returns boolean\n\n
    supportsRowLockHint()\n
    '''
def setDate():
    '''returns None\n\n
    setDate(final PreparedStatement ps, final int parameterIndex, final Date date, final Calendar cal)\n
    setDate(final PreparedStatement ps, final int parameterIndex, final Date date)\n
    '''
def setTime():
    '''returns None\n\n
    setTime(final PreparedStatement ps, final int parameterIndex, final Time time, final Calendar cal)\n
    setTime(final PreparedStatement ps, final int parameterIndex, final Time time)\n
    '''
def getDate():
    '''returns Date\n\n
    getDate(final ResultSet rs, final int columnIndex, final Calendar cal)\n
    getDate(final ResultSet rs, final String columnName, final Calendar cal)\n
    getDate(final ResultSet rs, final int columnIndex)\n
    getDate(final ResultSet rs, final String columnName)\n
    '''
def getTime():
    '''returns Time\n\n
    getTime(final ResultSet rs, final int columnIndex, final Calendar cal)\n
    getTime(final ResultSet rs, final String columnName, final Calendar cal)\n
    getTime(final ResultSet rs, final int columnIndex)\n
    getTime(final ResultSet rs, final String columnName)\n
    '''
def scanSQL():
    '''returns String\n\n
    scanSQL(final String sql)\n
    '''
def processSQL():
    '''returns String\n\n
    processSQL(final String sqlString, final int isolevel, final boolean addForUpdate, final boolean addextendedforUpdateSyntax)\n
    '''
def getColumnTypeSpec():
    '''returns String\n\n
    getColumnTypeSpec(final int type)\n
    '''
def getNamedColumnSpec():
    '''returns String\n\n
    getNamedColumnSpec(final int id)\n
    '''
def setTransactionIsolation():
    '''returns None\n\n
    setTransactionIsolation(final Connection connection, final int isolationLevel)\n
    '''
def getDataSource():
    '''returns ConnectionPoolDataSource\n\n
    getDataSource(final DataSourceProperties dsProps)\n
    '''
def getXADataSource():
    '''returns XADataSource\n\n
    getXADataSource(final DataSourceProperties dsProps)\n
    '''
def getDefaultDataSourceProps():
    '''returns Properties\n\n
    getDefaultDataSourceProps()\n
    '''
def supportsSchema():
    '''returns boolean\n\n
    supportsSchema()\n
    '''
def setHugeStringForPreparedStatement():
    '''returns None\n\n
    setHugeStringForPreparedStatement(final HugeString bigstr, final PreparedStatement ps, final int index)\n
    '''
def checkCMPStoreOperation():
    '''returns boolean\n\n
    checkCMPStoreOperation(final String beanId, final Connection c, final boolean loadedForUpdate)\n
    '''
def configureConnection():
    '''returns None\n\n
    configureConnection(final Connection conn, final CMPropertiesImpl props)\n
    '''
def configurePooledConnection():
    '''returns None\n\n
    configurePooledConnection(final PooledConnection conn, final CMProperties props)\n
    '''
def configureXAConnection():
    '''returns None\n\n
    configureXAConnection(final XAConnection conn, final CMProperties props)\n
    '''
def getBackendPortabilityLayer():
    '''returns PortabilityLayer\n\n
    getBackendPortabilityLayer()\n
    '''
def resetStatement():
    '''returns None\n\n
    resetStatement(final CachedStatement statement)\n
    '''
