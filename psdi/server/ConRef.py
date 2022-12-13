def copyConRef():
'''public ConRef copyConRef(final Connection refCon)
'''
pass
def isValid():
'''public boolean isValid()
public boolean isValid(final int timeout)
'''
pass
def checkConnection():
'''public boolean checkConnection()
'''
pass
def createStatement():
'''public Statement createStatement()
public Statement createStatement(final int resultSetType, final int resultSetConcurrency)
public Statement createStatement(final int resultSetType, final int resultSetConcurrency, final int resultSetHoldability)
'''
pass
def prepareStatement():
'''public PreparedStatement prepareStatement(final String sql)
public PreparedStatement prepareStatement(final String sql, final int resultSetType, final int resultSetConcurrency)
public PreparedStatement prepareStatement(final String sql, final int resultSetType, final int resultSetConcurrency, final int resultSetHoldability)
public PreparedStatement prepareStatement(final String sql, final int autoGeneratedKeys)
public PreparedStatement prepareStatement(final String sql, final int[] columnIndexes)
public PreparedStatement prepareStatement(final String sql, final String[] columnNames)
'''
pass
def prepareCall():
'''public CallableStatement prepareCall(final String sql)
public CallableStatement prepareCall(final String sql, final int resultSetType, final int resultSetConcurrency)
public CallableStatement prepareCall(final String sql, final int resultSetType, final int resultSetConcurrency, final int resultSetHoldability)
'''
pass
def nativeSQL():
'''public String nativeSQL(final String sql)
'''
pass
def setAutoCommit():
'''public void setAutoCommit(final boolean autoCommit)
'''
pass
def getAutoCommit():
'''public boolean getAutoCommit()
'''
pass
def commit():
'''public void commit()
'''
pass
def rollback():
'''public void rollback()
public void rollback(final Savepoint savepoint)
'''
pass
def close():
'''public void close()
'''
pass
def isClosed():
'''public boolean isClosed()
'''
pass
def getMetaData():
'''public DatabaseMetaData getMetaData()
'''
pass
def setReadOnly():
'''public void setReadOnly(final boolean readOnly)
'''
pass
def isReadOnly():
'''public boolean isReadOnly()
'''
pass
def setCatalog():
'''public void setCatalog(final String catalog)
'''
pass
def getCatalog():
'''public String getCatalog()
'''
pass
def setTransactionIsolation():
'''public void setTransactionIsolation(final int level)
'''
pass
def getTransactionIsolation():
'''public int getTransactionIsolation()
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
def getTypeMap():
'''public Map getTypeMap()
'''
pass
def setTypeMap():
'''public void setTypeMap(final Map map)
'''
pass
def setHoldability():
'''public void setHoldability(final int holdability)
'''
pass
def getHoldability():
'''public int getHoldability()
'''
pass
def setSavepoint():
'''public Savepoint setSavepoint()
public Savepoint setSavepoint(final String name)
'''
pass
def releaseSavepoint():
'''public void releaseSavepoint(final Savepoint savepoint)
'''
pass
def setConnectionPool():
'''public void setConnectionPool(final OracleOCIConnectionPool p)
'''
pass
def getConnectionPool():
'''public OracleOCIConnectionPool getConnectionPool()
'''
pass
def getSPID():
'''public String getSPID()
'''
pass
def copySPID():
'''public void copySPID(final ConRef old)
'''
pass
def createArrayOf():
'''public Array createArrayOf(final String typeName, final Object[] elements)
'''
pass
def createBlob():
'''public Blob createBlob()
'''
pass
def createClob():
'''public Clob createClob()
'''
pass
def createNClob():
'''public NClob createNClob()
'''
pass
def createSQLXML():
'''public SQLXML createSQLXML()
'''
pass
def createStruct():
'''public Struct createStruct(final String typeName, final Object[] attributes)
'''
pass
def getClientInfo():
'''public Properties getClientInfo()
public String getClientInfo(final String name)
'''
pass
def setClientInfo():
'''public void setClientInfo(final Properties properties)
public void setClientInfo(final String name, final String value)
'''
pass
def isWrapperFor():
'''public boolean isWrapperFor(final Class<?> iface)
'''
pass
def unwrap():
'''public <T> T unwrap(final Class<T> iface)
'''
pass
def setNetworkTimeout():
'''public void setNetworkTimeout(final Executor executor, final int milliseconds)
'''
pass
def getNetworkTimeout():
'''public int getNetworkTimeout()
'''
pass
def setSchema():
'''public void setSchema(final String schema)
'''
pass
def getSchema():
'''public String getSchema()
'''
pass
def abort():
'''public void abort(final Executor executor)
'''
pass
def print():
'''public void print()
'''
pass