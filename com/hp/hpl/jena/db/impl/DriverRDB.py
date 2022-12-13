PREFIX_CACHE_SIZE = "int  50"
def DriverRDB():
'''public DriverRDB()
'''
pass
def getConnection():
'''public IDBConnection getConnection()
'''
pass
def getSystemSpecializedGraph():
'''public SpecializedGraph getSystemSpecializedGraph(final boolean doInit)
'''
pass
def createSpecializedGraphs():
'''public List<SpecializedGraph> createSpecializedGraphs(final String graphName, final Graph requestedProperties)
'''
pass
def recreateSpecializedGraphs():
'''public List<SpecializedGraph> recreateSpecializedGraphs(final DBPropGraph graphProperties)
'''
pass
def removeSpecializedGraphs():
'''public void removeSpecializedGraphs(final DBPropGraph graphProperties, final List<SpecializedGraph> specializedGraphs)
'''
pass
def setDatabaseProperties():
'''public void setDatabaseProperties(final Graph databaseProperties)
'''
pass
def getDefaultModelProperties():
'''public DBPropGraph getDefaultModelProperties()
'''
pass
def isDBFormatOK():
'''public boolean isDBFormatOK()
'''
pass
def stringToDBname():
'''public String stringToDBname(final String aName)
'''
pass
def tryLockDB():
'''public boolean tryLockDB()
'''
pass
def lockDB():
'''public void lockDB()
'''
pass
def unlockDB():
'''public void unlockDB()
'''
pass
def DBisLocked():
'''public boolean DBisLocked()
'''
pass
def cleanDB():
'''public void cleanDB()
'''
pass
def clearSequences():
'''public void clearSequences()
'''
pass
def removeSequence():
'''public void removeSequence(final String seqName)
'''
pass
def sequenceExists():
'''public boolean sequenceExists(final String seqName)
'''
pass
def getSequences():
'''public List<String> getSequences()
'''
pass
def createTable():
'''public String createTable(final int graphId, final boolean isReif)
'''
pass
def deleteTable():
'''public void deleteTable(final String tableName)
'''
pass
def begin():
'''public synchronized void begin()
'''
pass
def commit():
'''public void commit()
'''
pass
def abort():
'''public synchronized void abort()
'''
pass
def getDatabaseType():
'''public String getDatabaseType()
'''
pass
def transactionsSupported():
'''public boolean transactionsSupported()
'''
pass
def close():
'''public void close()
'''
pass
def nodeToRDBString():
'''public String nodeToRDBString(final Node node, final boolean addIfLong)
'''
pass
def RDBStringToNode():
'''public Node RDBStringToNode(final String RDBString)
'''
pass
def dbSplitNamespace():
'''public static int dbSplitNamespace(final String uri)
'''
pass
def litLangTypeToRDBString():
'''public String litLangTypeToRDBString(final String lang, final String dtype)
'''
pass
def getBlankID():
'''public DBIDInt getBlankID(final String bstr, final boolean add)
'''
pass
def getURIID():
'''public DBIDInt getURIID(final String qname, final boolean add)
'''
pass
def getLiteralID():
'''public DBIDInt getLiteralID(final Node_Literal lnode, final boolean add)
'''
pass
def getLongObjectID():
'''public DBIDInt getLongObjectID(final RDBLongObject lobj, final String table, final boolean add)
'''
pass
def addRDBLongObject():
'''public DBIDInt addRDBLongObject(final RDBLongObject lobj, final String table)
'''
pass
def getInsertID():
'''public int getInsertID(final String tableName)
'''
pass
def wrapDBID():
'''public DBIDInt wrapDBID(final Object id)
'''
pass
def genSQLReifQualStmt():
'''public String genSQLReifQualStmt()
'''
pass
def genSQLReifQualAnyObj():
'''public String genSQLReifQualAnyObj(final boolean objIsStmt)
'''
pass
def genSQLReifQualObj():
'''public String genSQLReifQualObj(final char reifProp, final boolean hasObj)
'''
pass
def genSQLQualConst():
'''public String genSQLQualConst(final int alias, final char pred, final Node lit)
'''
pass
def genSQLReifQualConst():
'''public String genSQLReifQualConst(final int alias, final char pred, final Node lit)
'''
pass
def genSQLQualParam():
'''public String genSQLQualParam(final int alias, final char pred)
'''
pass
def genSQLQualGraphId():
'''public String genSQLQualGraphId(final int alias, final int graphId)
'''
pass
def genSQLJoin():
'''public String genSQLJoin(final int lhsAlias, final char lhsCol, final int rhsAlias, final char rhsCol)
'''
pass
def genSQLStringMatch():
'''public String genSQLStringMatch(final int alias, final char col, final String fun, final String stringToMatch)
'''
pass
def genSQLStringMatchLHS():
'''public String genSQLStringMatchLHS(final boolean ignCase, final String var)
'''
pass
def genSQLStringMatchLong():
'''public String genSQLStringMatchLong()
'''
pass
def genSQLStringMatchOp():
'''public String genSQLStringMatchOp(final boolean ignCase, final String fun)
public String genSQLStringMatchOp(final String fun)
'''
pass
def stringMatchAllChar():
'''public String stringMatchAllChar()
'''
pass
def stringMatchAnyChar():
'''public String stringMatchAnyChar()
'''
pass
def stringMatchEscapeChar():
'''public String stringMatchEscapeChar()
'''
pass
def stringMatchLongObj():
'''public String stringMatchLongObj()
'''
pass
def stringMatchShortObj():
'''public String stringMatchShortObj()
'''
pass
def genSQLStringMatchRHS():
'''public String genSQLStringMatchRHS(final boolean ignCase, final boolean pfxMatch, String strToMatch)
'''
pass
def genSQLStringMatchLHS_IC():
'''public String genSQLStringMatchLHS_IC(final String var)
'''
pass
def genSQLStringMatchRHS_IC():
'''public String genSQLStringMatchRHS_IC(final String strToMatch)
'''
pass
def genSQLStringMatchOp_IC():
'''public String genSQLStringMatchOp_IC(final String fun)
'''
pass
def stringMatchNeedsEscape():
'''public boolean stringMatchNeedsEscape(final String strToMatch)
'''
pass
def addEscape():
'''public String addEscape(final String strToMatch)
'''
pass
def genSQLStringMatchEscape():
'''public String genSQLStringMatchEscape()
'''
pass
def genSQLResList():
'''public String genSQLResList(final int[] resIndex, final VarDesc[] binding)
'''
pass
def genSQLFromList():
'''public String genSQLFromList(final int aliasCnt, final String table)
'''
pass
def genSQLLikeKW():
'''public String genSQLLikeKW()
'''
pass
def genSQLEscapeKW():
'''public String genSQLEscapeKW()
'''
pass
def genSQLSelectKW():
'''public String genSQLSelectKW()
'''
pass
def genSQLFromKW():
'''public String genSQLFromKW()
'''
pass
def genSQLWhereKW():
'''public String genSQLWhereKW()
'''
pass
def genSQLOrKW():
'''public String genSQLOrKW()
'''
pass
def genSQLSelectStmt():
'''public String genSQLSelectStmt(final String res, final String from, final String qual)
'''
pass
def getLongObjectLengthMax():
'''public int getLongObjectLengthMax()
'''
pass
def getLongObjectLength():
'''public int getLongObjectLength()
'''
pass
def setLongObjectLength():
'''public void setLongObjectLength(final int len)
'''
pass
def getIndexKeyLengthMax():
'''public int getIndexKeyLengthMax()
'''
pass
def getIndexKeyLength():
'''public int getIndexKeyLength()
'''
pass
def setIndexKeyLength():
'''public void setIndexKeyLength(final int len)
'''
pass
def getIsTransactionDb():
'''public boolean getIsTransactionDb()
'''
pass
def setIsTransactionDb():
'''public void setIsTransactionDb(final boolean bool)
'''
pass
def getDoCompressURI():
'''public boolean getDoCompressURI()
'''
pass
def setDoCompressURI():
'''public void setDoCompressURI(final boolean bool)
'''
pass
def getCompressURILength():
'''public int getCompressURILength()
'''
pass
def setCompressURILength():
'''public void setCompressURILength(final int len)
'''
pass
def getDoDuplicateCheck():
'''public boolean getDoDuplicateCheck()
'''
pass
def setDoDuplicateCheck():
'''public void setDoDuplicateCheck(final boolean bool)
'''
pass
def getTableNamePrefix():
'''public String getTableNamePrefix()
'''
pass
def setTableNamePrefix():
'''public void setTableNamePrefix(final String prefix)
'''
pass
def getSystemTableCount():
'''public int getSystemTableCount()
'''
pass
def getSystemTableName():
'''public String getSystemTableName(final int i)
'''
pass
def getStoreWithModel():
'''public String getStoreWithModel()
'''
pass
def setStoreWithModel():
'''public void setStoreWithModel(final String modelName)
'''
pass
def getCompressCacheSize():
'''public int getCompressCacheSize()
'''
pass
def setCompressCacheSize():
'''public void setCompressCacheSize(final int count)
'''
pass
