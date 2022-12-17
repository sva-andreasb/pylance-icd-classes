def ():
    '''returns PreparedStatementCreatorImpl\n\n
    (final String sql)\n
    (final String sql, final int[] types)\n
    (final String sql, final List declaredParameters)\n
    (final List parameters)\n
    '''
def addParameter():
    '''returns None\n\n
    addParameter(final SqlParameter param)\n
    '''
def setResultSetType():
    '''returns None\n\n
    setResultSetType(final int resultSetType)\n
    '''
def setUpdatableResults():
    '''returns None\n\n
    setUpdatableResults(final boolean updatableResults)\n
    '''
def setReturnGeneratedKeys():
    '''returns None\n\n
    setReturnGeneratedKeys(final boolean returnGeneratedKeys)\n
    '''
def setGeneratedKeysColumnNames():
    '''returns None\n\n
    setGeneratedKeysColumnNames(final String[] names)\n
    '''
def setNativeJdbcExtractor():
    '''returns None\n\n
    setNativeJdbcExtractor(final NativeJdbcExtractor nativeJdbcExtractor)\n
    '''
def newPreparedStatementCreator():
    '''returns PreparedStatementCreator\n\n
    newPreparedStatementCreator(final Object[] params)\n
    newPreparedStatementCreator(final List params)\n
    '''
def newPreparedStatementSetter():
    '''returns PreparedStatementSetter\n\n
    newPreparedStatementSetter(final Object[] params)\n
    newPreparedStatementSetter(final List params)\n
    '''
def createPreparedStatement():
    '''returns PreparedStatement\n\n
    createPreparedStatement(final Connection con)\n
    '''
def setValues():
    '''returns None\n\n
    setValues(final PreparedStatement ps)\n
    '''
def getSql():
    '''returns String\n\n
    getSql()\n
    '''
def cleanupParameters():
    '''returns None\n\n
    cleanupParameters()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
