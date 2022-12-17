def ():
    '''returns SQLCache\n\n
    (final String sqlFile, final Properties defaultOps, final IDBConnection connection, final String idType)\n
    '''
def setCachePreparedStatements():
    '''returns None\n\n
    setCachePreparedStatements(final boolean state)\n
    '''
def getCachePreparedStatements():
    '''returns boolean\n\n
    getCachePreparedStatements()\n
    '''
def flushPreparedStatementCache():
    '''returns None\n\n
    flushPreparedStatementCache()\n
    '''
def getConnection():
    '''returns Connection\n\n
    getConnection()\n
    '''
def setConnection():
    '''returns None\n\n
    setConnection(final IDBConnection connection)\n
    '''
def getSQLStatement():
    '''returns String\n\n
    getSQLStatement(final String opname)\n
    getSQLStatement(final String opname, final String[] attr)\n
    getSQLStatement(final String opname, final String attr)\n
    getSQLStatement(final String opname, final String attrA, final String attrB)\n
    '''
def getSQLStatementGroup():
    '''returns Collection<String>\n\n
    getSQLStatementGroup(final String opname)\n
    '''
def runSQLUpdate():
    '''returns int\n\n
    runSQLUpdate(final String opname, final Object[] args)\n
    runSQLUpdate(final String opname, final String attrA, final Object[] args)\n
    runSQLUpdate(final String opname, final String attrA, final String attrB, final Object[] args)\n
    '''
def runSQLGroup():
    '''returns None\n\n
    runSQLGroup(final String opname, final String[] attr)\n
    runSQLGroup(final String opname)\n
    runSQLGroup(final String opname, final String attr)\n
    runSQLGroup(final String opname, final String attrA, final String attrB)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
