def getUseBulkCopyForBatchInsert():
    '''returns boolean\n\n
    getUseBulkCopyForBatchInsert()\n
    '''
def setUseBulkCopyForBatchInsert():
    '''returns None\n\n
    setUseBulkCopyForBatchInsert(final boolean useBulkCopyForBatchInsert)\n
    '''
def getClientConnectionId():
    '''returns UUID\n\n
    getClientConnectionId()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def createStatement():
    '''returns Statement\n\n
    createStatement()\n
    createStatement(final int resultSetType, final int resultSetConcurrency)\n
    createStatement(final int nType, final int nConcur, final int resultSetHoldability)\n
    createStatement(final int nType, final int nConcur, final int resultSetHoldability, final SQLServerStatementColumnEncryptionSetting stmtColEncSetting)\n
    '''
def prepareStatement():
    '''returns PreparedStatement\n\n
    prepareStatement(final String sql)\n
    prepareStatement(final String sql, final int resultSetType, final int resultSetConcurrency)\n
    prepareStatement(final String sql, final int nType, final int nConcur, final int resultSetHoldability)\n
    prepareStatement(final String sql, final int nType, final int nConcur, final int resultSetHoldability, final SQLServerStatementColumnEncryptionSetting stmtColEncSetting)\n
    prepareStatement(final String sql, final int flag)\n
    prepareStatement(final String sql, final int flag, final SQLServerStatementColumnEncryptionSetting stmtColEncSetting)\n
    prepareStatement(final String sql, final int[] columnIndexes)\n
    prepareStatement(final String sql, final int[] columnIndexes, final SQLServerStatementColumnEncryptionSetting stmtColEncSetting)\n
    prepareStatement(final String sql, final String[] columnNames)\n
    prepareStatement(final String sql, final String[] columnNames, final SQLServerStatementColumnEncryptionSetting stmtColEncSetting)\n
    '''
def prepareCall():
    '''returns CallableStatement\n\n
    prepareCall(final String sql)\n
    prepareCall(final String sql, final int resultSetType, final int resultSetConcurrency)\n
    prepareCall(final String sql, final int nType, final int nConcur, final int resultSetHoldability)\n
    prepareCall(final String sql, final int nType, final int nConcur, final int resultSetHoldability, final SQLServerStatementColumnEncryptionSetting stmtColEncSetiing)\n
    '''
def nativeSQL():
    '''returns String\n\n
    nativeSQL(final String sql)\n
    '''
def setAutoCommit():
    '''returns None\n\n
    setAutoCommit(final boolean newAutoCommitMode)\n
    '''
def getAutoCommit():
    '''returns boolean\n\n
    getAutoCommit()\n
    '''
def commit():
    '''returns None\n\n
    commit()\n
    '''
def rollback():
    '''returns None\n\n
    rollback()\n
    rollback(final Savepoint s)\n
    '''
def abort():
    '''returns None\n\n
    abort(final Executor executor)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
def getMetaData():
    '''returns DatabaseMetaData\n\n
    getMetaData()\n
    '''
def setReadOnly():
    '''returns None\n\n
    setReadOnly(final boolean readOnly)\n
    '''
def isReadOnly():
    '''returns boolean\n\n
    isReadOnly()\n
    '''
def setCatalog():
    '''returns None\n\n
    setCatalog(final String catalog)\n
    '''
def getCatalog():
    '''returns String\n\n
    getCatalog()\n
    '''
def setTransactionIsolation():
    '''returns None\n\n
    setTransactionIsolation(final int level)\n
    '''
def getTransactionIsolation():
    '''returns int\n\n
    getTransactionIsolation()\n
    '''
def getWarnings():
    '''returns SQLWarning\n\n
    getWarnings()\n
    '''
def clearWarnings():
    '''returns None\n\n
    clearWarnings()\n
    '''
def setTypeMap():
    '''returns None\n\n
    setTypeMap(final Map<String, Class<?>> map)\n
    '''
def releaseSavepoint():
    '''returns None\n\n
    releaseSavepoint(final Savepoint savepoint)\n
    '''
def setSavepoint():
    '''returns Savepoint\n\n
    setSavepoint(final String sName)\n
    setSavepoint()\n
    '''
def getHoldability():
    '''returns int\n\n
    getHoldability()\n
    '''
def setHoldability():
    '''returns None\n\n
    setHoldability(final int holdability)\n
    '''
def getNetworkTimeout():
    '''returns int\n\n
    getNetworkTimeout()\n
    '''
def setNetworkTimeout():
    '''returns None\n\n
    setNetworkTimeout(final Executor executor, final int timeout)\n
    '''
def getSchema():
    '''returns String\n\n
    getSchema()\n
    '''
def setSchema():
    '''returns None\n\n
    setSchema(final String schema)\n
    '''
def setSendTimeAsDatetime():
    '''returns None\n\n
    setSendTimeAsDatetime(final boolean sendTimeAsDateTimeValue)\n
    '''
def setUseFmtOnly():
    '''returns None\n\n
    setUseFmtOnly(final boolean useFmtOnly)\n
    '''
def createArrayOf():
    '''returns Array\n\n
    createArrayOf(final String typeName, final Object[] elements)\n
    '''
def createBlob():
    '''returns Blob\n\n
    createBlob()\n
    '''
def createClob():
    '''returns Clob\n\n
    createClob()\n
    '''
def createNClob():
    '''returns NClob\n\n
    createNClob()\n
    '''
def createSQLXML():
    '''returns SQLXML\n\n
    createSQLXML()\n
    '''
def createStruct():
    '''returns Struct\n\n
    createStruct(final String typeName, final Object[] attributes)\n
    '''
def getClientInfo():
    '''returns String\n\n
    getClientInfo()\n
    getClientInfo(final String name)\n
    '''
def setClientInfo():
    '''returns None\n\n
    setClientInfo(final Properties properties)\n
    setClientInfo(final String name, final String value)\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid(final int timeout)\n
    '''
def isWrapperFor():
    '''returns boolean\n\n
    isWrapperFor(final Class<?> iface)\n
    '''
def getDiscardedServerPreparedStatementCount():
    '''returns int\n\n
    getDiscardedServerPreparedStatementCount()\n
    '''
def closeUnreferencedPreparedStatementHandles():
    '''returns None\n\n
    closeUnreferencedPreparedStatementHandles()\n
    '''
def getEnablePrepareOnFirstPreparedStatementCall():
    '''returns boolean\n\n
    getEnablePrepareOnFirstPreparedStatementCall()\n
    '''
def setEnablePrepareOnFirstPreparedStatementCall():
    '''returns None\n\n
    setEnablePrepareOnFirstPreparedStatementCall(final boolean value)\n
    '''
def getServerPreparedStatementDiscardThreshold():
    '''returns int\n\n
    getServerPreparedStatementDiscardThreshold()\n
    '''
def setServerPreparedStatementDiscardThreshold():
    '''returns None\n\n
    setServerPreparedStatementDiscardThreshold(final int value)\n
    '''
def getDisableStatementPooling():
    '''returns boolean\n\n
    getDisableStatementPooling()\n
    '''
def setDisableStatementPooling():
    '''returns None\n\n
    setDisableStatementPooling(final boolean value)\n
    '''
def getStatementPoolingCacheSize():
    '''returns int\n\n
    getStatementPoolingCacheSize()\n
    '''
def getStatementHandleCacheEntryCount():
    '''returns int\n\n
    getStatementHandleCacheEntryCount()\n
    '''
def isStatementPoolingEnabled():
    '''returns boolean\n\n
    isStatementPoolingEnabled()\n
    '''
def setStatementPoolingCacheSize():
    '''returns None\n\n
    setStatementPoolingCacheSize(int value)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def onEviction():
    '''returns None\n\n
    onEviction(final CityHash128Key key, final PreparedStatementHandle handle)\n
    '''
