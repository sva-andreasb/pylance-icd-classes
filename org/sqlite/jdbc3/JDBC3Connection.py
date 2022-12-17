def getCatalog():
    '''returns String\n\n
    getCatalog()\n
    '''
def setCatalog():
    '''returns None\n\n
    setCatalog(final String catalog)\n
    '''
def getHoldability():
    '''returns int\n\n
    getHoldability()\n
    '''
def setHoldability():
    '''returns None\n\n
    setHoldability(final int h)\n
    '''
def setTypeMap():
    '''returns None\n\n
    setTypeMap(final Map map)\n
    '''
def isReadOnly():
    '''returns boolean\n\n
    isReadOnly()\n
    '''
def setReadOnly():
    '''returns None\n\n
    setReadOnly(final boolean ro)\n
    '''
def nativeSQL():
    '''returns String\n\n
    nativeSQL(final String sql)\n
    '''
def clearWarnings():
    '''returns None\n\n
    clearWarnings()\n
    '''
def getWarnings():
    '''returns SQLWarning\n\n
    getWarnings()\n
    '''
def createStatement():
    '''returns Statement\n\n
    createStatement()\n
    createStatement(final int rsType, final int rsConcurr)\n
    '''
def prepareCall():
    '''returns CallableStatement\n\n
    prepareCall(final String sql)\n
    prepareCall(final String sql, final int rst, final int rsc)\n
    prepareCall(final String sql, final int rst, final int rsc, final int rsh)\n
    '''
def prepareStatement():
    '''returns PreparedStatement\n\n
    prepareStatement(final String sql)\n
    prepareStatement(final String sql, final int autoC)\n
    prepareStatement(final String sql, final int[] colInds)\n
    prepareStatement(final String sql, final String[] colNames)\n
    prepareStatement(final String sql, final int rst, final int rsc)\n
    '''
def setSavepoint():
    '''returns Savepoint\n\n
    setSavepoint()\n
    setSavepoint(final String name)\n
    '''
def releaseSavepoint():
    '''returns None\n\n
    releaseSavepoint(final Savepoint savepoint)\n
    '''
def rollback():
    '''returns None\n\n
    rollback(final Savepoint savepoint)\n
    '''
def createStruct():
    '''returns Struct\n\n
    createStruct(final String t, final Object[] attr)\n
    '''
