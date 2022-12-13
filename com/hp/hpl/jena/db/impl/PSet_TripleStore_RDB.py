def PSet_TripleStore_RDB():
    '''public PSet_TripleStore_RDB()
    '''
def setDriver():
    '''public void setDriver(final IRDBDriver driver)
    '''
def setSQLType():
    '''public void setSQLType(final String value)
    '''
def setSkipDuplicateCheck():
    '''public void setSkipDuplicateCheck(final boolean value)
    '''
def setSQLCache():
    '''public void setSQLCache(final SQLCache cache)
    '''
def getSQLCache():
    '''public SQLCache getSQLCache()
    '''
def setCachePreparedStatements():
    '''public void setCachePreparedStatements(final boolean value)
    '''
def setTblName():
    '''public void setTblName(final String tblName)
    '''
def getTblName():
    '''public String getTblName()
    '''
def close():
    '''public void close()
    '''
def driver():
    '''public IRDBDriver driver()
    '''
def cleanDB():
    '''public void cleanDB()
    '''
def toString():
    '''public String toString()
    '''
def getLiteralFromCache():
    '''public Node_Literal getLiteralFromCache(final IDBID id)
    '''
def wrapDBID():
    '''public IDBID wrapDBID(final Object id)
    '''
def rowCount():
    '''public int rowCount(final int gid)
    '''
def extractTripleFromRowData():
    '''public Triple extractTripleFromRowData(final String subj, final String pred, final String obj)
    '''
def wrapFlag():
    '''public Object wrapFlag(final boolean flag)
    '''
def deleteTriple():
    '''public void deleteTriple(final Triple t, final IDBID graphID)
    public void deleteTriple(final Triple t, final IDBID graphID, final boolean isBatch, final Hashtable<String, PreparedStatement> batchedPreparedStatements)
    '''
def deleteTripleAR():
    '''public void deleteTripleAR(final Triple t, final IDBID graphID, final Node reifNode, final boolean isBatch, final Hashtable<String, PreparedStatement> batchedPreparedStatements)
    '''
def storeTriple():
    '''public void storeTriple(final Triple t, final IDBID graphID)
    public void storeTriple(final Triple t, final IDBID graphID, final boolean isBatch, final Hashtable<String, PreparedStatement> batchedPreparedStatements)
    '''
def getPreparedStatement():
    '''public PreparedStatement getPreparedStatement(final String op, final String tableName, final boolean isBatch, final Hashtable<String, PreparedStatement> batchedPreparedStatements)
    '''
def storeTripleAR():
    '''public void storeTripleAR(final Triple t, final IDBID graphID, final Node reifNode, final boolean hasType, final boolean isBatch, final Hashtable<String, PreparedStatement> batchedPreparedStatements)
    '''
def storeTripleList():
    '''public void storeTripleList(final List<Triple> triples, final IDBID my_GID)
    '''
def deleteTripleList():
    '''public void deleteTripleList(final List<Triple> triples, final IDBID my_GID)
    '''
def tripleCount():
    '''public int tripleCount(final IDBID graphId)
    '''
def statementTableContains():
    '''public boolean statementTableContains(final IDBID graphID, final Triple t)
    '''
def find():
    '''public ExtendedIterator<Triple> find(final TripleMatch t, final IDBID graphID)
    '''
def removeStatementsFromDB():
    '''public void removeStatementsFromDB(final IDBID graphID)
    '''
