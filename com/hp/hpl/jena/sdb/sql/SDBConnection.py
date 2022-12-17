def ():
    '''returns SDBConnection\n\n
    (final DataSource ds)\n
    (final String url, final String user, final String password)\n
    (final Connection jdbcConnection)\n
    (final Connection jdbcConnection, final String url)\n
    '''
def hasSQLConnection():
    '''returns boolean\n\n
    hasSQLConnection()\n
    '''
def getTransactionHandler():
    '''returns TransactionHandler\n\n
    getTransactionHandler()\n
    '''
def execQuery():
    '''returns ResultSetJDBC\n\n
    execQuery(final String sqlString)\n
    execQuery(final String sqlString, final int fetchSize)\n
    '''
def executeInTransaction():
    '''returns Object\n\n
    executeInTransaction(final Command c)\n
    '''
def executeSQL():
    '''returns Object\n\n
    executeSQL(final SQLCommand c)\n
    '''
def execUpdate():
    '''returns int\n\n
    execUpdate(final String sqlString)\n
    '''
def exec():
    '''returns ResultSetJDBC\n\n
    exec(final String sqlString)\n
    '''
def execSilent():
    '''returns ResultSetJDBC\n\n
    execSilent(final String sqlString)\n
    '''
def prepareStatement():
    '''returns PreparedStatement\n\n
    prepareStatement(final String sqlString)\n
    '''
def closePreparedStatement():
    '''returns None\n\n
    closePreparedStatement(final PreparedStatement ps)\n
    '''
def getTableNames():
    '''returns List<String>\n\n
    getTableNames()\n
    '''
def getSqlConnection():
    '''returns Connection\n\n
    getSqlConnection()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def loggingSQLExceptions():
    '''returns boolean\n\n
    loggingSQLExceptions()\n
    '''
def setLogSQLExceptions():
    '''returns None\n\n
    setLogSQLExceptions(final boolean thisLogSQLExceptions)\n
    '''
def loggingSQLQueries():
    '''returns boolean\n\n
    loggingSQLQueries()\n
    '''
def setLogSQLQueries():
    '''returns None\n\n
    setLogSQLQueries(final boolean thisLogSQLQueries)\n
    '''
def loggingSQLStatements():
    '''returns boolean\n\n
    loggingSQLStatements()\n
    '''
def setLogSQLStatements():
    '''returns None\n\n
    setLogSQLStatements(final boolean thisLogSQLStatements)\n
    '''
def getLabel():
    '''returns String\n\n
    getLabel()\n
    '''
def setLabel():
    '''returns None\n\n
    setLabel(final String label)\n
    '''
def getJdbcURL():
    '''returns String\n\n
    getJdbcURL()\n
    '''
def setJdbcURL():
    '''returns None\n\n
    setJdbcURL(final String jdbcURL)\n
    '''
