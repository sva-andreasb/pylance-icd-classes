def registerOutParameter():
    '''returns None\n\n
    registerOutParameter(final int index, final int sqlType)\n
    registerOutParameter(final int index, final int sqlType, final String typeName)\n
    registerOutParameter(final int index, final int sqlType, final int scale)\n
    registerOutParameter(final int index, final int sqlType, final int precision, final int scale)\n
    registerOutParameter(final String parameterName, final int sqlType, final String typeName)\n
    registerOutParameter(final String parameterName, final int sqlType, final int scale)\n
    registerOutParameter(final String parameterName, final int sqlType, final int precision, final int scale)\n
    registerOutParameter(final String parameterName, final int sqlType)\n
    registerOutParameter(final int parameterIndex, final SQLType sqlType)\n
    registerOutParameter(final int parameterIndex, final SQLType sqlType, final String typeName)\n
    registerOutParameter(final int parameterIndex, final SQLType sqlType, final int scale)\n
    registerOutParameter(final int parameterIndex, final SQLType sqlType, final int precision, final int scale)\n
    registerOutParameter(final String parameterName, final SQLType sqlType, final String typeName)\n
    registerOutParameter(final String parameterName, final SQLType sqlType, final int scale)\n
    registerOutParameter(final String parameterName, final SQLType sqlType, final int precision, final int scale)\n
    registerOutParameter(final String parameterName, final SQLType sqlType)\n
    '''
def getInt():
    '''returns int\n\n
    getInt(final int index)\n
    getInt(final String parameterName)\n
    '''
def getString():
    '''returns String\n\n
    getString(final int index)\n
    getString(final String parameterName)\n
    '''
def getBigDecimal():
    '''returns BigDecimal\n\n
    getBigDecimal(final int parameterIndex, final int scale)\n
    getBigDecimal(final String parameterName, final int scale)\n
    getBigDecimal(final int parameterIndex)\n
    getBigDecimal(final String parameterName)\n
    '''
def getBoolean():
    '''returns boolean\n\n
    getBoolean(final int index)\n
    getBoolean(final String parameterName)\n
    '''
def getByte():
    '''returns byte\n\n
    getByte(final int index)\n
    getByte(final String parameterName)\n
    '''
def getBytes():
    '''returns byte[]\n\n
    getBytes(final int index)\n
    getBytes(final String parameterName)\n
    '''
def getDate():
    '''returns Date\n\n
    getDate(final int index)\n
    getDate(final String parameterName)\n
    getDate(final int index, final Calendar cal)\n
    getDate(final String parameterName, final Calendar cal)\n
    '''
def getDouble():
    '''returns double\n\n
    getDouble(final int index)\n
    getDouble(final String parameterName)\n
    '''
def getFloat():
    '''returns float\n\n
    getFloat(final int index)\n
    getFloat(final String parameterName)\n
    '''
def getLong():
    '''returns long\n\n
    getLong(final int index)\n
    getLong(final String parameterName)\n
    '''
def getObject():
    '''returns Object\n\n
    getObject(final int index)\n
    getObject(final String parameterName)\n
    getObject(final int parameterIndex, final Map<String, Class<?>> map)\n
    getObject(final String parameterName, final Map<String, Class<?>> m)\n
    '''
def getShort():
    '''returns short\n\n
    getShort(final int index)\n
    getShort(final String parameterName)\n
    '''
def getTime():
    '''returns Time\n\n
    getTime(final int index)\n
    getTime(final String parameterName)\n
    getTime(final int index, final Calendar cal)\n
    getTime(final String parameterName, final Calendar cal)\n
    '''
def getTimestamp():
    '''returns Timestamp\n\n
    getTimestamp(final int index)\n
    getTimestamp(final String parameterName)\n
    getTimestamp(final int index, final Calendar cal)\n
    getTimestamp(final String name, final Calendar cal)\n
    '''
def getDateTime():
    '''returns Timestamp\n\n
    getDateTime(final int index)\n
    getDateTime(final String parameterName)\n
    getDateTime(final int index, final Calendar cal)\n
    getDateTime(final String name, final Calendar cal)\n
    '''
def getSmallDateTime():
    '''returns Timestamp\n\n
    getSmallDateTime(final int index)\n
    getSmallDateTime(final String parameterName)\n
    getSmallDateTime(final int index, final Calendar cal)\n
    getSmallDateTime(final String name, final Calendar cal)\n
    '''
def getDateTimeOffset():
    '''returns DateTimeOffset\n\n
    getDateTimeOffset(final int index)\n
    getDateTimeOffset(final String parameterName)\n
    '''
def wasNull():
    '''returns boolean\n\n
    wasNull()\n
    '''
def getMoney():
    '''returns BigDecimal\n\n
    getMoney(final int parameterIndex)\n
    getMoney(final String parameterName)\n
    '''
def getSmallMoney():
    '''returns BigDecimal\n\n
    getSmallMoney(final int parameterIndex)\n
    getSmallMoney(final String parameterName)\n
    '''
def getBlob():
    '''returns Blob\n\n
    getBlob(final int parameterIndex)\n
    getBlob(final String parameterName)\n
    '''
def getClob():
    '''returns Clob\n\n
    getClob(final int parameterIndex)\n
    getClob(final String parameterName)\n
    '''
def getNClob():
    '''returns NClob\n\n
    getNClob(final int parameterIndex)\n
    getNClob(final String parameterName)\n
    '''
def getRef():
    '''returns Ref\n\n
    getRef(final int parameterIndex)\n
    getRef(final String parameterName)\n
    '''
def getArray():
    '''returns Array\n\n
    getArray(final int parameterIndex)\n
    getArray(final String parameterName)\n
    '''
def setTimestamp():
    '''returns None\n\n
    setTimestamp(final String parameterName, final Timestamp value, final Calendar calendar)\n
    setTimestamp(final String parameterName, final Timestamp value, final Calendar calendar, final boolean forceEncrypt)\n
    setTimestamp(final String parameterName, final Timestamp value)\n
    setTimestamp(final String parameterName, final Timestamp value, final int scale)\n
    setTimestamp(final String parameterName, final Timestamp value, final int scale, final boolean forceEncrypt)\n
    '''
def setTime():
    '''returns None\n\n
    setTime(final String parameterName, final Time value, final Calendar calendar)\n
    setTime(final String parameterName, final Time value, final Calendar calendar, final boolean forceEncrypt)\n
    setTime(final String parameterName, final Time value)\n
    setTime(final String parameterName, final Time value, final int scale)\n
    setTime(final String parameterName, final Time value, final int scale, final boolean forceEncrypt)\n
    '''
def setDate():
    '''returns None\n\n
    setDate(final String parameterName, final Date value, final Calendar calendar)\n
    setDate(final String parameterName, final Date value, final Calendar calendar, final boolean forceEncrypt)\n
    setDate(final String parameterName, final Date value)\n
    '''
def setObject():
    '''returns None\n\n
    setObject(final String parameterName, final Object value)\n
    setObject(final String parameterName, final Object value, final int sqlType)\n
    setObject(final String parameterName, final Object value, final int sqlType, final int decimals)\n
    setObject(final String parameterName, final Object value, final int sqlType, final int decimals, final boolean forceEncrypt)\n
    setObject(final String parameterName, final Object value, final SQLType jdbcType)\n
    setObject(final String parameterName, final Object value, final SQLType jdbcType, final int scale)\n
    setObject(final String parameterName, final Object value, final SQLType jdbcType, final int scale, final boolean forceEncrypt)\n
    '''
def setDateTimeOffset():
    '''returns None\n\n
    setDateTimeOffset(final String parameterName, final DateTimeOffset value)\n
    setDateTimeOffset(final String parameterName, final DateTimeOffset value, final int scale)\n
    setDateTimeOffset(final String parameterName, final DateTimeOffset value, final int scale, final boolean forceEncrypt)\n
    '''
def setDateTime():
    '''returns None\n\n
    setDateTime(final String parameterName, final Timestamp value)\n
    setDateTime(final String parameterName, final Timestamp value, final boolean forceEncrypt)\n
    '''
def setSmallDateTime():
    '''returns None\n\n
    setSmallDateTime(final String parameterName, final Timestamp value)\n
    setSmallDateTime(final String parameterName, final Timestamp value, final boolean forceEncrypt)\n
    '''
def setUniqueIdentifier():
    '''returns None\n\n
    setUniqueIdentifier(final String parameterName, final String guid)\n
    setUniqueIdentifier(final String parameterName, final String guid, final boolean forceEncrypt)\n
    '''
def setBytes():
    '''returns None\n\n
    setBytes(final String parameterName, final byte[] value)\n
    setBytes(final String parameterName, final byte[] value, final boolean forceEncrypt)\n
    '''
def setByte():
    '''returns None\n\n
    setByte(final String parameterName, final byte value)\n
    setByte(final String parameterName, final byte value, final boolean forceEncrypt)\n
    '''
def setString():
    '''returns None\n\n
    setString(final String parameterName, final String value)\n
    setString(final String parameterName, final String value, final boolean forceEncrypt)\n
    '''
def setMoney():
    '''returns None\n\n
    setMoney(final String parameterName, final BigDecimal value)\n
    setMoney(final String parameterName, final BigDecimal value, final boolean forceEncrypt)\n
    '''
def setSmallMoney():
    '''returns None\n\n
    setSmallMoney(final String parameterName, final BigDecimal value)\n
    setSmallMoney(final String parameterName, final BigDecimal value, final boolean forceEncrypt)\n
    '''
def setBigDecimal():
    '''returns None\n\n
    setBigDecimal(final String parameterName, final BigDecimal value)\n
    setBigDecimal(final String parameterName, final BigDecimal value, final int precision, final int scale)\n
    setBigDecimal(final String parameterName, final BigDecimal value, final int precision, final int scale, final boolean forceEncrypt)\n
    '''
def setDouble():
    '''returns None\n\n
    setDouble(final String parameterName, final double value)\n
    setDouble(final String parameterName, final double value, final boolean forceEncrypt)\n
    '''
def setFloat():
    '''returns None\n\n
    setFloat(final String parameterName, final float value)\n
    setFloat(final String parameterName, final float value, final boolean forceEncrypt)\n
    '''
def setInt():
    '''returns None\n\n
    setInt(final String parameterName, final int value)\n
    setInt(final String parameterName, final int value, final boolean forceEncrypt)\n
    '''
def setLong():
    '''returns None\n\n
    setLong(final String parameterName, final long value)\n
    setLong(final String parameterName, final long value, final boolean forceEncrypt)\n
    '''
def setShort():
    '''returns None\n\n
    setShort(final String parameterName, final short value)\n
    setShort(final String parameterName, final short value, final boolean forceEncrypt)\n
    '''
def setBoolean():
    '''returns None\n\n
    setBoolean(final String parameterName, final boolean value)\n
    setBoolean(final String parameterName, final boolean value, final boolean forceEncrypt)\n
    '''
def setNull():
    '''returns None\n\n
    setNull(final String parameterName, final int nType)\n
    setNull(final String parameterName, final int nType, final String sTypeName)\n
    '''
def setURL():
    '''returns None\n\n
    setURL(final String parameterName, final URL url)\n
    '''
def getURL():
    '''returns URL\n\n
    getURL(final int parameterIndex)\n
    getURL(final String parameterName)\n
    '''
