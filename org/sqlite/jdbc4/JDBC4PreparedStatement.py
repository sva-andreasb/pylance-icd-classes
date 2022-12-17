def ():
    '''returns JDBC4PreparedStatement\n\n
    (final SQLiteConnection conn, final String sql)\n
    '''
def setRowId():
    '''returns None\n\n
    setRowId(final int parameterIndex, final RowId x)\n
    '''
def setNString():
    '''returns None\n\n
    setNString(final int parameterIndex, final String value)\n
    '''
def setNCharacterStream():
    '''returns None\n\n
    setNCharacterStream(final int parameterIndex, final Reader value, final long length)\n
    setNCharacterStream(final int parameterIndex, final Reader value)\n
    '''
def setNClob():
    '''returns None\n\n
    setNClob(final int parameterIndex, final NClob value)\n
    setNClob(final int parameterIndex, final Reader reader, final long length)\n
    setNClob(final int parameterIndex, final Reader reader)\n
    '''
def setClob():
    '''returns None\n\n
    setClob(final int parameterIndex, final Reader reader, final long length)\n
    setClob(final int parameterIndex, final Reader reader)\n
    '''
def setBlob():
    '''returns None\n\n
    setBlob(final int parameterIndex, final InputStream inputStream, final long length)\n
    setBlob(final int parameterIndex, final InputStream inputStream)\n
    '''
def setSQLXML():
    '''returns None\n\n
    setSQLXML(final int parameterIndex, final SQLXML xmlObject)\n
    '''
def setAsciiStream():
    '''returns None\n\n
    setAsciiStream(final int parameterIndex, final InputStream x, final long length)\n
    setAsciiStream(final int parameterIndex, final InputStream x)\n
    '''
def setBinaryStream():
    '''returns None\n\n
    setBinaryStream(final int parameterIndex, final InputStream x, final long length)\n
    setBinaryStream(final int parameterIndex, final InputStream x)\n
    '''
def setCharacterStream():
    '''returns None\n\n
    setCharacterStream(final int parameterIndex, final Reader reader, final long length)\n
    setCharacterStream(final int parameterIndex, final Reader reader)\n
    '''
