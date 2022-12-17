def ():
    '''returns JDBC4ResultSet\n\n
    (final CoreStatement stmt)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def isWrapperFor():
    '''returns boolean\n\n
    isWrapperFor(final Class<?> iface)\n
    '''
def getRowId():
    '''returns RowId\n\n
    getRowId(final int columnIndex)\n
    getRowId(final String columnLabel)\n
    '''
def updateRowId():
    '''returns None\n\n
    updateRowId(final int columnIndex, final RowId x)\n
    updateRowId(final String columnLabel, final RowId x)\n
    '''
def getHoldability():
    '''returns int\n\n
    getHoldability()\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
def updateNString():
    '''returns None\n\n
    updateNString(final int columnIndex, final String nString)\n
    updateNString(final String columnLabel, final String nString)\n
    '''
def updateNClob():
    '''returns None\n\n
    updateNClob(final int columnIndex, final NClob nClob)\n
    updateNClob(final String columnLabel, final NClob nClob)\n
    updateNClob(final int columnIndex, final Reader reader, final long length)\n
    updateNClob(final String columnLabel, final Reader reader, final long length)\n
    updateNClob(final int columnIndex, final Reader reader)\n
    updateNClob(final String columnLabel, final Reader reader)\n
    '''
def getNClob():
    '''returns NClob\n\n
    getNClob(final int columnIndex)\n
    getNClob(final String columnLabel)\n
    '''
def getSQLXML():
    '''returns SQLXML\n\n
    getSQLXML(final int columnIndex)\n
    getSQLXML(final String columnLabel)\n
    '''
def updateSQLXML():
    '''returns None\n\n
    updateSQLXML(final int columnIndex, final SQLXML xmlObject)\n
    updateSQLXML(final String columnLabel, final SQLXML xmlObject)\n
    '''
def getNString():
    '''returns String\n\n
    getNString(final int columnIndex)\n
    getNString(final String columnLabel)\n
    '''
def getNCharacterStream():
    '''returns Reader\n\n
    getNCharacterStream(final int col)\n
    getNCharacterStream(final String col)\n
    '''
def updateNCharacterStream():
    '''returns None\n\n
    updateNCharacterStream(final int columnIndex, final Reader x, final long length)\n
    updateNCharacterStream(final String columnLabel, final Reader reader, final long length)\n
    updateNCharacterStream(final int columnIndex, final Reader x)\n
    updateNCharacterStream(final String columnLabel, final Reader reader)\n
    '''
def updateAsciiStream():
    '''returns None\n\n
    updateAsciiStream(final int columnIndex, final InputStream x, final long length)\n
    updateAsciiStream(final String columnLabel, final InputStream x, final long length)\n
    updateAsciiStream(final int columnIndex, final InputStream x)\n
    updateAsciiStream(final String columnLabel, final InputStream x)\n
    updateAsciiStream(final int col, final InputStream x, final int l)\n
    updateAsciiStream(final String col, final InputStream x, final int l)\n
    '''
def updateBinaryStream():
    '''returns None\n\n
    updateBinaryStream(final int columnIndex, final InputStream x, final long length)\n
    updateBinaryStream(final String columnLabel, final InputStream x, final long length)\n
    updateBinaryStream(final int columnIndex, final InputStream x)\n
    updateBinaryStream(final String columnLabel, final InputStream x)\n
    updateBinaryStream(final int c, final InputStream x, final int l)\n
    updateBinaryStream(final String c, final InputStream x, final int l)\n
    '''
def updateCharacterStream():
    '''returns None\n\n
    updateCharacterStream(final int columnIndex, final Reader x, final long length)\n
    updateCharacterStream(final String columnLabel, final Reader reader, final long length)\n
    updateCharacterStream(final int columnIndex, final Reader x)\n
    updateCharacterStream(final String columnLabel, final Reader reader)\n
    updateCharacterStream(final int c, final Reader x, final int l)\n
    updateCharacterStream(final String c, final Reader r, final int l)\n
    '''
def updateBlob():
    '''returns None\n\n
    updateBlob(final int columnIndex, final InputStream inputStream, final long length)\n
    updateBlob(final String columnLabel, final InputStream inputStream, final long length)\n
    updateBlob(final int columnIndex, final InputStream inputStream)\n
    updateBlob(final String columnLabel, final InputStream inputStream)\n
    updateBlob(final int col, final Blob x)\n
    updateBlob(final String col, final Blob x)\n
    '''
def updateClob():
    '''returns None\n\n
    updateClob(final int columnIndex, final Reader reader, final long length)\n
    updateClob(final String columnLabel, final Reader reader, final long length)\n
    updateClob(final int columnIndex, final Reader reader)\n
    updateClob(final String columnLabel, final Reader reader)\n
    updateClob(final int col, final Clob x)\n
    updateClob(final String col, final Clob x)\n
    '''
def getArray():
    '''returns Array\n\n
    getArray(final int i)\n
    getArray(final String col)\n
    '''
def getAsciiStream():
    '''returns InputStream\n\n
    getAsciiStream(final int col)\n
    getAsciiStream(final String col)\n
    getAsciiStream()\n
    '''
def getBigDecimal():
    '''returns BigDecimal\n\n
    getBigDecimal(final int col, final int s)\n
    getBigDecimal(final String col, final int s)\n
    '''
def getBlob():
    '''returns Blob\n\n
    getBlob(final int col)\n
    getBlob(final String col)\n
    '''
def getClob():
    '''returns Clob\n\n
    getClob(final int col)\n
    getClob(final String col)\n
    '''
def getObject():
    '''returns Object\n\n
    getObject(final int col, final Map map)\n
    getObject(final String col, final Map map)\n
    '''
def getRef():
    '''returns Ref\n\n
    getRef(final int i)\n
    getRef(final String col)\n
    '''
def getUnicodeStream():
    '''returns InputStream\n\n
    getUnicodeStream(final int col)\n
    getUnicodeStream(final String col)\n
    '''
def getURL():
    '''returns URL\n\n
    getURL(final int col)\n
    getURL(final String col)\n
    '''
def insertRow():
    '''returns None\n\n
    insertRow()\n
    '''
def moveToCurrentRow():
    '''returns None\n\n
    moveToCurrentRow()\n
    '''
def moveToInsertRow():
    '''returns None\n\n
    moveToInsertRow()\n
    '''
def last():
    '''returns boolean\n\n
    last()\n
    '''
def previous():
    '''returns boolean\n\n
    previous()\n
    '''
def relative():
    '''returns boolean\n\n
    relative(final int rows)\n
    '''
def absolute():
    '''returns boolean\n\n
    absolute(final int row)\n
    '''
def afterLast():
    '''returns None\n\n
    afterLast()\n
    '''
def beforeFirst():
    '''returns None\n\n
    beforeFirst()\n
    '''
def first():
    '''returns boolean\n\n
    first()\n
    '''
def cancelRowUpdates():
    '''returns None\n\n
    cancelRowUpdates()\n
    '''
def deleteRow():
    '''returns None\n\n
    deleteRow()\n
    '''
def updateArray():
    '''returns None\n\n
    updateArray(final int col, final Array x)\n
    updateArray(final String col, final Array x)\n
    '''
def updateBigDecimal():
    '''returns None\n\n
    updateBigDecimal(final int col, final BigDecimal x)\n
    updateBigDecimal(final String col, final BigDecimal x)\n
    '''
def updateBoolean():
    '''returns None\n\n
    updateBoolean(final int col, final boolean x)\n
    updateBoolean(final String col, final boolean x)\n
    '''
def updateByte():
    '''returns None\n\n
    updateByte(final int col, final byte x)\n
    updateByte(final String col, final byte x)\n
    '''
def updateBytes():
    '''returns None\n\n
    updateBytes(final int col, final byte[] x)\n
    updateBytes(final String col, final byte[] x)\n
    '''
def updateDate():
    '''returns None\n\n
    updateDate(final int col, final Date x)\n
    updateDate(final String col, final Date x)\n
    '''
def updateDouble():
    '''returns None\n\n
    updateDouble(final int col, final double x)\n
    updateDouble(final String col, final double x)\n
    '''
def updateFloat():
    '''returns None\n\n
    updateFloat(final int col, final float x)\n
    updateFloat(final String col, final float x)\n
    '''
def updateInt():
    '''returns None\n\n
    updateInt(final int col, final int x)\n
    updateInt(final String col, final int x)\n
    '''
def updateLong():
    '''returns None\n\n
    updateLong(final int col, final long x)\n
    updateLong(final String col, final long x)\n
    '''
def updateNull():
    '''returns None\n\n
    updateNull(final int col)\n
    updateNull(final String col)\n
    '''
def updateObject():
    '''returns None\n\n
    updateObject(final int c, final Object x)\n
    updateObject(final int c, final Object x, final int s)\n
    updateObject(final String col, final Object x)\n
    updateObject(final String c, final Object x, final int s)\n
    '''
def updateRef():
    '''returns None\n\n
    updateRef(final int col, final Ref x)\n
    updateRef(final String c, final Ref x)\n
    '''
def updateRow():
    '''returns None\n\n
    updateRow()\n
    '''
def updateShort():
    '''returns None\n\n
    updateShort(final int c, final short x)\n
    updateShort(final String c, final short x)\n
    '''
def updateString():
    '''returns None\n\n
    updateString(final int c, final String x)\n
    updateString(final String c, final String x)\n
    '''
def updateTime():
    '''returns None\n\n
    updateTime(final int c, final Time x)\n
    updateTime(final String c, final Time x)\n
    '''
def updateTimestamp():
    '''returns None\n\n
    updateTimestamp(final int c, final Timestamp x)\n
    updateTimestamp(final String c, final Timestamp x)\n
    '''
def refreshRow():
    '''returns None\n\n
    refreshRow()\n
    '''
def free():
    '''returns None\n\n
    free()\n
    '''
def getCharacterStream():
    '''returns Reader\n\n
    getCharacterStream()\n
    getCharacterStream(final long arg0, final long arg1)\n
    '''
def getSubString():
    '''returns String\n\n
    getSubString(final long position, final int length)\n
    '''
def length():
    '''returns long\n\n
    length()\n
    '''
def position():
    '''returns long\n\n
    position(final String arg0, final long arg1)\n
    position(final Clob arg0, final long arg1)\n
    '''
def setAsciiStream():
    '''returns OutputStream\n\n
    setAsciiStream(final long arg0)\n
    '''
def setCharacterStream():
    '''returns Writer\n\n
    setCharacterStream(final long arg0)\n
    '''
def setString():
    '''returns int\n\n
    setString(final long arg0, final String arg1)\n
    setString(final long arg0, final String arg1, final int arg2, final int arg3)\n
    '''
def truncate():
    '''returns None\n\n
    truncate(final long arg0)\n
    '''
