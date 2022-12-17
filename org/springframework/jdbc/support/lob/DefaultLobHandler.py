def ():
    '''returns DefaultLobHandler\n\n
    ()\n
    '''
def getBlobAsBytes():
    '''returns byte[]\n\n
    getBlobAsBytes(final ResultSet rs, final int columnIndex)\n
    '''
def getBlobAsBinaryStream():
    '''returns InputStream\n\n
    getBlobAsBinaryStream(final ResultSet rs, final int columnIndex)\n
    '''
def getClobAsString():
    '''returns String\n\n
    getClobAsString(final ResultSet rs, final int columnIndex)\n
    '''
def getClobAsAsciiStream():
    '''returns InputStream\n\n
    getClobAsAsciiStream(final ResultSet rs, final int columnIndex)\n
    '''
def getClobAsCharacterStream():
    '''returns Reader\n\n
    getClobAsCharacterStream(final ResultSet rs, final int columnIndex)\n
    '''
def getLobCreator():
    '''returns LobCreator\n\n
    getLobCreator()\n
    '''
def setBlobAsBytes():
    '''returns None\n\n
    setBlobAsBytes(final PreparedStatement ps, final int paramIndex, final byte[] content)\n
    '''
def setBlobAsBinaryStream():
    '''returns None\n\n
    setBlobAsBinaryStream(final PreparedStatement ps, final int paramIndex, final InputStream binaryStream, final int contentLength)\n
    '''
def setClobAsString():
    '''returns None\n\n
    setClobAsString(final PreparedStatement ps, final int paramIndex, final String content)\n
    '''
def setClobAsAsciiStream():
    '''returns None\n\n
    setClobAsAsciiStream(final PreparedStatement ps, final int paramIndex, final InputStream asciiStream, final int contentLength)\n
    '''
def setClobAsCharacterStream():
    '''returns None\n\n
    setClobAsCharacterStream(final PreparedStatement ps, final int paramIndex, final Reader characterStream, final int contentLength)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
