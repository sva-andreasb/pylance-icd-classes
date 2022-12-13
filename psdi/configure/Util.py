def Util():
    '''    public Util(final Connection conparam, final PrintStream outparam, final String schemaOwnerparam)
    public Util(final Connection conparam, final PrintStream outparam, final String schemaOwnerparam, final boolean reloadAttrs)
    '''
def getMaxTableAttrs():
    '''    public String[] getMaxTableAttrs()
    '''
def reloadAttributeList():
    '''    public void reloadAttributeList()
    '''
def getCurrentNativeSchema():
    '''    public String getCurrentNativeSchema()
    '''
def writeDumpTable():
    '''    public void writeDumpTable(final String tbname, final TreeMap tableCols, final PrintStream out)
    public int writeDumpTable(final String tbname, TreeMap tableCols, PrintStream out, int maxLines, int numLines, final Unlcvt unlcvt, final boolean psFormat)
    '''
def getData():
    '''    public TreeMap getData(final String tbname, TreeMap tableCols, final String where)
    '''
def isTable():
    '''    public boolean isTable(final HashMap tableInfo)
    '''
def buildCreateTableStatement():
    '''    public String buildCreateTableStatement(final HashMap tableInfo, final boolean doColDefault, final boolean includeDroppedCols, final String dbstoragepartition, final boolean specifyStorage)
    public String buildCreateTableStatement(final String tbname, final TreeMap tableCols, final boolean doColDefault, final boolean includeDroppedCols, final String dbstoragepartition, final boolean addRowstamp, final String storageClause)
    '''
def buildCreateViewStatement():
    '''    public ArrayList<String> buildCreateViewStatement(final HashMap viewInfo, final boolean includeDroppedCols, final boolean forceDropStmt)
    '''
def getAttributeForMaxViewColumn():
    '''    public HashMap getAttributeForMaxViewColumn(final String viewName, final HashMap viewcolInfo, final TreeMap distinctAttrs)
    '''
def buildColumnLine():
    '''    public String buildColumnLine(final HashMap colInfo, final boolean doDefault, final boolean alter)
    public String buildColumnLine(final HashMap colInfo, final boolean doDefault, final boolean doNullClause, final boolean alter)
    '''
def buildDefaultDataStatement():
    '''    public ArrayList<String> buildDefaultDataStatement(final String tbname, final TreeMap newTableCols, final String colNameList, TreeMap<String, HashMap<String, String>> oldTableCols)
    public String buildDefaultDataStatement(final String tbname, final HashMap newColInfo, final HashMap oldColInfo)
    '''
def buildShortenStringStatement():
    '''    public ArrayList<String> buildShortenStringStatement(final String tbname, final TreeMap newTableCols, final TreeMap oldTableCols)
    '''
def buildChangeCaseStatement():
    '''    public ArrayList<String> buildChangeCaseStatement(final String tbname, TreeMap<String, HashMap<String, String>> oldCols, TreeMap<String, HashMap<String, String>> newCols)
    public String buildChangeCaseStatement(final String tbname, final String name, final String oldMaxtype, final String newMaxtype)
    '''
def buildSelectStatement():
    '''    public String buildSelectStatement(final String tbname, final TreeMap tableCols, final boolean includeDroppedCols, final boolean addRowstamp)
    public String buildSelectStatement(final String tbname, final TreeMap tableCols, final boolean includeDroppedCols, final boolean addRowstamp, final boolean addTenantID)
    public String buildSelectStatement(final String tbname, final TreeMap tableCols, final boolean includeDroppedCols, final boolean addRowstamp, final boolean addtenantID, final String colNameList)
    '''
def buildSelectStatementForRestore():
    '''    public String buildSelectStatementForRestore(final String tempTbName, final TreeMap newTableCols, final boolean addRowstamp, final String colNameList, final boolean doLineBreaks)
    '''
def getDefaultString():
    '''    public String getDefaultString(final String tbname, final HashMap colInfo)
    public String getDefaultString(final String tbname, final String colName, final String maxtype, final String metaDefaultValue, final String domainid)
    public String getDefaultString(final String tbname, final String colName, final String maxtype, String metaDefaultValue, final String domainid, String sequenceName, final int uidRule, final int seqRule, final int autoRule, final int mboRule, final int appRule, final boolean outputQuotes, final boolean assignIfNoMeta)
    '''
def isSpecialDefaultValue():
    '''    public boolean isSpecialDefaultValue(final String value)
    '''
def getOracleConvertString():
    '''    public String getOracleConvertString(String oldNativeType, String newNativeType, final String colName)
    '''
def getSqlServerConvertString():
    '''    public String getSqlServerConvertString(final String oldTbname, final String newTbname, final HashMap newColInfo)
    '''
def getDB2ConvertString():
    '''    public String getDB2ConvertString(String oldNativeType, String newNativeType, final String colName)
    '''
def nativeTypesAreCompatible():
    '''    public boolean nativeTypesAreCompatible(String oldNativeType, String newNativeType)
    '''
def buildInsertStatementPrefix():
    '''    public String buildInsertStatementPrefix(final String tbname, final TreeMap tableCols, final boolean doRowstamp, final boolean includeDroppedCols)
    public String buildInsertStatementPrefix(final String tbname, final TreeMap tableCols, final boolean doRowstamp, final boolean includeDroppedCols, final String colNameList, final boolean doLineBreaks)
    public String buildInsertStatementPrefix(final String tbname, final TreeMap tableCols, final boolean doRowstamp, final boolean includeDroppedCols, final String colNameList, final boolean doLineBreaks, final boolean addTenantid)
    '''
def buildInsertValuesStatement():
    '''    public TreeMap buildInsertValuesStatement(final String prefix, final ResultSet rs, final TreeMap tableCols, final boolean includeDroppedCols, final String rowstampValue)
    public TreeMap<Integer, String> buildInsertValuesStatement(final String prefix, final ResultSet rs, final TreeMap tableCols, final boolean includeDroppedCols, final String rowstampValue, final boolean psFormat)
    public TreeMap<Integer, String> buildInsertValuesStatement(final String prefix, final ResultSet rs, final TreeMap tableCols, final boolean includeDroppedCols, final String rowstampValue, final boolean psFormat, final Map<String, String> allSeq)
    public TreeMap<Integer, String> buildInsertValuesStatement(final String prefix, final ResultSet rs, final TreeMap tableCols, final boolean includeDroppedCols, final String rowstampValue, final boolean psFormat, final Map<String, String> allSeq, final int tenantid)
    '''
def getKeyColumns():
    '''    public TreeMap<String, String> getKeyColumns(final TreeMap indexMeta, final TreeMap tableCols, final String indexToSkip)
    '''
def getColumnNames():
    '''    public String getColumnNames(final TreeMap tableCols, final boolean doLineBreaks, final boolean includeDroppedCols)
    public String getColumnNames(final TreeMap tableCols, final boolean doLineBreaks, final boolean includeDroppedCols, final String colNameList, final boolean useAlias)
    '''
def processTemplateData():
    '''    public void processTemplateData(final int toTenantid, final boolean delete, final String maxUserGroup, final String allUserGroup, final String newUserGroup, final PrintStream out)
    '''
def copyData():
    '''    public void copyData(final String tabName, final String uniqueColumn, final int toTenantid, final int storageType, final boolean delete, final PrintStream out)
    '''
def updateGroupName():
    '''    public void updateGroupName(final String tabName, final String maxUserGroup, final String allUserGroup, final String newUserGroup, final int toTenantid)
    '''
def getColumnNamesNative():
    '''    public String getColumnNamesNative(final String tbname)
    '''
def getColumnInfo():
    '''    public HashMap getColumnInfo(final TreeMap tableCols, String name)
    '''
def getAddRowstampSql():
    '''    public String getAddRowstampSql(final String tbname)
    '''
def getRowstampTriggerSql():
    '''    public ArrayList<String> getRowstampTriggerSql(final String tbname, final boolean dropIfExists)
    public ArrayList<String> getRowstampTriggerSql(final String tbname, final boolean dropIfExists, final boolean makeSecure)
    '''
def getTrigRoot():
    '''    public String getTrigRoot(final String tbname)
    '''
def buildGrants():
    '''    public ArrayList<String> buildGrants(final String tbname, final boolean outputSchema, final boolean maxusersOnly)
    '''
def getGrants():
    '''    public HashMap<String, int[]> getGrants(final String username, final String entityname)
    '''
def getGrantSql():
    '''    public String getGrantSql(final String dbUserID, final String entityname, final String privilege, final boolean grant)
    '''
def getTriggerNames():
    '''    public ArrayList<String> getTriggerNames(final String tbname, final boolean getEnabled, final boolean getDisabled, final boolean includeRowstamp)
    '''
def getEnableTriggerStatement():
    '''    public String getEnableTriggerStatement(final String triggerName, final String tbname)
    '''
def getDisableTriggerStatement():
    '''    public String getDisableTriggerStatement(final String triggerName, final String tbname)
    '''
def getEnableDisableTriggersAll():
    '''    public String getEnableDisableTriggersAll(final String tbname, final boolean enable)
    '''
def changeAmountFormat():
    '''    public ArrayList<String> changeAmountFormat(final int newLength, final int newScale)
    '''
def isRichTextSupported():
    '''    public boolean isRichTextSupported(String tbname, String name)
    '''
def isHandleColumn():
    '''    public boolean isHandleColumn(final String colName, final TreeMap attrs)
    '''
def enableRichTextSearch():
    '''    public ArrayList<String> enableRichTextSearch(final HashMap objInfo, final TreeMap tbIndexes, final boolean doCheck, final boolean skipDb2Connect)
    public ArrayList<String> enableRichTextSearch(final String tbname, final String colName, final String handleColName, final HashMap ixInfo, final boolean skipCreateUniqueIndex)
    public ArrayList<String> enableRichTextSearch(final String tbname, final String colName, final String handleColName, final HashMap ixInfo, final boolean skipCreateUniqueIndex, final int startIxNum)
    public ArrayList<String> enableRichTextSearch(String tbname, String colName, final String handleColName, final HashMap ixInfo, final boolean skipCreateUniqueIndex, final int startIxNum, final boolean skipDb2Connect)
    '''
def getDB2TextIndexSpace():
    '''    public String getDB2TextIndexSpace()
    '''
def isRTSupportedForDB():
    '''    public boolean isRTSupportedForDB()
    '''
def revalidateTextSearchIndexes():
    '''    public ArrayList<String> revalidateTextSearchIndexes(final String tbname)
    '''
def isReorgPending():
    '''    public boolean isReorgPending(final String tbname)
    '''
def reorgTable():
    '''    public ArrayList<String> reorgTable(final String tbname, final boolean redoTriggers)
    '''
def db2textAlterIndexes():
    '''    public ArrayList<String> db2textAlterIndexes()
    public ArrayList<String> db2textAlterIndexes(final boolean updateNow)
    '''
def activateRichTextSearch():
    '''    public ArrayList<String> activateRichTextSearch(final ArrayList<String> list, final String tbname, final boolean doCheck)
    '''
def disableRichTextSearch():
    '''    public ArrayList<String> disableRichTextSearch(final String tbname, String colName, final String handleColName)
    '''
def getTextSearchIndexForColumn():
    '''    public HashMap getTextSearchIndexForColumn(final String tbname, final String colName, TreeMap tbIndexes)
    '''
def getRenameTableStatement():
    '''    public String getRenameTableStatement(final String oldTbname, final String newTbname)
    '''
def getDropStatisticsStatementsForConfig():
    '''    public ArrayList getDropStatisticsStatementsForConfig(final String entityname)
    '''
def getDropStatisticsStatements():
    '''    public ArrayList<String> getDropStatisticsStatements(String tbname, String colname)
    '''
def canAnalyzeTable():
    '''    public boolean canAnalyzeTable()
    '''
def getAnalyzeTableStatement():
    '''    public ArrayList<String> getAnalyzeTableStatement(String tbname)
    '''
def getDisallowPageLocks():
    '''    public ArrayList<String> getDisallowPageLocks()
    '''
def lockMaximoTables():
    '''    public boolean lockMaximoTables(String tbname, final boolean lock)
    '''
def isObjectLocked():
    '''    public boolean isObjectLocked(final String entityname)
    '''
def isReservedWord():
    '''    public boolean isReservedWord(final String testWord)
    '''
def getAttributeRefresh():
    '''    public ArrayList<String> getAttributeRefresh()
    public ArrayList<String> getAttributeRefresh(final int tenantId, final boolean mtEnabled, final String objectName)
    '''
def getAttributeCfgRefresh():
    '''    public ArrayList<String> getAttributeCfgRefresh()
    public ArrayList<String> getAttributeCfgRefresh(final int tenantId, final boolean mtEnabled)
    '''
def getViewColumnRefresh():
    '''    public String getViewColumnRefresh()
    public String getViewColumnRefresh(final int tenantId, final boolean mtEnabled)
    '''
def getViewColumnCfgRefresh():
    '''    public String getViewColumnCfgRefresh()
    public String getViewColumnCfgRefresh(final int tenantId, final boolean mtEnabled)
    '''
def getTableRefresh():
    '''    public String getTableRefresh()
    public String getTableRefresh(final int tenantId, final boolean mtEnabled, final String tableName)
    '''
def getTableCfgRefresh():
    '''    public String getTableCfgRefresh()
    public String getTableCfgRefresh(final int tenantId, final boolean mtEnabled)
    '''
def getViewRefresh():
    '''    public String getViewRefresh()
    public String getViewRefresh(final int tenantId, final boolean mtEnabled)
    '''
def getViewCfgRefresh():
    '''    public String getViewCfgRefresh()
    public String getViewCfgRefresh(final int tenantId, final boolean mtEnabled)
    '''
def deleteObjectDelta():
    '''    public ArrayList<String> deleteObjectDelta(final int tenantId)
    '''
def getObjectRefresh():
    '''    public ArrayList<String> getObjectRefresh()
    public ArrayList<String> getObjectRefresh(final int tenantId, final boolean mtEnabled, final String objectName)
    '''
def getObjectCfgRefresh():
    '''    public ArrayList<String> getObjectCfgRefresh()
    public ArrayList<String> getObjectCfgRefresh(final int tenantId, final boolean mtEnabled)
    '''
def getSysIndexRefresh():
    '''    public ArrayList<String> getSysIndexRefresh(String tbname, String ixname)
    '''
def updateIndexRequired():
    '''    public List<String> updateIndexRequired()
    '''
def longIndexNamesExist():
    '''    public boolean longIndexNamesExist(final String tbname)
    '''
def dupIndexNamesExist():
    '''    public boolean dupIndexNamesExist(final String tbname, final String ixname)
    '''
def descendingIndexesSupported():
    '''    public boolean descendingIndexesSupported()
    '''
def getPartitionRefresh():
    '''    public ArrayList<String> getPartitionRefresh()
    '''
def getOracleVersion():
    '''    public int getOracleVersion()
    public double getOracleVersion(final boolean getPoint)
    '''
def getDB2Version():
    '''    public int getDB2Version()
    public double getDB2Version(final boolean getPoint)
    '''
def getSqlServerVersion():
    '''    public int getSqlServerVersion()
    public double getSqlServerVersion(final boolean getPoint)
    '''
def getSqlServerCompatLevel():
    '''    public int getSqlServerCompatLevel()
    '''
def getUpdateStatistics():
    '''    public ArrayList<String> getUpdateStatistics(final TreeMap tableMap, final TreeMap indexMap)
    '''
def getRemoveChanges():
    '''    public ArrayList<String> getRemoveChanges()
    '''
def getRemoveTenantChanges():
    '''    public ArrayList<String> getRemoveTenantChanges(final int tenantid, final boolean mtEnabled)
    '''
def getApplyTenantChanges():
    '''    public ArrayList<String> getApplyTenantChanges(final int tenantid, final boolean mtEnabled)
    '''
def objAttrDelRefresh():
    '''    public ArrayList<String> objAttrDelRefresh(final int tenantid, final boolean mtEnabled)
    '''
def attrRefresh():
    '''    public ArrayList<String> attrRefresh(final int tenantid, final boolean mtEnabled)
    '''
def renumberAttributeNumber():
    '''    public ArrayList<String> renumberAttributeNumber(final String objectname, final TreeMap attrs)
    '''
def renumberExtAttributeNumber():
    '''    public ArrayList<String> renumberExtAttributeNumber(final String objectname, final Map extTables, final int start, ArrayList<String> sqlList)
    '''
def getPrimaryKeys():
    '''    public TreeMap<String, String> getPrimaryKeys(String objname, final boolean getCfg)
    '''
def indexMetaExistsForPrikeycolseq():
    '''    public boolean indexMetaExistsForPrikeycolseq(String objname, String tbname, final boolean getCfg)
    '''
def buildIndexStatement():
    '''    public String buildIndexStatement(final String tbname, final TreeMap tableCols, final String dbstoragepartition)
    public String buildIndexStatement(final HashMap ixInfo, final boolean specifySchema, final boolean specifyStorage)
    '''
def rebuildIndexes():
    '''    public ArrayList<String> rebuildIndexes(final TreeMap indexMeta, final boolean alwaysDrop, final boolean neverDrop, final boolean specifySchema, final boolean specifyStorage)
    '''
def adjustPrimaryKeyColSeq():
    '''    public ArrayList<String> adjustPrimaryKeyColSeq(final TreeMap indexMeta)
    '''
def buildSequences():
    '''    public ArrayList<String> buildSequences(final HashSet sequences, final boolean doMaxseq)
    public ArrayList<String> buildSequences(final HashSet sequences, final Map<String, Long> alreadyDone, final boolean doMaxseq)
    '''
def updateMaxSequence():
    '''    public ArrayList<String> updateMaxSequence(final HashSet sequences)
    public ArrayList<String> updateMaxSequence(final HashSet sequences, final Map<String, Long> lastNumbers)
    '''
def getNextSequenceNo():
    '''    public long getNextSequenceNo(final String sequenceName)
    '''
def rebuildMetadataSequences():
    '''    public ArrayList<String> rebuildMetadataSequences()
    '''
def getMetadataSequenceNames():
    '''    public HashSet<String[]> getMetadataSequenceNames()
    '''
def getMaxEAuditTransID():
    '''    public int getMaxEAuditTransID()
    '''
def createOneSequenceFromMaxSequence():
    '''    public ArrayList<String> createOneSequenceFromMaxSequence(final String sequenceName)
    '''
def getUnrestoredTables():
    '''    public String getUnrestoredTables(final String tbname)
    '''
def getBackupTableName():
    '''    public String getBackupTableName(final String tbname)
    '''
def getOldBackupTables():
    '''    public String getOldBackupTables(final String tbname)
    '''
def clearAlreadyDidUsingMultiSchema():
    '''    public void clearAlreadyDidUsingMultiSchema()
    '''
def usingMultiSchema():
    '''    public boolean usingMultiSchema()
    '''
def getSites():
    '''    public TreeMap<String, String> getSites(final boolean includeDisabled)
    '''
def getOrgs():
    '''    public TreeMap<String, String> getOrgs(final boolean includeDisabled)
    '''
def getSiteOrgType():
    '''    public String getSiteOrgType(final String objectname)
    '''
def getStoragePartition():
    '''    public String getStoragePartition(final String tbname)
    '''
def getUniqueIndexSpace():
    '''    public String getUniqueIndexSpace(final String tbname, final String tbPartition)
    '''
def getLangColumnName():
    '''    public String getLangColumnName(final String tbname)
    '''
def getUniqueColumnName():
    '''    public String getUniqueColumnName(final String tbname)
    '''
def getUniqueColumnNameNative():
    '''    public String getUniqueColumnNameNative(final String tbname)
    '''
def getObjectName():
    '''    public String getObjectName(final String entityname, final boolean useIsViewConstraint, final boolean isView)
    '''
def getTableName():
    '''    public String getTableName(final String objectname)
    '''
def getStorageType():
    '''    public MTStorageType getStorageType(final String tableName)
    '''
def getViewName():
    '''    public String getViewName(final String objectname)
    '''
def getAttributeName():
    '''    public String getAttributeName(final String objectname, final String tablename, final String columnname)
    '''
def getColumnName():
    '''    public String[] getColumnName(final String objectname, final String attributename)
    '''
def getKeyAttribute():
    '''    public String getKeyAttribute(String objectname, String tablename)
    '''
def getObjectMeta():
    '''    public TreeMap<String, HashMap<String, Object>> getObjectMeta(String objectname, final boolean getCfg, final boolean getPersistentOnly, boolean getChangedOnly, final boolean getColumns, final boolean colsOrderByName, boolean getTablesOnly, boolean getViewsOnly)
    '''
def getAttributeMeta():
    '''    public TreeMap<String, TreeMap<String, HashMap<String, String>>> getAttributeMeta(final String objectname, final boolean getCfg, final boolean orderByName, final boolean getPersistentOnly, boolean getChangedOnly, final boolean selectView, final String entityName)
    '''
def getTenantAttributeMeta():
    '''    public HashMap<String, HashMap<String, String>> getTenantAttributeMeta(final String objectname, final int tenantId)
    '''
def gettenantSameAsExtendedAtributes():
    '''    public Map<String, List<String>> gettenantSameAsExtendedAtributes(final int tenantId)
    '''
def getIndexMeta():
    '''    public TreeMap<String, HashMap<String, Object>> getIndexMeta(final String tbname, final boolean getChangedOnly)
    public TreeMap<String, HashMap<String, Object>> getIndexMeta(final String tbname, final boolean getChangedOnly, final boolean getPrimary)
    public TreeMap<String, HashMap<String, Object>> getIndexMeta(final String tbname, final boolean getChangedOnly, final boolean getPrimary, final boolean includeDeleted)
    '''
def getIndexNamesForColumn():
    '''    public ArrayList<String> getIndexNamesForColumn(final String tbname, final String colName)
    '''
def getMaxvar():
    '''    public String getMaxvar(String varname, final boolean getDefault)
    '''
def getYes():
    '''    public String getYes()
    '''
def getNo():
    '''    public String getNo()
    '''
def getMaxUpgVersion():
    '''    public String getMaxUpgVersion()
    '''
def nativeTableExists():
    '''    public boolean nativeTableExists(final String tbname)
    '''
def nativeColumnExists():
    '''    public boolean nativeColumnExists(final String tbname, final String name)
    '''
def nativeViewExists():
    '''    public boolean nativeViewExists(final String vname)
    '''
def nativeIndexExists():
    '''    public boolean nativeIndexExists(final String ixname, final String tbname)
    '''
def nativeIndexExistsForColumn():
    '''    public ArrayList<String> nativeIndexExistsForColumn(final String tbname, final String name)
    '''
def nativeIndexExistsForColumns():
    '''    public String nativeIndexExistsForColumns(final String tbname, final Object[] names)
    public String nativeIndexExistsForColumns(final String tbname, final Object[] names, final boolean ignoreTS)
    '''
def cleanStatisticNames():
    '''    public ArrayList<String> cleanStatisticNames()
    '''
def fixMetadataForDescendingKeys():
    '''    public ArrayList<String> fixMetadataForDescendingKeys(String tbname, String ixname)
    '''
def nativeIndexIsUnique():
    '''    public boolean nativeIndexIsUnique(final String ixname)
    '''
def nativeIndexIsPrimaryKey():
    '''    public boolean nativeIndexIsPrimaryKey(final String ixname)
    '''
def nativeColumnIsNullable():
    '''    public boolean nativeColumnIsNullable(final String tbname, final String name)
    '''
def addTenantIDIndex():
    '''    public ArrayList<String> addTenantIDIndex(final String tbname, String storagepartition, final MTStorageType storageType)
    '''
def addIndex():
    '''    public ArrayList<String> addIndex(final String tbname, String[] names, String startWith, final boolean addUnique, String storagepartition)
    '''
def getNewIndexName():
    '''    public String getNewIndexName(final String tbname, int startWith)
    '''
def nativeDefaultConstraintExists():
    '''    public ArrayList<String> nativeDefaultConstraintExists(final String tbname, final String name)
    '''
def nativeTriggerExists():
    '''    public boolean nativeTriggerExists(final String trigname)
    '''
def nativeSequenceExists():
    '''    public boolean nativeSequenceExists(final String name)
    '''
def isNickname():
    '''    public boolean isNickname(final String name)
    '''
def isSysYORN():
    '''    public boolean isSysYORN(String attrName)
    '''
def isSysNumeric():
    '''    public boolean isSysNumeric(String attrName)
    '''
def adjustViewMeta():
    '''    public ArrayList<String> adjustViewMeta(final String viewname)
    public ArrayList<String> adjustViewMeta(String viewname, final boolean addP, final boolean addNP)
    '''
def getMaximumColumnNameLength():
    '''    public int getMaximumColumnNameLength()
    '''
def useQuotes():
    '''    public boolean useQuotes(String maxtype)
    '''
def singleToDoubleQuotes():
    '''    public String singleToDoubleQuotes(final String in)
    '''
def toggleStringConcat():
    '''    public String toggleStringConcat(final String inString, final String inConcat, final String outConcat)
    '''
def getNativeType():
    '''    public String getNativeType(final String maxType, final String length, int dbPlatform)
    '''
def getJdbcType():
    '''    public int getJdbcType(String nativeType, final int dbPlatform)
    '''
def getNativeTypeForColumn():
    '''    public String getNativeTypeForColumn(final String tbname, final String name)
    '''
def getNativeDateDefault():
    '''    public String getNativeDateDefault()
    '''
def getNativePartition():
    '''    public String getNativePartition(final String tbname)
    '''
def spaceIsActive():
    '''    public boolean spaceIsActive(final String spaceName)
    '''
def spaceIsSysManaged():
    '''    public boolean spaceIsSysManaged(final String spaceName)
    '''
def bytesSpaceNeeded():
    '''    public int bytesSpaceNeeded(final String spaceName)
    '''
def spaceNeeded():
    '''    public Object[] spaceNeeded(final String spaceName)
    '''
def makeSpace():
    '''    public ArrayList<String> makeSpace(final String spaceName, final int numBytes)
    public ArrayList<String> makeSpace(final String spaceName, final int numBytes, final String multiplier)
    '''
def spaceCheckForDBConfig():
    '''    public String[] spaceCheckForDBConfig()
    '''
def getStorageClause():
    '''    public String getStorageClause(final String name, final boolean isTable)
    '''
def adjustNativeSql():
    '''    public String adjustNativeSql(final String origSql)
    '''
def getMaxType():
    '''    public String getMaxType(final String nativeType)
    '''
def getDefaultStoragePartition():
    '''    public String getDefaultStoragePartition(final boolean checkValuelist)
    '''
def getDBStoragePartitions():
    '''    public ArrayList<String> getDBStoragePartitions()
    '''
def nativeSpaceExists():
    '''    public boolean nativeSpaceExists(final String name)
    '''
def needLength():
    '''    public boolean needLength(String maxtype, String nativeType)
    '''
def needScale():
    '''    public boolean needScale(String maxtype, String nativeType)
    '''
def reEvaluateObjectChanged():
    '''    public String reEvaluateObjectChanged(final HashMap newObject, final HashMap oldObject, final boolean useAttrChanged, final String upgradeDir)
    public String reEvaluateObjectChanged(final HashMap newObject, final HashMap oldObject, final boolean useAttrChanged, final String upgradeDir, String langcode)
    '''
def reEvaluateObjectChangedQuickGL():
    '''    public String reEvaluateObjectChangedQuickGL(final String entityname, final boolean isView, final HashMap attrs, final boolean persistent, final String origChanged)
    '''
def reEvaluateAttributeChangedQuickGL():
    '''    public String reEvaluateAttributeChangedQuickGL(final String entityname, final String columnname, final boolean isView, final int oldLength, final int newLength, final boolean persistent, final String origChanged)
    '''
def reEvaluateAttributeChanged():
    '''    public String reEvaluateAttributeChanged(final String entityname, final HashMap newAttr, final HashMap oldAttr, final String upgradeDir, final boolean isView)
    '''
def reEvaluateTableAttributeChanged():
    '''    public String reEvaluateTableAttributeChanged(final String tablename, final HashMap newAttr, final HashMap oldAttr, final String upgradeDir)
    '''
def reEvaluateViewAttributeChanged():
    '''    public String reEvaluateViewAttributeChanged(final String viewname, final HashMap newAttr, final HashMap oldAttr, final String upgradeDir)
    '''
def canAlterTable():
    '''    public boolean canAlterTable(final String tablename, final HashMap newAttr, final HashMap oldAttr, final String upgradeDir)
    '''
def canAlterForLengthChange():
    '''    public boolean canAlterForLengthChange(final String tablename, final String columnname, final int oldLength, final int newLength)
    '''
def upgradeDefaultExists():
    '''    public boolean upgradeDefaultExists(String tbname, String name, final String upgradeDir)
    '''
def implicitConversionSupported():
    '''    public boolean implicitConversionSupported(String newType, String oldType)
    '''
def explicitConversionSupported():
    '''    public boolean explicitConversionSupported(String newType, String oldType)
    '''
def tableIsEmpty():
    '''    public boolean tableIsEmpty(final String tbname)
    '''
def columnIsEmpty():
    '''    public boolean columnIsEmpty(final String tbname, final String name)
    '''
def nullValueExists():
    '''    public boolean nullValueExists(final String tbname, final String name)
    '''
def getMaxColumnLength():
    '''    public int getMaxColumnLength(final String tbname, final String name)
    '''
def getMaxColno():
    '''    public int getMaxColno(final String objectname, final boolean getCfg, final String where)
    '''
def getMaxLengthColumnInIndex():
    '''    public int getMaxLengthColumnInIndex()
    '''
def getMaxLengthIndex():
    '''    public int getMaxLengthIndex()
    '''
def getMaxVarcharLength():
    '''    public int getMaxVarcharLength()
    '''
def setVarcharMultiple():
    '''    public void setVarcharMultiple(final int val)
    '''
def getVarcharMultiple():
    '''    public int getVarcharMultiple()
    '''
def setVargraphic():
    '''    public void setVargraphic(final boolean val)
    '''
def useVargraphic():
    '''    public boolean useVargraphic()
    '''
def getInternalSiteOrgType():
    '''    public String getInternalSiteOrgType(final String externalSiteOrgType)
    '''
def getInternalSearchType():
    '''    public String getInternalSearchType(final String externalSearchType)
    '''
def isLocAllowed():
    '''    public boolean isLocAllowed(final String objectName, final String attributeName, final HashMap attrInfo, final HashMap sameasAtrInfo)
    '''
def getLocDefault():
    '''    public boolean getLocDefault(final String objectName, final String attributeName, final HashMap attrInfo, final HashMap sameasAttrInfo)
    '''
def nameInList():
    '''    public boolean nameInList(final String name, final String list)
    '''
def selectString():
    '''    public String selectString(final String sql)
    '''
def rowFound():
    '''    public boolean rowFound(final String sql)
    '''
def changeTreeKey():
    '''    public TreeMap<String, HashMap<String, String>> changeTreeKey(final TreeMap<String, HashMap<String, String>> oldMap, final String keyAttr)
    '''
def setConnection():
    '''    public void setConnection(final Connection connection)
    '''
def setPrintStream():
    '''    public void setPrintStream(final PrintStream outstream)
    '''
def setDB2tsPreferSysproc():
    '''    public void setDB2tsPreferSysproc(final boolean val)
    '''
def setDBOut():
    '''    public void setDBOut(final int platform)
    '''
def mxServerIsUp():
    '''    public boolean mxServerIsUp(final String serverName)
    '''
def configInProcess():
    '''    public boolean configInProcess()
    '''
def setConfigInProcess():
    '''    public String setConfigInProcess(final boolean inProcess)
    '''
def createStatement():
    '''    public Statement createStatement()
    '''
def prepareStatement():
    '''    public PreparedStatement prepareStatement(final String sql)
    '''
def getNextSequenceValueForSqlServer():
    '''    public String getNextSequenceValueForSqlServer(final String seqName)
    '''
def updateDMSource():
    '''    public List<String> updateDMSource()
    '''
def getDatabaseName():
    '''    public String getDatabaseName()
    '''
def getSchemaName():
    '''    public String getSchemaName()
    '''
def getDBHostName():
    '''    public String getDBHostName()
    '''
def getFileText():
    '''    public static String getFileText(final InputStream fileStrm)
    '''
def enableForMultiTenancy():
    '''    public ArrayList<String> enableForMultiTenancy(final String tabName, final String uniqueName, final String userName, final String adminUser, final MTStorageType storageType)
    '''
def addTenantidToTable():
    '''    public ArrayList<String> addTenantidToTable(final String tabName, final MTStorageType storageType)
    '''
def changeStorageType():
    '''    public ArrayList<String> changeStorageType(final String tabName, final String uniqueName, final MTStorageType oldType, final MTStorageType newType, final String userName, final String adminUser, final boolean isInternal)
    '''
def disableMTPermission():
    '''    public ArrayList<String> disableMTPermission(final String tabName, final MTStorageType storageType)
    '''
def createPermission():
    '''    public List<String> createPermission(final String tabName, final String uniqueName, final String newTenantUser, final String landlordUser, final MTStorageType type)
    public List<String> createPermission(String tabName, final String uniqueName, final String newTenantUser, final String landlordUser, MTStorageType type, final boolean addProcessUser)
    '''
def rebuildProcessUserVariable():
    '''    public List<String> rebuildProcessUserVariable(final String adminUser)
    '''
def rebuildPermissions():
    '''    public void rebuildPermissions(final String processUser)
    '''
def createTenantidTriggeres():
    '''    public List<String> createTenantidTriggeres(String tbname, final MTStorageType storageType, final boolean secureRowlevelTriggers, final boolean dropInsert, final boolean dropUpdateDelete, final boolean createDeltaTriggers)
    '''
def dropDeltaTriggers():
    '''    public ArrayList<String> dropDeltaTriggers()
    '''
def getDeltaTriggerSql():
    '''    public List<String> getDeltaTriggerSql(final String tbname)
    '''
def getSequences():
    '''    public HashMap<String, String> getSequences(final String tableName)
    '''
def registerTableFromTemplate():
    '''    public List<String> registerTableFromTemplate(final String tbname, TreeMap tableCols, final String whereClause)
    '''
def getColumnNamesForExtendedView():
    '''    public String[] getColumnNamesForExtendedView(final TreeMap tableCols, final String tableName, final Map<String, Map<String, String>> extendedTables, final String uniqueColumnName, final String isView, final boolean mtEnabled)
    '''
def getExtendedUniqueColumnForView():
    '''    public String getExtendedUniqueColumnForView(final String viewName, final String extTableName)
    '''
def isMTEnabled():
    '''    public boolean isMTEnabled()
    '''
def getUserFromProperties():
    '''    public String getUserFromProperties(final boolean getLandlordUser)
    '''
def getTenantExtAttributes():
    '''    public Map<String, Map<String, Map<String, String>>> getTenantExtAttributes(final Connection conn, final String objectName, final int tenantId)
    '''
def updateViewMetaDataForExtendedAttr():
    '''    public ArrayList<String> updateViewMetaDataForExtendedAttr(final Connection conn, final String objectName, final String viewName, final Map<String, Map<String, String>> extAttr, final int tenantId)
    '''
def createExtensionView():
    '''    public List<String> createExtensionView(final String objectName, final Map<String, Map<String, String>> extendedTables, final Connection masterCon, final int tenantId, final boolean deleteOnly, final boolean mtEnabled)
    '''
def storeChangedAttributes():
    '''    public void storeChangedAttributes(final HashMap<String, HashMap<String, HashMap<String, String[]>>> changedObjects, final TreeMap<String, HashMap<String, String>> attrs, final String objectname)
    '''
def renumberExtendedAttributes():
    '''    public ArrayList<String> renumberExtendedAttributes(final int tenantId, final Map<String, Integer> lastNumbers, ArrayList<String> list)
    '''
def getUpdateTenantDelta():
    '''    public ArrayList getUpdateTenantDelta(final HashMap<String, HashMap<String, HashMap<String, String[]>>> changedObjects, final int tenantId, final TreeMap<String, HashMap<String, String>> cfgAttrs, final Vector<String[]> skipList)
    '''
def getNextAttrNo():
    '''    public int getNextAttrNo(final String tablename)
    '''
def getTenantCodeMetadata():
    '''    public ArrayList<String> getTenantCodeMetadata()
    '''
def addTenantid():
    '''    public List<String> addTenantid(final String tablename, final String uniqueColumnName, final MTStorageType storageType)
    '''
def reorgBeforeDB2TSUpdate():
    '''    public void reorgBeforeDB2TSUpdate()
    '''
