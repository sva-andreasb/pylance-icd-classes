def getHoldability():
    '''returns int\n\n
    getHoldability()\n
    '''
def getNCharacterStream():
    '''returns Reader\n\n
    getNCharacterStream(final int columnIndex)\n
    getNCharacterStream(final String columnLabel)\n
    '''
def getNClob():
    '''returns NClob\n\n
    getNClob(final int columnIndex)\n
    getNClob(final String columnLabel)\n
    '''
def getNString():
    '''returns String\n\n
    getNString(final int columnIndex)\n
    getNString(final String columnLabel)\n
    '''
def getRowId():
    '''returns RowId\n\n
    getRowId(final int columnIndex)\n
    getRowId(final String columnLabel)\n
    '''
def getSQLXML():
    '''returns SQLXML\n\n
    getSQLXML(final int columnIndex)\n
    getSQLXML(final String columnLabel)\n
    '''
def updateAsciiStream():
    '''returns None\n\n
    updateAsciiStream(final int columnIndex, final InputStream x)\n
    updateAsciiStream(final String columnLabel, final InputStream x)\n
    updateAsciiStream(final int columnIndex, final InputStream x, final long length)\n
    updateAsciiStream(final String columnLabel, final InputStream x, final long length)\n
    updateAsciiStream(final int columnIndex, final InputStream x, final int length)\n
    updateAsciiStream(final String columnName, final InputStream x, final int length)\n
    '''
def updateBinaryStream():
    '''returns None\n\n
    updateBinaryStream(final int columnIndex, final InputStream x)\n
    updateBinaryStream(final String columnLabel, final InputStream x)\n
    updateBinaryStream(final int columnIndex, final InputStream x, final long length)\n
    updateBinaryStream(final String columnLabel, final InputStream x, final long length)\n
    updateBinaryStream(final int columnIndex, final InputStream x, final int length)\n
    updateBinaryStream(final String columnName, final InputStream x, final int length)\n
    '''
def updateBlob():
    '''returns None\n\n
    updateBlob(final int columnIndex, final InputStream inputStream)\n
    updateBlob(final String columnLabel, final InputStream inputStream)\n
    updateBlob(final int columnIndex, final InputStream inputStream, final long length)\n
    updateBlob(final String columnLabel, final InputStream inputStream, final long length)\n
    updateBlob(final int i, final Blob b)\n
    updateBlob(final String s, final Blob b)\n
    '''
def updateCharacterStream():
    '''returns None\n\n
    updateCharacterStream(final int columnIndex, final Reader x)\n
    updateCharacterStream(final String columnLabel, final Reader reader)\n
    updateCharacterStream(final int columnIndex, final Reader x, final long length)\n
    updateCharacterStream(final String columnLabel, final Reader reader, final long length)\n
    updateCharacterStream(final int columnIndex, final Reader x, final int length)\n
    updateCharacterStream(final String columnName, final Reader reader, final int length)\n
    '''
def updateClob():
    '''returns None\n\n
    updateClob(final int columnIndex, final Reader reader)\n
    updateClob(final String columnLabel, final Reader reader)\n
    updateClob(final int columnIndex, final Reader reader, final long length)\n
    updateClob(final String columnLabel, final Reader reader, final long length)\n
    updateClob(final int i, final Clob c)\n
    updateClob(final String s, final Clob c)\n
    '''
def updateNCharacterStream():
    '''returns None\n\n
    updateNCharacterStream(final int columnIndex, final Reader x)\n
    updateNCharacterStream(final String columnLabel, final Reader reader)\n
    updateNCharacterStream(final int columnIndex, final Reader x, final long length)\n
    updateNCharacterStream(final String columnLabel, final Reader reader, final long length)\n
    '''
def updateNClob():
    '''returns None\n\n
    updateNClob(final int columnIndex, final NClob nClob)\n
    updateNClob(final String columnLabel, final NClob nClob)\n
    updateNClob(final int columnIndex, final Reader reader)\n
    updateNClob(final String columnLabel, final Reader reader)\n
    updateNClob(final int columnIndex, final Reader reader, final long length)\n
    updateNClob(final String columnLabel, final Reader reader, final long length)\n
    '''
def updateNString():
    '''returns None\n\n
    updateNString(final int columnIndex, final String nString)\n
    updateNString(final String columnLabel, final String nString)\n
    '''
def updateRowId():
    '''returns None\n\n
    updateRowId(final int columnIndex, final RowId x)\n
    updateRowId(final String columnLabel, final RowId x)\n
    '''
def updateSQLXML():
    '''returns None\n\n
    updateSQLXML(final int columnIndex, final SQLXML xmlObject)\n
    updateSQLXML(final String columnLabel, final SQLXML xmlObject)\n
    '''
def isWrapperFor():
    '''returns boolean\n\n
    isWrapperFor(final Class<?> iface)\n
    '''
def getURL():
    '''returns URL\n\n
    getURL(final int i)\n
    getURL(final String s)\n
    '''
def updateArray():
    '''returns None\n\n
    updateArray(final int i, final Array array)\n
    updateArray(final String s, final Array array)\n
    '''
def updateRef():
    '''returns None\n\n
    updateRef(final int i, final Ref r)\n
    updateRef(final String s, final Ref r)\n
    '''
def getCharacterStream():
    '''returns Reader\n\n
    getCharacterStream(final int columnIndex)\n
    getCharacterStream(final String columnName)\n
    '''
def getBigDecimal():
    '''returns BigDecimal\n\n
    getBigDecimal(final int columnIndex)\n
    getBigDecimal(final String columnName)\n
    getBigDecimal(final int columnIndex, final int scale)\n
    getBigDecimal(final String columnName, final int scale)\n
    '''
def isBeforeFirst():
    '''returns boolean\n\n
    isBeforeFirst()\n
    '''
def isAfterLast():
    '''returns boolean\n\n
    isAfterLast()\n
    '''
def isFirst():
    '''returns boolean\n\n
    isFirst()\n
    '''
def isLast():
    '''returns boolean\n\n
    isLast()\n
    '''
def beforeFirst():
    '''returns None\n\n
    beforeFirst()\n
    '''
def afterLast():
    '''returns None\n\n
    afterLast()\n
    '''
def first():
    '''returns boolean\n\n
    first()\n
    '''
def last():
    '''returns boolean\n\n
    last()\n
    '''
def getRow():
    '''returns int\n\n
    getRow()\n
    '''
def absolute():
    '''returns boolean\n\n
    absolute(final int row)\n
    '''
def relative():
    '''returns boolean\n\n
    relative(final int rows)\n
    '''
def previous():
    '''returns boolean\n\n
    previous()\n
    '''
def setFetchDirection():
    '''returns None\n\n
    setFetchDirection(final int direction)\n
    '''
def getFetchDirection():
    '''returns int\n\n
    getFetchDirection()\n
    '''
def setFetchSize():
    '''returns None\n\n
    setFetchSize(final int rows)\n
    '''
def getFetchSize():
    '''returns int\n\n
    getFetchSize()\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
def getConcurrency():
    '''returns int\n\n
    getConcurrency()\n
    '''
def rowUpdated():
    '''returns boolean\n\n
    rowUpdated()\n
    '''
def rowInserted():
    '''returns boolean\n\n
    rowInserted()\n
    '''
def rowDeleted():
    '''returns boolean\n\n
    rowDeleted()\n
    '''
def updateNull():
    '''returns None\n\n
    updateNull(final int columnIndex)\n
    updateNull(final String columnName)\n
    '''
def updateBoolean():
    '''returns None\n\n
    updateBoolean(final int columnIndex, final boolean x)\n
    updateBoolean(final String columnName, final boolean x)\n
    '''
def updateByte():
    '''returns None\n\n
    updateByte(final int columnIndex, final byte x)\n
    updateByte(final String columnName, final byte x)\n
    '''
def updateShort():
    '''returns None\n\n
    updateShort(final int columnIndex, final short x)\n
    updateShort(final String columnName, final short x)\n
    '''
def updateInt():
    '''returns None\n\n
    updateInt(final int columnIndex, final int x)\n
    updateInt(final String columnName, final int x)\n
    '''
def updateLong():
    '''returns None\n\n
    updateLong(final int columnIndex, final long x)\n
    updateLong(final String columnName, final long x)\n
    '''
def updateFloat():
    '''returns None\n\n
    updateFloat(final int columnIndex, final float x)\n
    updateFloat(final String columnName, final float x)\n
    '''
def updateDouble():
    '''returns None\n\n
    updateDouble(final int columnIndex, final double x)\n
    updateDouble(final String columnName, final double x)\n
    '''
def updateBigDecimal():
    '''returns None\n\n
    updateBigDecimal(final int columnIndex, final BigDecimal x)\n
    updateBigDecimal(final String columnName, final BigDecimal x)\n
    '''
def updateString():
    '''returns None\n\n
    updateString(final int columnIndex, final String x)\n
    updateString(final String columnName, final String x)\n
    '''
def updateBytes():
    '''returns None\n\n
    updateBytes(final int columnIndex, final byte[] x)\n
    updateBytes(final String columnName, final byte[] x)\n
    '''
def updateDate():
    '''returns None\n\n
    updateDate(final int columnIndex, final Date x)\n
    updateDate(final String columnName, final Date x)\n
    '''
def updateTime():
    '''returns None\n\n
    updateTime(final int columnIndex, final Time x)\n
    updateTime(final String columnName, final Time x)\n
    '''
def updateTimestamp():
    '''returns None\n\n
    updateTimestamp(final int columnIndex, final Timestamp x)\n
    updateTimestamp(final String columnName, final Timestamp x)\n
    '''
def updateObject():
    '''returns None\n\n
    updateObject(final int columnIndex, final Object x, final int scale)\n
    updateObject(final int columnIndex, final Object x)\n
    updateObject(final String columnName, final Object x, final int scale)\n
    updateObject(final String columnName, final Object x)\n
    '''
def insertRow():
    '''returns None\n\n
    insertRow()\n
    '''
def updateRow():
    '''returns None\n\n
    updateRow()\n
    '''
def deleteRow():
    '''returns None\n\n
    deleteRow()\n
    '''
def refreshRow():
    '''returns None\n\n
    refreshRow()\n
    '''
def cancelRowUpdates():
    '''returns None\n\n
    cancelRowUpdates()\n
    '''
def moveToInsertRow():
    '''returns None\n\n
    moveToInsertRow()\n
    '''
def moveToCurrentRow():
    '''returns None\n\n
    moveToCurrentRow()\n
    '''
def getStatement():
    '''returns Statement\n\n
    getStatement()\n
    '''
def getObject():
    '''returns Object\n\n
    getObject(final int i, final Map map)\n
    getObject(final String colName, final Map map)\n
    getObject(final int columnIndex)\n
    getObject(final String columnName)\n
    '''
def getRef():
    '''returns Ref\n\n
    getRef(final int i)\n
    getRef(final String colName)\n
    '''
def getBlob():
    '''returns Blob\n\n
    getBlob(final int i)\n
    getBlob(final String colName)\n
    '''
def getClob():
    '''returns Clob\n\n
    getClob(final int i)\n
    getClob(final String colName)\n
    '''
def getArray():
    '''returns Array\n\n
    getArray(final int i)\n
    getArray(final String colName)\n
    '''
def getDate():
    '''returns Date\n\n
    getDate(final int columnIndex, final Calendar cal)\n
    getDate(final String columnName, final Calendar cal)\n
    getDate(final int columnIndex)\n
    getDate(final String columnName)\n
    '''
def getTime():
    '''returns Time\n\n
    getTime(final int columnIndex, final Calendar cal)\n
    getTime(final String columnName, final Calendar cal)\n
    getTime(final int columnIndex)\n
    getTime(final String columnName)\n
    '''
def getTimestamp():
    '''returns Timestamp\n\n
    getTimestamp(final int columnIndex, final Calendar cal)\n
    getTimestamp(final String columnName, final Calendar cal)\n
    getTimestamp(final int columnIndex)\n
    getTimestamp(final String columnName)\n
    '''
def next():
    '''returns boolean\n\n
    next()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def reallyClose():
    '''returns None\n\n
    reallyClose()\n
    '''
def wasNull():
    '''returns boolean\n\n
    wasNull()\n
    '''
def getString():
    '''returns String\n\n
    getString(final int columnIndex)\n
    getString(final String columnName)\n
    '''
def getBoolean():
    '''returns boolean\n\n
    getBoolean(final int columnIndex)\n
    getBoolean(final String columnName)\n
    '''
def getByte():
    '''returns byte\n\n
    getByte(final int columnIndex)\n
    getByte(final String columnName)\n
    '''
def getShort():
    '''returns short\n\n
    getShort(final int columnIndex)\n
    getShort(final String columnName)\n
    '''
def getInt():
    '''returns int\n\n
    getInt(final int columnIndex)\n
    getInt(final String columnName)\n
    '''
def getLong():
    '''returns long\n\n
    getLong(final int columnIndex)\n
    getLong(final String columnName)\n
    '''
def getFloat():
    '''returns float\n\n
    getFloat(final int columnIndex)\n
    getFloat(final String columnName)\n
    '''
def getDouble():
    '''returns double\n\n
    getDouble(final int columnIndex)\n
    getDouble(final String columnName)\n
    '''
def getBytes():
    '''returns byte[]\n\n
    getBytes(final int columnIndex)\n
    getBytes(final String columnName)\n
    '''
def getAsciiStream():
    '''returns InputStream\n\n
    getAsciiStream(final int columnIndex)\n
    getAsciiStream(final String columnName)\n
    '''
def getUnicodeStream():
    '''returns InputStream\n\n
    getUnicodeStream(final int columnIndex)\n
    getUnicodeStream(final String columnName)\n
    '''
def getBinaryStream():
    '''returns InputStream\n\n
    getBinaryStream(final int columnIndex)\n
    getBinaryStream(final String columnName)\n
    '''
def getWarnings():
    '''returns SQLWarning\n\n
    getWarnings()\n
    '''
def clearWarnings():
    '''returns None\n\n
    clearWarnings()\n
    '''
def getCursorName():
    '''returns String\n\n
    getCursorName()\n
    '''
def getMetaData():
    '''returns ResultSetMetaData\n\n
    getMetaData()\n
    '''
def findColumn():
    '''returns int\n\n
    findColumn(final String columnName)\n
    '''
def translateException():
    '''returns SQLException\n\n
    translateException(final SQLException e)\n
    '''
