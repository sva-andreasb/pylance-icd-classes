def ():
    '''returns SQLServerDatabaseMetaData\n\n
    (final SQLServerConnection con)\n
    '''
def isWrapperFor():
    '''returns boolean\n\n
    isWrapperFor(final Class<?> iface)\n
    '''
def allProceduresAreCallable():
    '''returns boolean\n\n
    allProceduresAreCallable()\n
    '''
def allTablesAreSelectable():
    '''returns boolean\n\n
    allTablesAreSelectable()\n
    '''
def autoCommitFailureClosesAllResultSets():
    '''returns boolean\n\n
    autoCommitFailureClosesAllResultSets()\n
    '''
def dataDefinitionCausesTransactionCommit():
    '''returns boolean\n\n
    dataDefinitionCausesTransactionCommit()\n
    '''
def dataDefinitionIgnoredInTransactions():
    '''returns boolean\n\n
    dataDefinitionIgnoredInTransactions()\n
    '''
def doesMaxRowSizeIncludeBlobs():
    '''returns boolean\n\n
    doesMaxRowSizeIncludeBlobs()\n
    '''
def generatedKeyAlwaysReturned():
    '''returns boolean\n\n
    generatedKeyAlwaysReturned()\n
    '''
def getMaxLogicalLobSize():
    '''returns long\n\n
    getMaxLogicalLobSize()\n
    '''
def supportsRefCursors():
    '''returns boolean\n\n
    supportsRefCursors()\n
    '''
def supportsSharding():
    '''returns boolean\n\n
    supportsSharding()\n
    '''
def getCatalogs():
    '''returns ResultSet\n\n
    getCatalogs()\n
    '''
def getCatalogSeparator():
    '''returns String\n\n
    getCatalogSeparator()\n
    '''
def getCatalogTerm():
    '''returns String\n\n
    getCatalogTerm()\n
    '''
def getColumnPrivileges():
    '''returns ResultSet\n\n
    getColumnPrivileges(final String catalog, final String schema, final String table, String col)\n
    '''
def getTables():
    '''returns ResultSet\n\n
    getTables(final String catalog, String schema, String table, final String[] types)\n
    '''
def getColumns():
    '''returns ResultSet\n\n
    getColumns(final String catalog, final String schema, final String table, final String col)\n
    '''
def getFunctions():
    '''returns ResultSet\n\n
    getFunctions(final String catalog, final String schemaPattern, final String functionNamePattern)\n
    '''
def getFunctionColumns():
    '''returns ResultSet\n\n
    getFunctionColumns(final String catalog, final String schemaPattern, final String functionNamePattern, final String columnNamePattern)\n
    '''
def getClientInfoProperties():
    '''returns ResultSet\n\n
    getClientInfoProperties()\n
    '''
def getBestRowIdentifier():
    '''returns ResultSet\n\n
    getBestRowIdentifier(final String catalog, final String schema, final String table, final int scope, final boolean nullable)\n
    '''
def getCrossReference():
    '''returns ResultSet\n\n
    getCrossReference(final String cat1, final String schem1, final String tab1, final String cat2, final String schem2, final String tab2)\n
    '''
def getDatabaseProductName():
    '''returns String\n\n
    getDatabaseProductName()\n
    '''
def getDatabaseProductVersion():
    '''returns String\n\n
    getDatabaseProductVersion()\n
    '''
def getDefaultTransactionIsolation():
    '''returns int\n\n
    getDefaultTransactionIsolation()\n
    '''
def getDriverMajorVersion():
    '''returns int\n\n
    getDriverMajorVersion()\n
    '''
def getDriverMinorVersion():
    '''returns int\n\n
    getDriverMinorVersion()\n
    '''
def getDriverName():
    '''returns String\n\n
    getDriverName()\n
    '''
def getDriverVersion():
    '''returns String\n\n
    getDriverVersion()\n
    '''
def getExportedKeys():
    '''returns ResultSet\n\n
    getExportedKeys(final String cat, final String schema, final String table)\n
    '''
def getExtraNameCharacters():
    '''returns String\n\n
    getExtraNameCharacters()\n
    '''
def getIdentifierQuoteString():
    '''returns String\n\n
    getIdentifierQuoteString()\n
    '''
def getImportedKeys():
    '''returns ResultSet\n\n
    getImportedKeys(final String cat, final String schema, final String table)\n
    '''
def getIndexInfo():
    '''returns ResultSet\n\n
    getIndexInfo(final String cat, final String schema, final String table, final boolean unique, final boolean approximate)\n
    '''
def getMaxBinaryLiteralLength():
    '''returns int\n\n
    getMaxBinaryLiteralLength()\n
    '''
def getMaxCatalogNameLength():
    '''returns int\n\n
    getMaxCatalogNameLength()\n
    '''
def getMaxCharLiteralLength():
    '''returns int\n\n
    getMaxCharLiteralLength()\n
    '''
def getMaxColumnNameLength():
    '''returns int\n\n
    getMaxColumnNameLength()\n
    '''
def getMaxColumnsInGroupBy():
    '''returns int\n\n
    getMaxColumnsInGroupBy()\n
    '''
def getMaxColumnsInIndex():
    '''returns int\n\n
    getMaxColumnsInIndex()\n
    '''
def getMaxColumnsInOrderBy():
    '''returns int\n\n
    getMaxColumnsInOrderBy()\n
    '''
def getMaxColumnsInSelect():
    '''returns int\n\n
    getMaxColumnsInSelect()\n
    '''
def getMaxColumnsInTable():
    '''returns int\n\n
    getMaxColumnsInTable()\n
    '''
def getMaxConnections():
    '''returns int\n\n
    getMaxConnections()\n
    '''
def getMaxCursorNameLength():
    '''returns int\n\n
    getMaxCursorNameLength()\n
    '''
def getMaxIndexLength():
    '''returns int\n\n
    getMaxIndexLength()\n
    '''
def getMaxProcedureNameLength():
    '''returns int\n\n
    getMaxProcedureNameLength()\n
    '''
def getMaxRowSize():
    '''returns int\n\n
    getMaxRowSize()\n
    '''
def getMaxSchemaNameLength():
    '''returns int\n\n
    getMaxSchemaNameLength()\n
    '''
def getMaxStatementLength():
    '''returns int\n\n
    getMaxStatementLength()\n
    '''
def getMaxStatements():
    '''returns int\n\n
    getMaxStatements()\n
    '''
def getMaxTableNameLength():
    '''returns int\n\n
    getMaxTableNameLength()\n
    '''
def getMaxTablesInSelect():
    '''returns int\n\n
    getMaxTablesInSelect()\n
    '''
def getMaxUserNameLength():
    '''returns int\n\n
    getMaxUserNameLength()\n
    '''
def getNumericFunctions():
    '''returns String\n\n
    getNumericFunctions()\n
    '''
def getPrimaryKeys():
    '''returns ResultSet\n\n
    getPrimaryKeys(final String cat, final String schema, final String table)\n
    '''
def getProcedureColumns():
    '''returns ResultSet\n\n
    getProcedureColumns(final String catalog, final String schema, String proc, String col)\n
    '''
def getProcedures():
    '''returns ResultSet\n\n
    getProcedures(final String catalog, final String schema, final String proc)\n
    '''
def getProcedureTerm():
    '''returns String\n\n
    getProcedureTerm()\n
    '''
def getPseudoColumns():
    '''returns ResultSet\n\n
    getPseudoColumns(final String catalog, final String schemaPattern, final String tableNamePattern, final String columnNamePattern)\n
    '''
def getSchemas():
    '''returns ResultSet\n\n
    getSchemas()\n
    getSchemas(final String catalog, final String schemaPattern)\n
    '''
def getSchemaTerm():
    '''returns String\n\n
    getSchemaTerm()\n
    '''
def getSearchStringEscape():
    '''returns String\n\n
    getSearchStringEscape()\n
    '''
def getSQLKeywords():
    '''returns String\n\n
    getSQLKeywords()\n
    '''
def getStringFunctions():
    '''returns String\n\n
    getStringFunctions()\n
    '''
def getSystemFunctions():
    '''returns String\n\n
    getSystemFunctions()\n
    '''
def getTablePrivileges():
    '''returns ResultSet\n\n
    getTablePrivileges(final String catalog, String schema, String table)\n
    '''
def getTableTypes():
    '''returns ResultSet\n\n
    getTableTypes()\n
    '''
def getTimeDateFunctions():
    '''returns String\n\n
    getTimeDateFunctions()\n
    '''
def getTypeInfo():
    '''returns ResultSet\n\n
    getTypeInfo()\n
    '''
def getURL():
    '''returns String\n\n
    getURL()\n
    '''
def getUserName():
    '''returns String\n\n
    getUserName()\n
    '''
def getVersionColumns():
    '''returns ResultSet\n\n
    getVersionColumns(final String catalog, final String schema, final String table)\n
    '''
def isCatalogAtStart():
    '''returns boolean\n\n
    isCatalogAtStart()\n
    '''
def isReadOnly():
    '''returns boolean\n\n
    isReadOnly()\n
    '''
def nullPlusNonNullIsNull():
    '''returns boolean\n\n
    nullPlusNonNullIsNull()\n
    '''
def nullsAreSortedAtEnd():
    '''returns boolean\n\n
    nullsAreSortedAtEnd()\n
    '''
def nullsAreSortedAtStart():
    '''returns boolean\n\n
    nullsAreSortedAtStart()\n
    '''
def nullsAreSortedHigh():
    '''returns boolean\n\n
    nullsAreSortedHigh()\n
    '''
def nullsAreSortedLow():
    '''returns boolean\n\n
    nullsAreSortedLow()\n
    '''
def storesLowerCaseIdentifiers():
    '''returns boolean\n\n
    storesLowerCaseIdentifiers()\n
    '''
def storesLowerCaseQuotedIdentifiers():
    '''returns boolean\n\n
    storesLowerCaseQuotedIdentifiers()\n
    '''
def storesMixedCaseIdentifiers():
    '''returns boolean\n\n
    storesMixedCaseIdentifiers()\n
    '''
def storesMixedCaseQuotedIdentifiers():
    '''returns boolean\n\n
    storesMixedCaseQuotedIdentifiers()\n
    '''
def storesUpperCaseIdentifiers():
    '''returns boolean\n\n
    storesUpperCaseIdentifiers()\n
    '''
def storesUpperCaseQuotedIdentifiers():
    '''returns boolean\n\n
    storesUpperCaseQuotedIdentifiers()\n
    '''
def supportsAlterTableWithAddColumn():
    '''returns boolean\n\n
    supportsAlterTableWithAddColumn()\n
    '''
def supportsAlterTableWithDropColumn():
    '''returns boolean\n\n
    supportsAlterTableWithDropColumn()\n
    '''
def supportsANSI92EntryLevelSQL():
    '''returns boolean\n\n
    supportsANSI92EntryLevelSQL()\n
    '''
def supportsANSI92FullSQL():
    '''returns boolean\n\n
    supportsANSI92FullSQL()\n
    '''
def supportsANSI92IntermediateSQL():
    '''returns boolean\n\n
    supportsANSI92IntermediateSQL()\n
    '''
def supportsCatalogsInDataManipulation():
    '''returns boolean\n\n
    supportsCatalogsInDataManipulation()\n
    '''
def supportsCatalogsInIndexDefinitions():
    '''returns boolean\n\n
    supportsCatalogsInIndexDefinitions()\n
    '''
def supportsCatalogsInPrivilegeDefinitions():
    '''returns boolean\n\n
    supportsCatalogsInPrivilegeDefinitions()\n
    '''
def supportsCatalogsInProcedureCalls():
    '''returns boolean\n\n
    supportsCatalogsInProcedureCalls()\n
    '''
def supportsCatalogsInTableDefinitions():
    '''returns boolean\n\n
    supportsCatalogsInTableDefinitions()\n
    '''
def supportsColumnAliasing():
    '''returns boolean\n\n
    supportsColumnAliasing()\n
    '''
def supportsConvert():
    '''returns boolean\n\n
    supportsConvert()\n
    supportsConvert(final int fromType, final int toType)\n
    '''
def supportsCoreSQLGrammar():
    '''returns boolean\n\n
    supportsCoreSQLGrammar()\n
    '''
def supportsCorrelatedSubqueries():
    '''returns boolean\n\n
    supportsCorrelatedSubqueries()\n
    '''
def supportsDataDefinitionAndDataManipulationTransactions():
    '''returns boolean\n\n
    supportsDataDefinitionAndDataManipulationTransactions()\n
    '''
def supportsDataManipulationTransactionsOnly():
    '''returns boolean\n\n
    supportsDataManipulationTransactionsOnly()\n
    '''
def supportsDifferentTableCorrelationNames():
    '''returns boolean\n\n
    supportsDifferentTableCorrelationNames()\n
    '''
def supportsExpressionsInOrderBy():
    '''returns boolean\n\n
    supportsExpressionsInOrderBy()\n
    '''
def supportsExtendedSQLGrammar():
    '''returns boolean\n\n
    supportsExtendedSQLGrammar()\n
    '''
def supportsFullOuterJoins():
    '''returns boolean\n\n
    supportsFullOuterJoins()\n
    '''
def supportsGroupBy():
    '''returns boolean\n\n
    supportsGroupBy()\n
    '''
def supportsGroupByBeyondSelect():
    '''returns boolean\n\n
    supportsGroupByBeyondSelect()\n
    '''
def supportsGroupByUnrelated():
    '''returns boolean\n\n
    supportsGroupByUnrelated()\n
    '''
def supportsIntegrityEnhancementFacility():
    '''returns boolean\n\n
    supportsIntegrityEnhancementFacility()\n
    '''
def supportsLikeEscapeClause():
    '''returns boolean\n\n
    supportsLikeEscapeClause()\n
    '''
def supportsLimitedOuterJoins():
    '''returns boolean\n\n
    supportsLimitedOuterJoins()\n
    '''
def supportsMinimumSQLGrammar():
    '''returns boolean\n\n
    supportsMinimumSQLGrammar()\n
    '''
def supportsMixedCaseIdentifiers():
    '''returns boolean\n\n
    supportsMixedCaseIdentifiers()\n
    '''
def supportsMixedCaseQuotedIdentifiers():
    '''returns boolean\n\n
    supportsMixedCaseQuotedIdentifiers()\n
    '''
def supportsMultipleResultSets():
    '''returns boolean\n\n
    supportsMultipleResultSets()\n
    '''
def supportsMultipleTransactions():
    '''returns boolean\n\n
    supportsMultipleTransactions()\n
    '''
def supportsNonNullableColumns():
    '''returns boolean\n\n
    supportsNonNullableColumns()\n
    '''
def supportsOpenCursorsAcrossCommit():
    '''returns boolean\n\n
    supportsOpenCursorsAcrossCommit()\n
    '''
def supportsOpenCursorsAcrossRollback():
    '''returns boolean\n\n
    supportsOpenCursorsAcrossRollback()\n
    '''
def supportsOpenStatementsAcrossCommit():
    '''returns boolean\n\n
    supportsOpenStatementsAcrossCommit()\n
    '''
def supportsOpenStatementsAcrossRollback():
    '''returns boolean\n\n
    supportsOpenStatementsAcrossRollback()\n
    '''
def supportsOrderByUnrelated():
    '''returns boolean\n\n
    supportsOrderByUnrelated()\n
    '''
def supportsOuterJoins():
    '''returns boolean\n\n
    supportsOuterJoins()\n
    '''
def supportsPositionedDelete():
    '''returns boolean\n\n
    supportsPositionedDelete()\n
    '''
def supportsPositionedUpdate():
    '''returns boolean\n\n
    supportsPositionedUpdate()\n
    '''
def supportsSchemasInDataManipulation():
    '''returns boolean\n\n
    supportsSchemasInDataManipulation()\n
    '''
def supportsSchemasInIndexDefinitions():
    '''returns boolean\n\n
    supportsSchemasInIndexDefinitions()\n
    '''
def supportsSchemasInPrivilegeDefinitions():
    '''returns boolean\n\n
    supportsSchemasInPrivilegeDefinitions()\n
    '''
def supportsSchemasInProcedureCalls():
    '''returns boolean\n\n
    supportsSchemasInProcedureCalls()\n
    '''
def supportsSchemasInTableDefinitions():
    '''returns boolean\n\n
    supportsSchemasInTableDefinitions()\n
    '''
def supportsSelectForUpdate():
    '''returns boolean\n\n
    supportsSelectForUpdate()\n
    '''
def supportsStoredProcedures():
    '''returns boolean\n\n
    supportsStoredProcedures()\n
    '''
def supportsSubqueriesInComparisons():
    '''returns boolean\n\n
    supportsSubqueriesInComparisons()\n
    '''
def supportsSubqueriesInExists():
    '''returns boolean\n\n
    supportsSubqueriesInExists()\n
    '''
def supportsSubqueriesInIns():
    '''returns boolean\n\n
    supportsSubqueriesInIns()\n
    '''
def supportsSubqueriesInQuantifieds():
    '''returns boolean\n\n
    supportsSubqueriesInQuantifieds()\n
    '''
def supportsTableCorrelationNames():
    '''returns boolean\n\n
    supportsTableCorrelationNames()\n
    '''
def supportsTransactionIsolationLevel():
    '''returns boolean\n\n
    supportsTransactionIsolationLevel(final int level)\n
    '''
def supportsTransactions():
    '''returns boolean\n\n
    supportsTransactions()\n
    '''
def supportsUnion():
    '''returns boolean\n\n
    supportsUnion()\n
    '''
def supportsUnionAll():
    '''returns boolean\n\n
    supportsUnionAll()\n
    '''
def usesLocalFilePerTable():
    '''returns boolean\n\n
    usesLocalFilePerTable()\n
    '''
def usesLocalFiles():
    '''returns boolean\n\n
    usesLocalFiles()\n
    '''
def supportsResultSetType():
    '''returns boolean\n\n
    supportsResultSetType(final int type)\n
    '''
def supportsResultSetConcurrency():
    '''returns boolean\n\n
    supportsResultSetConcurrency(final int type, final int concurrency)\n
    '''
def ownUpdatesAreVisible():
    '''returns boolean\n\n
    ownUpdatesAreVisible(final int type)\n
    '''
def ownDeletesAreVisible():
    '''returns boolean\n\n
    ownDeletesAreVisible(final int type)\n
    '''
def ownInsertsAreVisible():
    '''returns boolean\n\n
    ownInsertsAreVisible(final int type)\n
    '''
def othersUpdatesAreVisible():
    '''returns boolean\n\n
    othersUpdatesAreVisible(final int type)\n
    '''
def othersDeletesAreVisible():
    '''returns boolean\n\n
    othersDeletesAreVisible(final int type)\n
    '''
def othersInsertsAreVisible():
    '''returns boolean\n\n
    othersInsertsAreVisible(final int type)\n
    '''
def updatesAreDetected():
    '''returns boolean\n\n
    updatesAreDetected(final int type)\n
    '''
def deletesAreDetected():
    '''returns boolean\n\n
    deletesAreDetected(final int type)\n
    '''
def insertsAreDetected():
    '''returns boolean\n\n
    insertsAreDetected(final int type)\n
    '''
def supportsBatchUpdates():
    '''returns boolean\n\n
    supportsBatchUpdates()\n
    '''
def getUDTs():
    '''returns ResultSet\n\n
    getUDTs(final String catalog, final String schemaPattern, final String typeNamePattern, final int[] types)\n
    '''
def getConnection():
    '''returns Connection\n\n
    getConnection()\n
    '''
def getSQLStateType():
    '''returns int\n\n
    getSQLStateType()\n
    '''
def getDatabaseMajorVersion():
    '''returns int\n\n
    getDatabaseMajorVersion()\n
    '''
def getDatabaseMinorVersion():
    '''returns int\n\n
    getDatabaseMinorVersion()\n
    '''
def getJDBCMajorVersion():
    '''returns int\n\n
    getJDBCMajorVersion()\n
    '''
def getJDBCMinorVersion():
    '''returns int\n\n
    getJDBCMinorVersion()\n
    '''
def getResultSetHoldability():
    '''returns int\n\n
    getResultSetHoldability()\n
    '''
def getRowIdLifetime():
    '''returns RowIdLifetime\n\n
    getRowIdLifetime()\n
    '''
def supportsResultSetHoldability():
    '''returns boolean\n\n
    supportsResultSetHoldability(final int holdability)\n
    '''
def getAttributes():
    '''returns ResultSet\n\n
    getAttributes(final String catalog, final String schemaPattern, final String typeNamePattern, final String attributeNamePattern)\n
    '''
def getSuperTables():
    '''returns ResultSet\n\n
    getSuperTables(final String catalog, final String schemaPattern, final String tableNamePattern)\n
    '''
def getSuperTypes():
    '''returns ResultSet\n\n
    getSuperTypes(final String catalog, final String schemaPattern, final String typeNamePattern)\n
    '''
def supportsGetGeneratedKeys():
    '''returns boolean\n\n
    supportsGetGeneratedKeys()\n
    '''
def supportsMultipleOpenResults():
    '''returns boolean\n\n
    supportsMultipleOpenResults()\n
    '''
def supportsNamedParameters():
    '''returns boolean\n\n
    supportsNamedParameters()\n
    '''
def supportsSavepoints():
    '''returns boolean\n\n
    supportsSavepoints()\n
    '''
def supportsStatementPooling():
    '''returns boolean\n\n
    supportsStatementPooling()\n
    '''
def supportsStoredFunctionsUsingCallSyntax():
    '''returns boolean\n\n
    supportsStoredFunctionsUsingCallSyntax()\n
    '''
def locatorsUpdateCopy():
    '''returns boolean\n\n
    locatorsUpdateCopy()\n
    '''
