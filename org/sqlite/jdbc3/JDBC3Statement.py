def close():
'''public void close()
'''
pass
def execute():
'''public boolean execute(final String sql)
public boolean execute(final String sql, final int[] colinds)
public boolean execute(final String sql, final String[] colnames)
public boolean execute(final String sql, final int autokeys)
'''
pass
def executeQuery():
'''public ResultSet executeQuery(final String sql, final boolean closeStmt)
public ResultSet executeQuery(final String sql)
'''
pass
def executeUpdate():
'''public int executeUpdate(final String sql)
public int executeUpdate(final String sql, final int autoKeys)
public int executeUpdate(final String sql, final int[] colinds)
public int executeUpdate(final String sql, final String[] cols)
'''
pass
def getResultSet():
'''public ResultSet getResultSet()
'''
pass
def getUpdateCount():
'''public int getUpdateCount()
'''
pass
def addBatch():
'''public void addBatch(final String sql)
'''
pass
def clearBatch():
'''public void clearBatch()
'''
pass
def executeBatch():
'''public int[] executeBatch()
'''
pass
def setCursorName():
'''public void setCursorName(final String name)
'''
pass
def getWarnings():
'''public SQLWarning getWarnings()
'''
pass
def clearWarnings():
'''public void clearWarnings()
'''
pass
def getConnection():
'''public Connection getConnection()
'''
pass
def cancel():
'''public void cancel()
'''
pass
def getQueryTimeout():
'''public int getQueryTimeout()
'''
pass
def setQueryTimeout():
'''public void setQueryTimeout(final int seconds)
'''
pass
def getMaxRows():
'''public int getMaxRows()
'''
pass
def setMaxRows():
'''public void setMaxRows(final int max)
'''
pass
def getMaxFieldSize():
'''public int getMaxFieldSize()
'''
pass
def setMaxFieldSize():
'''public void setMaxFieldSize(final int max)
'''
pass
def getFetchSize():
'''public int getFetchSize()
'''
pass
def setFetchSize():
'''public void setFetchSize(final int r)
'''
pass
def getFetchDirection():
'''public int getFetchDirection()
'''
pass
def setFetchDirection():
'''public void setFetchDirection(final int d)
'''
pass
def getGeneratedKeys():
'''public ResultSet getGeneratedKeys()
'''
pass
def getMoreResults():
'''public boolean getMoreResults()
public boolean getMoreResults(final int c)
'''
pass
def getResultSetConcurrency():
'''public int getResultSetConcurrency()
'''
pass
def getResultSetHoldability():
'''public int getResultSetHoldability()
'''
pass
def getResultSetType():
'''public int getResultSetType()
'''
pass
def setEscapeProcessing():
'''public void setEscapeProcessing(final boolean enable)
'''
pass
def progress():
'''public void progress(final int remaining, final int pageCount)
'''
pass
