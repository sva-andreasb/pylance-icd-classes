def getUseBulkCopyForBatchInsert():
'''public boolean getUseBulkCopyForBatchInsert()
'''
pass
def setUseBulkCopyForBatchInsert():
'''public void setUseBulkCopyForBatchInsert(final boolean useBulkCopyForBatchInsert)
'''
pass
def getSendTimeAsDatetime():
'''public final boolean getSendTimeAsDatetime()
'''
pass
def registerColumnEncryptionKeyStoreProviders():
'''public static synchronized void registerColumnEncryptionKeyStoreProviders(final Map<String, SQLServerColumnEncryptionKeyStoreProvider> clientKeyStoreProviders)
'''
pass
def setColumnEncryptionTrustedMasterKeyPaths():
'''public static synchronized void setColumnEncryptionTrustedMasterKeyPaths(final Map<String, List<String>> trustedKeyPaths)
'''
pass
def updateColumnEncryptionTrustedMasterKeyPaths():
'''public static synchronized void updateColumnEncryptionTrustedMasterKeyPaths(final String server, final List<String> trustedKeyPaths)
'''
pass
def removeColumnEncryptionTrustedMasterKeyPaths():
'''public static synchronized void removeColumnEncryptionTrustedMasterKeyPaths(final String server)
'''
pass
def getColumnEncryptionTrustedMasterKeyPaths():
'''public static synchronized Map<String, List<String>> getColumnEncryptionTrustedMasterKeyPaths()
'''
pass
def getClientConnectionId():
'''public UUID getClientConnectionId()
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def createStatement():
'''public Statement createStatement()
public Statement createStatement(final int resultSetType, final int resultSetConcurrency)
public Statement createStatement(final int nType, final int nConcur, final int resultSetHoldability)
public Statement createStatement(final int nType, final int nConcur, final int resultSetHoldability, final SQLServerStatementColumnEncryptionSetting stmtColEncSetting)
'''
pass
def prepareStatement():
'''public PreparedStatement prepareStatement(final String sql)
public PreparedStatement prepareStatement(final String sql, final int resultSetType, final int resultSetConcurrency)
public PreparedStatement prepareStatement(final String sql, final int nType, final int nConcur, final int resultSetHoldability)
public PreparedStatement prepareStatement(final String sql, final int nType, final int nConcur, final int resultSetHoldability, final SQLServerStatementColumnEncryptionSetting stmtColEncSetting)
public PreparedStatement prepareStatement(final String sql, final int flag)
public PreparedStatement prepareStatement(final String sql, final int flag, final SQLServerStatementColumnEncryptionSetting stmtColEncSetting)
public PreparedStatement prepareStatement(final String sql, final int[] columnIndexes)
public PreparedStatement prepareStatement(final String sql, final int[] columnIndexes, final SQLServerStatementColumnEncryptionSetting stmtColEncSetting)
public PreparedStatement prepareStatement(final String sql, final String[] columnNames)
public PreparedStatement prepareStatement(final String sql, final String[] columnNames, final SQLServerStatementColumnEncryptionSetting stmtColEncSetting)
'''
pass
def prepareCall():
'''public CallableStatement prepareCall(final String sql)
public CallableStatement prepareCall(final String sql, final int resultSetType, final int resultSetConcurrency)
public CallableStatement prepareCall(final String sql, final int nType, final int nConcur, final int resultSetHoldability)
public CallableStatement prepareCall(final String sql, final int nType, final int nConcur, final int resultSetHoldability, final SQLServerStatementColumnEncryptionSetting stmtColEncSetiing)
'''
pass
def nativeSQL():
'''public String nativeSQL(final String sql)
'''
pass
def setAutoCommit():
'''public void setAutoCommit(final boolean newAutoCommitMode)
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
public void rollback(final Savepoint s)
'''
pass
def abort():
'''public void abort(final Executor executor)
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
def setTypeMap():
'''public void setTypeMap(final Map<String, Class<?>> map)
'''
pass
def releaseSavepoint():
'''public void releaseSavepoint(final Savepoint savepoint)
'''
pass
def setSavepoint():
'''public Savepoint setSavepoint(final String sName)
public Savepoint setSavepoint()
'''
pass
def getHoldability():
'''public int getHoldability()
'''
pass
def setHoldability():
'''public void setHoldability(final int holdability)
'''
pass
def getNetworkTimeout():
'''public int getNetworkTimeout()
'''
pass
def setNetworkTimeout():
'''public void setNetworkTimeout(final Executor executor, final int timeout)
'''
pass
def getSchema():
'''public String getSchema()
'''
pass
def setSchema():
'''public void setSchema(final String schema)
'''
pass
def setSendTimeAsDatetime():
'''public void setSendTimeAsDatetime(final boolean sendTimeAsDateTimeValue)
'''
pass
def setUseFmtOnly():
'''public void setUseFmtOnly(final boolean useFmtOnly)
'''
pass
def getUseFmtOnly():
'''public final boolean getUseFmtOnly()
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
def isValid():
'''public boolean isValid(final int timeout)
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
def setColumnEncryptionKeyCacheTtl():
'''public static synchronized void setColumnEncryptionKeyCacheTtl(final int columnEncryptionKeyCacheTTL, final TimeUnit unit)
'''
pass
def getDiscardedServerPreparedStatementCount():
'''public int getDiscardedServerPreparedStatementCount()
'''
pass
def closeUnreferencedPreparedStatementHandles():
'''public void closeUnreferencedPreparedStatementHandles()
'''
pass
def getEnablePrepareOnFirstPreparedStatementCall():
'''public boolean getEnablePrepareOnFirstPreparedStatementCall()
'''
pass
def setEnablePrepareOnFirstPreparedStatementCall():
'''public void setEnablePrepareOnFirstPreparedStatementCall(final boolean value)
'''
pass
def getServerPreparedStatementDiscardThreshold():
'''public int getServerPreparedStatementDiscardThreshold()
'''
pass
def setServerPreparedStatementDiscardThreshold():
'''public void setServerPreparedStatementDiscardThreshold(final int value)
'''
pass
def getDisableStatementPooling():
'''public boolean getDisableStatementPooling()
'''
pass
def setDisableStatementPooling():
'''public void setDisableStatementPooling(final boolean value)
'''
pass
def getStatementPoolingCacheSize():
'''public int getStatementPoolingCacheSize()
'''
pass
def getStatementHandleCacheEntryCount():
'''public int getStatementHandleCacheEntryCount()
'''
pass
def isStatementPoolingEnabled():
'''public boolean isStatementPoolingEnabled()
'''
pass
def setStatementPoolingCacheSize():
'''public void setStatementPoolingCacheSize(int value)
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def onEviction():
'''public void onEviction(final CityHash128Key key, final PreparedStatementHandle handle)
'''
pass
