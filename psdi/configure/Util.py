def Util():
'''public Util(final Connection conparam, final PrintStream outparam, final String schemaOwnerparam)
public Util(final Connection conparam, final PrintStream outparam, final String schemaOwnerparam, final boolean reloadAttrs)
'''
pass
def getMaxTableAttrs():
'''public String[] getMaxTableAttrs()
'''
pass
def reloadAttributeList():
'''public void reloadAttributeList()
'''
pass
def getCurrentNativeSchema():
'''public String getCurrentNativeSchema()
'''
pass
def writeDumpTable():
'''public void writeDumpTable(final String tbname, final TreeMap tableCols, final PrintStream out)
public int writeDumpTable(final String tbname, TreeMap tableCols, PrintStream out, int maxLines, int numLines, final Unlcvt unlcvt, final boolean psFormat)
'''
pass
def getData():
'''public TreeMap getData(final String tbname, TreeMap tableCols, final String where)
'''
pass
def isTable():
'''public boolean isTable(final HashMap tableInfo)
'''
pass
def buildCreateTableStatement():
'''public String buildCreateTableStatement(final HashMap tableInfo, final boolean doColDefault, final boolean includeDroppedCols, final String dbstoragepartition, final boolean specifyStorage)
public String buildCreateTableStatement(final String tbname, final TreeMap tableCols, final boolean doColDefault, final boolean includeDroppedCols, final String dbstoragepartition, final boolean addRowstamp, final String storageClause)
'''
pass
def buildCreateViewStatement():
'''public ArrayList<String> buildCreateViewStatement(final HashMap viewInfo, final boolean includeDroppedCols, final boolean forceDropStmt)
'''
pass
def getAttributeForMaxViewColumn():
'''public HashMap getAttributeForMaxViewColumn(final String viewName, final HashMap viewcolInfo, final TreeMap distinctAttrs)
'''
pass
def buildColumnLine():
'''public String buildColumnLine(final HashMap colInfo, final boolean doDefault, final boolean alter)
public String buildColumnLine(final HashMap colInfo, final boolean doDefault, final boolean doNullClause, final boolean alter)
'''
pass
def buildDefaultDataStatement():
'''public ArrayList<String> buildDefaultDataStatement(final String tbname, final TreeMap newTableCols, final String colNameList, TreeMap<String, HashMap<String, String>> oldTableCols)
public String buildDefaultDataStatement(final String tbname, final HashMap newColInfo, final HashMap oldColInfo)
'''
pass
def buildShortenStringStatement():
'''public ArrayList<String> buildShortenStringStatement(final String tbname, final TreeMap newTableCols, final TreeMap oldTableCols)
'''
pass
def buildChangeCaseStatement():
'''public ArrayList<String> buildChangeCaseStatement(final String tbname, TreeMap<String, HashMap<String, String>> oldCols, TreeMap<String, HashMap<String, String>> newCols)
public String buildChangeCaseStatement(final String tbname, final String name, final String oldMaxtype, final String newMaxtype)
'''
pass
def buildSelectStatement():
'''public String buildSelectStatement(final String tbname, final TreeMap tableCols, final boolean includeDroppedCols, final boolean addRowstamp)
public String buildSelectStatement(final String tbname, final TreeMap tableCols, final boolean includeDroppedCols, final boolean addRowstamp, final boolean addTenantID)
public String buildSelectStatement(final String tbname, final TreeMap tableCols, final boolean includeDroppedCols, final boolean addRowstamp, final boolean addtenantID, final String colNameList)
'''
pass
def buildSelectStatementForRestore():
'''public String buildSelectStatementForRestore(final String tempTbName, final TreeMap newTableCols, final boolean addRowstamp, final String colNameList, final boolean doLineBreaks)
'''
pass
def getDefaultString():
'''public String getDefaultString(final String tbname, final HashMap colInfo)
public String getDefaultString(final String tbname, final String colName, final String maxtype, final String metaDefaultValue, final String domainid)
public String getDefaultString(final String tbname, final String colName, final String maxtype, String metaDefaultValue, final String domainid, String sequenceName, final int uidRule, final int seqRule, final int autoRule, final int mboRule, final int appRule, final boolean outputQuotes, final boolean assignIfNoMeta)
'''
pass
def isSpecialDefaultValue():
'''public boolean isSpecialDefaultValue(final String value)
'''
pass
def getOracleConvertString():
'''public String getOracleConvertString(String oldNativeType, String newNativeType, final String colName)
'''
pass
def getSqlServerConvertString():
'''public String getSqlServerConvertString(final String oldTbname, final String newTbname, final HashMap newColInfo)
'''
pass
def getDB2ConvertString():
'''public String getDB2ConvertString(String oldNativeType, String newNativeType, final String colName)
'''
pass
def nativeTypesAreCompatible():
'''public boolean nativeTypesAreCompatible(String oldNativeType, String newNativeType)
'''
pass
def buildInsertStatementPrefix():
'''public String buildInsertStatementPrefix(final String tbname, final TreeMap tableCols, final boolean doRowstamp, final boolean includeDroppedCols)
public String buildInsertStatementPrefix(final String tbname, final TreeMap tableCols, final boolean doRowstamp, final boolean includeDroppedCols, final String colNameList, final boolean doLineBreaks)
public String buildInsertStatementPrefix(final String tbname, final TreeMap tableCols, final boolean doRowstamp, final boolean includeDroppedCols, final String colNameList, final boolean doLineBreaks, final boolean addTenantid)
'''
pass
def buildInsertValuesStatement():
'''public TreeMap buildInsertValuesStatement(final String prefix, final ResultSet rs, final TreeMap tableCols, final boolean includeDroppedCols, final String rowstampValue)
public TreeMap<Integer, String> buildInsertValuesStatement(final String prefix, final ResultSet rs, final TreeMap tableCols, final boolean includeDroppedCols, final String rowstampValue, final boolean psFormat)
public TreeMap<Integer, String> buildInsertValuesStatement(final String prefix, final ResultSet rs, final TreeMap tableCols, final boolean includeDroppedCols, final String rowstampValue, final boolean psFormat, final Map<String, String> allSeq)
public TreeMap<Integer, String> buildInsertValuesStatement(final String prefix, final ResultSet rs, final TreeMap tableCols, final boolean includeDroppedCols, final String rowstampValue, final boolean psFormat, final Map<String, String> allSeq, final int tenantid)
'''
pass
def getKeyColumns():
'''public TreeMap<String, String> getKeyColumns(final TreeMap indexMeta, final TreeMap tableCols, final String indexToSkip)
'''
pass
def getColumnNames():
'''public String getColumnNames(final TreeMap tableCols, final boolean doLineBreaks, final boolean includeDroppedCols)
public String getColumnNames(final TreeMap tableCols, final boolean doLineBreaks, final boolean includeDroppedCols, final String colNameList, final boolean useAlias)
'''
pass
def processTemplateData():
'''public void processTemplateData(final int toTenantid, final boolean delete, final String maxUserGroup, final String allUserGroup, final String newUserGroup, final PrintStream out)
'''
pass
def copyData():
'''public void copyData(final String tabName, final String uniqueColumn, final int toTenantid, final int storageType, final boolean delete, final PrintStream out)
'''
pass
def updateGroupName():
'''public void updateGroupName(final String tabName, final String maxUserGroup, final String allUserGroup, final String newUserGroup, final int toTenantid)
'''
pass
def getColumnNamesNative():
'''public String getColumnNamesNative(final String tbname)
'''
pass
def getColumnInfo():
'''public HashMap getColumnInfo(final TreeMap tableCols, String name)
'''
pass
def getAddRowstampSql():
'''public String getAddRowstampSql(final String tbname)
'''
pass
def getRowstampTriggerSql():
'''public ArrayList<String> getRowstampTriggerSql(final String tbname, final boolean dropIfExists)
public ArrayList<String> getRowstampTriggerSql(final String tbname, final boolean dropIfExists, final boolean makeSecure)
'''
pass
def getTrigRoot():
'''public String getTrigRoot(final String tbname)
'''
pass
def buildGrants():
'''public ArrayList<String> buildGrants(final String tbname, final boolean outputSchema, final boolean maxusersOnly)
'''
pass
def getGrants():
'''public HashMap<String, int[]> getGrants(final String username, final String entityname)
'''
pass
def getGrantSql():
'''public String getGrantSql(final String dbUserID, final String entityname, final String privilege, final boolean grant)
'''
pass
def getTriggerNames():
'''public ArrayList<String> getTriggerNames(final String tbname, final boolean getEnabled, final boolean getDisabled, final boolean includeRowstamp)
'''
pass
def getEnableTriggerStatement():
'''public String getEnableTriggerStatement(final String triggerName, final String tbname)
'''
pass
def getDisableTriggerStatement():
'''public String getDisableTriggerStatement(final String triggerName, final String tbname)
'''
pass
def getEnableDisableTriggersAll():
'''public String getEnableDisableTriggersAll(final String tbname, final boolean enable)
'''
pass
def changeAmountFormat():
'''public ArrayList<String> changeAmountFormat(final int newLength, final int newScale)
'''
pass
def isRichTextSupported():
'''public boolean isRichTextSupported(String tbname, String name)
'''
pass
def isHandleColumn():
'''public boolean isHandleColumn(final String colName, final TreeMap attrs)
'''
pass
def enableRichTextSearch():
'''public ArrayList<String> enableRichTextSearch(final HashMap objInfo, final TreeMap tbIndexes, final boolean doCheck, final boolean skipDb2Connect)
public ArrayList<String> enableRichTextSearch(final String tbname, final String colName, final String handleColName, final HashMap ixInfo, final boolean skipCreateUniqueIndex)
public ArrayList<String> enableRichTextSearch(final String tbname, final String colName, final String handleColName, final HashMap ixInfo, final boolean skipCreateUniqueIndex, final int startIxNum)
public ArrayList<String> enableRichTextSearch(String tbname, String colName, final String handleColName, final HashMap ixInfo, final boolean skipCreateUniqueIndex, final int startIxNum, final boolean skipDb2Connect)
'''
pass
def getDB2TextIndexSpace():
'''public String getDB2TextIndexSpace()
'''
pass
def isRTSupportedForDB():
'''public boolean isRTSupportedForDB()
'''
pass
def revalidateTextSearchIndexes():
'''public ArrayList<String> revalidateTextSearchIndexes(final String tbname)
'''
pass
def isReorgPending():
'''public boolean isReorgPending(final String tbname)
'''
pass
def reorgTable():
'''public ArrayList<String> reorgTable(final String tbname, final boolean redoTriggers)
'''
pass
def db2textAlterIndexes():
'''public ArrayList<String> db2textAlterIndexes()
public ArrayList<String> db2textAlterIndexes(final boolean updateNow)
'''
pass
def activateRichTextSearch():
'''public ArrayList<String> activateRichTextSearch(final ArrayList<String> list, final String tbname, final boolean doCheck)
'''
pass
def disableRichTextSearch():
'''public ArrayList<String> disableRichTextSearch(final String tbname, String colName, final String handleColName)
'''
pass
def getTextSearchIndexForColumn():
'''public HashMap getTextSearchIndexForColumn(final String tbname, final String colName, TreeMap tbIndexes)
'''
pass
def getRenameTableStatement():
'''public String getRenameTableStatement(final String oldTbname, final String newTbname)
'''
pass
def getDropStatisticsStatementsForConfig():
'''public ArrayList getDropStatisticsStatementsForConfig(final String entityname)
'''
pass
def getDropStatisticsStatements():
'''public ArrayList<String> getDropStatisticsStatements(String tbname, String colname)
'''
pass
def canAnalyzeTable():
'''public boolean canAnalyzeTable()
'''
pass
def getAnalyzeTableStatement():
'''public ArrayList<String> getAnalyzeTableStatement(String tbname)
'''
pass
def getDisallowPageLocks():
'''public ArrayList<String> getDisallowPageLocks()
'''
pass
def lockMaximoTables():
'''public boolean lockMaximoTables(String tbname, final boolean lock)
'''
pass
def isObjectLocked():
'''public boolean isObjectLocked(final String entityname)
'''
pass
def isReservedWord():
'''public boolean isReservedWord(final String testWord)
'''
pass
def getAttributeRefresh():
'''public ArrayList<String> getAttributeRefresh()
public ArrayList<String> getAttributeRefresh(final int tenantId, final boolean mtEnabled, final String objectName)
'''
pass
def getAttributeCfgRefresh():
'''public ArrayList<String> getAttributeCfgRefresh()
public ArrayList<String> getAttributeCfgRefresh(final int tenantId, final boolean mtEnabled)
'''
pass
def getViewColumnRefresh():
'''public String getViewColumnRefresh()
public String getViewColumnRefresh(final int tenantId, final boolean mtEnabled)
'''
pass
def getViewColumnCfgRefresh():
'''public String getViewColumnCfgRefresh()
public String getViewColumnCfgRefresh(final int tenantId, final boolean mtEnabled)
'''
pass
def getTableRefresh():
'''public String getTableRefresh()
public String getTableRefresh(final int tenantId, final boolean mtEnabled, final String tableName)
'''
pass
def getTableCfgRefresh():
'''public String getTableCfgRefresh()
public String getTableCfgRefresh(final int tenantId, final boolean mtEnabled)
'''
pass
def getViewRefresh():
'''public String getViewRefresh()
public String getViewRefresh(final int tenantId, final boolean mtEnabled)
'''
pass
def getViewCfgRefresh():
'''public String getViewCfgRefresh()
public String getViewCfgRefresh(final int tenantId, final boolean mtEnabled)
'''
pass
def deleteObjectDelta():
'''public ArrayList<String> deleteObjectDelta(final int tenantId)
'''
pass
def getObjectRefresh():
'''public ArrayList<String> getObjectRefresh()
public ArrayList<String> getObjectRefresh(final int tenantId, final boolean mtEnabled, final String objectName)
'''
pass
def getObjectCfgRefresh():
'''public ArrayList<String> getObjectCfgRefresh()
public ArrayList<String> getObjectCfgRefresh(final int tenantId, final boolean mtEnabled)
'''
pass
def getSysIndexRefresh():
'''public ArrayList<String> getSysIndexRefresh(String tbname, String ixname)
'''
pass
def updateIndexRequired():
'''public List<String> updateIndexRequired()
'''
pass
def longIndexNamesExist():
'''public boolean longIndexNamesExist(final String tbname)
'''
pass
def dupIndexNamesExist():
'''public boolean dupIndexNamesExist(final String tbname, final String ixname)
'''
pass
def descendingIndexesSupported():
'''public boolean descendingIndexesSupported()
'''
pass
def getPartitionRefresh():
'''public ArrayList<String> getPartitionRefresh()
'''
pass
def getOracleVersion():
'''public int getOracleVersion()
public double getOracleVersion(final boolean getPoint)
'''
pass
def getDB2Version():
'''public int getDB2Version()
public double getDB2Version(final boolean getPoint)
'''
pass
def getSqlServerVersion():
'''public int getSqlServerVersion()
public double getSqlServerVersion(final boolean getPoint)
'''
pass
def getSqlServerCompatLevel():
'''public int getSqlServerCompatLevel()
'''
pass
def getUpdateStatistics():
'''public ArrayList<String> getUpdateStatistics(final TreeMap tableMap, final TreeMap indexMap)
'''
pass
def getRemoveChanges():
'''public ArrayList<String> getRemoveChanges()
'''
pass
def getRemoveTenantChanges():
'''public ArrayList<String> getRemoveTenantChanges(final int tenantid, final boolean mtEnabled)
'''
pass
def getApplyTenantChanges():
'''public ArrayList<String> getApplyTenantChanges(final int tenantid, final boolean mtEnabled)
'''
pass
def objAttrDelRefresh():
'''public ArrayList<String> objAttrDelRefresh(final int tenantid, final boolean mtEnabled)
'''
pass
def attrRefresh():
'''public ArrayList<String> attrRefresh(final int tenantid, final boolean mtEnabled)
'''
pass
def renumberAttributeNumber():
'''public ArrayList<String> renumberAttributeNumber(final String objectname, final TreeMap attrs)
'''
pass
def renumberExtAttributeNumber():
'''public ArrayList<String> renumberExtAttributeNumber(final String objectname, final Map extTables, final int start, ArrayList<String> sqlList)
'''
pass
def getPrimaryKeys():
'''public TreeMap<String, String> getPrimaryKeys(String objname, final boolean getCfg)
'''
pass
def indexMetaExistsForPrikeycolseq():
'''public boolean indexMetaExistsForPrikeycolseq(String objname, String tbname, final boolean getCfg)
'''
pass
def buildIndexStatement():
'''public String buildIndexStatement(final String tbname, final TreeMap tableCols, final String dbstoragepartition)
public String buildIndexStatement(final HashMap ixInfo, final boolean specifySchema, final boolean specifyStorage)
'''
pass
def rebuildIndexes():
'''public ArrayList<String> rebuildIndexes(final TreeMap indexMeta, final boolean alwaysDrop, final boolean neverDrop, final boolean specifySchema, final boolean specifyStorage)
'''
pass
def adjustPrimaryKeyColSeq():
'''public ArrayList<String> adjustPrimaryKeyColSeq(final TreeMap indexMeta)
'''
pass
def buildSequences():
'''public ArrayList<String> buildSequences(final HashSet sequences, final boolean doMaxseq)
public ArrayList<String> buildSequences(final HashSet sequences, final Map<String, Long> alreadyDone, final boolean doMaxseq)
'''
pass
def updateMaxSequence():
'''public ArrayList<String> updateMaxSequence(final HashSet sequences)
public ArrayList<String> updateMaxSequence(final HashSet sequences, final Map<String, Long> lastNumbers)
'''
pass
def getNextSequenceNo():
'''public long getNextSequenceNo(final String sequenceName)
'''
pass
def rebuildMetadataSequences():
'''public ArrayList<String> rebuildMetadataSequences()
'''
pass
def getMetadataSequenceNames():
'''public HashSet<String[]> getMetadataSequenceNames()
'''
pass
def getMaxEAuditTransID():
'''public int getMaxEAuditTransID()
'''
pass
def createOneSequenceFromMaxSequence():
'''public ArrayList<String> createOneSequenceFromMaxSequence(final String sequenceName)
'''
pass
def getUnrestoredTables():
'''public String getUnrestoredTables(final String tbname)
'''
pass
def getBackupTableName():
'''public String getBackupTableName(final String tbname)
'''
pass
def getOldBackupTables():
'''public String getOldBackupTables(final String tbname)
'''
pass
def clearAlreadyDidUsingMultiSchema():
'''public void clearAlreadyDidUsingMultiSchema()
'''
pass
def usingMultiSchema():
'''public boolean usingMultiSchema()
'''
pass
def getSites():
'''public TreeMap<String, String> getSites(final boolean includeDisabled)
'''
pass
def getOrgs():
'''public TreeMap<String, String> getOrgs(final boolean includeDisabled)
'''
pass
def getSiteOrgType():
'''public String getSiteOrgType(final String objectname)
'''
pass
def getStoragePartition():
'''public String getStoragePartition(final String tbname)
'''
pass
def getUniqueIndexSpace():
'''public String getUniqueIndexSpace(final String tbname, final String tbPartition)
'''
pass
def getLangColumnName():
'''public String getLangColumnName(final String tbname)
'''
pass
def getUniqueColumnName():
'''public String getUniqueColumnName(final String tbname)
'''
pass
def getUniqueColumnNameNative():
'''public String getUniqueColumnNameNative(final String tbname)
'''
pass
def getObjectName():
'''public String getObjectName(final String entityname, final boolean useIsViewConstraint, final boolean isView)
'''
pass
def getTableName():
'''public String getTableName(final String objectname)
'''
pass
def getStorageType():
'''public MTStorageType getStorageType(final String tableName)
'''
pass
def getViewName():
'''public String getViewName(final String objectname)
'''
pass
def getAttributeName():
'''public String getAttributeName(final String objectname, final String tablename, final String columnname)
'''
pass
def getColumnName():
'''public String[] getColumnName(final String objectname, final String attributename)
'''
pass
def getKeyAttribute():
'''public String getKeyAttribute(String objectname, String tablename)
'''
pass
def getObjectMeta():
'''public TreeMap<String, HashMap<String, Object>> getObjectMeta(String objectname, final boolean getCfg, final boolean getPersistentOnly, boolean getChangedOnly, final boolean getColumns, final boolean colsOrderByName, boolean getTablesOnly, boolean getViewsOnly)
'''
pass
def getAttributeMeta():
'''public TreeMap<String, TreeMap<String, HashMap<String, String>>> getAttributeMeta(final String objectname, final boolean getCfg, final boolean orderByName, final boolean getPersistentOnly, boolean getChangedOnly, final boolean selectView, final String entityName)
'''
pass
def getTenantAttributeMeta():
'''public HashMap<String, HashMap<String, String>> getTenantAttributeMeta(final String objectname, final int tenantId)
'''
pass
def gettenantSameAsExtendedAtributes():
'''public Map<String, List<String>> gettenantSameAsExtendedAtributes(final int tenantId)
'''
pass
def getIndexMeta():
'''public TreeMap<String, HashMap<String, Object>> getIndexMeta(final String tbname, final boolean getChangedOnly)
public TreeMap<String, HashMap<String, Object>> getIndexMeta(final String tbname, final boolean getChangedOnly, final boolean getPrimary)
public TreeMap<String, HashMap<String, Object>> getIndexMeta(final String tbname, final boolean getChangedOnly, final boolean getPrimary, final boolean includeDeleted)
'''
pass
def getIndexNamesForColumn():
'''public ArrayList<String> getIndexNamesForColumn(final String tbname, final String colName)
'''
pass
def getMaxvar():
'''public String getMaxvar(String varname, final boolean getDefault)
'''
pass
def getYes():
'''public String getYes()
'''
pass
def getNo():
'''public String getNo()
'''
pass
def getMaxUpgVersion():
'''public String getMaxUpgVersion()
'''
pass
def nativeTableExists():
'''public boolean nativeTableExists(final String tbname)
'''
pass
def nativeColumnExists():
'''public boolean nativeColumnExists(final String tbname, final String name)
'''
pass
def nativeViewExists():
'''public boolean nativeViewExists(final String vname)
'''
pass
def nativeIndexExists():
'''public boolean nativeIndexExists(final String ixname, final String tbname)
'''
pass
def nativeIndexExistsForColumn():
'''public ArrayList<String> nativeIndexExistsForColumn(final String tbname, final String name)
'''
pass
def nativeIndexExistsForColumns():
'''public String nativeIndexExistsForColumns(final String tbname, final Object[] names)
public String nativeIndexExistsForColumns(final String tbname, final Object[] names, final boolean ignoreTS)
'''
pass
def cleanStatisticNames():
'''public ArrayList<String> cleanStatisticNames()
'''
pass
def fixMetadataForDescendingKeys():
'''public ArrayList<String> fixMetadataForDescendingKeys(String tbname, String ixname)
'''
pass
def nativeIndexIsUnique():
'''public boolean nativeIndexIsUnique(final String ixname)
'''
pass
def nativeIndexIsPrimaryKey():
'''public boolean nativeIndexIsPrimaryKey(final String ixname)
'''
pass
def nativeColumnIsNullable():
'''public boolean nativeColumnIsNullable(final String tbname, final String name)
'''
pass
def addTenantIDIndex():
'''public ArrayList<String> addTenantIDIndex(final String tbname, String storagepartition, final MTStorageType storageType)
'''
pass
def addIndex():
'''public ArrayList<String> addIndex(final String tbname, String[] names, String startWith, final boolean addUnique, String storagepartition)
'''
pass
def getNewIndexName():
'''public String getNewIndexName(final String tbname, int startWith)
'''
pass
def nativeDefaultConstraintExists():
'''public ArrayList<String> nativeDefaultConstraintExists(final String tbname, final String name)
'''
pass
def nativeTriggerExists():
'''public boolean nativeTriggerExists(final String trigname)
'''
pass
def nativeSequenceExists():
'''public boolean nativeSequenceExists(final String name)
'''
pass
def isNickname():
'''public boolean isNickname(final String name)
'''
pass
def isSysYORN():
'''public boolean isSysYORN(String attrName)
'''
pass
def isSysNumeric():
'''public boolean isSysNumeric(String attrName)
'''
pass
def adjustViewMeta():
'''public ArrayList<String> adjustViewMeta(final String viewname)
public ArrayList<String> adjustViewMeta(String viewname, final boolean addP, final boolean addNP)
'''
pass
def getMaximumColumnNameLength():
'''public int getMaximumColumnNameLength()
'''
pass
def useQuotes():
'''public boolean useQuotes(String maxtype)
'''
pass
def singleToDoubleQuotes():
'''public String singleToDoubleQuotes(final String in)
'''
pass
def toggleStringConcat():
'''public String toggleStringConcat(final String inString, final String inConcat, final String outConcat)
'''
pass
def getNativeType():
'''public String getNativeType(final String maxType, final String length, int dbPlatform)
'''
pass
def getJdbcType():
'''public int getJdbcType(String nativeType, final int dbPlatform)
'''
pass
def getNativeTypeForColumn():
'''public String getNativeTypeForColumn(final String tbname, final String name)
'''
pass
def getNativeDateDefault():
'''public String getNativeDateDefault()
'''
pass
def getNativePartition():
'''public String getNativePartition(final String tbname)
'''
pass
def spaceIsActive():
'''public boolean spaceIsActive(final String spaceName)
'''
pass
def spaceIsSysManaged():
'''public boolean spaceIsSysManaged(final String spaceName)
'''
pass
def bytesSpaceNeeded():
'''public int bytesSpaceNeeded(final String spaceName)
'''
pass
def spaceNeeded():
'''public Object[] spaceNeeded(final String spaceName)
'''
pass
def makeSpace():
'''public ArrayList<String> makeSpace(final String spaceName, final int numBytes)
public ArrayList<String> makeSpace(final String spaceName, final int numBytes, final String multiplier)
'''
pass
def spaceCheckForDBConfig():
'''public String[] spaceCheckForDBConfig()
'''
pass
def getStorageClause():
'''public String getStorageClause(final String name, final boolean isTable)
'''
pass
def adjustNativeSql():
'''public String adjustNativeSql(final String origSql)
'''
pass
def getMaxType():
'''public String getMaxType(final String nativeType)
'''
pass
def getDefaultStoragePartition():
'''public String getDefaultStoragePartition(final boolean checkValuelist)
'''
pass
def getDBStoragePartitions():
'''public ArrayList<String> getDBStoragePartitions()
'''
pass
def nativeSpaceExists():
'''public boolean nativeSpaceExists(final String name)
'''
pass
def needLength():
'''public boolean needLength(String maxtype, String nativeType)
'''
pass
def needScale():
'''public boolean needScale(String maxtype, String nativeType)
'''
pass
def reEvaluateObjectChanged():
'''public String reEvaluateObjectChanged(final HashMap newObject, final HashMap oldObject, final boolean useAttrChanged, final String upgradeDir)
public String reEvaluateObjectChanged(final HashMap newObject, final HashMap oldObject, final boolean useAttrChanged, final String upgradeDir, String langcode)
'''
pass
def reEvaluateObjectChangedQuickGL():
'''public String reEvaluateObjectChangedQuickGL(final String entityname, final boolean isView, final HashMap attrs, final boolean persistent, final String origChanged)
'''
pass
def reEvaluateAttributeChangedQuickGL():
'''public String reEvaluateAttributeChangedQuickGL(final String entityname, final String columnname, final boolean isView, final int oldLength, final int newLength, final boolean persistent, final String origChanged)
'''
pass
def reEvaluateAttributeChanged():
'''public String reEvaluateAttributeChanged(final String entityname, final HashMap newAttr, final HashMap oldAttr, final String upgradeDir, final boolean isView)
'''
pass
def reEvaluateTableAttributeChanged():
'''public String reEvaluateTableAttributeChanged(final String tablename, final HashMap newAttr, final HashMap oldAttr, final String upgradeDir)
'''
pass
def reEvaluateViewAttributeChanged():
'''public String reEvaluateViewAttributeChanged(final String viewname, final HashMap newAttr, final HashMap oldAttr, final String upgradeDir)
'''
pass
def canAlterTable():
'''public boolean canAlterTable(final String tablename, final HashMap newAttr, final HashMap oldAttr, final String upgradeDir)
'''
pass
def canAlterForLengthChange():
'''public boolean canAlterForLengthChange(final String tablename, final String columnname, final int oldLength, final int newLength)
'''
pass
def upgradeDefaultExists():
'''public boolean upgradeDefaultExists(String tbname, String name, final String upgradeDir)
'''
pass
def implicitConversionSupported():
'''public boolean implicitConversionSupported(String newType, String oldType)
'''
pass
def explicitConversionSupported():
'''public boolean explicitConversionSupported(String newType, String oldType)
'''
pass
def tableIsEmpty():
'''public boolean tableIsEmpty(final String tbname)
'''
pass
def columnIsEmpty():
'''public boolean columnIsEmpty(final String tbname, final String name)
'''
pass
def nullValueExists():
'''public boolean nullValueExists(final String tbname, final String name)
'''
pass
def getMaxColumnLength():
'''public int getMaxColumnLength(final String tbname, final String name)
'''
pass
def getMaxColno():
'''public int getMaxColno(final String objectname, final boolean getCfg, final String where)
'''
pass
def getMaxLengthColumnInIndex():
'''public int getMaxLengthColumnInIndex()
'''
pass
def getMaxLengthIndex():
'''public int getMaxLengthIndex()
'''
pass
def getMaxVarcharLength():
'''public int getMaxVarcharLength()
'''
pass
def setVarcharMultiple():
'''public void setVarcharMultiple(final int val)
'''
pass
def getVarcharMultiple():
'''public int getVarcharMultiple()
'''
pass
def setVargraphic():
'''public void setVargraphic(final boolean val)
'''
pass
def useVargraphic():
'''public boolean useVargraphic()
'''
pass
def getInternalSiteOrgType():
'''public String getInternalSiteOrgType(final String externalSiteOrgType)
'''
pass
def getInternalSearchType():
'''public String getInternalSearchType(final String externalSearchType)
'''
pass
def isLocAllowed():
'''public boolean isLocAllowed(final String objectName, final String attributeName, final HashMap attrInfo, final HashMap sameasAtrInfo)
'''
pass
def getLocDefault():
'''public boolean getLocDefault(final String objectName, final String attributeName, final HashMap attrInfo, final HashMap sameasAttrInfo)
'''
pass
def nameInList():
'''public boolean nameInList(final String name, final String list)
'''
pass
def selectString():
'''public String selectString(final String sql)
'''
pass
def rowFound():
'''public boolean rowFound(final String sql)
'''
pass
def changeTreeKey():
'''public TreeMap<String, HashMap<String, String>> changeTreeKey(final TreeMap<String, HashMap<String, String>> oldMap, final String keyAttr)
'''
pass
def setConnection():
'''public void setConnection(final Connection connection)
'''
pass
def setPrintStream():
'''public void setPrintStream(final PrintStream outstream)
'''
pass
def setDB2tsPreferSysproc():
'''public void setDB2tsPreferSysproc(final boolean val)
'''
pass
def setDBOut():
'''public void setDBOut(final int platform)
'''
pass
def mxServerIsUp():
'''public boolean mxServerIsUp(final String serverName)
'''
pass
def configInProcess():
'''public boolean configInProcess()
'''
pass
def setConfigInProcess():
'''public String setConfigInProcess(final boolean inProcess)
'''
pass
def createStatement():
'''public Statement createStatement()
'''
pass
def prepareStatement():
'''public PreparedStatement prepareStatement(final String sql)
'''
pass
def getNextSequenceValueForSqlServer():
'''public String getNextSequenceValueForSqlServer(final String seqName)
'''
pass
def updateDMSource():
'''public List<String> updateDMSource()
'''
pass
def getDatabaseName():
'''public String getDatabaseName()
'''
pass
def getSchemaName():
'''public String getSchemaName()
'''
pass
def getDBHostName():
'''public String getDBHostName()
'''
pass
def getFileText():
'''public static String getFileText(final InputStream fileStrm)
'''
pass
def enableForMultiTenancy():
'''public ArrayList<String> enableForMultiTenancy(final String tabName, final String uniqueName, final String userName, final String adminUser, final MTStorageType storageType)
'''
pass
def addTenantidToTable():
'''public ArrayList<String> addTenantidToTable(final String tabName, final MTStorageType storageType)
'''
pass
def changeStorageType():
'''public ArrayList<String> changeStorageType(final String tabName, final String uniqueName, final MTStorageType oldType, final MTStorageType newType, final String userName, final String adminUser, final boolean isInternal)
'''
pass
def disableMTPermission():
'''public ArrayList<String> disableMTPermission(final String tabName, final MTStorageType storageType)
'''
pass
def createPermission():
'''public List<String> createPermission(final String tabName, final String uniqueName, final String newTenantUser, final String landlordUser, final MTStorageType type)
public List<String> createPermission(String tabName, final String uniqueName, final String newTenantUser, final String landlordUser, MTStorageType type, final boolean addProcessUser)
'''
pass
def rebuildProcessUserVariable():
'''public List<String> rebuildProcessUserVariable(final String adminUser)
'''
pass
def rebuildPermissions():
'''public void rebuildPermissions(final String processUser)
'''
pass
def createTenantidTriggeres():
'''public List<String> createTenantidTriggeres(String tbname, final MTStorageType storageType, final boolean secureRowlevelTriggers, final boolean dropInsert, final boolean dropUpdateDelete, final boolean createDeltaTriggers)
'''
pass
def dropDeltaTriggers():
'''public ArrayList<String> dropDeltaTriggers()
'''
pass
def getDeltaTriggerSql():
'''public List<String> getDeltaTriggerSql(final String tbname)
'''
pass
def getSequences():
'''public HashMap<String, String> getSequences(final String tableName)
'''
pass
def registerTableFromTemplate():
'''public List<String> registerTableFromTemplate(final String tbname, TreeMap tableCols, final String whereClause)
'''
pass
def getColumnNamesForExtendedView():
'''public String[] getColumnNamesForExtendedView(final TreeMap tableCols, final String tableName, final Map<String, Map<String, String>> extendedTables, final String uniqueColumnName, final String isView, final boolean mtEnabled)
'''
pass
def getExtendedUniqueColumnForView():
'''public String getExtendedUniqueColumnForView(final String viewName, final String extTableName)
'''
pass
def isMTEnabled():
'''public boolean isMTEnabled()
'''
pass
def getUserFromProperties():
'''public String getUserFromProperties(final boolean getLandlordUser)
'''
pass
def getTenantExtAttributes():
'''public Map<String, Map<String, Map<String, String>>> getTenantExtAttributes(final Connection conn, final String objectName, final int tenantId)
'''
pass
def updateViewMetaDataForExtendedAttr():
'''public ArrayList<String> updateViewMetaDataForExtendedAttr(final Connection conn, final String objectName, final String viewName, final Map<String, Map<String, String>> extAttr, final int tenantId)
'''
pass
def createExtensionView():
'''public List<String> createExtensionView(final String objectName, final Map<String, Map<String, String>> extendedTables, final Connection masterCon, final int tenantId, final boolean deleteOnly, final boolean mtEnabled)
'''
pass
def storeChangedAttributes():
'''public void storeChangedAttributes(final HashMap<String, HashMap<String, HashMap<String, String[]>>> changedObjects, final TreeMap<String, HashMap<String, String>> attrs, final String objectname)
'''
pass
def renumberExtendedAttributes():
'''public ArrayList<String> renumberExtendedAttributes(final int tenantId, final Map<String, Integer> lastNumbers, ArrayList<String> list)
'''
pass
def getUpdateTenantDelta():
'''public ArrayList getUpdateTenantDelta(final HashMap<String, HashMap<String, HashMap<String, String[]>>> changedObjects, final int tenantId, final TreeMap<String, HashMap<String, String>> cfgAttrs, final Vector<String[]> skipList)
'''
pass
def getNextAttrNo():
'''public int getNextAttrNo(final String tablename)
'''
pass
def getTenantCodeMetadata():
'''public ArrayList<String> getTenantCodeMetadata()
'''
pass
def addTenantid():
'''public List<String> addTenantid(final String tablename, final String uniqueColumnName, final MTStorageType storageType)
'''
pass
def reorgBeforeDB2TSUpdate():
'''public void reorgBeforeDB2TSUpdate()
'''
pass
