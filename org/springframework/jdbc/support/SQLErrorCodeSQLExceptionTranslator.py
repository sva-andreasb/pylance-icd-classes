def ():
    '''returns SQLErrorCodeSQLExceptionTranslator\n\n
    ()\n
    (final DataSource dataSource)\n
    (final String dbName)\n
    (final SQLErrorCodes sec)\n
    '''
def setDataSource():
    '''returns None\n\n
    setDataSource(final DataSource dataSource)\n
    '''
def setDatabaseProductName():
    '''returns None\n\n
    setDatabaseProductName(final String dbName)\n
    '''
def setSqlErrorCodes():
    '''returns None\n\n
    setSqlErrorCodes(final SQLErrorCodes sec)\n
    '''
def getSqlErrorCodes():
    '''returns SQLErrorCodes\n\n
    getSqlErrorCodes()\n
    '''
def setFallbackTranslator():
    '''returns None\n\n
    setFallbackTranslator(final SQLExceptionTranslator fallback)\n
    '''
def getFallbackTranslator():
    '''returns SQLExceptionTranslator\n\n
    getFallbackTranslator()\n
    '''
def translate():
    '''returns DataAccessException\n\n
    translate(String task, String sql, final SQLException sqlEx)\n
    '''
