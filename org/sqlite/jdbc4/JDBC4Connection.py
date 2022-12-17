def ():
    '''returns JDBC4Connection\n\n
    (final String url, final String fileName, final Properties prop)\n
    '''
def createStatement():
    '''returns Statement\n\n
    createStatement(final int rst, final int rsc, final int rsh)\n
    '''
def prepareStatement():
    '''returns PreparedStatement\n\n
    prepareStatement(final String sql, final int rst, final int rsc, final int rsh)\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
def isWrapperFor():
    '''returns boolean\n\n
    isWrapperFor(final Class<?> iface)\n
    '''
def createClob():
    '''returns Clob\n\n
    createClob()\n
    '''
def createBlob():
    '''returns Blob\n\n
    createBlob()\n
    '''
def createNClob():
    '''returns NClob\n\n
    createNClob()\n
    '''
def createSQLXML():
    '''returns SQLXML\n\n
    createSQLXML()\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid(final int timeout)\n
    '''
def setClientInfo():
    '''returns None\n\n
    setClientInfo(final String name, final String value)\n
    setClientInfo(final Properties properties)\n
    '''
def getClientInfo():
    '''returns Properties\n\n
    getClientInfo(final String name)\n
    getClientInfo()\n
    '''
def createArrayOf():
    '''returns Array\n\n
    createArrayOf(final String typeName, final Object[] elements)\n
    '''
