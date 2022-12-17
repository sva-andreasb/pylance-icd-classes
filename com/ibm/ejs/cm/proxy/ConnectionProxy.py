def createArrayOf():
    '''returns Array\n\n
    createArrayOf(final String typeName, final Object[] elements)\n
    '''
def createBlob():
    '''returns Blob\n\n
    createBlob()\n
    '''
def createClob():
    '''returns Clob\n\n
    createClob()\n
    '''
def createNClob():
    '''returns NClob\n\n
    createNClob()\n
    '''
def createSQLXML():
    '''returns SQLXML\n\n
    createSQLXML()\n
    '''
def createStruct():
    '''returns Struct\n\n
    createStruct(final String typeName, final Object[] attributes)\n
    '''
def getClientInfo():
    '''returns String\n\n
    getClientInfo()\n
    getClientInfo(final String name)\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid(final int timeout)\n
    '''
def setClientInfo():
    '''returns None\n\n
    setClientInfo(final Properties properties)\n
    setClientInfo(final String name, final String value)\n
    '''
def isWrapperFor():
    '''returns boolean\n\n
    isWrapperFor(final Class<?> iface)\n
    '''
def setHoldability():
    '''returns None\n\n
    setHoldability(final int h)\n
    '''
def getHoldability():
    '''returns int\n\n
    getHoldability()\n
    '''
def setSavepoint():
    '''returns Savepoint\n\n
    setSavepoint()\n
    setSavepoint(final String s)\n
    '''
def rollback():
    '''returns None\n\n
    rollback(final Savepoint sp)\n
    '''
def releaseSavepoint():
    '''returns None\n\n
    releaseSavepoint(final Savepoint sp)\n
    '''
def createStatement():
    '''returns Statement\n\n
    createStatement(final int x, final int y, final int z)\n
    createStatement(final int type, final int concurrency)\n
    createStatement()\n
    '''
def prepareStatement():
    '''returns PreparedStatement\n\n
    prepareStatement(final String s, final int x, final int y, final int z)\n
    prepareStatement(final String s, final int x)\n
    prepareStatement(final String s, final int[] x)\n
    prepareStatement(final String s, final String[] strs)\n
    prepareStatement(final String sql, final int type, final int concurrency)\n
    prepareStatement(final String sql)\n
    '''
def prepareCall():
    '''returns CallableStatement\n\n
    prepareCall(final String s, final int x, final int y, final int z)\n
    prepareCall(final String sql, final int type, final int concurrency)\n
    prepareCall(final String sql)\n
    '''
def ():
    '''returns ConnectionProxy\n\n
    (final ConnectO connection)\n
    '''
def connectionEnlisted():
    '''returns None\n\n
    connectionEnlisted(final ConnectO c, final Object coord)\n
    '''
def connectionDestroyed():
    '''returns None\n\n
    connectionDestroyed(final ConnectO c)\n
    '''
def setDestroyed():
    '''returns None\n\n
    setDestroyed(final ConnectO c)\n
    '''
def connectionIdleTimeout():
    '''returns boolean\n\n
    connectionIdleTimeout(final ConnectO c)\n
    '''
def connectionAgedTimeout():
    '''returns boolean\n\n
    connectionAgedTimeout(final ConnectO c)\n
    '''
def connectionTxComplete():
    '''returns None\n\n
    connectionTxComplete(final ConnectO c, final int status, final Object tx)\n
    '''
def connectionOrphaned():
    '''returns None\n\n
    connectionOrphaned(final ConnectO c)\n
    '''
def getPortabilityLayer():
    '''returns PortabilityLayerExt\n\n
    getPortabilityLayer()\n
    '''
def translateException():
    '''returns SQLException\n\n
    translateException(final SQLException e)\n
    '''
def getColumnTypeSpec():
    '''returns String\n\n
    getColumnTypeSpec(final int type)\n
    '''
def addRowLockHint():
    '''returns String\n\n
    addRowLockHint(final String sql)\n
    '''
def getPhysicalConnection():
    '''returns Connection\n\n
    getPhysicalConnection()\n
    '''
def unilateralCommit():
    '''returns None\n\n
    unilateralCommit()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
