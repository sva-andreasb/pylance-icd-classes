def SQLCache():
'''public SQLCache(final String sqlFile, final Properties defaultOps, final IDBConnection connection, final String idType)
'''
pass
def setCachePreparedStatements():
'''public void setCachePreparedStatements(final boolean state)
'''
pass
def getCachePreparedStatements():
'''public boolean getCachePreparedStatements()
'''
pass
def flushPreparedStatementCache():
'''public void flushPreparedStatementCache()
'''
pass
def getConnection():
'''public Connection getConnection()
'''
pass
def setConnection():
'''public void setConnection(final IDBConnection connection)
'''
pass
def getSQLStatement():
'''public String getSQLStatement(final String opname)
public String getSQLStatement(final String opname, final String[] attr)
public String getSQLStatement(final String opname, final String attr)
public String getSQLStatement(final String opname, final String attrA, final String attrB)
'''
pass
def getSQLStatementGroup():
'''public Collection<String> getSQLStatementGroup(final String opname)
'''
pass
def getPreparedSQLStatement():
'''public synchronized PreparedStatement getPreparedSQLStatement(final String opname, final String[] attr)
public synchronized PreparedStatement getPreparedSQLStatement(final String opname)
public synchronized PreparedStatement getPreparedSQLStatement(final String opname, final String attr)
public synchronized PreparedStatement getPreparedSQLStatement(final String opname, final String attrA, final String attrB)
'''
pass
def prepareSQLStatement():
'''public synchronized PreparedStatement prepareSQLStatement(final String sql)
'''
pass
def returnPreparedSQLStatement():
'''public synchronized void returnPreparedSQLStatement(final PreparedStatement ps)
'''
pass
def runSQLUpdate():
'''public int runSQLUpdate(final String opname, final Object[] args)
public int runSQLUpdate(final String opname, final String attrA, final Object[] args)
public int runSQLUpdate(final String opname, final String attrA, final String attrB, final Object[] args)
'''
pass
def runSQLGroup():
'''public void runSQLGroup(final String opname, final String[] attr)
public void runSQLGroup(final String opname)
public void runSQLGroup(final String opname, final String attr)
public void runSQLGroup(final String opname, final String attrA, final String attrB)
'''
pass
def close():
'''public void close()
'''
pass
def loadSQLFile():
'''public static Properties loadSQLFile(final String sqlFile, final Properties defaultOps, final String idType)
'''
pass
def concatOpName():
'''public static String concatOpName(final String opName, final String attr)
public static String concatOpName(final String opName, final String attrA, final String attrB)
'''
pass
def substitute():
'''public static String substitute(final String line, final String macro, final String subs)
'''
pass
def openResourceFile():
'''public static BufferedReader openResourceFile(final String filename)
'''
pass
