def ():
    '''returns PSet_TripleStore_RDB\n\n
    ()\n
    '''
def setDriver():
    '''returns None\n\n
    setDriver(final IRDBDriver driver)\n
    '''
def setSQLType():
    '''returns None\n\n
    setSQLType(final String value)\n
    '''
def setSkipDuplicateCheck():
    '''returns None\n\n
    setSkipDuplicateCheck(final boolean value)\n
    '''
def setSQLCache():
    '''returns None\n\n
    setSQLCache(final SQLCache cache)\n
    '''
def getSQLCache():
    '''returns SQLCache\n\n
    getSQLCache()\n
    '''
def setCachePreparedStatements():
    '''returns None\n\n
    setCachePreparedStatements(final boolean value)\n
    '''
def setTblName():
    '''returns None\n\n
    setTblName(final String tblName)\n
    '''
def getTblName():
    '''returns String\n\n
    getTblName()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def driver():
    '''returns IRDBDriver\n\n
    driver()\n
    '''
def cleanDB():
    '''returns None\n\n
    cleanDB()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getLiteralFromCache():
    '''returns Node_Literal\n\n
    getLiteralFromCache(final IDBID id)\n
    '''
def wrapDBID():
    '''returns IDBID\n\n
    wrapDBID(final Object id)\n
    '''
def rowCount():
    '''returns int\n\n
    rowCount(final int gid)\n
    '''
def extractTripleFromRowData():
    '''returns Triple\n\n
    extractTripleFromRowData(final String subj, final String pred, final String obj)\n
    '''
def wrapFlag():
    '''returns Object\n\n
    wrapFlag(final boolean flag)\n
    '''
def deleteTriple():
    '''returns None\n\n
    deleteTriple(final Triple t, final IDBID graphID)\n
    deleteTriple(final Triple t, final IDBID graphID, final boolean isBatch, final Hashtable<String, PreparedStatement> batchedPreparedStatements)\n
    '''
def deleteTripleAR():
    '''returns None\n\n
    deleteTripleAR(final Triple t, final IDBID graphID, final Node reifNode, final boolean isBatch, final Hashtable<String, PreparedStatement> batchedPreparedStatements)\n
    '''
def storeTriple():
    '''returns None\n\n
    storeTriple(final Triple t, final IDBID graphID)\n
    storeTriple(final Triple t, final IDBID graphID, final boolean isBatch, final Hashtable<String, PreparedStatement> batchedPreparedStatements)\n
    '''
def getPreparedStatement():
    '''returns PreparedStatement\n\n
    getPreparedStatement(final String op, final String tableName, final boolean isBatch, final Hashtable<String, PreparedStatement> batchedPreparedStatements)\n
    '''
def storeTripleAR():
    '''returns None\n\n
    storeTripleAR(final Triple t, final IDBID graphID, final Node reifNode, final boolean hasType, final boolean isBatch, final Hashtable<String, PreparedStatement> batchedPreparedStatements)\n
    '''
def storeTripleList():
    '''returns None\n\n
    storeTripleList(final List<Triple> triples, final IDBID my_GID)\n
    '''
def deleteTripleList():
    '''returns None\n\n
    deleteTripleList(final List<Triple> triples, final IDBID my_GID)\n
    '''
def tripleCount():
    '''returns int\n\n
    tripleCount(final IDBID graphId)\n
    '''
def statementTableContains():
    '''returns boolean\n\n
    statementTableContains(final IDBID graphID, final Triple t)\n
    '''
def find():
    '''returns ExtendedIterator<Triple>\n\n
    find(final TripleMatch t, final IDBID graphID)\n
    '''
def removeStatementsFromDB():
    '''returns None\n\n
    removeStatementsFromDB(final IDBID graphID)\n
    '''
