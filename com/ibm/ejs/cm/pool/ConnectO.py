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
    '''
def prepareStatement():
    '''returns PreparedStatement\n\n
    prepareStatement(final String s, final int x, final int y, final int z)\n
    prepareStatement(final String s, final int x)\n
    prepareStatement(final String s, final int[] x)\n
    prepareStatement(final String s, final String[] strs)\n
    '''
def prepareCall():
    '''returns CallableStatement\n\n
    prepareCall(final String s, final int x, final int y, final int z)\n
    '''
def setCurrentSQLID():
    '''returns None\n\n
    setCurrentSQLID(final String currentSQLID)\n
    '''
def supportsRRSTransactional():
    '''returns boolean\n\n
    supportsRRSTransactional()\n
    '''
def getRefCount():
    '''returns int\n\n
    getRefCount()\n
    '''
def run():
    '''returns Object\n\n
    run()\n
    '''
def afterCompletion():
    '''returns None\n\n
    afterCompletion(final int status)\n
    '''
def unilateralCommit():
    '''returns None\n\n
    unilateralCommit()\n
    '''
def validate():
    '''returns boolean\n\n
    validate()\n
    '''
def setMaybeStale():
    '''returns None\n\n
    setMaybeStale(final boolean value)\n
    '''
def getResourceName():
    '''returns String\n\n
    getResourceName()\n
    '''
