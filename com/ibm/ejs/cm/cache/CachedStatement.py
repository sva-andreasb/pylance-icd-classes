def setAsciiStream():
    '''returns None\n\n
    setAsciiStream(final int parameterIndex, final InputStream x)\n
    setAsciiStream(final int parameterIndex, final InputStream x, final long length)\n
    setAsciiStream(final int parameterIndex, final InputStream x, final int length)\n
    '''
def setBinaryStream():
    '''returns None\n\n
    setBinaryStream(final int parameterIndex, final InputStream x)\n
    setBinaryStream(final int parameterIndex, final InputStream x, final long length)\n
    setBinaryStream(final int parameterIndex, final InputStream x, final int length)\n
    '''
def setBlob():
    '''returns None\n\n
    setBlob(final int parameterIndex, final InputStream inputStream)\n
    setBlob(final int parameterIndex, final InputStream inputStream, final long length)\n
    setBlob(final int i, final Blob x)\n
    '''
def setCharacterStream():
    '''returns None\n\n
    setCharacterStream(final int parameterIndex, final Reader reader)\n
    setCharacterStream(final int parameterIndex, final Reader reader, final long length)\n
    setCharacterStream(final int parameterIndex, final Reader reader, final int length)\n
    '''
def setClob():
    '''returns None\n\n
    setClob(final int parameterIndex, final Reader reader)\n
    setClob(final int parameterIndex, final Reader reader, final long length)\n
    setClob(final int i, final Clob x)\n
    '''
def setNCharacterStream():
    '''returns None\n\n
    setNCharacterStream(final int parameterIndex, final Reader value)\n
    setNCharacterStream(final int parameterIndex, final Reader value, final long length)\n
    '''
def setNClob():
    '''returns None\n\n
    setNClob(final int parameterIndex, final NClob value)\n
    setNClob(final int parameterIndex, final Reader reader)\n
    setNClob(final int parameterIndex, final Reader reader, final long length)\n
    '''
def setNString():
    '''returns None\n\n
    setNString(final int parameterIndex, final String value)\n
    '''
def setRowId():
    '''returns None\n\n
    setRowId(final int parameterIndex, final RowId x)\n
    '''
def setSQLXML():
    '''returns None\n\n
    setSQLXML(final int parameterIndex, final SQLXML xmlObject)\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
def isPoolable():
    '''returns boolean\n\n
    isPoolable()\n
    '''
def setPoolable():
    '''returns None\n\n
    setPoolable(final boolean poolable)\n
    '''
def isWrapperFor():
    '''returns boolean\n\n
    isWrapperFor(final Class<?> iface)\n
    '''
def setURL():
    '''returns None\n\n
    setURL(final int i, final URL url)\n
    '''
def getParameterMetaData():
    '''returns ParameterMetaData\n\n
    getParameterMetaData()\n
    '''
def execute():
    '''returns boolean\n\n
    execute(final String s, final int i)\n
    execute(final String s, final int[] i)\n
    execute(final String s, final String[] ss)\n
    execute(final String sql)\n
    execute()\n
    '''
def executeUpdate():
    '''returns int\n\n
    executeUpdate(final String s, final int i)\n
    executeUpdate(final String s, final int[] i)\n
    executeUpdate(final String s, final String[] ss)\n
    executeUpdate(final String sql)\n
    executeUpdate()\n
    '''
def getGeneratedKeys():
    '''returns ResultSet\n\n
    getGeneratedKeys()\n
    '''
def getMoreResults():
    '''returns boolean\n\n
    getMoreResults(final int i)\n
    getMoreResults()\n
    '''
def getResultSetHoldability():
    '''returns int\n\n
    getResultSetHoldability()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getStatementString():
    '''returns String\n\n
    getStatementString()\n
    '''
def cancel():
    '''returns None\n\n
    cancel()\n
    '''
def clearWarnings():
    '''returns None\n\n
    clearWarnings()\n
    '''
def executeQuery():
    '''returns ResultSet\n\n
    executeQuery(final String sql)\n
    executeQuery()\n
    '''
def getMaxFieldSize():
    '''returns int\n\n
    getMaxFieldSize()\n
    '''
def getMaxRows():
    '''returns int\n\n
    getMaxRows()\n
    '''
def getQueryTimeout():
    '''returns int\n\n
    getQueryTimeout()\n
    '''
def getResultSet():
    '''returns ResultSet\n\n
    getResultSet()\n
    '''
def getUpdateCount():
    '''returns int\n\n
    getUpdateCount()\n
    '''
def getWarnings():
    '''returns SQLWarning\n\n
    getWarnings()\n
    '''
def setCursorName():
    '''returns None\n\n
    setCursorName(final String name)\n
    '''
def setEscapeProcessing():
    '''returns None\n\n
    setEscapeProcessing(final boolean enable)\n
    '''
def setMaxFieldSize():
    '''returns None\n\n
    setMaxFieldSize(final int max)\n
    '''
def setMaxRows():
    '''returns None\n\n
    setMaxRows(final int max)\n
    '''
def setQueryTimeout():
    '''returns None\n\n
    setQueryTimeout(final int timeout)\n
    '''
def addBatch():
    '''returns None\n\n
    addBatch()\n
    '''
def setRef():
    '''returns None\n\n
    setRef(final int i, final Ref x)\n
    '''
def setArray():
    '''returns None\n\n
    setArray(final int i, final Array x)\n
    '''
def getMetaData():
    '''returns ResultSetMetaData\n\n
    getMetaData()\n
    '''
def setDate():
    '''returns None\n\n
    setDate(final int parameterIndex, final Date x, final Calendar cal)\n
    setDate(final int parameterIndex, final Date x)\n
    '''
def setTime():
    '''returns None\n\n
    setTime(final int parameterIndex, final Time x, final Calendar cal)\n
    setTime(final int parameterIndex, final Time x)\n
    '''
def setTimestamp():
    '''returns None\n\n
    setTimestamp(final int parameterIndex, final Timestamp x, final Calendar cal)\n
    setTimestamp(final int parameterIndex, final Timestamp x)\n
    '''
def setNull():
    '''returns None\n\n
    setNull(final int paramIndex, final int sqlType, final String typeName)\n
    setNull(final int parameterIndex, final int sqlType)\n
    '''
def setBoolean():
    '''returns None\n\n
    setBoolean(final int parameterIndex, final boolean x)\n
    '''
def setByte():
    '''returns None\n\n
    setByte(final int parameterIndex, final byte x)\n
    '''
def setShort():
    '''returns None\n\n
    setShort(final int parameterIndex, final short x)\n
    '''
def setInt():
    '''returns None\n\n
    setInt(final int parameterIndex, final int x)\n
    '''
def setLong():
    '''returns None\n\n
    setLong(final int parameterIndex, final long x)\n
    '''
def setFloat():
    '''returns None\n\n
    setFloat(final int parameterIndex, final float x)\n
    '''
def setDouble():
    '''returns None\n\n
    setDouble(final int parameterIndex, final double x)\n
    '''
def setBigDecimal():
    '''returns None\n\n
    setBigDecimal(final int parameterIndex, final BigDecimal x)\n
    '''
def setString():
    '''returns None\n\n
    setString(final int parameterIndex, final String x)\n
    '''
def setBytes():
    '''returns None\n\n
    setBytes(final int parameterIndex, final byte[] x)\n
    '''
def setUnicodeStream():
    '''returns None\n\n
    setUnicodeStream(final int parameterIndex, final InputStream x, final int length)\n
    '''
def clearParameters():
    '''returns None\n\n
    clearParameters()\n
    '''
def setObject():
    '''returns None\n\n
    setObject(final int parameterIndex, final Object x, final int targetSqlType, final int scale)\n
    setObject(final int parameterIndex, final Object x, final int targetSqlType)\n
    setObject(final int parameterIndex, final Object x)\n
    '''
def getPreparedStatement():
    '''returns PreparedStatement\n\n
    getPreparedStatement()\n
    '''
