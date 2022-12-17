def close():
    '''returns None\n\n
    close()\n
    '''
def execute():
    '''returns boolean\n\n
    execute(final String sql)\n
    execute(final String sql, final int[] colinds)\n
    execute(final String sql, final String[] colnames)\n
    execute(final String sql, final int autokeys)\n
    '''
def executeQuery():
    '''returns ResultSet\n\n
    executeQuery(final String sql, final boolean closeStmt)\n
    executeQuery(final String sql)\n
    '''
def executeUpdate():
    '''returns int\n\n
    executeUpdate(final String sql)\n
    executeUpdate(final String sql, final int autoKeys)\n
    executeUpdate(final String sql, final int[] colinds)\n
    executeUpdate(final String sql, final String[] cols)\n
    '''
def getResultSet():
    '''returns ResultSet\n\n
    getResultSet()\n
    '''
def getUpdateCount():
    '''returns int\n\n
    getUpdateCount()\n
    '''
def addBatch():
    '''returns None\n\n
    addBatch(final String sql)\n
    '''
def clearBatch():
    '''returns None\n\n
    clearBatch()\n
    '''
def executeBatch():
    '''returns int[]\n\n
    executeBatch()\n
    '''
def setCursorName():
    '''returns None\n\n
    setCursorName(final String name)\n
    '''
def getWarnings():
    '''returns SQLWarning\n\n
    getWarnings()\n
    '''
def clearWarnings():
    '''returns None\n\n
    clearWarnings()\n
    '''
def getConnection():
    '''returns Connection\n\n
    getConnection()\n
    '''
def cancel():
    '''returns None\n\n
    cancel()\n
    '''
def getQueryTimeout():
    '''returns int\n\n
    getQueryTimeout()\n
    '''
def setQueryTimeout():
    '''returns None\n\n
    setQueryTimeout(final int seconds)\n
    '''
def getMaxRows():
    '''returns int\n\n
    getMaxRows()\n
    '''
def setMaxRows():
    '''returns None\n\n
    setMaxRows(final int max)\n
    '''
def getMaxFieldSize():
    '''returns int\n\n
    getMaxFieldSize()\n
    '''
def setMaxFieldSize():
    '''returns None\n\n
    setMaxFieldSize(final int max)\n
    '''
def getFetchSize():
    '''returns int\n\n
    getFetchSize()\n
    '''
def setFetchSize():
    '''returns None\n\n
    setFetchSize(final int r)\n
    '''
def getFetchDirection():
    '''returns int\n\n
    getFetchDirection()\n
    '''
def setFetchDirection():
    '''returns None\n\n
    setFetchDirection(final int d)\n
    '''
def getGeneratedKeys():
    '''returns ResultSet\n\n
    getGeneratedKeys()\n
    '''
def getMoreResults():
    '''returns boolean\n\n
    getMoreResults()\n
    getMoreResults(final int c)\n
    '''
def getResultSetConcurrency():
    '''returns int\n\n
    getResultSetConcurrency()\n
    '''
def getResultSetHoldability():
    '''returns int\n\n
    getResultSetHoldability()\n
    '''
def getResultSetType():
    '''returns int\n\n
    getResultSetType()\n
    '''
def setEscapeProcessing():
    '''returns None\n\n
    setEscapeProcessing(final boolean enable)\n
    '''
def progress():
    '''returns None\n\n
    progress(final int remaining, final int pageCount)\n
    '''
