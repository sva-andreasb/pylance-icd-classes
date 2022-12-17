def ():
    '''returns LoggingPreparedStatement\n\n
    (final PreparedStatement ps, final String sql)\n
    '''
def addBatch():
    '''returns None\n\n
    addBatch()\n
    '''
def clearParameters():
    '''returns None\n\n
    clearParameters()\n
    '''
def execute():
    '''returns boolean\n\n
    execute()\n
    '''
def executeQuery():
    '''returns ResultSet\n\n
    executeQuery()\n
    '''
def executeUpdate():
    '''returns int\n\n
    executeUpdate()\n
    '''
def getMetaData():
    '''returns ResultSetMetaData\n\n
    getMetaData()\n
    '''
def getParameterMetaData():
    '''returns ParameterMetaData\n\n
    getParameterMetaData()\n
    '''
def setArray():
    '''returns None\n\n
    setArray(final int parameterIndex, final Array theArray)\n
    '''
def setAsciiStream():
    '''returns None\n\n
    setAsciiStream(final int parameterIndex, final InputStream theInputStream, final int length)\n
    setAsciiStream(final int parameterIndex, final InputStream x, final long length)\n
    setAsciiStream(final int parameterIndex, final InputStream x)\n
    '''
def setBigDecimal():
    '''returns None\n\n
    setBigDecimal(final int parameterIndex, final BigDecimal theBigDecimal)\n
    '''
def setBinaryStream():
    '''returns None\n\n
    setBinaryStream(final int parameterIndex, final InputStream theInputStream, final int length)\n
    setBinaryStream(final int parameterIndex, final InputStream x, final long length)\n
    setBinaryStream(final int parameterIndex, final InputStream x)\n
    '''
def setBlob():
    '''returns None\n\n
    setBlob(final int parameterIndex, final Blob theBlob)\n
    setBlob(final int parameterIndex, final InputStream inputStream, final long length)\n
    setBlob(final int parameterIndex, final InputStream inputStream)\n
    '''
def setBytesForBlob():
    '''returns None\n\n
    setBytesForBlob(final int paramIndex, final byte[] blobContent)\n
    '''
def setBoolean():
    '''returns None\n\n
    setBoolean(final int parameterIndex, final boolean theBoolean)\n
    '''
def setByte():
    '''returns None\n\n
    setByte(final int parameterIndex, final byte theByte)\n
    '''
def setBytes():
    '''returns None\n\n
    setBytes(final int parameterIndex, final byte[] theBytes)\n
    '''
def setCharacterStream():
    '''returns None\n\n
    setCharacterStream(final int parameterIndex, final Reader reader, final int length)\n
    setCharacterStream(final int parameterIndex, final Reader reader, final long length)\n
    setCharacterStream(final int parameterIndex, final Reader reader)\n
    '''
def setClob():
    '''returns None\n\n
    setClob(final int parameterIndex, final Clob theClob)\n
    setClob(final int parameterIndex, final Reader reader, final long length)\n
    setClob(final int parameterIndex, final Reader reader)\n
    '''
def setDate():
    '''returns None\n\n
    setDate(final int parameterIndex, final Date theDate)\n
    setDate(final int parameterIndex, final Date theDate, final Calendar cal)\n
    '''
def setDouble():
    '''returns None\n\n
    setDouble(final int parameterIndex, final double theDouble)\n
    '''
def setFloat():
    '''returns None\n\n
    setFloat(final int parameterIndex, final float theFloat)\n
    '''
def setInt():
    '''returns None\n\n
    setInt(final int parameterIndex, final int theInt)\n
    '''
def setLong():
    '''returns None\n\n
    setLong(final int parameterIndex, final long theLong)\n
    '''
def setNull():
    '''returns None\n\n
    setNull(final int parameterIndex, final int sqlType)\n
    setNull(final int paramIndex, final int sqlType, final String typeName)\n
    '''
def setObject():
    '''returns None\n\n
    setObject(final int parameterIndex, final Object theObject)\n
    setObject(final int parameterIndex, final Object theObject, final int targetSqlType)\n
    setObject(final int parameterIndex, final Object theObject, final int targetSqlType, final int scale)\n
    '''
def setRef():
    '''returns None\n\n
    setRef(final int parameterIndex, final Ref theRef)\n
    '''
def setShort():
    '''returns None\n\n
    setShort(final int parameterIndex, final short theShort)\n
    '''
def setString():
    '''returns None\n\n
    setString(final int parameterIndex, final String theString)\n
    '''
def setTime():
    '''returns None\n\n
    setTime(final int parameterIndex, final Time theTime)\n
    setTime(final int parameterIndex, final Time theTime, final Calendar cal)\n
    '''
def setTimestamp():
    '''returns None\n\n
    setTimestamp(final int parameterIndex, final Timestamp theTimestamp)\n
    setTimestamp(final int parameterIndex, final Timestamp theTimestamp, final Calendar cal)\n
    '''
def setUnicodeStream():
    '''returns None\n\n
    setUnicodeStream(final int parameterIndex, final InputStream theInputStream, final int length)\n
    '''
def setURL():
    '''returns None\n\n
    setURL(final int parameterIndex, final URL theURL)\n
    '''
def setRowId():
    '''returns None\n\n
    setRowId(final int parameterIndex, final RowId x)\n
    '''
def setNString():
    '''returns None\n\n
    setNString(final int parameterIndex, final String value)\n
    '''
def setNCharacterStream():
    '''returns None\n\n
    setNCharacterStream(final int parameterIndex, final Reader value, final long length)\n
    setNCharacterStream(final int parameterIndex, final Reader value)\n
    '''
def setNClob():
    '''returns None\n\n
    setNClob(final int parameterIndex, final NClob value)\n
    setNClob(final int parameterIndex, final Reader reader, final long length)\n
    setNClob(final int parameterIndex, final Reader reader)\n
    '''
def setSQLXML():
    '''returns None\n\n
    setSQLXML(final int parameterIndex, final SQLXML xmlObject)\n
    '''
def executeBatch():
    '''returns int[]\n\n
    executeBatch()\n
    '''
