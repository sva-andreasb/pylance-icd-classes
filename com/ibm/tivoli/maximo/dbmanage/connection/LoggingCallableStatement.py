def LoggingCallableStatement():
    '''    public LoggingCallableStatement(final CallableStatement prepareCall, final String sql)
    '''
def getArray():
    '''    public Array getArray(final int parameterIndex)
    public Array getArray(final String parameterName)
    '''
def getBigDecimal():
    '''    public BigDecimal getBigDecimal(final int parameterIndex)
    public BigDecimal getBigDecimal(final String parameterName)
    public BigDecimal getBigDecimal(final int parameterIndex, final int scale)
    '''
def getBlob():
    '''    public Blob getBlob(final int parameterIndex)
    public Blob getBlob(final String parameterName)
    '''
def getBoolean():
    '''    public boolean getBoolean(final int parameterIndex)
    public boolean getBoolean(final String parameterName)
    '''
def getByte():
    '''    public byte getByte(final int parameterIndex)
    public byte getByte(final String parameterName)
    '''
def getBytes():
    '''    public byte[] getBytes(final int parameterIndex)
    public byte[] getBytes(final String parameterName)
    '''
def getCharacterStream():
    '''    public Reader getCharacterStream(final int parameterIndex)
    public Reader getCharacterStream(final String parameterName)
    '''
def getClob():
    '''    public Clob getClob(final int parameterIndex)
    public Clob getClob(final String parameterName)
    '''
def getDate():
    '''    public Date getDate(final int parameterIndex)
    public Date getDate(final String parameterName)
    public Date getDate(final int parameterIndex, final Calendar cal)
    public Date getDate(final String parameterName, final Calendar cal)
    '''
def getDouble():
    '''    public double getDouble(final int parameterIndex)
    public double getDouble(final String parameterName)
    '''
def getFloat():
    '''    public float getFloat(final int parameterIndex)
    public float getFloat(final String parameterName)
    '''
def getInt():
    '''    public int getInt(final int parameterIndex)
    public int getInt(final String parameterName)
    '''
def getLong():
    '''    public long getLong(final int parameterIndex)
    public long getLong(final String parameterName)
    '''
def getNCharacterStream():
    '''    public Reader getNCharacterStream(final int parameterIndex)
    public Reader getNCharacterStream(final String parameterName)
    '''
def getNClob():
    '''    public NClob getNClob(final int parameterIndex)
    public NClob getNClob(final String parameterName)
    '''
def getNString():
    '''    public String getNString(final int parameterIndex)
    public String getNString(final String parameterName)
    '''
def getObject():
    '''    public Object getObject(final int parameterIndex)
    public Object getObject(final String parameterName)
    public Object getObject(final int parameterIndex, final Map<String, Class<?>> map)
    public Object getObject(final String parameterName, final Map<String, Class<?>> map)
    public <T> T getObject(final int parameterIndex, final Class<T> type)
    public <T> T getObject(final String parameterName, final Class<T> type)
    '''
def getRef():
    '''    public Ref getRef(final int parameterIndex)
    public Ref getRef(final String parameterName)
    '''
def getRowId():
    '''    public RowId getRowId(final int parameterIndex)
    public RowId getRowId(final String parameterName)
    '''
def getSQLXML():
    '''    public SQLXML getSQLXML(final int parameterIndex)
    public SQLXML getSQLXML(final String parameterName)
    '''
def getShort():
    '''    public short getShort(final int parameterIndex)
    public short getShort(final String parameterName)
    '''
def getString():
    '''    public String getString(final int parameterIndex)
    public String getString(final String parameterName)
    '''
def getTime():
    '''    public Time getTime(final int parameterIndex)
    public Time getTime(final String parameterName)
    public Time getTime(final int parameterIndex, final Calendar cal)
    public Time getTime(final String parameterName, final Calendar cal)
    '''
def getTimestamp():
    '''    public Timestamp getTimestamp(final int parameterIndex)
    public Timestamp getTimestamp(final String parameterName)
    public Timestamp getTimestamp(final int parameterIndex, final Calendar cal)
    public Timestamp getTimestamp(final String parameterName, final Calendar cal)
    '''
def getURL():
    '''    public URL getURL(final int parameterIndex)
    public URL getURL(final String parameterName)
    '''
def registerOutParameter():
    '''    public void registerOutParameter(final int parameterIndex, final int sqlType)
    public void registerOutParameter(final String parameterName, final int sqlType)
    public void registerOutParameter(final int parameterIndex, final int sqlType, final int scale)
    public void registerOutParameter(final int parameterIndex, final int sqlType, final String typeName)
    public void registerOutParameter(final String parameterName, final int sqlType, final int scale)
    public void registerOutParameter(final String parameterName, final int sqlType, final String typeName)
    '''
def setAsciiStream():
    '''    public void setAsciiStream(final String parameterName, final InputStream x)
    public void setAsciiStream(final String parameterName, final InputStream x, final int length)
    public void setAsciiStream(final String parameterName, final InputStream x, final long length)
    '''
def setBigDecimal():
    '''    public void setBigDecimal(final String parameterName, final BigDecimal x)
    '''
def setBinaryStream():
    '''    public void setBinaryStream(final String parameterName, final InputStream x)
    public void setBinaryStream(final String parameterName, final InputStream x, final int length)
    public void setBinaryStream(final String parameterName, final InputStream x, final long length)
    '''
def setBlob():
    '''    public void setBlob(final String parameterName, final Blob x)
    public void setBlob(final String parameterName, final InputStream inputStream)
    public void setBlob(final String parameterName, final InputStream inputStream, final long length)
    '''
def setBoolean():
    '''    public void setBoolean(final String parameterName, final boolean x)
    '''
def setByte():
    '''    public void setByte(final String parameterName, final byte x)
    '''
def setBytes():
    '''    public void setBytes(final String parameterName, final byte[] x)
    '''
def setCharacterStream():
    '''    public void setCharacterStream(final String parameterName, final Reader reader)
    public void setCharacterStream(final String parameterName, final Reader reader, final int length)
    public void setCharacterStream(final String parameterName, final Reader reader, final long length)
    '''
def setClob():
    '''    public void setClob(final String parameterName, final Clob x)
    public void setClob(final String parameterName, final Reader reader)
    public void setClob(final String parameterName, final Reader reader, final long length)
    '''
def setDate():
    '''    public void setDate(final String parameterName, final Date x)
    public void setDate(final String parameterName, final Date x, final Calendar cal)
    '''
def setDouble():
    '''    public void setDouble(final String parameterName, final double x)
    '''
def setFloat():
    '''    public void setFloat(final String parameterName, final float x)
    '''
def setInt():
    '''    public void setInt(final String parameterName, final int x)
    '''
def setLong():
    '''    public void setLong(final String parameterName, final long x)
    '''
def setNCharacterStream():
    '''    public void setNCharacterStream(final String parameterName, final Reader value)
    public void setNCharacterStream(final String parameterName, final Reader value, final long length)
    '''
def setNClob():
    '''    public void setNClob(final String parameterName, final NClob value)
    public void setNClob(final String parameterName, final Reader reader)
    public void setNClob(final String parameterName, final Reader reader, final long length)
    '''
def setNString():
    '''    public void setNString(final String parameterName, final String value)
    '''
def setNull():
    '''    public void setNull(final String parameterName, final int sqlType)
    public void setNull(final String parameterName, final int sqlType, final String typeName)
    '''
def setObject():
    '''    public void setObject(final String parameterName, final Object x)
    public void setObject(final String parameterName, final Object x, final int targetSqlType)
    public void setObject(final String parameterName, final Object x, final int targetSqlType, final int scale)
    '''
def setRowId():
    '''    public void setRowId(final String parameterName, final RowId x)
    '''
def setSQLXML():
    '''    public void setSQLXML(final String parameterName, final SQLXML xmlObject)
    '''
def setShort():
    '''    public void setShort(final String parameterName, final short x)
    '''
def setString():
    '''    public void setString(final String parameterName, final String x)
    '''
def setTime():
    '''    public void setTime(final String parameterName, final Time x)
    public void setTime(final String parameterName, final Time x, final Calendar cal)
    '''
def setTimestamp():
    '''    public void setTimestamp(final String parameterName, final Timestamp x)
    public void setTimestamp(final String parameterName, final Timestamp x, final Calendar cal)
    '''
def setURL():
    '''    public void setURL(final String parameterName, final URL val)
    '''
def wasNull():
    '''    public boolean wasNull()
    '''
