def close():
    '''    public void close()
    '''
def execute():
    '''    public boolean execute(final String sql)
    public boolean execute(final String sql, final int[] colinds)
    public boolean execute(final String sql, final String[] colnames)
    public boolean execute(final String sql, final int autokeys)
    '''
def executeQuery():
    '''    public ResultSet executeQuery(final String sql, final boolean closeStmt)
    public ResultSet executeQuery(final String sql)
    '''
def executeUpdate():
    '''    public int executeUpdate(final String sql)
    public int executeUpdate(final String sql, final int autoKeys)
    public int executeUpdate(final String sql, final int[] colinds)
    public int executeUpdate(final String sql, final String[] cols)
    '''
def getResultSet():
    '''    public ResultSet getResultSet()
    '''
def getUpdateCount():
    '''    public int getUpdateCount()
    '''
def addBatch():
    '''    public void addBatch(final String sql)
    '''
def clearBatch():
    '''    public void clearBatch()
    '''
def executeBatch():
    '''    public int[] executeBatch()
    '''
def setCursorName():
    '''    public void setCursorName(final String name)
    '''
def getWarnings():
    '''    public SQLWarning getWarnings()
    '''
def clearWarnings():
    '''    public void clearWarnings()
    '''
def getConnection():
    '''    public Connection getConnection()
    '''
def cancel():
    '''    public void cancel()
    '''
def getQueryTimeout():
    '''    public int getQueryTimeout()
    '''
def setQueryTimeout():
    '''    public void setQueryTimeout(final int seconds)
    '''
def getMaxRows():
    '''    public int getMaxRows()
    '''
def setMaxRows():
    '''    public void setMaxRows(final int max)
    '''
def getMaxFieldSize():
    '''    public int getMaxFieldSize()
    '''
def setMaxFieldSize():
    '''    public void setMaxFieldSize(final int max)
    '''
def getFetchSize():
    '''    public int getFetchSize()
    '''
def setFetchSize():
    '''    public void setFetchSize(final int r)
    '''
def getFetchDirection():
    '''    public int getFetchDirection()
    '''
def setFetchDirection():
    '''    public void setFetchDirection(final int d)
    '''
def getGeneratedKeys():
    '''    public ResultSet getGeneratedKeys()
    '''
def getMoreResults():
    '''    public boolean getMoreResults()
    public boolean getMoreResults(final int c)
    '''
def getResultSetConcurrency():
    '''    public int getResultSetConcurrency()
    '''
def getResultSetHoldability():
    '''    public int getResultSetHoldability()
    '''
def getResultSetType():
    '''    public int getResultSetType()
    '''
def setEscapeProcessing():
    '''    public void setEscapeProcessing(final boolean enable)
    '''
def progress():
    '''    public void progress(final int remaining, final int pageCount)
    '''
