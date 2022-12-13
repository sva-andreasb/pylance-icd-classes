def MTDatabaseMetaData():
    '''public MTDatabaseMetaData(final DatabaseMetaData metaData)
    '''
def supportsBatchUpdates():
    '''public boolean supportsBatchUpdates()
    '''
def allProceduresAreCallable():
    '''public boolean allProceduresAreCallable()
    '''
def allTablesAreSelectable():
    '''public boolean allTablesAreSelectable()
    '''
def autoCommitFailureClosesAllResultSets():
    '''public boolean autoCommitFailureClosesAllResultSets()
    '''
def dataDefinitionCausesTransactionCommit():
    '''public boolean dataDefinitionCausesTransactionCommit()
    '''
def dataDefinitionIgnoredInTransactions():
    '''public boolean dataDefinitionIgnoredInTransactions()
    '''
def deletesAreDetected():
    '''public boolean deletesAreDetected(final int type)
    '''
def doesMaxRowSizeIncludeBlobs():
    '''public boolean doesMaxRowSizeIncludeBlobs()
    '''
def getAttributes():
    '''public ResultSet getAttributes(final String catalog, final String schemaPattern, final String typeNamePattern, final String attributeNamePattern)
    '''
def getBestRowIdentifier():
    '''public ResultSet getBestRowIdentifier(final String catalog, final String schema, final String table, final int scope, final boolean nullable)
    '''
def getCatalogSeparator():
    '''public String getCatalogSeparator()
    '''
def getCatalogTerm():
    '''public String getCatalogTerm()
    '''
def getCatalogs():
    '''public ResultSet getCatalogs()
    '''
def getClientInfoProperties():
    '''public ResultSet getClientInfoProperties()
    '''
def getColumnPrivileges():
    '''public ResultSet getColumnPrivileges(final String catalog, final String schema, final String table, final String columnNamePattern)
    '''
def getColumns():
    '''public ResultSet getColumns(final String catalog, final String schemaPattern, final String tableNamePattern, final String columnNamePattern)
    '''
def getConnection():
    '''public Connection getConnection()
    '''
def getCrossReference():
    '''public ResultSet getCrossReference(final String parentCatalog, final String parentSchema, final String parentTable, final String foreignCatalog, final String foreignSchema, final String foreignTable)
    '''
def getDatabaseMajorVersion():
    '''public int getDatabaseMajorVersion()
    '''
def getDatabaseMinorVersion():
    '''public int getDatabaseMinorVersion()
    '''
def getDatabaseProductName():
    '''public String getDatabaseProductName()
    '''
def getDatabaseProductVersion():
    '''public String getDatabaseProductVersion()
    '''
def getDefaultTransactionIsolation():
    '''public int getDefaultTransactionIsolation()
    '''
def getDriverMajorVersion():
    '''public int getDriverMajorVersion()
    '''
def getDriverMinorVersion():
    '''public int getDriverMinorVersion()
    '''
def getDriverName():
    '''public String getDriverName()
    '''
def getDriverVersion():
    '''public String getDriverVersion()
    '''
def getExportedKeys():
    '''public ResultSet getExportedKeys(final String catalog, final String schema, final String table)
    '''
def getExtraNameCharacters():
    '''public String getExtraNameCharacters()
    '''
def getFunctionColumns():
    '''public ResultSet getFunctionColumns(final String catalog, final String schemaPattern, final String functionNamePattern, final String columnNamePattern)
    '''
def getFunctions():
    '''public ResultSet getFunctions(final String catalog, final String schemaPattern, final String functionNamePattern)
    '''
def getIdentifierQuoteString():
    '''public String getIdentifierQuoteString()
    '''
def getImportedKeys():
    '''public ResultSet getImportedKeys(final String catalog, final String schema, final String table)
    '''
def getIndexInfo():
    '''public ResultSet getIndexInfo(final String catalog, final String schema, final String table, final boolean unique, final boolean approximate)
    '''
def getJDBCMajorVersion():
    '''public int getJDBCMajorVersion()
    '''
def getJDBCMinorVersion():
    '''public int getJDBCMinorVersion()
    '''
def getMaxBinaryLiteralLength():
    '''public int getMaxBinaryLiteralLength()
    '''
def getMaxCatalogNameLength():
    '''public int getMaxCatalogNameLength()
    '''
def getMaxCharLiteralLength():
    '''public int getMaxCharLiteralLength()
    '''
def getMaxColumnNameLength():
    '''public int getMaxColumnNameLength()
    '''
def getMaxColumnsInGroupBy():
    '''public int getMaxColumnsInGroupBy()
    '''
def getMaxColumnsInIndex():
    '''public int getMaxColumnsInIndex()
    '''
def getMaxColumnsInOrderBy():
    '''public int getMaxColumnsInOrderBy()
    '''
def getMaxColumnsInSelect():
    '''public int getMaxColumnsInSelect()
    '''
def getMaxColumnsInTable():
    '''public int getMaxColumnsInTable()
    '''
def getMaxConnections():
    '''public int getMaxConnections()
    '''
def getMaxCursorNameLength():
    '''public int getMaxCursorNameLength()
    '''
def getMaxIndexLength():
    '''public int getMaxIndexLength()
    '''
def getMaxProcedureNameLength():
    '''public int getMaxProcedureNameLength()
    '''
def getMaxRowSize():
    '''public int getMaxRowSize()
    '''
def getMaxSchemaNameLength():
    '''public int getMaxSchemaNameLength()
    '''
def getMaxStatementLength():
    '''public int getMaxStatementLength()
    '''
def getMaxStatements():
    '''public int getMaxStatements()
    '''
def getMaxTableNameLength():
    '''public int getMaxTableNameLength()
    '''
def getMaxTablesInSelect():
    '''public int getMaxTablesInSelect()
    '''
def getMaxUserNameLength():
    '''public int getMaxUserNameLength()
    '''
def getNumericFunctions():
    '''public String getNumericFunctions()
    '''
def getPrimaryKeys():
    '''public ResultSet getPrimaryKeys(final String catalog, final String schema, final String table)
    '''
def getProcedureColumns():
    '''public ResultSet getProcedureColumns(final String catalog, final String schemaPattern, final String procedureNamePattern, final String columnNamePattern)
    '''
def getProcedureTerm():
    '''public String getProcedureTerm()
    '''
def getProcedures():
    '''public ResultSet getProcedures(final String catalog, final String schemaPattern, final String procedureNamePattern)
    '''
def getResultSetHoldability():
    '''public int getResultSetHoldability()
    '''
def getRowIdLifetime():
    '''public RowIdLifetime getRowIdLifetime()
    '''
def getSQLKeywords():
    '''public String getSQLKeywords()
    '''
def getSQLStateType():
    '''public int getSQLStateType()
    '''
def getSchemaTerm():
    '''public String getSchemaTerm()
    '''
def getSchemas():
    '''public ResultSet getSchemas()
    public ResultSet getSchemas(final String catalog, final String schemaPattern)
    '''
def getSearchStringEscape():
    '''public String getSearchStringEscape()
    '''
def getStringFunctions():
    '''public String getStringFunctions()
    '''
def getSuperTables():
    '''public ResultSet getSuperTables(final String catalog, final String schemaPattern, final String tableNamePattern)
    '''
def getSuperTypes():
    '''public ResultSet getSuperTypes(final String catalog, final String schemaPattern, final String typeNamePattern)
    '''
def getSystemFunctions():
    '''public String getSystemFunctions()
    '''
def getTablePrivileges():
    '''public ResultSet getTablePrivileges(final String catalog, final String schemaPattern, final String tableNamePattern)
    '''
def getTableTypes():
    '''public ResultSet getTableTypes()
    '''
def getTables():
    '''public ResultSet getTables(final String catalog, final String schemaPattern, final String tableNamePattern, final String[] types)
    '''
def getTimeDateFunctions():
    '''public String getTimeDateFunctions()
    '''
def getTypeInfo():
    '''public ResultSet getTypeInfo()
    '''
def getUDTs():
    '''public ResultSet getUDTs(final String catalog, final String schemaPattern, final String typeNamePattern, final int[] types)
    '''
def getURL():
    '''public String getURL()
    '''
def getUserName():
    '''public String getUserName()
    '''
def getVersionColumns():
    '''public ResultSet getVersionColumns(final String catalog, final String schema, final String table)
    '''
def insertsAreDetected():
    '''public boolean insertsAreDetected(final int type)
    '''
def isCatalogAtStart():
    '''public boolean isCatalogAtStart()
    '''
def isReadOnly():
    '''public boolean isReadOnly()
    '''
def locatorsUpdateCopy():
    '''public boolean locatorsUpdateCopy()
    '''
def nullPlusNonNullIsNull():
    '''public boolean nullPlusNonNullIsNull()
    '''
def nullsAreSortedAtEnd():
    '''public boolean nullsAreSortedAtEnd()
    '''
def nullsAreSortedAtStart():
    '''public boolean nullsAreSortedAtStart()
    '''
def nullsAreSortedHigh():
    '''public boolean nullsAreSortedHigh()
    '''
def nullsAreSortedLow():
    '''public boolean nullsAreSortedLow()
    '''
def othersDeletesAreVisible():
    '''public boolean othersDeletesAreVisible(final int type)
    '''
def othersInsertsAreVisible():
    '''public boolean othersInsertsAreVisible(final int type)
    '''
def othersUpdatesAreVisible():
    '''public boolean othersUpdatesAreVisible(final int type)
    '''
def ownDeletesAreVisible():
    '''public boolean ownDeletesAreVisible(final int type)
    '''
def ownInsertsAreVisible():
    '''public boolean ownInsertsAreVisible(final int type)
    '''
def ownUpdatesAreVisible():
    '''public boolean ownUpdatesAreVisible(final int type)
    '''
def storesLowerCaseIdentifiers():
    '''public boolean storesLowerCaseIdentifiers()
    '''
def storesLowerCaseQuotedIdentifiers():
    '''public boolean storesLowerCaseQuotedIdentifiers()
    '''
def storesMixedCaseIdentifiers():
    '''public boolean storesMixedCaseIdentifiers()
    '''
def storesMixedCaseQuotedIdentifiers():
    '''public boolean storesMixedCaseQuotedIdentifiers()
    '''
def storesUpperCaseIdentifiers():
    '''public boolean storesUpperCaseIdentifiers()
    '''
def storesUpperCaseQuotedIdentifiers():
    '''public boolean storesUpperCaseQuotedIdentifiers()
    '''
def supportsANSI92EntryLevelSQL():
    '''public boolean supportsANSI92EntryLevelSQL()
    '''
def supportsANSI92FullSQL():
    '''public boolean supportsANSI92FullSQL()
    '''
def supportsANSI92IntermediateSQL():
    '''public boolean supportsANSI92IntermediateSQL()
    '''
def supportsAlterTableWithAddColumn():
    '''public boolean supportsAlterTableWithAddColumn()
    '''
def supportsAlterTableWithDropColumn():
    '''public boolean supportsAlterTableWithDropColumn()
    '''
def supportsCatalogsInDataManipulation():
    '''public boolean supportsCatalogsInDataManipulation()
    '''
def supportsCatalogsInIndexDefinitions():
    '''public boolean supportsCatalogsInIndexDefinitions()
    '''
def supportsCatalogsInPrivilegeDefinitions():
    '''public boolean supportsCatalogsInPrivilegeDefinitions()
    '''
def supportsCatalogsInProcedureCalls():
    '''public boolean supportsCatalogsInProcedureCalls()
    '''
def supportsCatalogsInTableDefinitions():
    '''public boolean supportsCatalogsInTableDefinitions()
    '''
def supportsColumnAliasing():
    '''public boolean supportsColumnAliasing()
    '''
def supportsConvert():
    '''public boolean supportsConvert()
    public boolean supportsConvert(final int fromType, final int toType)
    '''
def supportsCoreSQLGrammar():
    '''public boolean supportsCoreSQLGrammar()
    '''
def supportsCorrelatedSubqueries():
    '''public boolean supportsCorrelatedSubqueries()
    '''
def supportsDataDefinitionAndDataManipulationTransactions():
    '''public boolean supportsDataDefinitionAndDataManipulationTransactions()
    '''
def supportsDataManipulationTransactionsOnly():
    '''public boolean supportsDataManipulationTransactionsOnly()
    '''
def supportsDifferentTableCorrelationNames():
    '''public boolean supportsDifferentTableCorrelationNames()
    '''
def supportsExpressionsInOrderBy():
    '''public boolean supportsExpressionsInOrderBy()
    '''
def supportsExtendedSQLGrammar():
    '''public boolean supportsExtendedSQLGrammar()
    '''
def supportsFullOuterJoins():
    '''public boolean supportsFullOuterJoins()
    '''
def supportsGetGeneratedKeys():
    '''public boolean supportsGetGeneratedKeys()
    '''
def supportsGroupBy():
    '''public boolean supportsGroupBy()
    '''
def supportsGroupByBeyondSelect():
    '''public boolean supportsGroupByBeyondSelect()
    '''
def supportsGroupByUnrelated():
    '''public boolean supportsGroupByUnrelated()
    '''
def supportsIntegrityEnhancementFacility():
    '''public boolean supportsIntegrityEnhancementFacility()
    '''
def supportsLikeEscapeClause():
    '''public boolean supportsLikeEscapeClause()
    '''
def supportsLimitedOuterJoins():
    '''public boolean supportsLimitedOuterJoins()
    '''
def supportsMinimumSQLGrammar():
    '''public boolean supportsMinimumSQLGrammar()
    '''
def supportsMixedCaseIdentifiers():
    '''public boolean supportsMixedCaseIdentifiers()
    '''
def supportsMixedCaseQuotedIdentifiers():
    '''public boolean supportsMixedCaseQuotedIdentifiers()
    '''
def supportsMultipleOpenResults():
    '''public boolean supportsMultipleOpenResults()
    '''
def supportsMultipleResultSets():
    '''public boolean supportsMultipleResultSets()
    '''
def supportsMultipleTransactions():
    '''public boolean supportsMultipleTransactions()
    '''
def supportsNamedParameters():
    '''public boolean supportsNamedParameters()
    '''
def supportsNonNullableColumns():
    '''public boolean supportsNonNullableColumns()
    '''
def supportsOpenCursorsAcrossCommit():
    '''public boolean supportsOpenCursorsAcrossCommit()
    '''
def supportsOpenCursorsAcrossRollback():
    '''public boolean supportsOpenCursorsAcrossRollback()
    '''
def supportsOpenStatementsAcrossCommit():
    '''public boolean supportsOpenStatementsAcrossCommit()
    '''
def supportsOpenStatementsAcrossRollback():
    '''public boolean supportsOpenStatementsAcrossRollback()
    '''
def supportsOrderByUnrelated():
    '''public boolean supportsOrderByUnrelated()
    '''
def supportsOuterJoins():
    '''public boolean supportsOuterJoins()
    '''
def supportsPositionedDelete():
    '''public boolean supportsPositionedDelete()
    '''
def supportsPositionedUpdate():
    '''public boolean supportsPositionedUpdate()
    '''
def supportsResultSetConcurrency():
    '''public boolean supportsResultSetConcurrency(final int type, final int concurrency)
    '''
def supportsResultSetHoldability():
    '''public boolean supportsResultSetHoldability(final int holdability)
    '''
def supportsResultSetType():
    '''public boolean supportsResultSetType(final int type)
    '''
def supportsSavepoints():
    '''public boolean supportsSavepoints()
    '''
def supportsSchemasInDataManipulation():
    '''public boolean supportsSchemasInDataManipulation()
    '''
def supportsSchemasInIndexDefinitions():
    '''public boolean supportsSchemasInIndexDefinitions()
    '''
def supportsSchemasInPrivilegeDefinitions():
    '''public boolean supportsSchemasInPrivilegeDefinitions()
    '''
def supportsSchemasInProcedureCalls():
    '''public boolean supportsSchemasInProcedureCalls()
    '''
def supportsSchemasInTableDefinitions():
    '''public boolean supportsSchemasInTableDefinitions()
    '''
def supportsSelectForUpdate():
    '''public boolean supportsSelectForUpdate()
    '''
def supportsStatementPooling():
    '''public boolean supportsStatementPooling()
    '''
def supportsStoredFunctionsUsingCallSyntax():
    '''public boolean supportsStoredFunctionsUsingCallSyntax()
    '''
def supportsStoredProcedures():
    '''public boolean supportsStoredProcedures()
    '''
def supportsSubqueriesInComparisons():
    '''public boolean supportsSubqueriesInComparisons()
    '''
def supportsSubqueriesInExists():
    '''public boolean supportsSubqueriesInExists()
    '''
def supportsSubqueriesInIns():
    '''public boolean supportsSubqueriesInIns()
    '''
def supportsSubqueriesInQuantifieds():
    '''public boolean supportsSubqueriesInQuantifieds()
    '''
def supportsTableCorrelationNames():
    '''public boolean supportsTableCorrelationNames()
    '''
def supportsTransactionIsolationLevel():
    '''public boolean supportsTransactionIsolationLevel(final int level)
    '''
def supportsTransactions():
    '''public boolean supportsTransactions()
    '''
def supportsUnion():
    '''public boolean supportsUnion()
    '''
def supportsUnionAll():
    '''public boolean supportsUnionAll()
    '''
def updatesAreDetected():
    '''public boolean updatesAreDetected(final int type)
    '''
def usesLocalFilePerTable():
    '''public boolean usesLocalFilePerTable()
    '''
def usesLocalFiles():
    '''public boolean usesLocalFiles()
    '''
def isWrapperFor():
    '''public boolean isWrapperFor(final Class<?> iface)
    '''
def unwrap():
    '''public <T> T unwrap(final Class<T> iface)
    '''
def getPseudoColumns():
    '''public ResultSet getPseudoColumns(final String catalog, final String schemaPattern, final String tableNamePattern, final String columnNamePattern)
    '''
def generatedKeyAlwaysReturned():
    '''public boolean generatedKeyAlwaysReturned()
    '''
