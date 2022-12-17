def ():
    '''returns SQLiteConnection\n\n
    (final DB db)\n
    (final String url, final String fileName)\n
    (final String url, final String fileName, final Properties prop)\n
    '''
def getConnectionConfig():
    '''returns SQLiteConnectionConfig\n\n
    getConnectionConfig()\n
    '''
def getSQLiteDatabaseMetaData():
    '''returns CoreDatabaseMetaData\n\n
    getSQLiteDatabaseMetaData()\n
    '''
def getMetaData():
    '''returns DatabaseMetaData\n\n
    getMetaData()\n
    '''
def getUrl():
    '''returns String\n\n
    getUrl()\n
    '''
def setSchema():
    '''returns None\n\n
    setSchema(final String schema)\n
    '''
def getSchema():
    '''returns String\n\n
    getSchema()\n
    '''
def abort():
    '''returns None\n\n
    abort(final Executor executor)\n
    '''
def setNetworkTimeout():
    '''returns None\n\n
    setNetworkTimeout(final Executor executor, final int milliseconds)\n
    '''
def getNetworkTimeout():
    '''returns int\n\n
    getNetworkTimeout()\n
    '''
def getTransactionIsolation():
    '''returns int\n\n
    getTransactionIsolation()\n
    '''
def setTransactionIsolation():
    '''returns None\n\n
    setTransactionIsolation(final int level)\n
    '''
def getDatabase():
    '''returns DB\n\n
    getDatabase()\n
    '''
def getAutoCommit():
    '''returns boolean\n\n
    getAutoCommit()\n
    '''
def setAutoCommit():
    '''returns None\n\n
    setAutoCommit(final boolean ac)\n
    '''
def getBusyTimeout():
    '''returns int\n\n
    getBusyTimeout()\n
    '''
def setBusyTimeout():
    '''returns None\n\n
    setBusyTimeout(final int timeoutMillis)\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def libversion():
    '''returns String\n\n
    libversion()\n
    '''
def commit():
    '''returns None\n\n
    commit()\n
    '''
def rollback():
    '''returns None\n\n
    rollback()\n
    '''
