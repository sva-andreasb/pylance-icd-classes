def getUseBulkCopyForBatchInsert():
    '''public boolean getUseBulkCopyForBatchInsert()
    '''
def setUseBulkCopyForBatchInsert():
    '''public void setUseBulkCopyForBatchInsert(final boolean useBulkCopyForBatchInsert)
    '''
def getSendTimeAsDatetime():
    '''public final boolean getSendTimeAsDatetime()
    '''
def registerColumnEncryptionKeyStoreProviders():
    '''public static synchronized void registerColumnEncryptionKeyStoreProviders(final Map<String, SQLServerColumnEncryptionKeyStoreProvider> clientKeyStoreProviders)
    '''
def setColumnEncryptionTrustedMasterKeyPaths():
    '''public static synchronized void setColumnEncryptionTrustedMasterKeyPaths(final Map<String, List<String>> trustedKeyPaths)
    '''
def updateColumnEncryptionTrustedMasterKeyPaths():
    '''public static synchronized void updateColumnEncryptionTrustedMasterKeyPaths(final String server, final List<String> trustedKeyPaths)
    '''
def removeColumnEncryptionTrustedMasterKeyPaths():
    '''public static synchronized void removeColumnEncryptionTrustedMasterKeyPaths(final String server)
    '''
def getColumnEncryptionTrustedMasterKeyPaths():
    '''public static synchronized Map<String, List<String>> getColumnEncryptionTrustedMasterKeyPaths()
    '''
def getClientConnectionId():
    '''public UUID getClientConnectionId()
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def createStatement():
    '''public Statement createStatement()
    public Statement createStatement(final int resultSetType, final int resultSetConcurrency)
    public Statement createStatement(final int nType, final int nConcur, final int resultSetHoldability)
    public Statement createStatement(final int nType, final int nConcur, final int resultSetHoldability, final SQLServerStatementColumnEncryptionSetting stmtColEncSetting)
    '''
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
def prepareCall():
    '''public CallableStatement prepareCall(final String sql)
    public CallableStatement prepareCall(final String sql, final int resultSetType, final int resultSetConcurrency)
    public CallableStatement prepareCall(final String sql, final int nType, final int nConcur, final int resultSetHoldability)
    public CallableStatement prepareCall(final String sql, final int nType, final int nConcur, final int resultSetHoldability, final SQLServerStatementColumnEncryptionSetting stmtColEncSetiing)
    '''
def nativeSQL():
    '''public String nativeSQL(final String sql)
    '''
def setAutoCommit():
    '''public void setAutoCommit(final boolean newAutoCommitMode)
    '''
def getAutoCommit():
    '''public boolean getAutoCommit()
    '''
def commit():
    '''public void commit()
    '''
def rollback():
    '''public void rollback()
    public void rollback(final Savepoint s)
    '''
def abort():
    '''public void abort(final Executor executor)
    '''
def close():
    '''public void close()
    '''
def isClosed():
    '''public boolean isClosed()
    '''
def getMetaData():
    '''public DatabaseMetaData getMetaData()
    '''
def setReadOnly():
    '''public void setReadOnly(final boolean readOnly)
    '''
def isReadOnly():
    '''public boolean isReadOnly()
    '''
def setCatalog():
    '''public void setCatalog(final String catalog)
    '''
def getCatalog():
    '''public String getCatalog()
    '''
def setTransactionIsolation():
    '''public void setTransactionIsolation(final int level)
    '''
def getTransactionIsolation():
    '''public int getTransactionIsolation()
    '''
def getWarnings():
    '''public SQLWarning getWarnings()
    '''
def clearWarnings():
    '''public void clearWarnings()
    '''
def setTypeMap():
    '''public void setTypeMap(final Map<String, Class<?>> map)
    '''
def releaseSavepoint():
    '''public void releaseSavepoint(final Savepoint savepoint)
    '''
def setSavepoint():
    '''public Savepoint setSavepoint(final String sName)
    public Savepoint setSavepoint()
    '''
def getHoldability():
    '''public int getHoldability()
    '''
def setHoldability():
    '''public void setHoldability(final int holdability)
    '''
def getNetworkTimeout():
    '''public int getNetworkTimeout()
    '''
def setNetworkTimeout():
    '''public void setNetworkTimeout(final Executor executor, final int timeout)
    '''
def getSchema():
    '''public String getSchema()
    '''
def setSchema():
    '''public void setSchema(final String schema)
    '''
def setSendTimeAsDatetime():
    '''public void setSendTimeAsDatetime(final boolean sendTimeAsDateTimeValue)
    '''
def setUseFmtOnly():
    '''public void setUseFmtOnly(final boolean useFmtOnly)
    '''
def getUseFmtOnly():
    '''public final boolean getUseFmtOnly()
    '''
def createArrayOf():
    '''public Array createArrayOf(final String typeName, final Object[] elements)
    '''
def createBlob():
    '''public Blob createBlob()
    '''
def createClob():
    '''public Clob createClob()
    '''
def createNClob():
    '''public NClob createNClob()
    '''
def createSQLXML():
    '''public SQLXML createSQLXML()
    '''
def createStruct():
    '''public Struct createStruct(final String typeName, final Object[] attributes)
    '''
def getClientInfo():
    '''public Properties getClientInfo()
    public String getClientInfo(final String name)
    '''
def setClientInfo():
    '''public void setClientInfo(final Properties properties)
    public void setClientInfo(final String name, final String value)
    '''
def isValid():
    '''public boolean isValid(final int timeout)
    '''
def isWrapperFor():
    '''public boolean isWrapperFor(final Class<?> iface)
    '''
def unwrap():
    '''public <T> T unwrap(final Class<T> iface)
    '''
def setColumnEncryptionKeyCacheTtl():
    '''public static synchronized void setColumnEncryptionKeyCacheTtl(final int columnEncryptionKeyCacheTTL, final TimeUnit unit)
    '''
def getDiscardedServerPreparedStatementCount():
    '''public int getDiscardedServerPreparedStatementCount()
    '''
def closeUnreferencedPreparedStatementHandles():
    '''public void closeUnreferencedPreparedStatementHandles()
    '''
def getEnablePrepareOnFirstPreparedStatementCall():
    '''public boolean getEnablePrepareOnFirstPreparedStatementCall()
    '''
def setEnablePrepareOnFirstPreparedStatementCall():
    '''public void setEnablePrepareOnFirstPreparedStatementCall(final boolean value)
    '''
def getServerPreparedStatementDiscardThreshold():
    '''public int getServerPreparedStatementDiscardThreshold()
    '''
def setServerPreparedStatementDiscardThreshold():
    '''public void setServerPreparedStatementDiscardThreshold(final int value)
    '''
def getDisableStatementPooling():
    '''public boolean getDisableStatementPooling()
    '''
def setDisableStatementPooling():
    '''public void setDisableStatementPooling(final boolean value)
    '''
def getStatementPoolingCacheSize():
    '''public int getStatementPoolingCacheSize()
    '''
def getStatementHandleCacheEntryCount():
    '''public int getStatementHandleCacheEntryCount()
    '''
def isStatementPoolingEnabled():
    '''public boolean isStatementPoolingEnabled()
    '''
def setStatementPoolingCacheSize():
    '''public void setStatementPoolingCacheSize(int value)
    '''
def equals():
    '''public boolean equals(final Object obj)
    '''
def hashCode():
    '''public int hashCode()
    '''
def onEviction():
    '''public void onEviction(final CityHash128Key key, final PreparedStatementHandle handle)
    '''
