PREFIX_CACHE_SIZE = "int  50"
def DriverRDB():
    '''public DriverRDB()
    '''
def getConnection():
    '''public IDBConnection getConnection()
    '''
def getSystemSpecializedGraph():
    '''public SpecializedGraph getSystemSpecializedGraph(final boolean doInit)
    '''
def createSpecializedGraphs():
    '''public List<SpecializedGraph> createSpecializedGraphs(final String graphName, final Graph requestedProperties)
    '''
def recreateSpecializedGraphs():
    '''public List<SpecializedGraph> recreateSpecializedGraphs(final DBPropGraph graphProperties)
    '''
def removeSpecializedGraphs():
    '''public void removeSpecializedGraphs(final DBPropGraph graphProperties, final List<SpecializedGraph> specializedGraphs)
    '''
def setDatabaseProperties():
    '''public void setDatabaseProperties(final Graph databaseProperties)
    '''
def getDefaultModelProperties():
    '''public DBPropGraph getDefaultModelProperties()
    '''
def isDBFormatOK():
    '''public boolean isDBFormatOK()
    '''
def stringToDBname():
    '''public String stringToDBname(final String aName)
    '''
def tryLockDB():
    '''public boolean tryLockDB()
    '''
def lockDB():
    '''public void lockDB()
    '''
def unlockDB():
    '''public void unlockDB()
    '''
def DBisLocked():
    '''public boolean DBisLocked()
    '''
def cleanDB():
    '''public void cleanDB()
    '''
def clearSequences():
    '''public void clearSequences()
    '''
def removeSequence():
    '''public void removeSequence(final String seqName)
    '''
def sequenceExists():
    '''public boolean sequenceExists(final String seqName)
    '''
def getSequences():
    '''public List<String> getSequences()
    '''
def createTable():
    '''public String createTable(final int graphId, final boolean isReif)
    '''
def deleteTable():
    '''public void deleteTable(final String tableName)
    '''
def begin():
    '''public synchronized void begin()
    '''
def commit():
    '''public void commit()
    '''
def abort():
    '''public synchronized void abort()
    '''
def getDatabaseType():
    '''public String getDatabaseType()
    '''
def transactionsSupported():
    '''public boolean transactionsSupported()
    '''
def close():
    '''public void close()
    '''
def nodeToRDBString():
    '''public String nodeToRDBString(final Node node, final boolean addIfLong)
    '''
def RDBStringToNode():
    '''public Node RDBStringToNode(final String RDBString)
    '''
def dbSplitNamespace():
    '''public static int dbSplitNamespace(final String uri)
    '''
def litLangTypeToRDBString():
    '''public String litLangTypeToRDBString(final String lang, final String dtype)
    '''
def getBlankID():
    '''public DBIDInt getBlankID(final String bstr, final boolean add)
    '''
def getURIID():
    '''public DBIDInt getURIID(final String qname, final boolean add)
    '''
def getLiteralID():
    '''public DBIDInt getLiteralID(final Node_Literal lnode, final boolean add)
    '''
def getLongObjectID():
    '''public DBIDInt getLongObjectID(final RDBLongObject lobj, final String table, final boolean add)
    '''
def addRDBLongObject():
    '''public DBIDInt addRDBLongObject(final RDBLongObject lobj, final String table)
    '''
def getInsertID():
    '''public int getInsertID(final String tableName)
    '''
def wrapDBID():
    '''public DBIDInt wrapDBID(final Object id)
    '''
def genSQLReifQualStmt():
    '''public String genSQLReifQualStmt()
    '''
def genSQLReifQualAnyObj():
    '''public String genSQLReifQualAnyObj(final boolean objIsStmt)
    '''
def genSQLReifQualObj():
    '''public String genSQLReifQualObj(final char reifProp, final boolean hasObj)
    '''
def genSQLQualConst():
    '''public String genSQLQualConst(final int alias, final char pred, final Node lit)
    '''
def genSQLReifQualConst():
    '''public String genSQLReifQualConst(final int alias, final char pred, final Node lit)
    '''
def genSQLQualParam():
    '''public String genSQLQualParam(final int alias, final char pred)
    '''
def genSQLQualGraphId():
    '''public String genSQLQualGraphId(final int alias, final int graphId)
    '''
def genSQLJoin():
    '''public String genSQLJoin(final int lhsAlias, final char lhsCol, final int rhsAlias, final char rhsCol)
    '''
def genSQLStringMatch():
    '''public String genSQLStringMatch(final int alias, final char col, final String fun, final String stringToMatch)
    '''
def genSQLStringMatchLHS():
    '''public String genSQLStringMatchLHS(final boolean ignCase, final String var)
    '''
def genSQLStringMatchLong():
    '''public String genSQLStringMatchLong()
    '''
def genSQLStringMatchOp():
    '''public String genSQLStringMatchOp(final boolean ignCase, final String fun)
    public String genSQLStringMatchOp(final String fun)
    '''
def stringMatchAllChar():
    '''public String stringMatchAllChar()
    '''
def stringMatchAnyChar():
    '''public String stringMatchAnyChar()
    '''
def stringMatchEscapeChar():
    '''public String stringMatchEscapeChar()
    '''
def stringMatchLongObj():
    '''public String stringMatchLongObj()
    '''
def stringMatchShortObj():
    '''public String stringMatchShortObj()
    '''
def genSQLStringMatchRHS():
    '''public String genSQLStringMatchRHS(final boolean ignCase, final boolean pfxMatch, String strToMatch)
    '''
def genSQLStringMatchLHS_IC():
    '''public String genSQLStringMatchLHS_IC(final String var)
    '''
def genSQLStringMatchRHS_IC():
    '''public String genSQLStringMatchRHS_IC(final String strToMatch)
    '''
def genSQLStringMatchOp_IC():
    '''public String genSQLStringMatchOp_IC(final String fun)
    '''
def stringMatchNeedsEscape():
    '''public boolean stringMatchNeedsEscape(final String strToMatch)
    '''
def addEscape():
    '''public String addEscape(final String strToMatch)
    '''
def genSQLStringMatchEscape():
    '''public String genSQLStringMatchEscape()
    '''
def genSQLResList():
    '''public String genSQLResList(final int[] resIndex, final VarDesc[] binding)
    '''
def genSQLFromList():
    '''public String genSQLFromList(final int aliasCnt, final String table)
    '''
def genSQLLikeKW():
    '''public String genSQLLikeKW()
    '''
def genSQLEscapeKW():
    '''public String genSQLEscapeKW()
    '''
def genSQLSelectKW():
    '''public String genSQLSelectKW()
    '''
def genSQLFromKW():
    '''public String genSQLFromKW()
    '''
def genSQLWhereKW():
    '''public String genSQLWhereKW()
    '''
def genSQLOrKW():
    '''public String genSQLOrKW()
    '''
def genSQLSelectStmt():
    '''public String genSQLSelectStmt(final String res, final String from, final String qual)
    '''
def getLongObjectLengthMax():
    '''public int getLongObjectLengthMax()
    '''
def getLongObjectLength():
    '''public int getLongObjectLength()
    '''
def setLongObjectLength():
    '''public void setLongObjectLength(final int len)
    '''
def getIndexKeyLengthMax():
    '''public int getIndexKeyLengthMax()
    '''
def getIndexKeyLength():
    '''public int getIndexKeyLength()
    '''
def setIndexKeyLength():
    '''public void setIndexKeyLength(final int len)
    '''
def getIsTransactionDb():
    '''public boolean getIsTransactionDb()
    '''
def setIsTransactionDb():
    '''public void setIsTransactionDb(final boolean bool)
    '''
def getDoCompressURI():
    '''public boolean getDoCompressURI()
    '''
def setDoCompressURI():
    '''public void setDoCompressURI(final boolean bool)
    '''
def getCompressURILength():
    '''public int getCompressURILength()
    '''
def setCompressURILength():
    '''public void setCompressURILength(final int len)
    '''
def getDoDuplicateCheck():
    '''public boolean getDoDuplicateCheck()
    '''
def setDoDuplicateCheck():
    '''public void setDoDuplicateCheck(final boolean bool)
    '''
def getTableNamePrefix():
    '''public String getTableNamePrefix()
    '''
def setTableNamePrefix():
    '''public void setTableNamePrefix(final String prefix)
    '''
def getSystemTableCount():
    '''public int getSystemTableCount()
    '''
def getSystemTableName():
    '''public String getSystemTableName(final int i)
    '''
def getStoreWithModel():
    '''public String getStoreWithModel()
    '''
def setStoreWithModel():
    '''public void setStoreWithModel(final String modelName)
    '''
def getCompressCacheSize():
    '''public int getCompressCacheSize()
    '''
def setCompressCacheSize():
    '''public void setCompressCacheSize(final int count)
    '''
