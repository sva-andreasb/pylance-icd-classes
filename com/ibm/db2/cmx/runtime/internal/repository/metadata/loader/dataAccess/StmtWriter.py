def ():
    '''returns StmtWriter\n\n
    (final String schema)\n
    '''
def createStmt():
    '''returns int\n\n
    createStmt(final Connection connection, final String s, final String s2, final String s3, final String s4, final char c, final char c2, final int n, final String s5, final Integer n2, final char c3)\n
    createStmt(final Connection connection, final String expression, final String querytext, final String processedsqltext, final String statementtype, final char c, final char c2, final int value, final String id, final Integer dbpkg_key, final char c3, final Double totalcost, Long cardinality, final Integer joincount, final Integer tbscancount, final Integer ixscancount, final String defaultschema, final String path, final String specreg, final Integer execount, final String lastusedts)\n
    '''
def createStmtV221():
    '''returns int\n\n
    createStmtV221(final Connection connection, final String expression, final String querytext, final String processedsqltext, final String statementtype, final char c, final char c2, final int value, final String id, final Integer dbpkg_key, final char c3, final Double totalcost, Long cardinality, final Integer joincount, final Integer tbscancount, final Integer ixscancount)\n
    '''
def removeOrphanedStmtEntries():
    '''returns None\n\n
    removeOrphanedStmtEntries(final Connection connection)\n
    '''
def removeProjectExplainData():
    '''returns int\n\n
    removeProjectExplainData(final Connection connection, final String s)\n
    '''
def removeStmtsForMetadataSource():
    '''returns int\n\n
    removeStmtsForMetadataSource(final Connection connection, final int n)\n
    '''
