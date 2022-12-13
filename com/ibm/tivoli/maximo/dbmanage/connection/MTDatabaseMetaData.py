def MTDatabaseMetaData():
'''public MTDatabaseMetaData(final DatabaseMetaData metaData)
'''
pass
def supportsBatchUpdates():
'''public boolean supportsBatchUpdates()
'''
pass
def allProceduresAreCallable():
'''public boolean allProceduresAreCallable()
'''
pass
def allTablesAreSelectable():
'''public boolean allTablesAreSelectable()
'''
pass
def autoCommitFailureClosesAllResultSets():
'''public boolean autoCommitFailureClosesAllResultSets()
'''
pass
def dataDefinitionCausesTransactionCommit():
'''public boolean dataDefinitionCausesTransactionCommit()
'''
pass
def dataDefinitionIgnoredInTransactions():
'''public boolean dataDefinitionIgnoredInTransactions()
'''
pass
def deletesAreDetected():
'''public boolean deletesAreDetected(final int type)
'''
pass
def doesMaxRowSizeIncludeBlobs():
'''public boolean doesMaxRowSizeIncludeBlobs()
'''
pass
def getAttributes():
'''public ResultSet getAttributes(final String catalog, final String schemaPattern, final String typeNamePattern, final String attributeNamePattern)
'''
pass
def getBestRowIdentifier():
'''public ResultSet getBestRowIdentifier(final String catalog, final String schema, final String table, final int scope, final boolean nullable)
'''
pass
def getCatalogSeparator():
'''public String getCatalogSeparator()
'''
pass
def getCatalogTerm():
'''public String getCatalogTerm()
'''
pass
def getCatalogs():
'''public ResultSet getCatalogs()
'''
pass
def getClientInfoProperties():
'''public ResultSet getClientInfoProperties()
'''
pass
def getColumnPrivileges():
'''public ResultSet getColumnPrivileges(final String catalog, final String schema, final String table, final String columnNamePattern)
'''
pass
def getColumns():
'''public ResultSet getColumns(final String catalog, final String schemaPattern, final String tableNamePattern, final String columnNamePattern)
'''
pass
def getConnection():
'''public Connection getConnection()
'''
pass
def getCrossReference():
'''public ResultSet getCrossReference(final String parentCatalog, final String parentSchema, final String parentTable, final String foreignCatalog, final String foreignSchema, final String foreignTable)
'''
pass
def getDatabaseMajorVersion():
'''public int getDatabaseMajorVersion()
'''
pass
def getDatabaseMinorVersion():
'''public int getDatabaseMinorVersion()
'''
pass
def getDatabaseProductName():
'''public String getDatabaseProductName()
'''
pass
def getDatabaseProductVersion():
'''public String getDatabaseProductVersion()
'''
pass
def getDefaultTransactionIsolation():
'''public int getDefaultTransactionIsolation()
'''
pass
def getDriverMajorVersion():
'''public int getDriverMajorVersion()
'''
pass
def getDriverMinorVersion():
'''public int getDriverMinorVersion()
'''
pass
def getDriverName():
'''public String getDriverName()
'''
pass
def getDriverVersion():
'''public String getDriverVersion()
'''
pass
def getExportedKeys():
'''public ResultSet getExportedKeys(final String catalog, final String schema, final String table)
'''
pass
def getExtraNameCharacters():
'''public String getExtraNameCharacters()
'''
pass
def getFunctionColumns():
'''public ResultSet getFunctionColumns(final String catalog, final String schemaPattern, final String functionNamePattern, final String columnNamePattern)
'''
pass
def getFunctions():
'''public ResultSet getFunctions(final String catalog, final String schemaPattern, final String functionNamePattern)
'''
pass
def getIdentifierQuoteString():
'''public String getIdentifierQuoteString()
'''
pass
def getImportedKeys():
'''public ResultSet getImportedKeys(final String catalog, final String schema, final String table)
'''
pass
def getIndexInfo():
'''public ResultSet getIndexInfo(final String catalog, final String schema, final String table, final boolean unique, final boolean approximate)
'''
pass
def getJDBCMajorVersion():
'''public int getJDBCMajorVersion()
'''
pass
def getJDBCMinorVersion():
'''public int getJDBCMinorVersion()
'''
pass
def getMaxBinaryLiteralLength():
'''public int getMaxBinaryLiteralLength()
'''
pass
def getMaxCatalogNameLength():
'''public int getMaxCatalogNameLength()
'''
pass
def getMaxCharLiteralLength():
'''public int getMaxCharLiteralLength()
'''
pass
def getMaxColumnNameLength():
'''public int getMaxColumnNameLength()
'''
pass
def getMaxColumnsInGroupBy():
'''public int getMaxColumnsInGroupBy()
'''
pass
def getMaxColumnsInIndex():
'''public int getMaxColumnsInIndex()
'''
pass
def getMaxColumnsInOrderBy():
'''public int getMaxColumnsInOrderBy()
'''
pass
def getMaxColumnsInSelect():
'''public int getMaxColumnsInSelect()
'''
pass
def getMaxColumnsInTable():
'''public int getMaxColumnsInTable()
'''
pass
def getMaxConnections():
'''public int getMaxConnections()
'''
pass
def getMaxCursorNameLength():
'''public int getMaxCursorNameLength()
'''
pass
def getMaxIndexLength():
'''public int getMaxIndexLength()
'''
pass
def getMaxProcedureNameLength():
'''public int getMaxProcedureNameLength()
'''
pass
def getMaxRowSize():
'''public int getMaxRowSize()
'''
pass
def getMaxSchemaNameLength():
'''public int getMaxSchemaNameLength()
'''
pass
def getMaxStatementLength():
'''public int getMaxStatementLength()
'''
pass
def getMaxStatements():
'''public int getMaxStatements()
'''
pass
def getMaxTableNameLength():
'''public int getMaxTableNameLength()
'''
pass
def getMaxTablesInSelect():
'''public int getMaxTablesInSelect()
'''
pass
def getMaxUserNameLength():
'''public int getMaxUserNameLength()
'''
pass
def getNumericFunctions():
'''public String getNumericFunctions()
'''
pass
def getPrimaryKeys():
'''public ResultSet getPrimaryKeys(final String catalog, final String schema, final String table)
'''
pass
def getProcedureColumns():
'''public ResultSet getProcedureColumns(final String catalog, final String schemaPattern, final String procedureNamePattern, final String columnNamePattern)
'''
pass
def getProcedureTerm():
'''public String getProcedureTerm()
'''
pass
def getProcedures():
'''public ResultSet getProcedures(final String catalog, final String schemaPattern, final String procedureNamePattern)
'''
pass
def getResultSetHoldability():
'''public int getResultSetHoldability()
'''
pass
def getRowIdLifetime():
'''public RowIdLifetime getRowIdLifetime()
'''
pass
def getSQLKeywords():
'''public String getSQLKeywords()
'''
pass
def getSQLStateType():
'''public int getSQLStateType()
'''
pass
def getSchemaTerm():
'''public String getSchemaTerm()
'''
pass
def getSchemas():
'''public ResultSet getSchemas()
public ResultSet getSchemas(final String catalog, final String schemaPattern)
'''
pass
def getSearchStringEscape():
'''public String getSearchStringEscape()
'''
pass
def getStringFunctions():
'''public String getStringFunctions()
'''
pass
def getSuperTables():
'''public ResultSet getSuperTables(final String catalog, final String schemaPattern, final String tableNamePattern)
'''
pass
def getSuperTypes():
'''public ResultSet getSuperTypes(final String catalog, final String schemaPattern, final String typeNamePattern)
'''
pass
def getSystemFunctions():
'''public String getSystemFunctions()
'''
pass
def getTablePrivileges():
'''public ResultSet getTablePrivileges(final String catalog, final String schemaPattern, final String tableNamePattern)
'''
pass
def getTableTypes():
'''public ResultSet getTableTypes()
'''
pass
def getTables():
'''public ResultSet getTables(final String catalog, final String schemaPattern, final String tableNamePattern, final String[] types)
'''
pass
def getTimeDateFunctions():
'''public String getTimeDateFunctions()
'''
pass
def getTypeInfo():
'''public ResultSet getTypeInfo()
'''
pass
def getUDTs():
'''public ResultSet getUDTs(final String catalog, final String schemaPattern, final String typeNamePattern, final int[] types)
'''
pass
def getURL():
'''public String getURL()
'''
pass
def getUserName():
'''public String getUserName()
'''
pass
def getVersionColumns():
'''public ResultSet getVersionColumns(final String catalog, final String schema, final String table)
'''
pass
def insertsAreDetected():
'''public boolean insertsAreDetected(final int type)
'''
pass
def isCatalogAtStart():
'''public boolean isCatalogAtStart()
'''
pass
def isReadOnly():
'''public boolean isReadOnly()
'''
pass
def locatorsUpdateCopy():
'''public boolean locatorsUpdateCopy()
'''
pass
def nullPlusNonNullIsNull():
'''public boolean nullPlusNonNullIsNull()
'''
pass
def nullsAreSortedAtEnd():
'''public boolean nullsAreSortedAtEnd()
'''
pass
def nullsAreSortedAtStart():
'''public boolean nullsAreSortedAtStart()
'''
pass
def nullsAreSortedHigh():
'''public boolean nullsAreSortedHigh()
'''
pass
def nullsAreSortedLow():
'''public boolean nullsAreSortedLow()
'''
pass
def othersDeletesAreVisible():
'''public boolean othersDeletesAreVisible(final int type)
'''
pass
def othersInsertsAreVisible():
'''public boolean othersInsertsAreVisible(final int type)
'''
pass
def othersUpdatesAreVisible():
'''public boolean othersUpdatesAreVisible(final int type)
'''
pass
def ownDeletesAreVisible():
'''public boolean ownDeletesAreVisible(final int type)
'''
pass
def ownInsertsAreVisible():
'''public boolean ownInsertsAreVisible(final int type)
'''
pass
def ownUpdatesAreVisible():
'''public boolean ownUpdatesAreVisible(final int type)
'''
pass
def storesLowerCaseIdentifiers():
'''public boolean storesLowerCaseIdentifiers()
'''
pass
def storesLowerCaseQuotedIdentifiers():
'''public boolean storesLowerCaseQuotedIdentifiers()
'''
pass
def storesMixedCaseIdentifiers():
'''public boolean storesMixedCaseIdentifiers()
'''
pass
def storesMixedCaseQuotedIdentifiers():
'''public boolean storesMixedCaseQuotedIdentifiers()
'''
pass
def storesUpperCaseIdentifiers():
'''public boolean storesUpperCaseIdentifiers()
'''
pass
def storesUpperCaseQuotedIdentifiers():
'''public boolean storesUpperCaseQuotedIdentifiers()
'''
pass
def supportsANSI92EntryLevelSQL():
'''public boolean supportsANSI92EntryLevelSQL()
'''
pass
def supportsANSI92FullSQL():
'''public boolean supportsANSI92FullSQL()
'''
pass
def supportsANSI92IntermediateSQL():
'''public boolean supportsANSI92IntermediateSQL()
'''
pass
def supportsAlterTableWithAddColumn():
'''public boolean supportsAlterTableWithAddColumn()
'''
pass
def supportsAlterTableWithDropColumn():
'''public boolean supportsAlterTableWithDropColumn()
'''
pass
def supportsCatalogsInDataManipulation():
'''public boolean supportsCatalogsInDataManipulation()
'''
pass
def supportsCatalogsInIndexDefinitions():
'''public boolean supportsCatalogsInIndexDefinitions()
'''
pass
def supportsCatalogsInPrivilegeDefinitions():
'''public boolean supportsCatalogsInPrivilegeDefinitions()
'''
pass
def supportsCatalogsInProcedureCalls():
'''public boolean supportsCatalogsInProcedureCalls()
'''
pass
def supportsCatalogsInTableDefinitions():
'''public boolean supportsCatalogsInTableDefinitions()
'''
pass
def supportsColumnAliasing():
'''public boolean supportsColumnAliasing()
'''
pass
def supportsConvert():
'''public boolean supportsConvert()
public boolean supportsConvert(final int fromType, final int toType)
'''
pass
def supportsCoreSQLGrammar():
'''public boolean supportsCoreSQLGrammar()
'''
pass
def supportsCorrelatedSubqueries():
'''public boolean supportsCorrelatedSubqueries()
'''
pass
def supportsDataDefinitionAndDataManipulationTransactions():
'''public boolean supportsDataDefinitionAndDataManipulationTransactions()
'''
pass
def supportsDataManipulationTransactionsOnly():
'''public boolean supportsDataManipulationTransactionsOnly()
'''
pass
def supportsDifferentTableCorrelationNames():
'''public boolean supportsDifferentTableCorrelationNames()
'''
pass
def supportsExpressionsInOrderBy():
'''public boolean supportsExpressionsInOrderBy()
'''
pass
def supportsExtendedSQLGrammar():
'''public boolean supportsExtendedSQLGrammar()
'''
pass
def supportsFullOuterJoins():
'''public boolean supportsFullOuterJoins()
'''
pass
def supportsGetGeneratedKeys():
'''public boolean supportsGetGeneratedKeys()
'''
pass
def supportsGroupBy():
'''public boolean supportsGroupBy()
'''
pass
def supportsGroupByBeyondSelect():
'''public boolean supportsGroupByBeyondSelect()
'''
pass
def supportsGroupByUnrelated():
'''public boolean supportsGroupByUnrelated()
'''
pass
def supportsIntegrityEnhancementFacility():
'''public boolean supportsIntegrityEnhancementFacility()
'''
pass
def supportsLikeEscapeClause():
'''public boolean supportsLikeEscapeClause()
'''
pass
def supportsLimitedOuterJoins():
'''public boolean supportsLimitedOuterJoins()
'''
pass
def supportsMinimumSQLGrammar():
'''public boolean supportsMinimumSQLGrammar()
'''
pass
def supportsMixedCaseIdentifiers():
'''public boolean supportsMixedCaseIdentifiers()
'''
pass
def supportsMixedCaseQuotedIdentifiers():
'''public boolean supportsMixedCaseQuotedIdentifiers()
'''
pass
def supportsMultipleOpenResults():
'''public boolean supportsMultipleOpenResults()
'''
pass
def supportsMultipleResultSets():
'''public boolean supportsMultipleResultSets()
'''
pass
def supportsMultipleTransactions():
'''public boolean supportsMultipleTransactions()
'''
pass
def supportsNamedParameters():
'''public boolean supportsNamedParameters()
'''
pass
def supportsNonNullableColumns():
'''public boolean supportsNonNullableColumns()
'''
pass
def supportsOpenCursorsAcrossCommit():
'''public boolean supportsOpenCursorsAcrossCommit()
'''
pass
def supportsOpenCursorsAcrossRollback():
'''public boolean supportsOpenCursorsAcrossRollback()
'''
pass
def supportsOpenStatementsAcrossCommit():
'''public boolean supportsOpenStatementsAcrossCommit()
'''
pass
def supportsOpenStatementsAcrossRollback():
'''public boolean supportsOpenStatementsAcrossRollback()
'''
pass
def supportsOrderByUnrelated():
'''public boolean supportsOrderByUnrelated()
'''
pass
def supportsOuterJoins():
'''public boolean supportsOuterJoins()
'''
pass
def supportsPositionedDelete():
'''public boolean supportsPositionedDelete()
'''
pass
def supportsPositionedUpdate():
'''public boolean supportsPositionedUpdate()
'''
pass
def supportsResultSetConcurrency():
'''public boolean supportsResultSetConcurrency(final int type, final int concurrency)
'''
pass
def supportsResultSetHoldability():
'''public boolean supportsResultSetHoldability(final int holdability)
'''
pass
def supportsResultSetType():
'''public boolean supportsResultSetType(final int type)
'''
pass
def supportsSavepoints():
'''public boolean supportsSavepoints()
'''
pass
def supportsSchemasInDataManipulation():
'''public boolean supportsSchemasInDataManipulation()
'''
pass
def supportsSchemasInIndexDefinitions():
'''public boolean supportsSchemasInIndexDefinitions()
'''
pass
def supportsSchemasInPrivilegeDefinitions():
'''public boolean supportsSchemasInPrivilegeDefinitions()
'''
pass
def supportsSchemasInProcedureCalls():
'''public boolean supportsSchemasInProcedureCalls()
'''
pass
def supportsSchemasInTableDefinitions():
'''public boolean supportsSchemasInTableDefinitions()
'''
pass
def supportsSelectForUpdate():
'''public boolean supportsSelectForUpdate()
'''
pass
def supportsStatementPooling():
'''public boolean supportsStatementPooling()
'''
pass
def supportsStoredFunctionsUsingCallSyntax():
'''public boolean supportsStoredFunctionsUsingCallSyntax()
'''
pass
def supportsStoredProcedures():
'''public boolean supportsStoredProcedures()
'''
pass
def supportsSubqueriesInComparisons():
'''public boolean supportsSubqueriesInComparisons()
'''
pass
def supportsSubqueriesInExists():
'''public boolean supportsSubqueriesInExists()
'''
pass
def supportsSubqueriesInIns():
'''public boolean supportsSubqueriesInIns()
'''
pass
def supportsSubqueriesInQuantifieds():
'''public boolean supportsSubqueriesInQuantifieds()
'''
pass
def supportsTableCorrelationNames():
'''public boolean supportsTableCorrelationNames()
'''
pass
def supportsTransactionIsolationLevel():
'''public boolean supportsTransactionIsolationLevel(final int level)
'''
pass
def supportsTransactions():
'''public boolean supportsTransactions()
'''
pass
def supportsUnion():
'''public boolean supportsUnion()
'''
pass
def supportsUnionAll():
'''public boolean supportsUnionAll()
'''
pass
def updatesAreDetected():
'''public boolean updatesAreDetected(final int type)
'''
pass
def usesLocalFilePerTable():
'''public boolean usesLocalFilePerTable()
'''
pass
def usesLocalFiles():
'''public boolean usesLocalFiles()
'''
pass
def isWrapperFor():
'''public boolean isWrapperFor(final Class<?> iface)
'''
pass
def unwrap():
'''public <T> T unwrap(final Class<T> iface)
'''
pass
def getPseudoColumns():
'''public ResultSet getPseudoColumns(final String catalog, final String schemaPattern, final String tableNamePattern, final String columnNamePattern)
'''
pass
def generatedKeyAlwaysReturned():
'''public boolean generatedKeyAlwaysReturned()
'''
pass
