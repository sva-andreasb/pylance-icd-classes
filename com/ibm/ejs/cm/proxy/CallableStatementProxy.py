def getCharacterStream():
    '''returns Reader\n\n
    getCharacterStream(final int parameterIndex)\n
    getCharacterStream(final String parameterName)\n
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
def setAsciiStream():
    '''returns None\n\n
    setAsciiStream(final String parameterName, final InputStream x)\n
    setAsciiStream(final String parameterName, final InputStream x, final long length)\n
    setAsciiStream(final String s, final InputStream is, final int i)\n
    '''
def setBinaryStream():
    '''returns None\n\n
    setBinaryStream(final String parameterName, final InputStream x)\n
    setBinaryStream(final String parameterName, final InputStream x, final long length)\n
    setBinaryStream(final String s, final InputStream is, final int i)\n
    '''
def setBlob():
    '''returns None\n\n
    setBlob(final String parameterName, final Blob x)\n
    setBlob(final String parameterName, final InputStream inputStream)\n
    setBlob(final String parameterName, final InputStream inputStream, final long length)\n
    '''
def setCharacterStream():
    '''returns None\n\n
    setCharacterStream(final String parameterName, final Reader reader)\n
    setCharacterStream(final String parameterName, final Reader reader, final long length)\n
    setCharacterStream(final String s, final Reader r, final int i)\n
    '''
def setClob():
    '''returns None\n\n
    setClob(final String parameterName, final Clob x)\n
    setClob(final String parameterName, final Reader reader)\n
    setClob(final String parameterName, final Reader reader, final long length)\n
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
def setRowId():
    '''returns None\n\n
    setRowId(final String parameterName, final RowId x)\n
    '''
def setSQLXML():
    '''returns None\n\n
    setSQLXML(final String parameterName, final SQLXML xmlObject)\n
    '''
def registerOutParameter():
    '''returns None\n\n
    registerOutParameter(final String s, final int i)\n
    registerOutParameter(final String s, final int i1, final int i2)\n
    registerOutParameter(final String s, final int i, final String s2)\n
    registerOutParameter(final int paramIndex, final int sqlType, final String typeName)\n
    registerOutParameter(final int parameterIndex, final int sqlType)\n
    registerOutParameter(final int parameterIndex, final int sqlType, final int scale)\n
    '''
def setURL():
    '''returns None\n\n
    setURL(final String s, final URL url)\n
    '''
def setNull():
    '''returns None\n\n
    setNull(final String s, final int i)\n
    setNull(final String s1, final String s2)\n
    setNull(final String s1, final int i, final String s2)\n
    '''
def setBoolean():
    '''returns None\n\n
    setBoolean(final String s, final boolean b)\n
    '''
def setByte():
    '''returns None\n\n
    setByte(final String s, final byte b)\n
    '''
def setShort():
    '''returns None\n\n
    setShort(final String s, final short sh)\n
    '''
def setInt():
    '''returns None\n\n
    setInt(final String s, final int i)\n
    '''
def setLong():
    '''returns None\n\n
    setLong(final String s, final long l)\n
    '''
def setFloat():
    '''returns None\n\n
    setFloat(final String s, final float f)\n
    '''
def setDouble():
    '''returns None\n\n
    setDouble(final String s, final double d)\n
    '''
def setBigDecimal():
    '''returns None\n\n
    setBigDecimal(final String s, final BigDecimal bd)\n
    '''
def setString():
    '''returns None\n\n
    setString(final String s, final String s2)\n
    '''
def setBytes():
    '''returns None\n\n
    setBytes(final String s, final byte[] b)\n
    '''
def setDate():
    '''returns None\n\n
    setDate(final String s, final Date d)\n
    setDate(final String s, final Date d, final Calendar c)\n
    '''
def setTime():
    '''returns None\n\n
    setTime(final String s, final Time t)\n
    setTime(final String s, final Time t, final Calendar c)\n
    '''
def setTimestamp():
    '''returns None\n\n
    setTimestamp(final String s, final Timestamp ts)\n
    setTimestamp(final String s, final Timestamp t, final Calendar c)\n
    '''
def setObject():
    '''returns None\n\n
    setObject(final String s, final Object o, final int i)\n
    setObject(final String s, final Object o, final int i, final int i2)\n
    setObject(final String s, final Object o)\n
    '''
def getArray():
    '''returns Array\n\n
    getArray(final String parameterName)\n
    getArray(final int i)\n
    '''
def getBigDecimal():
    '''returns BigDecimal\n\n
    getBigDecimal(final String parameterName)\n
    getBigDecimal(final int parameterIndex)\n
    getBigDecimal(final int parameterIndex, final int scale)\n
    '''
def getBlob():
    '''returns Blob\n\n
    getBlob(final String parameterName)\n
    getBlob(final int i)\n
    '''
def getBoolean():
    '''returns boolean\n\n
    getBoolean(final String parameterName)\n
    getBoolean(final int parameterIndex)\n
    '''
def getByte():
    '''returns byte\n\n
    getByte(final String parameterName)\n
    getByte(final int parameterIndex)\n
    '''
def getBytes():
    '''returns byte[]\n\n
    getBytes(final String parameterName)\n
    getBytes(final int parameterIndex)\n
    '''
def getClob():
    '''returns Clob\n\n
    getClob(final String parameterName)\n
    getClob(final int i)\n
    '''
def getDate():
    '''returns Date\n\n
    getDate(final String parameterName)\n
    getDate(final String parameterName, final Calendar cal)\n
    getDate(final int parameterIndex, final Calendar cal)\n
    getDate(final int parameterIndex)\n
    '''
def getDouble():
    '''returns double\n\n
    getDouble(final String parameterName)\n
    getDouble(final int parameterIndex)\n
    '''
def getFloat():
    '''returns float\n\n
    getFloat(final String parameterName)\n
    getFloat(final int parameterIndex)\n
    '''
def getInt():
    '''returns int\n\n
    getInt(final String parameterName)\n
    getInt(final int parameterIndex)\n
    '''
def getLong():
    '''returns long\n\n
    getLong(final String parameterName)\n
    getLong(final int parameterIndex)\n
    '''
def getObject():
    '''returns Object\n\n
    getObject(final String parameterName)\n
    getObject(final String parameterName, final Map map)\n
    getObject(final int i, final Map map)\n
    getObject(final int parameterIndex)\n
    '''
def getRef():
    '''returns Ref\n\n
    getRef(final String parameterName)\n
    getRef(final int i)\n
    '''
def getShort():
    '''returns short\n\n
    getShort(final String parameterName)\n
    getShort(final int parameterIndex)\n
    '''
def getString():
    '''returns String\n\n
    getString(final String s)\n
    getString(final int parameterIndex)\n
    '''
def getTime():
    '''returns Time\n\n
    getTime(final String parameterName)\n
    getTime(final String parameterName, final Calendar cal)\n
    getTime(final int parameterIndex, final Calendar cal)\n
    getTime(final int parameterIndex)\n
    '''
def getTimestamp():
    '''returns Timestamp\n\n
    getTimestamp(final String parameterName)\n
    getTimestamp(final String parameterName, final Calendar cal)\n
    getTimestamp(final int parameterIndex, final Calendar cal)\n
    getTimestamp(final int parameterIndex)\n
    '''
def getURL():
    '''returns URL\n\n
    getURL(final int parameterIndex)\n
    getURL(final String parameterName)\n
    '''
def wasNull():
    '''returns boolean\n\n
    wasNull()\n
    '''
