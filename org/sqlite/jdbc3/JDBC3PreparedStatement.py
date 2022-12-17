def clearParameters():
    '''returns None\n\n
    clearParameters()\n
    '''
def execute():
    '''returns boolean\n\n
    execute()\n
    execute(final String sql)\n
    '''
def executeQuery():
    '''returns ResultSet\n\n
    executeQuery()\n
    executeQuery(final String sql)\n
    '''
def executeUpdate():
    '''returns int\n\n
    executeUpdate()\n
    executeUpdate(final String sql)\n
    '''
def addBatch():
    '''returns None\n\n
    addBatch()\n
    addBatch(final String sql)\n
    '''
def getParameterMetaData():
    '''returns ParameterMetaData\n\n
    getParameterMetaData()\n
    '''
def getParameterCount():
    '''returns int\n\n
    getParameterCount()\n
    '''
def getParameterClassName():
    '''returns String\n\n
    getParameterClassName(final int param)\n
    '''
def getParameterTypeName():
    '''returns String\n\n
    getParameterTypeName(final int pos)\n
    '''
def getParameterType():
    '''returns int\n\n
    getParameterType(final int pos)\n
    '''
def getParameterMode():
    '''returns int\n\n
    getParameterMode(final int pos)\n
    '''
def getPrecision():
    '''returns int\n\n
    getPrecision(final int pos)\n
    '''
def getScale():
    '''returns int\n\n
    getScale(final int pos)\n
    '''
def isNullable():
    '''returns int\n\n
    isNullable(final int pos)\n
    '''
def isSigned():
    '''returns boolean\n\n
    isSigned(final int pos)\n
    '''
def getStatement():
    '''returns Statement\n\n
    getStatement()\n
    '''
def setBigDecimal():
    '''returns None\n\n
    setBigDecimal(final int pos, final BigDecimal value)\n
    '''
def setBinaryStream():
    '''returns None\n\n
    setBinaryStream(final int pos, final InputStream istream, final int length)\n
    '''
def setAsciiStream():
    '''returns None\n\n
    setAsciiStream(final int pos, final InputStream istream, final int length)\n
    '''
def setUnicodeStream():
    '''returns None\n\n
    setUnicodeStream(final int pos, final InputStream istream, final int length)\n
    '''
def setBoolean():
    '''returns None\n\n
    setBoolean(final int pos, final boolean value)\n
    '''
def setByte():
    '''returns None\n\n
    setByte(final int pos, final byte value)\n
    '''
def setBytes():
    '''returns None\n\n
    setBytes(final int pos, final byte[] value)\n
    '''
def setDouble():
    '''returns None\n\n
    setDouble(final int pos, final double value)\n
    '''
def setFloat():
    '''returns None\n\n
    setFloat(final int pos, final float value)\n
    '''
def setInt():
    '''returns None\n\n
    setInt(final int pos, final int value)\n
    '''
def setLong():
    '''returns None\n\n
    setLong(final int pos, final long value)\n
    '''
def setNull():
    '''returns None\n\n
    setNull(final int pos, final int u1)\n
    setNull(final int pos, final int u1, final String u2)\n
    '''
def setObject():
    '''returns None\n\n
    setObject(final int pos, final Object value)\n
    setObject(final int p, final Object v, final int t)\n
    setObject(final int p, final Object v, final int t, final int s)\n
    '''
def setShort():
    '''returns None\n\n
    setShort(final int pos, final short value)\n
    '''
def setString():
    '''returns None\n\n
    setString(final int pos, final String value)\n
    '''
def setCharacterStream():
    '''returns None\n\n
    setCharacterStream(final int pos, final Reader reader, final int length)\n
    '''
def setDate():
    '''returns None\n\n
    setDate(final int pos, final java.sql.Date x)\n
    setDate(final int pos, final java.sql.Date x, final Calendar cal)\n
    '''
def setTime():
    '''returns None\n\n
    setTime(final int pos, final Time x)\n
    setTime(final int pos, final Time x, final Calendar cal)\n
    '''
def setTimestamp():
    '''returns None\n\n
    setTimestamp(final int pos, final Timestamp x)\n
    setTimestamp(final int pos, final Timestamp x, final Calendar cal)\n
    '''
def getMetaData():
    '''returns ResultSetMetaData\n\n
    getMetaData()\n
    '''
def setArray():
    '''returns None\n\n
    setArray(final int i, final Array x)\n
    '''
def setBlob():
    '''returns None\n\n
    setBlob(final int i, final Blob x)\n
    '''
def setClob():
    '''returns None\n\n
    setClob(final int i, final Clob x)\n
    '''
def setRef():
    '''returns None\n\n
    setRef(final int i, final Ref x)\n
    '''
def setURL():
    '''returns None\n\n
    setURL(final int pos, final URL x)\n
    '''
