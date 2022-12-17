def toString():
    '''returns String\n\n
    toString()\n
    '''
def getSensitivityClassification():
    '''returns SensitivityClassification\n\n
    getSensitivityClassification()\n
    '''
def isWrapperFor():
    '''returns boolean\n\n
    isWrapperFor(final Class<?> iface)\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def findColumn():
    '''returns int\n\n
    findColumn(final String columnName)\n
    '''
def clearWarnings():
    '''returns None\n\n
    clearWarnings()\n
    '''
def relative():
    '''returns boolean\n\n
    relative(final int rows)\n
    '''
def next():
    '''returns boolean\n\n
    next()\n
    '''
def wasNull():
    '''returns boolean\n\n
    wasNull()\n
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
def previous():
    '''returns boolean\n\n
    previous()\n
    '''
def getWarnings():
    '''returns SQLWarning\n\n
    getWarnings()\n
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
def getAsciiStream():
    '''returns InputStream\n\n
    getAsciiStream(final int columnIndex)\n
    getAsciiStream(final String columnName)\n
    '''
def getBigDecimal():
    '''returns BigDecimal\n\n
    getBigDecimal(final int columnIndex, final int scale)\n
    getBigDecimal(final String columnName, final int scale)\n
    getBigDecimal(final int columnIndex)\n
    getBigDecimal(final String columnName)\n
    '''
def getBinaryStream():
    '''returns InputStream\n\n
    getBinaryStream(final int columnIndex)\n
    getBinaryStream(final String columnName)\n
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
def getBytes():
    '''returns byte[]\n\n
    getBytes(final int columnIndex)\n
    getBytes(final String columnName)\n
    '''
def getDate():
    '''returns Date\n\n
    getDate(final int columnIndex)\n
    getDate(final String columnName)\n
    getDate(final int columnIndex, final Calendar cal)\n
    getDate(final String colName, final Calendar cal)\n
    '''
def getDouble():
    '''returns double\n\n
    getDouble(final int columnIndex)\n
    getDouble(final String columnName)\n
    '''
def getFloat():
    '''returns float\n\n
    getFloat(final int columnIndex)\n
    getFloat(final String columnName)\n
    '''
def getGeometry():
    '''returns Geometry\n\n
    getGeometry(final int columnIndex)\n
    getGeometry(final String columnName)\n
    '''
def getGeography():
    '''returns Geography\n\n
    getGeography(final int columnIndex)\n
    getGeography(final String columnName)\n
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
def getMetaData():
    '''returns ResultSetMetaData\n\n
    getMetaData()\n
    '''
def getObject():
    '''returns Object\n\n
    getObject(final int columnIndex)\n
    getObject(final String columnName)\n
    getObject(final int i, final Map<String, Class<?>> map)\n
    getObject(final String colName, final Map<String, Class<?>> map)\n
    '''
def getShort():
    '''returns short\n\n
    getShort(final int columnIndex)\n
    getShort(final String columnName)\n
    '''
def getString():
    '''returns String\n\n
    getString(final int columnIndex)\n
    getString(final String columnName)\n
    '''
def getNString():
    '''returns String\n\n
    getNString(final int columnIndex)\n
    getNString(final String columnLabel)\n
    '''
def getUniqueIdentifier():
    '''returns String\n\n
    getUniqueIdentifier(final int columnIndex)\n
    getUniqueIdentifier(final String columnLabel)\n
    '''
def getTime():
    '''returns Time\n\n
    getTime(final int columnIndex)\n
    getTime(final String columnName)\n
    getTime(final int columnIndex, final Calendar cal)\n
    getTime(final String colName, final Calendar cal)\n
    '''
def getTimestamp():
    '''returns Timestamp\n\n
    getTimestamp(final int columnIndex)\n
    getTimestamp(final String columnName)\n
    getTimestamp(final int columnIndex, final Calendar cal)\n
    getTimestamp(final String colName, final Calendar cal)\n
    '''
def getDateTime():
    '''returns Timestamp\n\n
    getDateTime(final int columnIndex)\n
    getDateTime(final String columnName)\n
    getDateTime(final int columnIndex, final Calendar cal)\n
    getDateTime(final String colName, final Calendar cal)\n
    '''
def getSmallDateTime():
    '''returns Timestamp\n\n
    getSmallDateTime(final int columnIndex)\n
    getSmallDateTime(final String columnName)\n
    getSmallDateTime(final int columnIndex, final Calendar cal)\n
    getSmallDateTime(final String colName, final Calendar cal)\n
    '''
def getDateTimeOffset():
    '''returns DateTimeOffset\n\n
    getDateTimeOffset(final int columnIndex)\n
    getDateTimeOffset(final String columnName)\n
    '''
def getUnicodeStream():
    '''returns InputStream\n\n
    getUnicodeStream(final int columnIndex)\n
    getUnicodeStream(final String columnName)\n
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
    getClob(final int columnIndex)\n
    getClob(final String colName)\n
    '''
def getNClob():
    '''returns NClob\n\n
    getNClob(final int columnIndex)\n
    getNClob(final String columnLabel)\n
    '''
def getArray():
    '''returns Array\n\n
    getArray(final int i)\n
    getArray(final String colName)\n
    '''
def getCursorName():
    '''returns String\n\n
    getCursorName()\n
    '''
def getCharacterStream():
    '''returns Reader\n\n
    getCharacterStream(final int columnIndex)\n
    getCharacterStream(final String columnName)\n
    '''
def getNCharacterStream():
    '''returns Reader\n\n
    getNCharacterStream(final int columnIndex)\n
    getNCharacterStream(final String columnLabel)\n
    '''
def getMoney():
    '''returns BigDecimal\n\n
    getMoney(final int columnIndex)\n
    getMoney(final String columnName)\n
    '''
def getSmallMoney():
    '''returns BigDecimal\n\n
    getSmallMoney(final int columnIndex)\n
    getSmallMoney(final String columnName)\n
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
    updateNull(final int index)\n
    updateNull(final String columnName)\n
    '''
def updateBoolean():
    '''returns None\n\n
    updateBoolean(final int index, final boolean x)\n
    updateBoolean(final int index, final boolean x, final boolean forceEncrypt)\n
    updateBoolean(final String columnName, final boolean x)\n
    updateBoolean(final String columnName, final boolean x, final boolean forceEncrypt)\n
    '''
def updateByte():
    '''returns None\n\n
    updateByte(final int index, final byte x)\n
    updateByte(final int index, final byte x, final boolean forceEncrypt)\n
    updateByte(final String columnName, final byte x)\n
    updateByte(final String columnName, final byte x, final boolean forceEncrypt)\n
    '''
def updateShort():
    '''returns None\n\n
    updateShort(final int index, final short x)\n
    updateShort(final int index, final short x, final boolean forceEncrypt)\n
    updateShort(final String columnName, final short x)\n
    updateShort(final String columnName, final short x, final boolean forceEncrypt)\n
    '''
def updateInt():
    '''returns None\n\n
    updateInt(final int index, final int x)\n
    updateInt(final int index, final int x, final boolean forceEncrypt)\n
    updateInt(final String columnName, final int x)\n
    updateInt(final String columnName, final int x, final boolean forceEncrypt)\n
    '''
def updateLong():
    '''returns None\n\n
    updateLong(final int index, final long x)\n
    updateLong(final int index, final long x, final boolean forceEncrypt)\n
    updateLong(final String columnName, final long x)\n
    updateLong(final String columnName, final long x, final boolean forceEncrypt)\n
    '''
def updateFloat():
    '''returns None\n\n
    updateFloat(final int index, final float x)\n
    updateFloat(final int index, final float x, final boolean forceEncrypt)\n
    updateFloat(final String columnName, final float x)\n
    updateFloat(final String columnName, final float x, final boolean forceEncrypt)\n
    '''
def updateDouble():
    '''returns None\n\n
    updateDouble(final int index, final double x)\n
    updateDouble(final int index, final double x, final boolean forceEncrypt)\n
    updateDouble(final String columnName, final double x)\n
    updateDouble(final String columnName, final double x, final boolean forceEncrypt)\n
    '''
def updateMoney():
    '''returns None\n\n
    updateMoney(final int index, final BigDecimal x)\n
    updateMoney(final int index, final BigDecimal x, final boolean forceEncrypt)\n
    updateMoney(final String columnName, final BigDecimal x)\n
    updateMoney(final String columnName, final BigDecimal x, final boolean forceEncrypt)\n
    '''
def updateSmallMoney():
    '''returns None\n\n
    updateSmallMoney(final int index, final BigDecimal x)\n
    updateSmallMoney(final int index, final BigDecimal x, final boolean forceEncrypt)\n
    updateSmallMoney(final String columnName, final BigDecimal x)\n
    updateSmallMoney(final String columnName, final BigDecimal x, final boolean forceEncrypt)\n
    '''
def updateBigDecimal():
    '''returns None\n\n
    updateBigDecimal(final int index, final BigDecimal x)\n
    updateBigDecimal(final int index, final BigDecimal x, final Integer precision, final Integer scale)\n
    updateBigDecimal(final int index, final BigDecimal x, final Integer precision, final Integer scale, final boolean forceEncrypt)\n
    updateBigDecimal(final String columnName, final BigDecimal x)\n
    updateBigDecimal(final String columnName, final BigDecimal x, final boolean forceEncrypt)\n
    updateBigDecimal(final String columnName, final BigDecimal x, final Integer precision, final Integer scale)\n
    updateBigDecimal(final String columnName, final BigDecimal x, final Integer precision, final Integer scale, final boolean forceEncrypt)\n
    '''
def updateString():
    '''returns None\n\n
    updateString(final int columnIndex, final String stringValue)\n
    updateString(final int columnIndex, final String stringValue, final boolean forceEncrypt)\n
    updateString(final String columnName, final String x)\n
    updateString(final String columnName, final String x, final boolean forceEncrypt)\n
    '''
def updateNString():
    '''returns None\n\n
    updateNString(final int columnIndex, final String nString)\n
    updateNString(final int columnIndex, final String nString, final boolean forceEncrypt)\n
    updateNString(final String columnLabel, final String nString)\n
    updateNString(final String columnLabel, final String nString, final boolean forceEncrypt)\n
    '''
def updateBytes():
    '''returns None\n\n
    updateBytes(final int index, final byte[] x)\n
    updateBytes(final int index, final byte[] x, final boolean forceEncrypt)\n
    updateBytes(final String columnName, final byte[] x)\n
    updateBytes(final String columnName, final byte[] x, final boolean forceEncrypt)\n
    '''
def updateDate():
    '''returns None\n\n
    updateDate(final int index, final Date x)\n
    updateDate(final int index, final Date x, final boolean forceEncrypt)\n
    updateDate(final String columnName, final Date x)\n
    updateDate(final String columnName, final Date x, final boolean forceEncrypt)\n
    '''
def updateTime():
    '''returns None\n\n
    updateTime(final int index, final Time x)\n
    updateTime(final int index, final Time x, final Integer scale)\n
    updateTime(final int index, final Time x, final Integer scale, final boolean forceEncrypt)\n
    updateTime(final String columnName, final Time x)\n
    updateTime(final String columnName, final Time x, final int scale)\n
    updateTime(final String columnName, final Time x, final int scale, final boolean forceEncrypt)\n
    '''
def updateTimestamp():
    '''returns None\n\n
    updateTimestamp(final int index, final Timestamp x)\n
    updateTimestamp(final int index, final Timestamp x, final int scale)\n
    updateTimestamp(final int index, final Timestamp x, final int scale, final boolean forceEncrypt)\n
    updateTimestamp(final String columnName, final Timestamp x)\n
    updateTimestamp(final String columnName, final Timestamp x, final int scale)\n
    updateTimestamp(final String columnName, final Timestamp x, final int scale, final boolean forceEncrypt)\n
    '''
def updateDateTime():
    '''returns None\n\n
    updateDateTime(final int index, final Timestamp x)\n
    updateDateTime(final int index, final Timestamp x, final Integer scale)\n
    updateDateTime(final int index, final Timestamp x, final Integer scale, final boolean forceEncrypt)\n
    updateDateTime(final String columnName, final Timestamp x)\n
    updateDateTime(final String columnName, final Timestamp x, final int scale)\n
    updateDateTime(final String columnName, final Timestamp x, final int scale, final boolean forceEncrypt)\n
    '''
def updateSmallDateTime():
    '''returns None\n\n
    updateSmallDateTime(final int index, final Timestamp x)\n
    updateSmallDateTime(final int index, final Timestamp x, final Integer scale)\n
    updateSmallDateTime(final int index, final Timestamp x, final Integer scale, final boolean forceEncrypt)\n
    updateSmallDateTime(final String columnName, final Timestamp x)\n
    updateSmallDateTime(final String columnName, final Timestamp x, final int scale)\n
    updateSmallDateTime(final String columnName, final Timestamp x, final int scale, final boolean forceEncrypt)\n
    '''
def updateDateTimeOffset():
    '''returns None\n\n
    updateDateTimeOffset(final int index, final DateTimeOffset x)\n
    updateDateTimeOffset(final int index, final DateTimeOffset x, final Integer scale)\n
    updateDateTimeOffset(final int index, final DateTimeOffset x, final Integer scale, final boolean forceEncrypt)\n
    updateDateTimeOffset(final String columnName, final DateTimeOffset x)\n
    updateDateTimeOffset(final String columnName, final DateTimeOffset x, final int scale)\n
    updateDateTimeOffset(final String columnName, final DateTimeOffset x, final int scale, final boolean forceEncrypt)\n
    '''
def updateUniqueIdentifier():
    '''returns None\n\n
    updateUniqueIdentifier(final int index, final String x)\n
    updateUniqueIdentifier(final int index, final String x, final boolean forceEncrypt)\n
    updateUniqueIdentifier(final String columnName, final String x)\n
    updateUniqueIdentifier(final String columnName, final String x, final boolean forceEncrypt)\n
    '''
def updateAsciiStream():
    '''returns None\n\n
    updateAsciiStream(final int columnIndex, final InputStream x)\n
    updateAsciiStream(final int index, final InputStream x, final int length)\n
    updateAsciiStream(final int columnIndex, final InputStream x, final long length)\n
    updateAsciiStream(final String columnLabel, final InputStream x)\n
    updateAsciiStream(final String columnName, final InputStream x, final int length)\n
    updateAsciiStream(final String columnName, final InputStream streamValue, final long length)\n
    '''
def updateBinaryStream():
    '''returns None\n\n
    updateBinaryStream(final int columnIndex, final InputStream x)\n
    updateBinaryStream(final int columnIndex, final InputStream streamValue, final int length)\n
    updateBinaryStream(final int columnIndex, final InputStream x, final long length)\n
    updateBinaryStream(final String columnLabel, final InputStream x)\n
    updateBinaryStream(final String columnName, final InputStream streamValue, final int length)\n
    updateBinaryStream(final String columnLabel, final InputStream x, final long length)\n
    '''
def updateCharacterStream():
    '''returns None\n\n
    updateCharacterStream(final int columnIndex, final Reader x)\n
    updateCharacterStream(final int columnIndex, final Reader readerValue, final int length)\n
    updateCharacterStream(final int columnIndex, final Reader x, final long length)\n
    updateCharacterStream(final String columnLabel, final Reader reader)\n
    updateCharacterStream(final String columnName, final Reader readerValue, final int length)\n
    updateCharacterStream(final String columnLabel, final Reader reader, final long length)\n
    '''
def updateNCharacterStream():
    '''returns None\n\n
    updateNCharacterStream(final int columnIndex, final Reader x)\n
    updateNCharacterStream(final int columnIndex, final Reader x, final long length)\n
    updateNCharacterStream(final String columnLabel, final Reader reader)\n
    updateNCharacterStream(final String columnLabel, final Reader reader, final long length)\n
    '''
def updateObject():
    '''returns None\n\n
    updateObject(final int index, final Object obj)\n
    updateObject(final int index, final Object x, final int scale)\n
    updateObject(final int index, final Object x, final int precision, final int scale)\n
    updateObject(final int index, final Object x, final int precision, final int scale, final boolean forceEncrypt)\n
    updateObject(final String columnName, final Object x, final int scale)\n
    updateObject(final String columnName, final Object x, final int precision, final int scale)\n
    updateObject(final String columnName, final Object x, final int precision, final int scale, final boolean forceEncrypt)\n
    updateObject(final String columnName, final Object x)\n
    updateObject(final int index, final Object obj, final SQLType targetSqlType)\n
    updateObject(final int index, final Object obj, final SQLType targetSqlType, final int scale)\n
    updateObject(final int index, final Object obj, final SQLType targetSqlType, final int scale, final boolean forceEncrypt)\n
    updateObject(final String columnName, final Object obj, final SQLType targetSqlType, final int scale)\n
    updateObject(final String columnName, final Object obj, final SQLType targetSqlType, final int scale, final boolean forceEncrypt)\n
    updateObject(final String columnName, final Object obj, final SQLType targetSqlType)\n
    '''
def updateRowId():
    '''returns None\n\n
    updateRowId(final int columnIndex, final RowId x)\n
    updateRowId(final String columnLabel, final RowId x)\n
    '''
def updateSQLXML():
    '''returns None\n\n
    updateSQLXML(final int columnIndex, final SQLXML xmlObject)\n
    updateSQLXML(final String columnLabel, final SQLXML x)\n
    '''
def getHoldability():
    '''returns int\n\n
    getHoldability()\n
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
def updateClob():
    '''returns None\n\n
    updateClob(final int columnIndex, final Clob clobValue)\n
    updateClob(final int columnIndex, final Reader reader)\n
    updateClob(final int columnIndex, final Reader reader, final long length)\n
    updateClob(final String columnName, final Clob clobValue)\n
    updateClob(final String columnLabel, final Reader reader)\n
    updateClob(final String columnLabel, final Reader reader, final long length)\n
    '''
def updateNClob():
    '''returns None\n\n
    updateNClob(final int columnIndex, final NClob nClob)\n
    updateNClob(final int columnIndex, final Reader reader)\n
    updateNClob(final int columnIndex, final Reader reader, final long length)\n
    updateNClob(final String columnLabel, final NClob nClob)\n
    updateNClob(final String columnLabel, final Reader reader)\n
    updateNClob(final String columnLabel, final Reader reader, final long length)\n
    '''
def updateBlob():
    '''returns None\n\n
    updateBlob(final int columnIndex, final Blob blobValue)\n
    updateBlob(final int columnIndex, final InputStream inputStream)\n
    updateBlob(final int columnIndex, final InputStream inputStream, final long length)\n
    updateBlob(final String columnName, final Blob blobValue)\n
    updateBlob(final String columnLabel, final InputStream inputStream)\n
    updateBlob(final String columnLabel, final InputStream inputStream, final long length)\n
    '''
def updateArray():
    '''returns None\n\n
    updateArray(final int columnIndex, final Array x)\n
    updateArray(final String columnName, final Array x)\n
    '''
def updateRef():
    '''returns None\n\n
    updateRef(final int columnIndex, final Ref x)\n
    updateRef(final String columnName, final Ref x)\n
    '''
def getURL():
    '''returns URL\n\n
    getURL(final int columnIndex)\n
    getURL(final String sColumn)\n
    '''
