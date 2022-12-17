def ():
    '''returns ResultSetSupportingSqlParameter\n\n
    (final String name, final int sqlType)\n
    (final String name, final int sqlType, final String typeName)\n
    (final String name, final int sqlType, final ResultSetExtractor rse)\n
    (final String name, final int sqlType, final RowCallbackHandler rch)\n
    (final String name, final int sqlType, final RowMapper rm)\n
    (final String name, final int sqlType, final RowMapper rm, final int rowsExpected)\n
    '''
def isResultSetSupported():
    '''returns boolean\n\n
    isResultSetSupported()\n
    '''
def isRowCallbackHandlerSupported():
    '''returns boolean\n\n
    isRowCallbackHandlerSupported()\n
    '''
def getResultSetExtractor():
    '''returns ResultSetExtractor\n\n
    getResultSetExtractor()\n
    '''
def getRowCallbackHandler():
    '''returns RowCallbackHandler\n\n
    getRowCallbackHandler()\n
    '''
