def ():
    '''returns SqlOutParameter\n\n
    (final String name, final int sqlType)\n
    (final String name, final int sqlType, final String typeName)\n
    (final String name, final int sqlType, final String typeName, final SqlReturnType sqlReturnType)\n
    (final String name, final int sqlType, final ResultSetExtractor rse)\n
    (final String name, final int sqlType, final RowCallbackHandler rch)\n
    (final String name, final int sqlType, final RowMapper rm)\n
    (final String name, final int sqlType, final RowMapper rm, final int rowsExpected)\n
    '''
def isReturnTypeSupported():
    '''returns boolean\n\n
    isReturnTypeSupported()\n
    '''
def getSqlReturnType():
    '''returns SqlReturnType\n\n
    getSqlReturnType()\n
    '''
