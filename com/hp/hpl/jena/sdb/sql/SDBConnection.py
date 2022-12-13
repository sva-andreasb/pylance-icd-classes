def SDBConnection():
    '''public SDBConnection(final DataSource ds)
    public SDBConnection(final String url, final String user, final String password)
    public SDBConnection(final Connection jdbcConnection)
    public SDBConnection(final Connection jdbcConnection, final String url)
    '''
def none():
    '''public static SDBConnection none()
    '''
def hasSQLConnection():
    '''public boolean hasSQLConnection()
    '''
def getTransactionHandler():
    '''public TransactionHandler getTransactionHandler()
    '''
def execQuery():
    '''public ResultSetJDBC execQuery(final String sqlString)
    public ResultSetJDBC execQuery(final String sqlString, final int fetchSize)
    '''
def executeInTransaction():
    '''public Object executeInTransaction(final Command c)
    '''
def executeSQL():
    '''public Object executeSQL(final SQLCommand c)
    '''
def execUpdate():
    '''public int execUpdate(final String sqlString)
    '''
def exec():
    '''public ResultSetJDBC exec(final String sqlString)
    '''
def execSilent():
    '''public ResultSetJDBC execSilent(final String sqlString)
    '''
def prepareStatement():
    '''public PreparedStatement prepareStatement(final String sqlString)
    '''
def closePreparedStatement():
    '''public void closePreparedStatement(final PreparedStatement ps)
    '''
def getTableNames():
    '''public List<String> getTableNames()
    '''
def getSqlConnection():
    '''public Connection getSqlConnection()
    '''
def close():
    '''public void close()
    '''
def toString():
    '''public String toString()
    '''
def loggingSQLExceptions():
    '''public boolean loggingSQLExceptions()
    '''
def setLogSQLExceptions():
    '''public void setLogSQLExceptions(final boolean thisLogSQLExceptions)
    '''
def loggingSQLQueries():
    '''public boolean loggingSQLQueries()
    '''
def setLogSQLQueries():
    '''public void setLogSQLQueries(final boolean thisLogSQLQueries)
    '''
def loggingSQLStatements():
    '''public boolean loggingSQLStatements()
    '''
def setLogSQLStatements():
    '''public void setLogSQLStatements(final boolean thisLogSQLStatements)
    '''
def getLabel():
    '''public String getLabel()
    '''
def setLabel():
    '''public void setLabel(final String label)
    '''
def getJdbcURL():
    '''public String getJdbcURL()
    '''
def setJdbcURL():
    '''public void setJdbcURL(final String jdbcURL)
    '''
