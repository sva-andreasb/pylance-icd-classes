def ():
    '''returns Util\n\n
    (final Connection conparam, final PrintStream outparam, final String schemaOwnerparam)\n
    (final Connection conparam, final PrintStream outparam, final String schemaOwnerparam, final boolean reloadAttrs)\n
    '''
def getMaxTableAttrs():
    '''returns String[]\n\n
    getMaxTableAttrs()\n
    '''
def reloadAttributeList():
    '''returns None\n\n
    reloadAttributeList()\n
    '''
def getCurrentNativeSchema():
    '''returns String\n\n
    getCurrentNativeSchema()\n
    '''
def writeDumpTable():
    '''returns int\n\n
    writeDumpTable(final String tbname, final TreeMap tableCols, final PrintStream out)\n
    writeDumpTable(final String tbname, TreeMap tableCols, PrintStream out, int maxLines, int numLines, final Unlcvt unlcvt, final boolean psFormat)\n
    '''
def getData():
    '''returns TreeMap\n\n
    getData(final String tbname, TreeMap tableCols, final String where)\n
    '''
def isTable():
    '''returns boolean\n\n
    isTable(final HashMap tableInfo)\n
    '''
def buildCreateTableStatement():
    '''returns String\n\n
    buildCreateTableStatement(final HashMap tableInfo, final boolean doColDefault, final boolean includeDroppedCols, final String dbstoragepartition, final boolean specifyStorage)\n
    buildCreateTableStatement(final String tbname, final TreeMap tableCols, final boolean doColDefault, final boolean includeDroppedCols, final String dbstoragepartition, final boolean addRowstamp, final String storageClause)\n
    '''
def buildCreateViewStatement():
    '''returns ArrayList<String>\n\n
    buildCreateViewStatement(final HashMap viewInfo, final boolean includeDroppedCols, final boolean forceDropStmt)\n
    '''
def getAttributeForMaxViewColumn():
    '''returns HashMap\n\n
    getAttributeForMaxViewColumn(final String viewName, final HashMap viewcolInfo, final TreeMap distinctAttrs)\n
    '''
def buildColumnLine():
    '''returns String\n\n
    buildColumnLine(final HashMap colInfo, final boolean doDefault, final boolean alter)\n
    buildColumnLine(final HashMap colInfo, final boolean doDefault, final boolean doNullClause, final boolean alter)\n
    '''
def buildDefaultDataStatement():
    '''returns String\n\n
    buildDefaultDataStatement(final String tbname, final TreeMap newTableCols, final String colNameList, TreeMap<String, HashMap<String, String>> oldTableCols)\n
    buildDefaultDataStatement(final String tbname, final HashMap newColInfo, final HashMap oldColInfo)\n
    '''
def buildShortenStringStatement():
    '''returns ArrayList<String>\n\n
    buildShortenStringStatement(final String tbname, final TreeMap newTableCols, final TreeMap oldTableCols)\n
    '''
def buildChangeCaseStatement():
    '''returns String\n\n
    buildChangeCaseStatement(final String tbname, TreeMap<String, HashMap<String, String>> oldCols, TreeMap<String, HashMap<String, String>> newCols)\n
    buildChangeCaseStatement(final String tbname, final String name, final String oldMaxtype, final String newMaxtype)\n
    '''
def buildSelectStatement():
    '''returns String\n\n
    buildSelectStatement(final String tbname, final TreeMap tableCols, final boolean includeDroppedCols, final boolean addRowstamp)\n
    buildSelectStatement(final String tbname, final TreeMap tableCols, final boolean includeDroppedCols, final boolean addRowstamp, final boolean addTenantID)\n
    buildSelectStatement(final String tbname, final TreeMap tableCols, final boolean includeDroppedCols, final boolean addRowstamp, final boolean addtenantID, final String colNameList)\n
    '''
def buildSelectStatementForRestore():
    '''returns String\n\n
    buildSelectStatementForRestore(final String tempTbName, final TreeMap newTableCols, final boolean addRowstamp, final String colNameList, final boolean doLineBreaks)\n
    '''
def getDefaultString():
    '''returns String\n\n
    getDefaultString(final String tbname, final HashMap colInfo)\n
    getDefaultString(final String tbname, final String colName, final String maxtype, final String metaDefaultValue, final String domainid)\n
    getDefaultString(final String tbname, final String colName, final String maxtype, String metaDefaultValue, final String domainid, String sequenceName, final int uidRule, final int seqRule, final int autoRule, final int mboRule, final int appRule, final boolean outputQuotes, final boolean assignIfNoMeta)\n
    '''
def isSpecialDefaultValue():
    '''returns boolean\n\n
    isSpecialDefaultValue(final String value)\n
    '''
def getOracleConvertString():
    '''returns String\n\n
    getOracleConvertString(String oldNativeType, String newNativeType, final String colName)\n
    '''
def getSqlServerConvertString():
    '''returns String\n\n
    getSqlServerConvertString(final String oldTbname, final String newTbname, final HashMap newColInfo)\n
    '''
def getDB2ConvertString():
    '''returns String\n\n
    getDB2ConvertString(String oldNativeType, String newNativeType, final String colName)\n
    '''
def nativeTypesAreCompatible():
    '''returns boolean\n\n
    nativeTypesAreCompatible(String oldNativeType, String newNativeType)\n
    '''
def buildInsertStatementPrefix():
    '''returns String\n\n
    buildInsertStatementPrefix(final String tbname, final TreeMap tableCols, final boolean doRowstamp, final boolean includeDroppedCols)\n
    buildInsertStatementPrefix(final String tbname, final TreeMap tableCols, final boolean doRowstamp, final boolean includeDroppedCols, final String colNameList, final boolean doLineBreaks)\n
    buildInsertStatementPrefix(final String tbname, final TreeMap tableCols, final boolean doRowstamp, final boolean includeDroppedCols, final String colNameList, final boolean doLineBreaks, final boolean addTenantid)\n
    '''
def buildInsertValuesStatement():
    '''returns TreeMap\n\n
    buildInsertValuesStatement(final String prefix, final ResultSet rs, final TreeMap tableCols, final boolean includeDroppedCols, final String rowstampValue)\n
    '''
def getColumnNames():
    '''returns String\n\n
    getColumnNames(final TreeMap tableCols, final boolean doLineBreaks, final boolean includeDroppedCols)\n
    getColumnNames(final TreeMap tableCols, final boolean doLineBreaks, final boolean includeDroppedCols, final String colNameList, final boolean useAlias)\n
    '''
def processTemplateData():
    '''returns None\n\n
    processTemplateData(final int toTenantid, final boolean delete, final String maxUserGroup, final String allUserGroup, final String newUserGroup, final PrintStream out)\n
    '''
def copyData():
    '''returns None\n\n
    copyData(final String tabName, final String uniqueColumn, final int toTenantid, final int storageType, final boolean delete, final PrintStream out)\n
    '''
def updateGroupName():
    '''returns None\n\n
    updateGroupName(final String tabName, final String maxUserGroup, final String allUserGroup, final String newUserGroup, final int toTenantid)\n
    '''
def getColumnNamesNative():
    '''returns String\n\n
    getColumnNamesNative(final String tbname)\n
    '''
def getColumnInfo():
    '''returns HashMap\n\n
    getColumnInfo(final TreeMap tableCols, String name)\n
    '''
def getAddRowstampSql():
    '''returns String\n\n
    getAddRowstampSql(final String tbname)\n
    '''
def getRowstampTriggerSql():
    '''returns ArrayList<String>\n\n
    getRowstampTriggerSql(final String tbname, final boolean dropIfExists)\n
    getRowstampTriggerSql(final String tbname, final boolean dropIfExists, final boolean makeSecure)\n
    '''
def getTrigRoot():
    '''returns String\n\n
    getTrigRoot(final String tbname)\n
    '''
def buildGrants():
    '''returns ArrayList<String>\n\n
    buildGrants(final String tbname, final boolean outputSchema, final boolean maxusersOnly)\n
    '''
def getGrantSql():
    '''returns String\n\n
    getGrantSql(final String dbUserID, final String entityname, final String privilege, final boolean grant)\n
    '''
def getTriggerNames():
    '''returns ArrayList<String>\n\n
    getTriggerNames(final String tbname, final boolean getEnabled, final boolean getDisabled, final boolean includeRowstamp)\n
    '''
def getEnableTriggerStatement():
    '''returns String\n\n
    getEnableTriggerStatement(final String triggerName, final String tbname)\n
    '''
def getDisableTriggerStatement():
    '''returns String\n\n
    getDisableTriggerStatement(final String triggerName, final String tbname)\n
    '''
def getEnableDisableTriggersAll():
    '''returns String\n\n
    getEnableDisableTriggersAll(final String tbname, final boolean enable)\n
    '''
def changeAmountFormat():
    '''returns ArrayList<String>\n\n
    changeAmountFormat(final int newLength, final int newScale)\n
    '''
def isRichTextSupported():
    '''returns boolean\n\n
    isRichTextSupported(String tbname, String name)\n
    '''
def isHandleColumn():
    '''returns boolean\n\n
    isHandleColumn(final String colName, final TreeMap attrs)\n
    '''
def enableRichTextSearch():
    '''returns ArrayList<String>\n\n
    enableRichTextSearch(final HashMap objInfo, final TreeMap tbIndexes, final boolean doCheck, final boolean skipDb2Connect)\n
    enableRichTextSearch(final String tbname, final String colName, final String handleColName, final HashMap ixInfo, final boolean skipCreateUniqueIndex)\n
    enableRichTextSearch(final String tbname, final String colName, final String handleColName, final HashMap ixInfo, final boolean skipCreateUniqueIndex, final int startIxNum)\n
    enableRichTextSearch(String tbname, String colName, final String handleColName, final HashMap ixInfo, final boolean skipCreateUniqueIndex, final int startIxNum, final boolean skipDb2Connect)\n
    '''
def getDB2TextIndexSpace():
    '''returns String\n\n
    getDB2TextIndexSpace()\n
    '''
def isRTSupportedForDB():
    '''returns boolean\n\n
    isRTSupportedForDB()\n
    '''
def revalidateTextSearchIndexes():
    '''returns ArrayList<String>\n\n
    revalidateTextSearchIndexes(final String tbname)\n
    '''
def isReorgPending():
    '''returns boolean\n\n
    isReorgPending(final String tbname)\n
    '''
def reorgTable():
    '''returns ArrayList<String>\n\n
    reorgTable(final String tbname, final boolean redoTriggers)\n
    '''
def db2textAlterIndexes():
    '''returns ArrayList<String>\n\n
    db2textAlterIndexes()\n
    db2textAlterIndexes(final boolean updateNow)\n
    '''
def activateRichTextSearch():
    '''returns ArrayList<String>\n\n
    activateRichTextSearch(final ArrayList<String> list, final String tbname, final boolean doCheck)\n
    '''
def disableRichTextSearch():
    '''returns ArrayList<String>\n\n
    disableRichTextSearch(final String tbname, String colName, final String handleColName)\n
    '''
def getTextSearchIndexForColumn():
    '''returns HashMap\n\n
    getTextSearchIndexForColumn(final String tbname, final String colName, TreeMap tbIndexes)\n
    '''
def getRenameTableStatement():
    '''returns String\n\n
    getRenameTableStatement(final String oldTbname, final String newTbname)\n
    '''
def getDropStatisticsStatementsForConfig():
    '''returns ArrayList\n\n
    getDropStatisticsStatementsForConfig(final String entityname)\n
    '''
def getDropStatisticsStatements():
    '''returns ArrayList<String>\n\n
    getDropStatisticsStatements(String tbname, String colname)\n
    '''
def canAnalyzeTable():
    '''returns boolean\n\n
    canAnalyzeTable()\n
    '''
def getAnalyzeTableStatement():
    '''returns ArrayList<String>\n\n
    getAnalyzeTableStatement(String tbname)\n
    '''
def getDisallowPageLocks():
    '''returns ArrayList<String>\n\n
    getDisallowPageLocks()\n
    '''
def lockMaximoTables():
    '''returns boolean\n\n
    lockMaximoTables(String tbname, final boolean lock)\n
    '''
def isObjectLocked():
    '''returns boolean\n\n
    isObjectLocked(final String entityname)\n
    '''
def isReservedWord():
    '''returns boolean\n\n
    isReservedWord(final String testWord)\n
    '''
def getAttributeRefresh():
    '''returns ArrayList<String>\n\n
    getAttributeRefresh()\n
    getAttributeRefresh(final int tenantId, final boolean mtEnabled, final String objectName)\n
    '''
def getAttributeCfgRefresh():
    '''returns ArrayList<String>\n\n
    getAttributeCfgRefresh()\n
    getAttributeCfgRefresh(final int tenantId, final boolean mtEnabled)\n
    '''
def getViewColumnRefresh():
    '''returns String\n\n
    getViewColumnRefresh()\n
    getViewColumnRefresh(final int tenantId, final boolean mtEnabled)\n
    '''
def getViewColumnCfgRefresh():
    '''returns String\n\n
    getViewColumnCfgRefresh()\n
    getViewColumnCfgRefresh(final int tenantId, final boolean mtEnabled)\n
    '''
def getTableRefresh():
    '''returns String\n\n
    getTableRefresh()\n
    getTableRefresh(final int tenantId, final boolean mtEnabled, final String tableName)\n
    '''
def getTableCfgRefresh():
    '''returns String\n\n
    getTableCfgRefresh()\n
    getTableCfgRefresh(final int tenantId, final boolean mtEnabled)\n
    '''
def getViewRefresh():
    '''returns String\n\n
    getViewRefresh()\n
    getViewRefresh(final int tenantId, final boolean mtEnabled)\n
    '''
def getViewCfgRefresh():
    '''returns String\n\n
    getViewCfgRefresh()\n
    getViewCfgRefresh(final int tenantId, final boolean mtEnabled)\n
    '''
def deleteObjectDelta():
    '''returns ArrayList<String>\n\n
    deleteObjectDelta(final int tenantId)\n
    '''
def getObjectRefresh():
    '''returns ArrayList<String>\n\n
    getObjectRefresh()\n
    getObjectRefresh(final int tenantId, final boolean mtEnabled, final String objectName)\n
    '''
def getObjectCfgRefresh():
    '''returns ArrayList<String>\n\n
    getObjectCfgRefresh()\n
    getObjectCfgRefresh(final int tenantId, final boolean mtEnabled)\n
    '''
def getSysIndexRefresh():
    '''returns ArrayList<String>\n\n
    getSysIndexRefresh(String tbname, String ixname)\n
    '''
def updateIndexRequired():
    '''returns List<String>\n\n
    updateIndexRequired()\n
    '''
def longIndexNamesExist():
    '''returns boolean\n\n
    longIndexNamesExist(final String tbname)\n
    '''
def dupIndexNamesExist():
    '''returns boolean\n\n
    dupIndexNamesExist(final String tbname, final String ixname)\n
    '''
def descendingIndexesSupported():
    '''returns boolean\n\n
    descendingIndexesSupported()\n
    '''
def getPartitionRefresh():
    '''returns ArrayList<String>\n\n
    getPartitionRefresh()\n
    '''
def getOracleVersion():
    '''returns double\n\n
    getOracleVersion()\n
    getOracleVersion(final boolean getPoint)\n
    '''
def getDB2Version():
    '''returns double\n\n
    getDB2Version()\n
    getDB2Version(final boolean getPoint)\n
    '''
def getSqlServerVersion():
    '''returns double\n\n
    getSqlServerVersion()\n
    getSqlServerVersion(final boolean getPoint)\n
    '''
def getSqlServerCompatLevel():
    '''returns int\n\n
    getSqlServerCompatLevel()\n
    '''
def getUpdateStatistics():
    '''returns ArrayList<String>\n\n
    getUpdateStatistics(final TreeMap tableMap, final TreeMap indexMap)\n
    '''
def getRemoveChanges():
    '''returns ArrayList<String>\n\n
    getRemoveChanges()\n
    '''
def getRemoveTenantChanges():
    '''returns ArrayList<String>\n\n
    getRemoveTenantChanges(final int tenantid, final boolean mtEnabled)\n
    '''
def getApplyTenantChanges():
    '''returns ArrayList<String>\n\n
    getApplyTenantChanges(final int tenantid, final boolean mtEnabled)\n
    '''
def objAttrDelRefresh():
    '''returns ArrayList<String>\n\n
    objAttrDelRefresh(final int tenantid, final boolean mtEnabled)\n
    '''
def attrRefresh():
    '''returns ArrayList<String>\n\n
    attrRefresh(final int tenantid, final boolean mtEnabled)\n
    '''
def renumberAttributeNumber():
    '''returns ArrayList<String>\n\n
    renumberAttributeNumber(final String objectname, final TreeMap attrs)\n
    '''
def renumberExtAttributeNumber():
    '''returns ArrayList<String>\n\n
    renumberExtAttributeNumber(final String objectname, final Map extTables, final int start, ArrayList<String> sqlList)\n
    '''
def indexMetaExistsForPrikeycolseq():
    '''returns boolean\n\n
    indexMetaExistsForPrikeycolseq(String objname, String tbname, final boolean getCfg)\n
    '''
def buildIndexStatement():
    '''returns String\n\n
    buildIndexStatement(final String tbname, final TreeMap tableCols, final String dbstoragepartition)\n
    buildIndexStatement(final HashMap ixInfo, final boolean specifySchema, final boolean specifyStorage)\n
    '''
def rebuildIndexes():
    '''returns ArrayList<String>\n\n
    rebuildIndexes(final TreeMap indexMeta, final boolean alwaysDrop, final boolean neverDrop, final boolean specifySchema, final boolean specifyStorage)\n
    '''
def adjustPrimaryKeyColSeq():
    '''returns ArrayList<String>\n\n
    adjustPrimaryKeyColSeq(final TreeMap indexMeta)\n
    '''
def buildSequences():
    '''returns ArrayList<String>\n\n
    buildSequences(final HashSet sequences, final boolean doMaxseq)\n
    buildSequences(final HashSet sequences, final Map<String, Long> alreadyDone, final boolean doMaxseq)\n
    '''
def updateMaxSequence():
    '''returns ArrayList<String>\n\n
    updateMaxSequence(final HashSet sequences)\n
    updateMaxSequence(final HashSet sequences, final Map<String, Long> lastNumbers)\n
    '''
def getNextSequenceNo():
    '''returns long\n\n
    getNextSequenceNo(final String sequenceName)\n
    '''
def rebuildMetadataSequences():
    '''returns ArrayList<String>\n\n
    rebuildMetadataSequences()\n
    '''
def getMetadataSequenceNames():
    '''returns HashSet<String[]>\n\n
    getMetadataSequenceNames()\n
    '''
def getMaxEAuditTransID():
    '''returns int\n\n
    getMaxEAuditTransID()\n
    '''
def createOneSequenceFromMaxSequence():
    '''returns ArrayList<String>\n\n
    createOneSequenceFromMaxSequence(final String sequenceName)\n
    '''
def getUnrestoredTables():
    '''returns String\n\n
    getUnrestoredTables(final String tbname)\n
    '''
def getBackupTableName():
    '''returns String\n\n
    getBackupTableName(final String tbname)\n
    '''
def getOldBackupTables():
    '''returns String\n\n
    getOldBackupTables(final String tbname)\n
    '''
def clearAlreadyDidUsingMultiSchema():
    '''returns None\n\n
    clearAlreadyDidUsingMultiSchema()\n
    '''
def usingMultiSchema():
    '''returns boolean\n\n
    usingMultiSchema()\n
    '''
def getSiteOrgType():
    '''returns String\n\n
    getSiteOrgType(final String objectname)\n
    '''
def getStoragePartition():
    '''returns String\n\n
    getStoragePartition(final String tbname)\n
    '''
def getUniqueIndexSpace():
    '''returns String\n\n
    getUniqueIndexSpace(final String tbname, final String tbPartition)\n
    '''
def getLangColumnName():
    '''returns String\n\n
    getLangColumnName(final String tbname)\n
    '''
def getUniqueColumnName():
    '''returns String\n\n
    getUniqueColumnName(final String tbname)\n
    '''
def getUniqueColumnNameNative():
    '''returns String\n\n
    getUniqueColumnNameNative(final String tbname)\n
    '''
def getObjectName():
    '''returns String\n\n
    getObjectName(final String entityname, final boolean useIsViewConstraint, final boolean isView)\n
    '''
def getTableName():
    '''returns String\n\n
    getTableName(final String objectname)\n
    '''
def getStorageType():
    '''returns MTStorageType\n\n
    getStorageType(final String tableName)\n
    '''
def getViewName():
    '''returns String\n\n
    getViewName(final String objectname)\n
    '''
def getAttributeName():
    '''returns String\n\n
    getAttributeName(final String objectname, final String tablename, final String columnname)\n
    '''
def getColumnName():
    '''returns String[]\n\n
    getColumnName(final String objectname, final String attributename)\n
    '''
def getKeyAttribute():
    '''returns String\n\n
    getKeyAttribute(String objectname, String tablename)\n
    '''
def getIndexNamesForColumn():
    '''returns ArrayList<String>\n\n
    getIndexNamesForColumn(final String tbname, final String colName)\n
    '''
def getMaxvar():
    '''returns String\n\n
    getMaxvar(String varname, final boolean getDefault)\n
    '''
def getYes():
    '''returns String\n\n
    getYes()\n
    '''
def getNo():
    '''returns String\n\n
    getNo()\n
    '''
def getMaxUpgVersion():
    '''returns String\n\n
    getMaxUpgVersion()\n
    '''
def nativeTableExists():
    '''returns boolean\n\n
    nativeTableExists(final String tbname)\n
    '''
def nativeColumnExists():
    '''returns boolean\n\n
    nativeColumnExists(final String tbname, final String name)\n
    '''
def nativeViewExists():
    '''returns boolean\n\n
    nativeViewExists(final String vname)\n
    '''
def nativeIndexExists():
    '''returns boolean\n\n
    nativeIndexExists(final String ixname, final String tbname)\n
    '''
def nativeIndexExistsForColumn():
    '''returns ArrayList<String>\n\n
    nativeIndexExistsForColumn(final String tbname, final String name)\n
    '''
def nativeIndexExistsForColumns():
    '''returns String\n\n
    nativeIndexExistsForColumns(final String tbname, final Object[] names)\n
    nativeIndexExistsForColumns(final String tbname, final Object[] names, final boolean ignoreTS)\n
    '''
def cleanStatisticNames():
    '''returns ArrayList<String>\n\n
    cleanStatisticNames()\n
    '''
def fixMetadataForDescendingKeys():
    '''returns ArrayList<String>\n\n
    fixMetadataForDescendingKeys(String tbname, String ixname)\n
    '''
def nativeIndexIsUnique():
    '''returns boolean\n\n
    nativeIndexIsUnique(final String ixname)\n
    '''
def nativeIndexIsPrimaryKey():
    '''returns boolean\n\n
    nativeIndexIsPrimaryKey(final String ixname)\n
    '''
def nativeColumnIsNullable():
    '''returns boolean\n\n
    nativeColumnIsNullable(final String tbname, final String name)\n
    '''
def addTenantIDIndex():
    '''returns ArrayList<String>\n\n
    addTenantIDIndex(final String tbname, String storagepartition, final MTStorageType storageType)\n
    '''
def addIndex():
    '''returns ArrayList<String>\n\n
    addIndex(final String tbname, String[] names, String startWith, final boolean addUnique, String storagepartition)\n
    '''
def getNewIndexName():
    '''returns String\n\n
    getNewIndexName(final String tbname, int startWith)\n
    '''
def nativeDefaultConstraintExists():
    '''returns ArrayList<String>\n\n
    nativeDefaultConstraintExists(final String tbname, final String name)\n
    '''
def nativeTriggerExists():
    '''returns boolean\n\n
    nativeTriggerExists(final String trigname)\n
    '''
def nativeSequenceExists():
    '''returns boolean\n\n
    nativeSequenceExists(final String name)\n
    '''
def isNickname():
    '''returns boolean\n\n
    isNickname(final String name)\n
    '''
def isSysYORN():
    '''returns boolean\n\n
    isSysYORN(String attrName)\n
    '''
def isSysNumeric():
    '''returns boolean\n\n
    isSysNumeric(String attrName)\n
    '''
def adjustViewMeta():
    '''returns ArrayList<String>\n\n
    adjustViewMeta(final String viewname)\n
    adjustViewMeta(String viewname, final boolean addP, final boolean addNP)\n
    '''
def getMaximumColumnNameLength():
    '''returns int\n\n
    getMaximumColumnNameLength()\n
    '''
def useQuotes():
    '''returns boolean\n\n
    useQuotes(String maxtype)\n
    '''
def singleToDoubleQuotes():
    '''returns String\n\n
    singleToDoubleQuotes(final String in)\n
    '''
def toggleStringConcat():
    '''returns String\n\n
    toggleStringConcat(final String inString, final String inConcat, final String outConcat)\n
    '''
def getNativeType():
    '''returns String\n\n
    getNativeType(final String maxType, final String length, int dbPlatform)\n
    '''
def getJdbcType():
    '''returns int\n\n
    getJdbcType(String nativeType, final int dbPlatform)\n
    '''
def getNativeTypeForColumn():
    '''returns String\n\n
    getNativeTypeForColumn(final String tbname, final String name)\n
    '''
def getNativeDateDefault():
    '''returns String\n\n
    getNativeDateDefault()\n
    '''
def getNativePartition():
    '''returns String\n\n
    getNativePartition(final String tbname)\n
    '''
def spaceIsActive():
    '''returns boolean\n\n
    spaceIsActive(final String spaceName)\n
    '''
def spaceIsSysManaged():
    '''returns boolean\n\n
    spaceIsSysManaged(final String spaceName)\n
    '''
def bytesSpaceNeeded():
    '''returns int\n\n
    bytesSpaceNeeded(final String spaceName)\n
    '''
def spaceNeeded():
    '''returns Object[]\n\n
    spaceNeeded(final String spaceName)\n
    '''
def makeSpace():
    '''returns ArrayList<String>\n\n
    makeSpace(final String spaceName, final int numBytes)\n
    makeSpace(final String spaceName, final int numBytes, final String multiplier)\n
    '''
def spaceCheckForDBConfig():
    '''returns String[]\n\n
    spaceCheckForDBConfig()\n
    '''
def getStorageClause():
    '''returns String\n\n
    getStorageClause(final String name, final boolean isTable)\n
    '''
def adjustNativeSql():
    '''returns String\n\n
    adjustNativeSql(final String origSql)\n
    '''
def getMaxType():
    '''returns String\n\n
    getMaxType(final String nativeType)\n
    '''
def getDefaultStoragePartition():
    '''returns String\n\n
    getDefaultStoragePartition(final boolean checkValuelist)\n
    '''
def getDBStoragePartitions():
    '''returns ArrayList<String>\n\n
    getDBStoragePartitions()\n
    '''
def nativeSpaceExists():
    '''returns boolean\n\n
    nativeSpaceExists(final String name)\n
    '''
def needLength():
    '''returns boolean\n\n
    needLength(String maxtype, String nativeType)\n
    '''
def needScale():
    '''returns boolean\n\n
    needScale(String maxtype, String nativeType)\n
    '''
def reEvaluateObjectChanged():
    '''returns String\n\n
    reEvaluateObjectChanged(final HashMap newObject, final HashMap oldObject, final boolean useAttrChanged, final String upgradeDir)\n
    reEvaluateObjectChanged(final HashMap newObject, final HashMap oldObject, final boolean useAttrChanged, final String upgradeDir, String langcode)\n
    '''
def reEvaluateObjectChangedQuickGL():
    '''returns String\n\n
    reEvaluateObjectChangedQuickGL(final String entityname, final boolean isView, final HashMap attrs, final boolean persistent, final String origChanged)\n
    '''
def reEvaluateAttributeChangedQuickGL():
    '''returns String\n\n
    reEvaluateAttributeChangedQuickGL(final String entityname, final String columnname, final boolean isView, final int oldLength, final int newLength, final boolean persistent, final String origChanged)\n
    '''
def reEvaluateAttributeChanged():
    '''returns String\n\n
    reEvaluateAttributeChanged(final String entityname, final HashMap newAttr, final HashMap oldAttr, final String upgradeDir, final boolean isView)\n
    '''
def reEvaluateTableAttributeChanged():
    '''returns String\n\n
    reEvaluateTableAttributeChanged(final String tablename, final HashMap newAttr, final HashMap oldAttr, final String upgradeDir)\n
    '''
def reEvaluateViewAttributeChanged():
    '''returns String\n\n
    reEvaluateViewAttributeChanged(final String viewname, final HashMap newAttr, final HashMap oldAttr, final String upgradeDir)\n
    '''
def canAlterTable():
    '''returns boolean\n\n
    canAlterTable(final String tablename, final HashMap newAttr, final HashMap oldAttr, final String upgradeDir)\n
    '''
def canAlterForLengthChange():
    '''returns boolean\n\n
    canAlterForLengthChange(final String tablename, final String columnname, final int oldLength, final int newLength)\n
    '''
def upgradeDefaultExists():
    '''returns boolean\n\n
    upgradeDefaultExists(String tbname, String name, final String upgradeDir)\n
    '''
def implicitConversionSupported():
    '''returns boolean\n\n
    implicitConversionSupported(String newType, String oldType)\n
    '''
def explicitConversionSupported():
    '''returns boolean\n\n
    explicitConversionSupported(String newType, String oldType)\n
    '''
def tableIsEmpty():
    '''returns boolean\n\n
    tableIsEmpty(final String tbname)\n
    '''
def columnIsEmpty():
    '''returns boolean\n\n
    columnIsEmpty(final String tbname, final String name)\n
    '''
def nullValueExists():
    '''returns boolean\n\n
    nullValueExists(final String tbname, final String name)\n
    '''
def getMaxColumnLength():
    '''returns int\n\n
    getMaxColumnLength(final String tbname, final String name)\n
    '''
def getMaxColno():
    '''returns int\n\n
    getMaxColno(final String objectname, final boolean getCfg, final String where)\n
    '''
def getMaxLengthColumnInIndex():
    '''returns int\n\n
    getMaxLengthColumnInIndex()\n
    '''
def getMaxLengthIndex():
    '''returns int\n\n
    getMaxLengthIndex()\n
    '''
def getMaxVarcharLength():
    '''returns int\n\n
    getMaxVarcharLength()\n
    '''
def setVarcharMultiple():
    '''returns None\n\n
    setVarcharMultiple(final int val)\n
    '''
def getVarcharMultiple():
    '''returns int\n\n
    getVarcharMultiple()\n
    '''
def setVargraphic():
    '''returns None\n\n
    setVargraphic(final boolean val)\n
    '''
def useVargraphic():
    '''returns boolean\n\n
    useVargraphic()\n
    '''
def getInternalSiteOrgType():
    '''returns String\n\n
    getInternalSiteOrgType(final String externalSiteOrgType)\n
    '''
def getInternalSearchType():
    '''returns String\n\n
    getInternalSearchType(final String externalSearchType)\n
    '''
def isLocAllowed():
    '''returns boolean\n\n
    isLocAllowed(final String objectName, final String attributeName, final HashMap attrInfo, final HashMap sameasAtrInfo)\n
    '''
def getLocDefault():
    '''returns boolean\n\n
    getLocDefault(final String objectName, final String attributeName, final HashMap attrInfo, final HashMap sameasAttrInfo)\n
    '''
def nameInList():
    '''returns boolean\n\n
    nameInList(final String name, final String list)\n
    '''
def selectString():
    '''returns String\n\n
    selectString(final String sql)\n
    '''
def rowFound():
    '''returns boolean\n\n
    rowFound(final String sql)\n
    '''
def setConnection():
    '''returns None\n\n
    setConnection(final Connection connection)\n
    '''
def setPrintStream():
    '''returns None\n\n
    setPrintStream(final PrintStream outstream)\n
    '''
def setDB2tsPreferSysproc():
    '''returns None\n\n
    setDB2tsPreferSysproc(final boolean val)\n
    '''
def setDBOut():
    '''returns None\n\n
    setDBOut(final int platform)\n
    '''
def mxServerIsUp():
    '''returns boolean\n\n
    mxServerIsUp(final String serverName)\n
    '''
def configInProcess():
    '''returns boolean\n\n
    configInProcess()\n
    '''
def setConfigInProcess():
    '''returns String\n\n
    setConfigInProcess(final boolean inProcess)\n
    '''
def createStatement():
    '''returns Statement\n\n
    createStatement()\n
    '''
def prepareStatement():
    '''returns PreparedStatement\n\n
    prepareStatement(final String sql)\n
    '''
def getNextSequenceValueForSqlServer():
    '''returns String\n\n
    getNextSequenceValueForSqlServer(final String seqName)\n
    '''
def updateDMSource():
    '''returns List<String>\n\n
    updateDMSource()\n
    '''
def getDatabaseName():
    '''returns String\n\n
    getDatabaseName()\n
    '''
def getSchemaName():
    '''returns String\n\n
    getSchemaName()\n
    '''
def getDBHostName():
    '''returns String\n\n
    getDBHostName()\n
    '''
def enableForMultiTenancy():
    '''returns ArrayList<String>\n\n
    enableForMultiTenancy(final String tabName, final String uniqueName, final String userName, final String adminUser, final MTStorageType storageType)\n
    '''
def addTenantidToTable():
    '''returns ArrayList<String>\n\n
    addTenantidToTable(final String tabName, final MTStorageType storageType)\n
    '''
def changeStorageType():
    '''returns ArrayList<String>\n\n
    changeStorageType(final String tabName, final String uniqueName, final MTStorageType oldType, final MTStorageType newType, final String userName, final String adminUser, final boolean isInternal)\n
    '''
def disableMTPermission():
    '''returns ArrayList<String>\n\n
    disableMTPermission(final String tabName, final MTStorageType storageType)\n
    '''
def createPermission():
    '''returns List<String>\n\n
    createPermission(final String tabName, final String uniqueName, final String newTenantUser, final String landlordUser, final MTStorageType type)\n
    createPermission(String tabName, final String uniqueName, final String newTenantUser, final String landlordUser, MTStorageType type, final boolean addProcessUser)\n
    '''
def rebuildProcessUserVariable():
    '''returns List<String>\n\n
    rebuildProcessUserVariable(final String adminUser)\n
    '''
def rebuildPermissions():
    '''returns None\n\n
    rebuildPermissions(final String processUser)\n
    '''
def createTenantidTriggeres():
    '''returns List<String>\n\n
    createTenantidTriggeres(String tbname, final MTStorageType storageType, final boolean secureRowlevelTriggers, final boolean dropInsert, final boolean dropUpdateDelete, final boolean createDeltaTriggers)\n
    '''
def dropDeltaTriggers():
    '''returns ArrayList<String>\n\n
    dropDeltaTriggers()\n
    '''
def getDeltaTriggerSql():
    '''returns List<String>\n\n
    getDeltaTriggerSql(final String tbname)\n
    '''
def registerTableFromTemplate():
    '''returns List<String>\n\n
    registerTableFromTemplate(final String tbname, TreeMap tableCols, final String whereClause)\n
    '''
def getColumnNamesForExtendedView():
    '''returns String[]\n\n
    getColumnNamesForExtendedView(final TreeMap tableCols, final String tableName, final Map<String, Map<String, String>> extendedTables, final String uniqueColumnName, final String isView, final boolean mtEnabled)\n
    '''
def getExtendedUniqueColumnForView():
    '''returns String\n\n
    getExtendedUniqueColumnForView(final String viewName, final String extTableName)\n
    '''
def isMTEnabled():
    '''returns boolean\n\n
    isMTEnabled()\n
    '''
def getUserFromProperties():
    '''returns String\n\n
    getUserFromProperties(final boolean getLandlordUser)\n
    '''
def updateViewMetaDataForExtendedAttr():
    '''returns ArrayList<String>\n\n
    updateViewMetaDataForExtendedAttr(final Connection conn, final String objectName, final String viewName, final Map<String, Map<String, String>> extAttr, final int tenantId)\n
    '''
def createExtensionView():
    '''returns List<String>\n\n
    createExtensionView(final String objectName, final Map<String, Map<String, String>> extendedTables, final Connection masterCon, final int tenantId, final boolean deleteOnly, final boolean mtEnabled)\n
    '''
def storeChangedAttributes():
    '''returns None\n\n
    storeChangedAttributes(final HashMap<String, HashMap<String, HashMap<String, String[]>>> changedObjects, final TreeMap<String, HashMap<String, String>> attrs, final String objectname)\n
    '''
def renumberExtendedAttributes():
    '''returns ArrayList<String>\n\n
    renumberExtendedAttributes(final int tenantId, final Map<String, Integer> lastNumbers, ArrayList<String> list)\n
    '''
def getUpdateTenantDelta():
    '''returns ArrayList\n\n
    getUpdateTenantDelta(final HashMap<String, HashMap<String, HashMap<String, String[]>>> changedObjects, final int tenantId, final TreeMap<String, HashMap<String, String>> cfgAttrs, final Vector<String[]> skipList)\n
    '''
def getNextAttrNo():
    '''returns int\n\n
    getNextAttrNo(final String tablename)\n
    '''
def getTenantCodeMetadata():
    '''returns ArrayList<String>\n\n
    getTenantCodeMetadata()\n
    '''
def addTenantid():
    '''returns List<String>\n\n
    addTenantid(final String tablename, final String uniqueColumnName, final MTStorageType storageType)\n
    '''
def reorgBeforeDB2TSUpdate():
    '''returns None\n\n
    reorgBeforeDB2TSUpdate()\n
    '''
