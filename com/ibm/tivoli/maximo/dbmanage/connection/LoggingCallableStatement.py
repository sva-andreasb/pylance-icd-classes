def ():
    '''returns LoggingCallableStatement\n\n
    (final CallableStatement prepareCall, final String sql)\n
    '''
def getArray():
    '''returns Array\n\n
    getArray(final int parameterIndex)\n
    getArray(final String parameterName)\n
    '''
def getBigDecimal():
    '''returns BigDecimal\n\n
    getBigDecimal(final int parameterIndex)\n
    getBigDecimal(final String parameterName)\n
    getBigDecimal(final int parameterIndex, final int scale)\n
    '''
def getBlob():
    '''returns Blob\n\n
    getBlob(final int parameterIndex)\n
    getBlob(final String parameterName)\n
    '''
def getBoolean():
    '''returns boolean\n\n
    getBoolean(final int parameterIndex)\n
    getBoolean(final String parameterName)\n
    '''
def getByte():
    '''returns byte\n\n
    getByte(final int parameterIndex)\n
    getByte(final String parameterName)\n
    '''
def getBytes():
    '''returns byte[]\n\n
    getBytes(final int parameterIndex)\n
    getBytes(final String parameterName)\n
    '''
def getCharacterStream():
    '''returns Reader\n\n
    getCharacterStream(final int parameterIndex)\n
    getCharacterStream(final String parameterName)\n
    '''
def getClob():
    '''returns Clob\n\n
    getClob(final int parameterIndex)\n
    getClob(final String parameterName)\n
    '''
def getDate():
    '''returns Date\n\n
    getDate(final int parameterIndex)\n
    getDate(final String parameterName)\n
    getDate(final int parameterIndex, final Calendar cal)\n
    getDate(final String parameterName, final Calendar cal)\n
    '''
def getDouble():
    '''returns double\n\n
    getDouble(final int parameterIndex)\n
    getDouble(final String parameterName)\n
    '''
def getFloat():
    '''returns float\n\n
    getFloat(final int parameterIndex)\n
    getFloat(final String parameterName)\n
    '''
def getInt():
    '''returns int\n\n
    getInt(final int parameterIndex)\n
    getInt(final String parameterName)\n
    '''
def getLong():
    '''returns long\n\n
    getLong(final int parameterIndex)\n
    getLong(final String parameterName)\n
    '''
def getNCharacterStream():
    '''returns Reader\n\n
    getNCharacterStream(final int parameterIndex)\n
    getNCharacterStream(final String parameterName)\n
    '''
def getNClob():
    '''returns NClob\n\n
    getNClob(final int parameterIndex)\n
    getNClob(final String parameterName)\n
    '''
def getNString():
    '''returns String\n\n
    getNString(final int parameterIndex)\n
    getNString(final String parameterName)\n
    '''
def getObject():
    '''returns Object\n\n
    getObject(final int parameterIndex)\n
    getObject(final String parameterName)\n
    getObject(final int parameterIndex, final Map<String, Class<?>> map)\n
    getObject(final String parameterName, final Map<String, Class<?>> map)\n
    '''
def getRef():
    '''returns Ref\n\n
    getRef(final int parameterIndex)\n
    getRef(final String parameterName)\n
    '''
def getRowId():
    '''returns RowId\n\n
    getRowId(final int parameterIndex)\n
    getRowId(final String parameterName)\n
    '''
def getSQLXML():
    '''returns SQLXML\n\n
    getSQLXML(final int parameterIndex)\n
    getSQLXML(final String parameterName)\n
    '''
def getShort():
    '''returns short\n\n
    getShort(final int parameterIndex)\n
    getShort(final String parameterName)\n
    '''
def getString():
    '''returns String\n\n
    getString(final int parameterIndex)\n
    getString(final String parameterName)\n
    '''
def getTime():
    '''returns Time\n\n
    getTime(final int parameterIndex)\n
    getTime(final String parameterName)\n
    getTime(final int parameterIndex, final Calendar cal)\n
    getTime(final String parameterName, final Calendar cal)\n
    '''
def getTimestamp():
    '''returns Timestamp\n\n
    getTimestamp(final int parameterIndex)\n
    getTimestamp(final String parameterName)\n
    getTimestamp(final int parameterIndex, final Calendar cal)\n
    getTimestamp(final String parameterName, final Calendar cal)\n
    '''
def getURL():
    '''returns URL\n\n
    getURL(final int parameterIndex)\n
    getURL(final String parameterName)\n
    '''
def registerOutParameter():
    '''returns None\n\n
    registerOutParameter(final int parameterIndex, final int sqlType)\n
    registerOutParameter(final String parameterName, final int sqlType)\n
    registerOutParameter(final int parameterIndex, final int sqlType, final int scale)\n
    registerOutParameter(final int parameterIndex, final int sqlType, final String typeName)\n
    registerOutParameter(final String parameterName, final int sqlType, final int scale)\n
    registerOutParameter(final String parameterName, final int sqlType, final String typeName)\n
    '''
def setAsciiStream():
    '''returns None\n\n
    setAsciiStream(final String parameterName, final InputStream x)\n
    setAsciiStream(final String parameterName, final InputStream x, final int length)\n
    setAsciiStream(final String parameterName, final InputStream x, final long length)\n
    '''
def setBigDecimal():
    '''returns None\n\n
    setBigDecimal(final String parameterName, final BigDecimal x)\n
    '''
def setBinaryStream():
    '''returns None\n\n
    setBinaryStream(final String parameterName, final InputStream x)\n
    setBinaryStream(final String parameterName, final InputStream x, final int length)\n
    setBinaryStream(final String parameterName, final InputStream x, final long length)\n
    '''
def setBlob():
    '''returns None\n\n
    setBlob(final String parameterName, final Blob x)\n
    setBlob(final String parameterName, final InputStream inputStream)\n
    setBlob(final String parameterName, final InputStream inputStream, final long length)\n
    '''
def setBoolean():
    '''returns None\n\n
    setBoolean(final String parameterName, final boolean x)\n
    '''
def setByte():
    '''returns None\n\n
    setByte(final String parameterName, final byte x)\n
    '''
def setBytes():
    '''returns None\n\n
    setBytes(final String parameterName, final byte[] x)\n
    '''
def setCharacterStream():
    '''returns None\n\n
    setCharacterStream(final String parameterName, final Reader reader)\n
    setCharacterStream(final String parameterName, final Reader reader, final int length)\n
    setCharacterStream(final String parameterName, final Reader reader, final long length)\n
    '''
def setClob():
    '''returns None\n\n
    setClob(final String parameterName, final Clob x)\n
    setClob(final String parameterName, final Reader reader)\n
    setClob(final String parameterName, final Reader reader, final long length)\n
    '''
def setDate():
    '''returns None\n\n
    setDate(final String parameterName, final Date x)\n
    setDate(final String parameterName, final Date x, final Calendar cal)\n
    '''
def setDouble():
    '''returns None\n\n
    setDouble(final String parameterName, final double x)\n
    '''
def setFloat():
    '''returns None\n\n
    setFloat(final String parameterName, final float x)\n
    '''
def setInt():
    '''returns None\n\n
    setInt(final String parameterName, final int x)\n
    '''
def setLong():
    '''returns None\n\n
    setLong(final String parameterName, final long x)\n
    '''
def setNCharacterStream():
    '''returns None\n\n
    setNCharacterStream(final String parameterName, final Reader value)\n
    setNCharacterStream(final String parameterName, final Reader value, final long length)\n
    '''
def setNClob():
    '''returns None\n\n
    setNClob(final String parameterName, final NClob value)\n
    setNClob(final String parameterName, final Reader reader)\n
    setNClob(final String parameterName, final Reader reader, final long length)\n
    '''
def setNString():
    '''returns None\n\n
    setNString(final String parameterName, final String value)\n
    '''
def setNull():
    '''returns None\n\n
    setNull(final String parameterName, final int sqlType)\n
    setNull(final String parameterName, final int sqlType, final String typeName)\n
    '''
def setObject():
    '''returns None\n\n
    setObject(final String parameterName, final Object x)\n
    setObject(final String parameterName, final Object x, final int targetSqlType)\n
    setObject(final String parameterName, final Object x, final int targetSqlType, final int scale)\n
    '''
def setRowId():
    '''returns None\n\n
    setRowId(final String parameterName, final RowId x)\n
    '''
def setSQLXML():
    '''returns None\n\n
    setSQLXML(final String parameterName, final SQLXML xmlObject)\n
    '''
def setShort():
    '''returns None\n\n
    setShort(final String parameterName, final short x)\n
    '''
def setString():
    '''returns None\n\n
    setString(final String parameterName, final String x)\n
    '''
def setTime():
    '''returns None\n\n
    setTime(final String parameterName, final Time x)\n
    setTime(final String parameterName, final Time x, final Calendar cal)\n
    '''
def setTimestamp():
    '''returns None\n\n
    setTimestamp(final String parameterName, final Timestamp x)\n
    setTimestamp(final String parameterName, final Timestamp x, final Calendar cal)\n
    '''
def setURL():
    '''returns None\n\n
    setURL(final String parameterName, final URL val)\n
    '''
def wasNull():
    '''returns boolean\n\n
    wasNull()\n
    '''
