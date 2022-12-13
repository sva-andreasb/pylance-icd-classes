def registerOutParameter():
    '''public void registerOutParameter(final int index, final int sqlType)
    public void registerOutParameter(final int index, final int sqlType, final String typeName)
    public void registerOutParameter(final int index, final int sqlType, final int scale)
    public void registerOutParameter(final int index, final int sqlType, final int precision, final int scale)
    public void registerOutParameter(final String parameterName, final int sqlType, final String typeName)
    public void registerOutParameter(final String parameterName, final int sqlType, final int scale)
    public void registerOutParameter(final String parameterName, final int sqlType, final int precision, final int scale)
    public void registerOutParameter(final String parameterName, final int sqlType)
    public void registerOutParameter(final int parameterIndex, final SQLType sqlType)
    public void registerOutParameter(final int parameterIndex, final SQLType sqlType, final String typeName)
    public void registerOutParameter(final int parameterIndex, final SQLType sqlType, final int scale)
    public void registerOutParameter(final int parameterIndex, final SQLType sqlType, final int precision, final int scale)
    public void registerOutParameter(final String parameterName, final SQLType sqlType, final String typeName)
    public void registerOutParameter(final String parameterName, final SQLType sqlType, final int scale)
    public void registerOutParameter(final String parameterName, final SQLType sqlType, final int precision, final int scale)
    public void registerOutParameter(final String parameterName, final SQLType sqlType)
    '''
def getInt():
    '''public int getInt(final int index)
    public int getInt(final String parameterName)
    '''
def getString():
    '''public String getString(final int index)
    public String getString(final String parameterName)
    '''
def getNString():
    '''public final String getNString(final int parameterIndex)
    public final String getNString(final String parameterName)
    '''
def getBigDecimal():
    '''public BigDecimal getBigDecimal(final int parameterIndex, final int scale)
    public BigDecimal getBigDecimal(final String parameterName, final int scale)
    public BigDecimal getBigDecimal(final int parameterIndex)
    public BigDecimal getBigDecimal(final String parameterName)
    '''
def getBoolean():
    '''public boolean getBoolean(final int index)
    public boolean getBoolean(final String parameterName)
    '''
def getByte():
    '''public byte getByte(final int index)
    public byte getByte(final String parameterName)
    '''
def getBytes():
    '''public byte[] getBytes(final int index)
    public byte[] getBytes(final String parameterName)
    '''
def getDate():
    '''public Date getDate(final int index)
    public Date getDate(final String parameterName)
    public Date getDate(final int index, final Calendar cal)
    public Date getDate(final String parameterName, final Calendar cal)
    '''
def getDouble():
    '''public double getDouble(final int index)
    public double getDouble(final String parameterName)
    '''
def getFloat():
    '''public float getFloat(final int index)
    public float getFloat(final String parameterName)
    '''
def getLong():
    '''public long getLong(final int index)
    public long getLong(final String parameterName)
    '''
def getObject():
    '''public Object getObject(final int index)
    public <T> T getObject(final int index, final Class<T> type)
    public Object getObject(final String parameterName)
    public <T> T getObject(final String parameterName, final Class<T> type)
    public Object getObject(final int parameterIndex, final Map<String, Class<?>> map)
    public Object getObject(final String parameterName, final Map<String, Class<?>> m)
    '''
def getShort():
    '''public short getShort(final int index)
    public short getShort(final String parameterName)
    '''
def getTime():
    '''public Time getTime(final int index)
    public Time getTime(final String parameterName)
    public Time getTime(final int index, final Calendar cal)
    public Time getTime(final String parameterName, final Calendar cal)
    '''
def getTimestamp():
    '''public Timestamp getTimestamp(final int index)
    public Timestamp getTimestamp(final String parameterName)
    public Timestamp getTimestamp(final int index, final Calendar cal)
    public Timestamp getTimestamp(final String name, final Calendar cal)
    '''
def getDateTime():
    '''public Timestamp getDateTime(final int index)
    public Timestamp getDateTime(final String parameterName)
    public Timestamp getDateTime(final int index, final Calendar cal)
    public Timestamp getDateTime(final String name, final Calendar cal)
    '''
def getSmallDateTime():
    '''public Timestamp getSmallDateTime(final int index)
    public Timestamp getSmallDateTime(final String parameterName)
    public Timestamp getSmallDateTime(final int index, final Calendar cal)
    public Timestamp getSmallDateTime(final String name, final Calendar cal)
    '''
def getDateTimeOffset():
    '''public DateTimeOffset getDateTimeOffset(final int index)
    public DateTimeOffset getDateTimeOffset(final String parameterName)
    '''
def wasNull():
    '''public boolean wasNull()
    '''
def getAsciiStream():
    '''public final InputStream getAsciiStream(final int parameterIndex)
    public final InputStream getAsciiStream(final String parameterName)
    '''
def getMoney():
    '''public BigDecimal getMoney(final int parameterIndex)
    public BigDecimal getMoney(final String parameterName)
    '''
def getSmallMoney():
    '''public BigDecimal getSmallMoney(final int parameterIndex)
    public BigDecimal getSmallMoney(final String parameterName)
    '''
def getBinaryStream():
    '''public final InputStream getBinaryStream(final int parameterIndex)
    public final InputStream getBinaryStream(final String parameterName)
    '''
def getBlob():
    '''public Blob getBlob(final int parameterIndex)
    public Blob getBlob(final String parameterName)
    '''
def getCharacterStream():
    '''public final Reader getCharacterStream(final int parameterIndex)
    public final Reader getCharacterStream(final String parameterName)
    '''
def getNCharacterStream():
    '''public final Reader getNCharacterStream(final int parameterIndex)
    public final Reader getNCharacterStream(final String parameterName)
    '''
def getClob():
    '''public Clob getClob(final int parameterIndex)
    public Clob getClob(final String parameterName)
    '''
def getNClob():
    '''public NClob getNClob(final int parameterIndex)
    public NClob getNClob(final String parameterName)
    '''
def getRef():
    '''public Ref getRef(final int parameterIndex)
    public Ref getRef(final String parameterName)
    '''
def getArray():
    '''public Array getArray(final int parameterIndex)
    public Array getArray(final String parameterName)
    '''
def setTimestamp():
    '''public void setTimestamp(final String parameterName, final Timestamp value, final Calendar calendar)
    public void setTimestamp(final String parameterName, final Timestamp value, final Calendar calendar, final boolean forceEncrypt)
    public void setTimestamp(final String parameterName, final Timestamp value)
    public void setTimestamp(final String parameterName, final Timestamp value, final int scale)
    public void setTimestamp(final String parameterName, final Timestamp value, final int scale, final boolean forceEncrypt)
    '''
def setTime():
    '''public void setTime(final String parameterName, final Time value, final Calendar calendar)
    public void setTime(final String parameterName, final Time value, final Calendar calendar, final boolean forceEncrypt)
    public void setTime(final String parameterName, final Time value)
    public void setTime(final String parameterName, final Time value, final int scale)
    public void setTime(final String parameterName, final Time value, final int scale, final boolean forceEncrypt)
    '''
def setDate():
    '''public void setDate(final String parameterName, final Date value, final Calendar calendar)
    public void setDate(final String parameterName, final Date value, final Calendar calendar, final boolean forceEncrypt)
    public void setDate(final String parameterName, final Date value)
    '''
def setCharacterStream():
    '''public final void setCharacterStream(final String parameterName, final Reader reader)
    public final void setCharacterStream(final String parameterName, final Reader value, final int length)
    public final void setCharacterStream(final String parameterName, final Reader reader, final long length)
    '''
def setNCharacterStream():
    '''public final void setNCharacterStream(final String parameterName, final Reader value)
    public final void setNCharacterStream(final String parameterName, final Reader value, final long length)
    '''
def setClob():
    '''public final void setClob(final String parameterName, final Clob value)
    public final void setClob(final String parameterName, final Reader reader)
    public final void setClob(final String parameterName, final Reader value, final long length)
    '''
def setNClob():
    '''public final void setNClob(final String parameterName, final NClob value)
    public final void setNClob(final String parameterName, final Reader reader)
    public final void setNClob(final String parameterName, final Reader reader, final long length)
    '''
def setNString():
    '''public final void setNString(final String parameterName, final String value)
    public final void setNString(final String parameterName, final String value, final boolean forceEncrypt)
    '''
def setObject():
    '''public void setObject(final String parameterName, final Object value)
    public void setObject(final String parameterName, final Object value, final int sqlType)
    public void setObject(final String parameterName, final Object value, final int sqlType, final int decimals)
    public void setObject(final String parameterName, final Object value, final int sqlType, final int decimals, final boolean forceEncrypt)
    public final void setObject(final String parameterName, final Object value, final int targetSqlType, final Integer precision, final int scale)
    public void setObject(final String parameterName, final Object value, final SQLType jdbcType)
    public void setObject(final String parameterName, final Object value, final SQLType jdbcType, final int scale)
    public void setObject(final String parameterName, final Object value, final SQLType jdbcType, final int scale, final boolean forceEncrypt)
    '''
def setAsciiStream():
    '''public final void setAsciiStream(final String parameterName, final InputStream value)
    public final void setAsciiStream(final String parameterName, final InputStream value, final int length)
    public final void setAsciiStream(final String parameterName, final InputStream value, final long length)
    '''
def setBinaryStream():
    '''public final void setBinaryStream(final String parameterName, final InputStream value)
    public final void setBinaryStream(final String parameterName, final InputStream value, final int length)
    public final void setBinaryStream(final String parameterName, final InputStream value, final long length)
    '''
def setBlob():
    '''public final void setBlob(final String parameterName, final Blob inputStream)
    public final void setBlob(final String parameterName, final InputStream value)
    public final void setBlob(final String parameterName, final InputStream inputStream, final long length)
    '''
def setDateTimeOffset():
    '''public void setDateTimeOffset(final String parameterName, final DateTimeOffset value)
    public void setDateTimeOffset(final String parameterName, final DateTimeOffset value, final int scale)
    public void setDateTimeOffset(final String parameterName, final DateTimeOffset value, final int scale, final boolean forceEncrypt)
    '''
def setDateTime():
    '''public void setDateTime(final String parameterName, final Timestamp value)
    public void setDateTime(final String parameterName, final Timestamp value, final boolean forceEncrypt)
    '''
def setSmallDateTime():
    '''public void setSmallDateTime(final String parameterName, final Timestamp value)
    public void setSmallDateTime(final String parameterName, final Timestamp value, final boolean forceEncrypt)
    '''
def setUniqueIdentifier():
    '''public void setUniqueIdentifier(final String parameterName, final String guid)
    public void setUniqueIdentifier(final String parameterName, final String guid, final boolean forceEncrypt)
    '''
def setBytes():
    '''public void setBytes(final String parameterName, final byte[] value)
    public void setBytes(final String parameterName, final byte[] value, final boolean forceEncrypt)
    '''
def setByte():
    '''public void setByte(final String parameterName, final byte value)
    public void setByte(final String parameterName, final byte value, final boolean forceEncrypt)
    '''
def setString():
    '''public void setString(final String parameterName, final String value)
    public void setString(final String parameterName, final String value, final boolean forceEncrypt)
    '''
def setMoney():
    '''public void setMoney(final String parameterName, final BigDecimal value)
    public void setMoney(final String parameterName, final BigDecimal value, final boolean forceEncrypt)
    '''
def setSmallMoney():
    '''public void setSmallMoney(final String parameterName, final BigDecimal value)
    public void setSmallMoney(final String parameterName, final BigDecimal value, final boolean forceEncrypt)
    '''
def setBigDecimal():
    '''public void setBigDecimal(final String parameterName, final BigDecimal value)
    public void setBigDecimal(final String parameterName, final BigDecimal value, final int precision, final int scale)
    public void setBigDecimal(final String parameterName, final BigDecimal value, final int precision, final int scale, final boolean forceEncrypt)
    '''
def setDouble():
    '''public void setDouble(final String parameterName, final double value)
    public void setDouble(final String parameterName, final double value, final boolean forceEncrypt)
    '''
def setFloat():
    '''public void setFloat(final String parameterName, final float value)
    public void setFloat(final String parameterName, final float value, final boolean forceEncrypt)
    '''
def setInt():
    '''public void setInt(final String parameterName, final int value)
    public void setInt(final String parameterName, final int value, final boolean forceEncrypt)
    '''
def setLong():
    '''public void setLong(final String parameterName, final long value)
    public void setLong(final String parameterName, final long value, final boolean forceEncrypt)
    '''
def setShort():
    '''public void setShort(final String parameterName, final short value)
    public void setShort(final String parameterName, final short value, final boolean forceEncrypt)
    '''
def setBoolean():
    '''public void setBoolean(final String parameterName, final boolean value)
    public void setBoolean(final String parameterName, final boolean value, final boolean forceEncrypt)
    '''
def setNull():
    '''public void setNull(final String parameterName, final int nType)
    public void setNull(final String parameterName, final int nType, final String sTypeName)
    '''
def setURL():
    '''public void setURL(final String parameterName, final URL url)
    '''
def setStructured():
    '''public final void setStructured(final String parameterName, String tvpName, final SQLServerDataTable tvpDataTable)
    public final void setStructured(final String parameterName, String tvpName, final ResultSet tvpResultSet)
    public final void setStructured(final String parameterName, String tvpName, final ISQLServerDataRecord tvpDataRecord)
    '''
def getURL():
    '''public URL getURL(final int parameterIndex)
    public URL getURL(final String parameterName)
    '''
def setSQLXML():
    '''public final void setSQLXML(final String parameterName, final SQLXML xmlObject)
    '''
def getSQLXML():
    '''public final SQLXML getSQLXML(final int parameterIndex)
    public final SQLXML getSQLXML(final String parameterName)
    '''
def setRowId():
    '''public final void setRowId(final String parameterName, final RowId value)
    '''
def getRowId():
    '''public final RowId getRowId(final int parameterIndex)
    public final RowId getRowId(final String parameterName)
    '''
