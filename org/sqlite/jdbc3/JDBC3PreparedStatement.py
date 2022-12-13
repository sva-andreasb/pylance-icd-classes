def clearParameters():
    '''    public void clearParameters()
    '''
def execute():
    '''    public boolean execute()
    public boolean execute(final String sql)
    '''
def executeQuery():
    '''    public ResultSet executeQuery()
    public ResultSet executeQuery(final String sql)
    '''
def executeUpdate():
    '''    public int executeUpdate()
    public int executeUpdate(final String sql)
    '''
def addBatch():
    '''    public void addBatch()
    public void addBatch(final String sql)
    '''
def getParameterMetaData():
    '''    public ParameterMetaData getParameterMetaData()
    '''
def getParameterCount():
    '''    public int getParameterCount()
    '''
def getParameterClassName():
    '''    public String getParameterClassName(final int param)
    '''
def getParameterTypeName():
    '''    public String getParameterTypeName(final int pos)
    '''
def getParameterType():
    '''    public int getParameterType(final int pos)
    '''
def getParameterMode():
    '''    public int getParameterMode(final int pos)
    '''
def getPrecision():
    '''    public int getPrecision(final int pos)
    '''
def getScale():
    '''    public int getScale(final int pos)
    '''
def isNullable():
    '''    public int isNullable(final int pos)
    '''
def isSigned():
    '''    public boolean isSigned(final int pos)
    '''
def getStatement():
    '''    public Statement getStatement()
    '''
def setBigDecimal():
    '''    public void setBigDecimal(final int pos, final BigDecimal value)
    '''
def setBinaryStream():
    '''    public void setBinaryStream(final int pos, final InputStream istream, final int length)
    '''
def setAsciiStream():
    '''    public void setAsciiStream(final int pos, final InputStream istream, final int length)
    '''
def setUnicodeStream():
    '''    public void setUnicodeStream(final int pos, final InputStream istream, final int length)
    '''
def setBoolean():
    '''    public void setBoolean(final int pos, final boolean value)
    '''
def setByte():
    '''    public void setByte(final int pos, final byte value)
    '''
def setBytes():
    '''    public void setBytes(final int pos, final byte[] value)
    '''
def setDouble():
    '''    public void setDouble(final int pos, final double value)
    '''
def setFloat():
    '''    public void setFloat(final int pos, final float value)
    '''
def setInt():
    '''    public void setInt(final int pos, final int value)
    '''
def setLong():
    '''    public void setLong(final int pos, final long value)
    '''
def setNull():
    '''    public void setNull(final int pos, final int u1)
    public void setNull(final int pos, final int u1, final String u2)
    '''
def setObject():
    '''    public void setObject(final int pos, final Object value)
    public void setObject(final int p, final Object v, final int t)
    public void setObject(final int p, final Object v, final int t, final int s)
    '''
def setShort():
    '''    public void setShort(final int pos, final short value)
    '''
def setString():
    '''    public void setString(final int pos, final String value)
    '''
def setCharacterStream():
    '''    public void setCharacterStream(final int pos, final Reader reader, final int length)
    '''
def setDate():
    '''    public void setDate(final int pos, final java.sql.Date x)
    public void setDate(final int pos, final java.sql.Date x, final Calendar cal)
    '''
def setTime():
    '''    public void setTime(final int pos, final Time x)
    public void setTime(final int pos, final Time x, final Calendar cal)
    '''
def setTimestamp():
    '''    public void setTimestamp(final int pos, final Timestamp x)
    public void setTimestamp(final int pos, final Timestamp x, final Calendar cal)
    '''
def getMetaData():
    '''    public ResultSetMetaData getMetaData()
    '''
def setArray():
    '''    public void setArray(final int i, final Array x)
    '''
def setBlob():
    '''    public void setBlob(final int i, final Blob x)
    '''
def setClob():
    '''    public void setClob(final int i, final Clob x)
    '''
def setRef():
    '''    public void setRef(final int i, final Ref x)
    '''
def setURL():
    '''    public void setURL(final int pos, final URL x)
    '''
