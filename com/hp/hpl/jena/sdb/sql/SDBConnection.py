def SDBConnection():
'''public SDBConnection(final DataSource ds)
public SDBConnection(final String url, final String user, final String password)
public SDBConnection(final Connection jdbcConnection)
public SDBConnection(final Connection jdbcConnection, final String url)
'''
pass
def none():
'''public static SDBConnection none()
'''
pass
def hasSQLConnection():
'''public boolean hasSQLConnection()
'''
pass
def getTransactionHandler():
'''public TransactionHandler getTransactionHandler()
'''
pass
def execQuery():
'''public ResultSetJDBC execQuery(final String sqlString)
public ResultSetJDBC execQuery(final String sqlString, final int fetchSize)
'''
pass
def executeInTransaction():
'''public Object executeInTransaction(final Command c)
'''
pass
def executeSQL():
'''public Object executeSQL(final SQLCommand c)
'''
pass
def execUpdate():
'''public int execUpdate(final String sqlString)
'''
pass
def exec():
'''public ResultSetJDBC exec(final String sqlString)
'''
pass
def execSilent():
'''public ResultSetJDBC execSilent(final String sqlString)
'''
pass
def prepareStatement():
'''public PreparedStatement prepareStatement(final String sqlString)
'''
pass
def closePreparedStatement():
'''public void closePreparedStatement(final PreparedStatement ps)
'''
pass
def getTableNames():
'''public List<String> getTableNames()
'''
pass
def getSqlConnection():
'''public Connection getSqlConnection()
'''
pass
def close():
'''public void close()
'''
pass
def toString():
'''public String toString()
'''
pass
def loggingSQLExceptions():
'''public boolean loggingSQLExceptions()
'''
pass
def setLogSQLExceptions():
'''public void setLogSQLExceptions(final boolean thisLogSQLExceptions)
'''
pass
def loggingSQLQueries():
'''public boolean loggingSQLQueries()
'''
pass
def setLogSQLQueries():
'''public void setLogSQLQueries(final boolean thisLogSQLQueries)
'''
pass
def loggingSQLStatements():
'''public boolean loggingSQLStatements()
'''
pass
def setLogSQLStatements():
'''public void setLogSQLStatements(final boolean thisLogSQLStatements)
'''
pass
def getLabel():
'''public String getLabel()
'''
pass
def setLabel():
'''public void setLabel(final String label)
'''
pass
def getJdbcURL():
'''public String getJdbcURL()
'''
pass
def setJdbcURL():
'''public void setJdbcURL(final String jdbcURL)
'''
pass
