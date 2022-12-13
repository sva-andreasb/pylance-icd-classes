def JDBC4ResultSet():
'''public JDBC4ResultSet(final CoreStatement stmt)
'''
pass
def close():
'''public void close()
'''
pass
def unwrap():
'''public <T> T unwrap(final Class<T> iface)
'''
pass
def isWrapperFor():
'''public boolean isWrapperFor(final Class<?> iface)
'''
pass
def getRowId():
'''public RowId getRowId(final int columnIndex)
public RowId getRowId(final String columnLabel)
'''
pass
def updateRowId():
'''public void updateRowId(final int columnIndex, final RowId x)
public void updateRowId(final String columnLabel, final RowId x)
'''
pass
def getHoldability():
'''public int getHoldability()
'''
pass
def isClosed():
'''public boolean isClosed()
'''
pass
def updateNString():
'''public void updateNString(final int columnIndex, final String nString)
public void updateNString(final String columnLabel, final String nString)
'''
pass
def updateNClob():
'''public void updateNClob(final int columnIndex, final NClob nClob)
public void updateNClob(final String columnLabel, final NClob nClob)
public void updateNClob(final int columnIndex, final Reader reader, final long length)
public void updateNClob(final String columnLabel, final Reader reader, final long length)
public void updateNClob(final int columnIndex, final Reader reader)
public void updateNClob(final String columnLabel, final Reader reader)
'''
pass
def getNClob():
'''public NClob getNClob(final int columnIndex)
public NClob getNClob(final String columnLabel)
'''
pass
def getSQLXML():
'''public SQLXML getSQLXML(final int columnIndex)
public SQLXML getSQLXML(final String columnLabel)
'''
pass
def updateSQLXML():
'''public void updateSQLXML(final int columnIndex, final SQLXML xmlObject)
public void updateSQLXML(final String columnLabel, final SQLXML xmlObject)
'''
pass
def getNString():
'''public String getNString(final int columnIndex)
public String getNString(final String columnLabel)
'''
pass
def getNCharacterStream():
'''public Reader getNCharacterStream(final int col)
public Reader getNCharacterStream(final String col)
'''
pass
def updateNCharacterStream():
'''public void updateNCharacterStream(final int columnIndex, final Reader x, final long length)
public void updateNCharacterStream(final String columnLabel, final Reader reader, final long length)
public void updateNCharacterStream(final int columnIndex, final Reader x)
public void updateNCharacterStream(final String columnLabel, final Reader reader)
'''
pass
def updateAsciiStream():
'''public void updateAsciiStream(final int columnIndex, final InputStream x, final long length)
public void updateAsciiStream(final String columnLabel, final InputStream x, final long length)
public void updateAsciiStream(final int columnIndex, final InputStream x)
public void updateAsciiStream(final String columnLabel, final InputStream x)
public void updateAsciiStream(final int col, final InputStream x, final int l)
public void updateAsciiStream(final String col, final InputStream x, final int l)
'''
pass
def updateBinaryStream():
'''public void updateBinaryStream(final int columnIndex, final InputStream x, final long length)
public void updateBinaryStream(final String columnLabel, final InputStream x, final long length)
public void updateBinaryStream(final int columnIndex, final InputStream x)
public void updateBinaryStream(final String columnLabel, final InputStream x)
public void updateBinaryStream(final int c, final InputStream x, final int l)
public void updateBinaryStream(final String c, final InputStream x, final int l)
'''
pass
def updateCharacterStream():
'''public void updateCharacterStream(final int columnIndex, final Reader x, final long length)
public void updateCharacterStream(final String columnLabel, final Reader reader, final long length)
public void updateCharacterStream(final int columnIndex, final Reader x)
public void updateCharacterStream(final String columnLabel, final Reader reader)
public void updateCharacterStream(final int c, final Reader x, final int l)
public void updateCharacterStream(final String c, final Reader r, final int l)
'''
pass
def updateBlob():
'''public void updateBlob(final int columnIndex, final InputStream inputStream, final long length)
public void updateBlob(final String columnLabel, final InputStream inputStream, final long length)
public void updateBlob(final int columnIndex, final InputStream inputStream)
public void updateBlob(final String columnLabel, final InputStream inputStream)
public void updateBlob(final int col, final Blob x)
public void updateBlob(final String col, final Blob x)
'''
pass
def updateClob():
'''public void updateClob(final int columnIndex, final Reader reader, final long length)
public void updateClob(final String columnLabel, final Reader reader, final long length)
public void updateClob(final int columnIndex, final Reader reader)
public void updateClob(final String columnLabel, final Reader reader)
public void updateClob(final int col, final Clob x)
public void updateClob(final String col, final Clob x)
'''
pass
def getObject():
'''public <T> T getObject(final int columnIndex, final Class<T> type)
public <T> T getObject(final String columnLabel, final Class<T> type)
public Object getObject(final int col, final Map map)
public Object getObject(final String col, final Map map)
'''
pass
def getArray():
'''public Array getArray(final int i)
public Array getArray(final String col)
'''
pass
def getAsciiStream():
'''public InputStream getAsciiStream(final int col)
public InputStream getAsciiStream(final String col)
public InputStream getAsciiStream()
'''
pass
def getBigDecimal():
'''public BigDecimal getBigDecimal(final int col, final int s)
public BigDecimal getBigDecimal(final String col, final int s)
'''
pass
def getBlob():
'''public Blob getBlob(final int col)
public Blob getBlob(final String col)
'''
pass
def getClob():
'''public Clob getClob(final int col)
public Clob getClob(final String col)
'''
pass
def getRef():
'''public Ref getRef(final int i)
public Ref getRef(final String col)
'''
pass
def getUnicodeStream():
'''public InputStream getUnicodeStream(final int col)
public InputStream getUnicodeStream(final String col)
'''
pass
def getURL():
'''public URL getURL(final int col)
public URL getURL(final String col)
'''
pass
def insertRow():
'''public void insertRow()
'''
pass
def moveToCurrentRow():
'''public void moveToCurrentRow()
'''
pass
def moveToInsertRow():
'''public void moveToInsertRow()
'''
pass
def last():
'''public boolean last()
'''
pass
def previous():
'''public boolean previous()
'''
pass
def relative():
'''public boolean relative(final int rows)
'''
pass
def absolute():
'''public boolean absolute(final int row)
'''
pass
def afterLast():
'''public void afterLast()
'''
pass
def beforeFirst():
'''public void beforeFirst()
'''
pass
def first():
'''public boolean first()
'''
pass
def cancelRowUpdates():
'''public void cancelRowUpdates()
'''
pass
def deleteRow():
'''public void deleteRow()
'''
pass
def updateArray():
'''public void updateArray(final int col, final Array x)
public void updateArray(final String col, final Array x)
'''
pass
def updateBigDecimal():
'''public void updateBigDecimal(final int col, final BigDecimal x)
public void updateBigDecimal(final String col, final BigDecimal x)
'''
pass
def updateBoolean():
'''public void updateBoolean(final int col, final boolean x)
public void updateBoolean(final String col, final boolean x)
'''
pass
def updateByte():
'''public void updateByte(final int col, final byte x)
public void updateByte(final String col, final byte x)
'''
pass
def updateBytes():
'''public void updateBytes(final int col, final byte[] x)
public void updateBytes(final String col, final byte[] x)
'''
pass
def updateDate():
'''public void updateDate(final int col, final Date x)
public void updateDate(final String col, final Date x)
'''
pass
def updateDouble():
'''public void updateDouble(final int col, final double x)
public void updateDouble(final String col, final double x)
'''
pass
def updateFloat():
'''public void updateFloat(final int col, final float x)
public void updateFloat(final String col, final float x)
'''
pass
def updateInt():
'''public void updateInt(final int col, final int x)
public void updateInt(final String col, final int x)
'''
pass
def updateLong():
'''public void updateLong(final int col, final long x)
public void updateLong(final String col, final long x)
'''
pass
def updateNull():
'''public void updateNull(final int col)
public void updateNull(final String col)
'''
pass
def updateObject():
'''public void updateObject(final int c, final Object x)
public void updateObject(final int c, final Object x, final int s)
public void updateObject(final String col, final Object x)
public void updateObject(final String c, final Object x, final int s)
'''
pass
def updateRef():
'''public void updateRef(final int col, final Ref x)
public void updateRef(final String c, final Ref x)
'''
pass
def updateRow():
'''public void updateRow()
'''
pass
def updateShort():
'''public void updateShort(final int c, final short x)
public void updateShort(final String c, final short x)
'''
pass
def updateString():
'''public void updateString(final int c, final String x)
public void updateString(final String c, final String x)
'''
pass
def updateTime():
'''public void updateTime(final int c, final Time x)
public void updateTime(final String c, final Time x)
'''
pass
def updateTimestamp():
'''public void updateTimestamp(final int c, final Timestamp x)
public void updateTimestamp(final String c, final Timestamp x)
'''
pass
def refreshRow():
'''public void refreshRow()
'''
pass
def free():
'''public void free()
'''
pass
def getCharacterStream():
'''public Reader getCharacterStream()
public Reader getCharacterStream(final long arg0, final long arg1)
'''
pass
def getSubString():
'''public String getSubString(final long position, final int length)
'''
pass
def length():
'''public long length()
'''
pass
def position():
'''public long position(final String arg0, final long arg1)
public long position(final Clob arg0, final long arg1)
'''
pass
def setAsciiStream():
'''public OutputStream setAsciiStream(final long arg0)
'''
pass
def setCharacterStream():
'''public Writer setCharacterStream(final long arg0)
'''
pass
def setString():
'''public int setString(final long arg0, final String arg1)
public int setString(final long arg0, final String arg1, final int arg2, final int arg3)
'''
pass
def truncate():
'''public void truncate(final long arg0)
'''
pass
