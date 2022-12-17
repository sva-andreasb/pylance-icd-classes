def ():
    '''returns DatabaseUtils\n\n
    (final boolean debug, final ImportDocumentHandler handler)\n
    '''
def doDbUpdate():
    '''returns int\n\n
    doDbUpdate(final Connection con, final XMLObject objectElement)\n
    '''
def doDbInsert():
    '''returns int\n\n
    doDbInsert(final Connection con, final XMLObject objectElement)\n
    '''
def getColumnValue():
    '''returns String\n\n
    getColumnValue(final XMLColumn elem)\n
    '''
def getColumnOriginalValue():
    '''returns String\n\n
    getColumnOriginalValue(final XMLColumn elem)\n
    '''
def getValueText():
    '''returns String\n\n
    getValueText(final XMLColumn column, final String nodename)\n
    '''
def substituteQueryParameters():
    '''returns String\n\n
    substituteQueryParameters(final XMLObject e, String query)\n
    '''
def forThisDatabase():
    '''returns boolean\n\n
    forThisDatabase(final String dbtype)\n
    '''
def runExtension():
    '''returns boolean\n\n
    runExtension(final String extensionNames, final int mode, final Connection con, final Processable object)\n
    '''
def closeJDBCConnection():
    '''returns None\n\n
    closeJDBCConnection(final Connection conn)\n
    '''
def closeJDBCStatement():
    '''returns None\n\n
    closeJDBCStatement(final Statement stmt)\n
    '''
def closeJDBCResultSet():
    '''returns None\n\n
    closeJDBCResultSet(final ResultSet aResultSet)\n
    '''
