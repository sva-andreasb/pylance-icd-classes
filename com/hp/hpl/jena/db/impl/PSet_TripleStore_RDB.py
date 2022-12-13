def PSet_TripleStore_RDB():
'''public PSet_TripleStore_RDB()
'''
pass
def setDriver():
'''public void setDriver(final IRDBDriver driver)
'''
pass
def setSQLType():
'''public void setSQLType(final String value)
'''
pass
def setSkipDuplicateCheck():
'''public void setSkipDuplicateCheck(final boolean value)
'''
pass
def setSQLCache():
'''public void setSQLCache(final SQLCache cache)
'''
pass
def getSQLCache():
'''public SQLCache getSQLCache()
'''
pass
def setCachePreparedStatements():
'''public void setCachePreparedStatements(final boolean value)
'''
pass
def setTblName():
'''public void setTblName(final String tblName)
'''
pass
def getTblName():
'''public String getTblName()
'''
pass
def close():
'''public void close()
'''
pass
def driver():
'''public IRDBDriver driver()
'''
pass
def cleanDB():
'''public void cleanDB()
'''
pass
def toString():
'''public String toString()
'''
pass
def getLiteralFromCache():
'''public Node_Literal getLiteralFromCache(final IDBID id)
'''
pass
def wrapDBID():
'''public IDBID wrapDBID(final Object id)
'''
pass
def rowCount():
'''public int rowCount(final int gid)
'''
pass
def extractTripleFromRowData():
'''public Triple extractTripleFromRowData(final String subj, final String pred, final String obj)
'''
pass
def wrapFlag():
'''public Object wrapFlag(final boolean flag)
'''
pass
def deleteTriple():
'''public void deleteTriple(final Triple t, final IDBID graphID)
public void deleteTriple(final Triple t, final IDBID graphID, final boolean isBatch, final Hashtable<String, PreparedStatement> batchedPreparedStatements)
'''
pass
def deleteTripleAR():
'''public void deleteTripleAR(final Triple t, final IDBID graphID, final Node reifNode, final boolean isBatch, final Hashtable<String, PreparedStatement> batchedPreparedStatements)
'''
pass
def storeTriple():
'''public void storeTriple(final Triple t, final IDBID graphID)
public void storeTriple(final Triple t, final IDBID graphID, final boolean isBatch, final Hashtable<String, PreparedStatement> batchedPreparedStatements)
'''
pass
def getPreparedStatement():
'''public PreparedStatement getPreparedStatement(final String op, final String tableName, final boolean isBatch, final Hashtable<String, PreparedStatement> batchedPreparedStatements)
'''
pass
def storeTripleAR():
'''public void storeTripleAR(final Triple t, final IDBID graphID, final Node reifNode, final boolean hasType, final boolean isBatch, final Hashtable<String, PreparedStatement> batchedPreparedStatements)
'''
pass
def storeTripleList():
'''public void storeTripleList(final List<Triple> triples, final IDBID my_GID)
'''
pass
def deleteTripleList():
'''public void deleteTripleList(final List<Triple> triples, final IDBID my_GID)
'''
pass
def tripleCount():
'''public int tripleCount(final IDBID graphId)
'''
pass
def statementTableContains():
'''public boolean statementTableContains(final IDBID graphID, final Triple t)
'''
pass
def find():
'''public ExtendedIterator<Triple> find(final TripleMatch t, final IDBID graphID)
'''
pass
def removeStatementsFromDB():
'''public void removeStatementsFromDB(final IDBID graphID)
'''
pass
