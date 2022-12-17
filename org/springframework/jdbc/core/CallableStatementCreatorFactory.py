def ():
    '''returns CallableStatementCreatorImpl\n\n
    (final String callString)\n
    (final String callString, final List declaredParameters)\n
    (final Map inParams)\n
    (final ParameterMapper inParamMapper)\n
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
def setNativeJdbcExtractor():
    '''returns None\n\n
    setNativeJdbcExtractor(final NativeJdbcExtractor nativeJdbcExtractor)\n
    '''
def newCallableStatementCreator():
    '''returns CallableStatementCreator\n\n
    newCallableStatementCreator(final Map inParams)\n
    newCallableStatementCreator(final ParameterMapper inParamMapper)\n
    '''
def createCallableStatement():
    '''returns CallableStatement\n\n
    createCallableStatement(final Connection con)\n
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
