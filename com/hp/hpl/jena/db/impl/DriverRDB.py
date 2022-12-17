PREFIX_CACHE_SIZE = "int  50"
def ():
    '''returns DriverRDB\n\n
    ()\n
    '''
def getConnection():
    '''returns IDBConnection\n\n
    getConnection()\n
    '''
def getSystemSpecializedGraph():
    '''returns SpecializedGraph\n\n
    getSystemSpecializedGraph(final boolean doInit)\n
    '''
def createSpecializedGraphs():
    '''returns List<SpecializedGraph>\n\n
    createSpecializedGraphs(final String graphName, final Graph requestedProperties)\n
    '''
def recreateSpecializedGraphs():
    '''returns List<SpecializedGraph>\n\n
    recreateSpecializedGraphs(final DBPropGraph graphProperties)\n
    '''
def removeSpecializedGraphs():
    '''returns None\n\n
    removeSpecializedGraphs(final DBPropGraph graphProperties, final List<SpecializedGraph> specializedGraphs)\n
    '''
def setDatabaseProperties():
    '''returns None\n\n
    setDatabaseProperties(final Graph databaseProperties)\n
    '''
def getDefaultModelProperties():
    '''returns DBPropGraph\n\n
    getDefaultModelProperties()\n
    '''
def isDBFormatOK():
    '''returns boolean\n\n
    isDBFormatOK()\n
    '''
def stringToDBname():
    '''returns String\n\n
    stringToDBname(final String aName)\n
    '''
def tryLockDB():
    '''returns boolean\n\n
    tryLockDB()\n
    '''
def lockDB():
    '''returns None\n\n
    lockDB()\n
    '''
def unlockDB():
    '''returns None\n\n
    unlockDB()\n
    '''
def DBisLocked():
    '''returns boolean\n\n
    DBisLocked()\n
    '''
def cleanDB():
    '''returns None\n\n
    cleanDB()\n
    '''
def clearSequences():
    '''returns None\n\n
    clearSequences()\n
    '''
def removeSequence():
    '''returns None\n\n
    removeSequence(final String seqName)\n
    '''
def sequenceExists():
    '''returns boolean\n\n
    sequenceExists(final String seqName)\n
    '''
def getSequences():
    '''returns List<String>\n\n
    getSequences()\n
    '''
def createTable():
    '''returns String\n\n
    createTable(final int graphId, final boolean isReif)\n
    '''
def deleteTable():
    '''returns None\n\n
    deleteTable(final String tableName)\n
    '''
def commit():
    '''returns None\n\n
    commit()\n
    '''
def getDatabaseType():
    '''returns String\n\n
    getDatabaseType()\n
    '''
def transactionsSupported():
    '''returns boolean\n\n
    transactionsSupported()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def nodeToRDBString():
    '''returns String\n\n
    nodeToRDBString(final Node node, final boolean addIfLong)\n
    '''
def RDBStringToNode():
    '''returns Node\n\n
    RDBStringToNode(final String RDBString)\n
    '''
def litLangTypeToRDBString():
    '''returns String\n\n
    litLangTypeToRDBString(final String lang, final String dtype)\n
    '''
def getBlankID():
    '''returns DBIDInt\n\n
    getBlankID(final String bstr, final boolean add)\n
    '''
def getURIID():
    '''returns DBIDInt\n\n
    getURIID(final String qname, final boolean add)\n
    '''
def getLiteralID():
    '''returns DBIDInt\n\n
    getLiteralID(final Node_Literal lnode, final boolean add)\n
    '''
def getLongObjectID():
    '''returns DBIDInt\n\n
    getLongObjectID(final RDBLongObject lobj, final String table, final boolean add)\n
    '''
def addRDBLongObject():
    '''returns DBIDInt\n\n
    addRDBLongObject(final RDBLongObject lobj, final String table)\n
    '''
def getInsertID():
    '''returns int\n\n
    getInsertID(final String tableName)\n
    '''
def wrapDBID():
    '''returns DBIDInt\n\n
    wrapDBID(final Object id)\n
    '''
def genSQLReifQualStmt():
    '''returns String\n\n
    genSQLReifQualStmt()\n
    '''
def genSQLReifQualAnyObj():
    '''returns String\n\n
    genSQLReifQualAnyObj(final boolean objIsStmt)\n
    '''
def genSQLReifQualObj():
    '''returns String\n\n
    genSQLReifQualObj(final char reifProp, final boolean hasObj)\n
    '''
def genSQLQualConst():
    '''returns String\n\n
    genSQLQualConst(final int alias, final char pred, final Node lit)\n
    '''
def genSQLReifQualConst():
    '''returns String\n\n
    genSQLReifQualConst(final int alias, final char pred, final Node lit)\n
    '''
def genSQLQualParam():
    '''returns String\n\n
    genSQLQualParam(final int alias, final char pred)\n
    '''
def genSQLQualGraphId():
    '''returns String\n\n
    genSQLQualGraphId(final int alias, final int graphId)\n
    '''
def genSQLJoin():
    '''returns String\n\n
    genSQLJoin(final int lhsAlias, final char lhsCol, final int rhsAlias, final char rhsCol)\n
    '''
def genSQLStringMatch():
    '''returns String\n\n
    genSQLStringMatch(final int alias, final char col, final String fun, final String stringToMatch)\n
    '''
def genSQLStringMatchLHS():
    '''returns String\n\n
    genSQLStringMatchLHS(final boolean ignCase, final String var)\n
    '''
def genSQLStringMatchLong():
    '''returns String\n\n
    genSQLStringMatchLong()\n
    '''
def genSQLStringMatchOp():
    '''returns String\n\n
    genSQLStringMatchOp(final boolean ignCase, final String fun)\n
    genSQLStringMatchOp(final String fun)\n
    '''
def stringMatchAllChar():
    '''returns String\n\n
    stringMatchAllChar()\n
    '''
def stringMatchAnyChar():
    '''returns String\n\n
    stringMatchAnyChar()\n
    '''
def stringMatchEscapeChar():
    '''returns String\n\n
    stringMatchEscapeChar()\n
    '''
def stringMatchLongObj():
    '''returns String\n\n
    stringMatchLongObj()\n
    '''
def stringMatchShortObj():
    '''returns String\n\n
    stringMatchShortObj()\n
    '''
def genSQLStringMatchRHS():
    '''returns String\n\n
    genSQLStringMatchRHS(final boolean ignCase, final boolean pfxMatch, String strToMatch)\n
    '''
def genSQLStringMatchLHS_IC():
    '''returns String\n\n
    genSQLStringMatchLHS_IC(final String var)\n
    '''
def genSQLStringMatchRHS_IC():
    '''returns String\n\n
    genSQLStringMatchRHS_IC(final String strToMatch)\n
    '''
def genSQLStringMatchOp_IC():
    '''returns String\n\n
    genSQLStringMatchOp_IC(final String fun)\n
    '''
def stringMatchNeedsEscape():
    '''returns boolean\n\n
    stringMatchNeedsEscape(final String strToMatch)\n
    '''
def addEscape():
    '''returns String\n\n
    addEscape(final String strToMatch)\n
    '''
def genSQLStringMatchEscape():
    '''returns String\n\n
    genSQLStringMatchEscape()\n
    '''
def genSQLResList():
    '''returns String\n\n
    genSQLResList(final int[] resIndex, final VarDesc[] binding)\n
    '''
def genSQLFromList():
    '''returns String\n\n
    genSQLFromList(final int aliasCnt, final String table)\n
    '''
def genSQLLikeKW():
    '''returns String\n\n
    genSQLLikeKW()\n
    '''
def genSQLEscapeKW():
    '''returns String\n\n
    genSQLEscapeKW()\n
    '''
def genSQLSelectKW():
    '''returns String\n\n
    genSQLSelectKW()\n
    '''
def genSQLFromKW():
    '''returns String\n\n
    genSQLFromKW()\n
    '''
def genSQLWhereKW():
    '''returns String\n\n
    genSQLWhereKW()\n
    '''
def genSQLOrKW():
    '''returns String\n\n
    genSQLOrKW()\n
    '''
def genSQLSelectStmt():
    '''returns String\n\n
    genSQLSelectStmt(final String res, final String from, final String qual)\n
    '''
def getLongObjectLengthMax():
    '''returns int\n\n
    getLongObjectLengthMax()\n
    '''
def getLongObjectLength():
    '''returns int\n\n
    getLongObjectLength()\n
    '''
def setLongObjectLength():
    '''returns None\n\n
    setLongObjectLength(final int len)\n
    '''
def getIndexKeyLengthMax():
    '''returns int\n\n
    getIndexKeyLengthMax()\n
    '''
def getIndexKeyLength():
    '''returns int\n\n
    getIndexKeyLength()\n
    '''
def setIndexKeyLength():
    '''returns None\n\n
    setIndexKeyLength(final int len)\n
    '''
def getIsTransactionDb():
    '''returns boolean\n\n
    getIsTransactionDb()\n
    '''
def setIsTransactionDb():
    '''returns None\n\n
    setIsTransactionDb(final boolean bool)\n
    '''
def getDoCompressURI():
    '''returns boolean\n\n
    getDoCompressURI()\n
    '''
def setDoCompressURI():
    '''returns None\n\n
    setDoCompressURI(final boolean bool)\n
    '''
def getCompressURILength():
    '''returns int\n\n
    getCompressURILength()\n
    '''
def setCompressURILength():
    '''returns None\n\n
    setCompressURILength(final int len)\n
    '''
def getDoDuplicateCheck():
    '''returns boolean\n\n
    getDoDuplicateCheck()\n
    '''
def setDoDuplicateCheck():
    '''returns None\n\n
    setDoDuplicateCheck(final boolean bool)\n
    '''
def getTableNamePrefix():
    '''returns String\n\n
    getTableNamePrefix()\n
    '''
def setTableNamePrefix():
    '''returns None\n\n
    setTableNamePrefix(final String prefix)\n
    '''
def getSystemTableCount():
    '''returns int\n\n
    getSystemTableCount()\n
    '''
def getSystemTableName():
    '''returns String\n\n
    getSystemTableName(final int i)\n
    '''
def getStoreWithModel():
    '''returns String\n\n
    getStoreWithModel()\n
    '''
def setStoreWithModel():
    '''returns None\n\n
    setStoreWithModel(final String modelName)\n
    '''
def getCompressCacheSize():
    '''returns int\n\n
    getCompressCacheSize()\n
    '''
def setCompressCacheSize():
    '''returns None\n\n
    setCompressCacheSize(final int count)\n
    '''
