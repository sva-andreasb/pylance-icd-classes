SOURCE_RUNTIME = "int  0"
SOURCE_GENERATOR = "int  1"
def ():
    '''returns JdbcData\n\n
    (final Connection connection_, final Hook hook_, final Map<Object, Object> sqlOverrides_, final Integer queryTimeout_, final Integer maxRows_, final DatabaseMetaData dbMetaData_)\n
    '''
def getConnection():
    '''returns Connection\n\n
    getConnection()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def setConnection():
    '''returns None\n\n
    setConnection(final Connection connection_)\n
    '''
def commit():
    '''returns None\n\n
    commit()\n
    '''
def getAutoCommit():
    '''returns boolean\n\n
    getAutoCommit()\n
    '''
def rollback():
    '''returns None\n\n
    rollback()\n
    '''
def setAutoCommit():
    '''returns None\n\n
    setAutoCommit(final boolean b)\n
    '''
def endBatch():
    '''returns int[][]\n\n
    endBatch()\n
    '''
def getBatchKind():
    '''returns HeterogeneousBatchKind\n\n
    getBatchKind()\n
    '''
def startBatch():
    '''returns None\n\n
    startBatch(final HeterogeneousBatchKind heterogeneousBatchKind)\n
    '''
def cancelBatch():
    '''returns None\n\n
    cancelBatch()\n
    '''
def applySQLSettingsToStatement():
    '''returns None\n\n
    applySQLSettingsToStatement(final Statement statement)\n
    '''
