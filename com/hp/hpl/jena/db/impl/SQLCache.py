def SQLCache():
    '''public SQLCache(final String sqlFile, final Properties defaultOps, final IDBConnection connection, final String idType)
    '''
def setCachePreparedStatements():
    '''public void setCachePreparedStatements(final boolean state)
    '''
def getCachePreparedStatements():
    '''public boolean getCachePreparedStatements()
    '''
def flushPreparedStatementCache():
    '''public void flushPreparedStatementCache()
    '''
def getConnection():
    '''public Connection getConnection()
    '''
def setConnection():
    '''public void setConnection(final IDBConnection connection)
    '''
def getSQLStatement():
    '''public String getSQLStatement(final String opname)
    public String getSQLStatement(final String opname, final String[] attr)
    public String getSQLStatement(final String opname, final String attr)
    public String getSQLStatement(final String opname, final String attrA, final String attrB)
    '''
def getSQLStatementGroup():
    '''public Collection<String> getSQLStatementGroup(final String opname)
    '''
def getPreparedSQLStatement():
    '''public synchronized PreparedStatement getPreparedSQLStatement(final String opname, final String[] attr)
    public synchronized PreparedStatement getPreparedSQLStatement(final String opname)
    public synchronized PreparedStatement getPreparedSQLStatement(final String opname, final String attr)
    public synchronized PreparedStatement getPreparedSQLStatement(final String opname, final String attrA, final String attrB)
    '''
def prepareSQLStatement():
    '''public synchronized PreparedStatement prepareSQLStatement(final String sql)
    '''
def returnPreparedSQLStatement():
    '''public synchronized void returnPreparedSQLStatement(final PreparedStatement ps)
    '''
def runSQLUpdate():
    '''public int runSQLUpdate(final String opname, final Object[] args)
    public int runSQLUpdate(final String opname, final String attrA, final Object[] args)
    public int runSQLUpdate(final String opname, final String attrA, final String attrB, final Object[] args)
    '''
def runSQLGroup():
    '''public void runSQLGroup(final String opname, final String[] attr)
    public void runSQLGroup(final String opname)
    public void runSQLGroup(final String opname, final String attr)
    public void runSQLGroup(final String opname, final String attrA, final String attrB)
    '''
def close():
    '''public void close()
    '''
def loadSQLFile():
    '''public static Properties loadSQLFile(final String sqlFile, final Properties defaultOps, final String idType)
    '''
def concatOpName():
    '''public static String concatOpName(final String opName, final String attr)
    public static String concatOpName(final String opName, final String attrA, final String attrB)
    '''
def substitute():
    '''public static String substitute(final String line, final String macro, final String subs)
    '''
def openResourceFile():
    '''public static BufferedReader openResourceFile(final String filename)
    '''
