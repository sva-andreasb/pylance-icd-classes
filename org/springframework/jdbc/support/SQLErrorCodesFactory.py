SQL_ERROR_CODE_OVERRIDE_PATH = "String  \"sql-error-codes.xml\""
SQL_ERROR_CODE_DEFAULT_PATH = "String  \"org/springframework/jdbc/support/sql-error-codes.xml\""
def getErrorCodes():
    '''returns SQLErrorCodes\n\n
    getErrorCodes(final DataSource dataSource)\n
    getErrorCodes(final String dbName)\n
    '''
