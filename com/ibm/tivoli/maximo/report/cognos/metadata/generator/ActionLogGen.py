ROS_SITEORGTYPE = "String  \"SITEORGTYPE\""
ROS_APP = "String  \"APP\""
def ():
    '''returns ActionLogGen\n\n
    (final PrintWriter out)\n
    '''
def generateScriptHeader():
    '''returns None\n\n
    generateScriptHeader()\n
    '''
def generateScriptTail():
    '''returns None\n\n
    generateScriptTail()\n
    '''
def generateTransactionHeader():
    '''returns None\n\n
    generateTransactionHeader()\n
    generateTransactionHeader(final boolean useSavedAttribute)\n
    '''
def generateTransactionTail():
    '''returns None\n\n
    generateTransactionTail()\n
    '''
def generateProjectInitialization():
    '''returns None\n\n
    generateProjectInitialization(final String projectName, final String topLevelNamespace)\n
    generateProjectInitialization(final String projectName, final String topLevelNamespace, final String defaultLocale)\n
    generateProjectInitialization(final String projectName, final String topLevelNamespace, final String defaultLocale, final String queryMode)\n
    '''
def generateCreateNamespace():
    '''returns None\n\n
    generateCreateNamespace(final String namespace, final String parentNamespace)\n
    '''
def generateDBImport():
    '''returns None\n\n
    generateDBImport(final String parentNamespace, final String databaseType, final String dataSourceName, final String schema, final Set<MXObject> tables, final Set<MXObject> views, final String databaseName)\n
    '''
def generateModelQuerySubject():
    '''returns None\n\n
    generateModelQuerySubject(final String parentNamespace, final String querySubjectName)\n
    generateModelQuerySubject(final String parentNamespace, final String querySubjectName, final String defaultLocale)\n
    '''
def generateModelQueryItem():
    '''returns None\n\n
    generateModelQueryItem(final String parentNamespace, final String querySubjectName, final String queryItemName, final String basedOnNamespace, final String sourceQuerySubjectName, final String queryItemDescription, final String dataSourceQueryItemName)\n
    generateModelQueryItem(final String parentNamespace, final String querySubjectName, final String queryItemName, final String basedOnNamespace, final String sourceQuerySubjectName, final String queryItemDescription, final String dataSourceQueryItemName, final String defaultLocale)\n
    '''
def generateHideQueryItem():
    '''returns None\n\n
    generateHideQueryItem(final String parentNamespace, final String querySubjectName, final String queryItemName)\n
    '''
def generateEvaluateQuerySubject():
    '''returns None\n\n
    generateEvaluateQuerySubject(final String parentNamespace, final String querySubjectName)\n
    '''
def generateReorderByNameQuerySubject():
    '''returns None\n\n
    generateReorderByNameQuerySubject(final String parentNamespace, final String querySubjectName)\n
    '''
def generateRelationship():
    '''returns None\n\n
    generateRelationship(final String topLevelNamespace, final String parentNamespace, final String leftQuerySubjectName, final String leftMinCardinality, final String leftMaxCardinality, final String rightQuerySubjectName, final String rightMinCardinality, final String rightMaxCardinality, final String relationshipName, final List<String> leftQueryItems, final List<String> rightQueryItems)\n
    generateRelationship(final String topLevelNamespace, final String parentNamespace, final String leftQuerySubjectName, final String leftMinCardinality, final String leftMaxCardinality, final String rightQuerySubjectName, final String rightMinCardinality, final String rightMaxCardinality, final String relationshipName, final String cognosRelationship)\n
    '''
def generateAllowCrossProductJoin():
    '''returns None\n\n
    generateAllowCrossProductJoin()\n
    '''
def generateSetQueryProcessingToLocal():
    '''returns None\n\n
    generateSetQueryProcessingToLocal(final String dataSourceName)\n
    '''
def generateCreatePackage():
    '''returns None\n\n
    generateCreatePackage(final String packageName, final String excludedNamespace, final String topLevelNamespace)\n
    generateCreatePackage(final String packageName, final String excludedNamespace, final String topLevelNamespace, final String defaultLocale, final List<String> languages)\n
    '''
def generatePublishPackage():
    '''returns None\n\n
    generatePublishPackage(final String packageName, final String contentStorePackageLocation)\n
    '''
def generateAddProjectLocale():
    '''returns None\n\n
    generateAddProjectLocale(final String locale, final String defaultLocale)\n
    '''
def generatePackageNameTranslations():
    '''returns None\n\n
    generatePackageNameTranslations(final String packageName, final String nameTranslation, final int localeIndex)\n
    '''
def generateModelNameTranslation():
    '''returns None\n\n
    generateModelNameTranslation(final String modelName, final String nameTranslation, final int localeIndex)\n
    '''
def generateNamespaceTranslation():
    '''returns None\n\n
    generateNamespaceTranslation(final String namespace, final String nameTranslation, final int localeIndex)\n
    '''
def generateModelQuerySubjectTranslations():
    '''returns None\n\n
    generateModelQuerySubjectTranslations(final String parentNamespace, final String querySubjectName, final String nameTranslation, final int localeIndex)\n
    '''
def generateModelQueryItemNameTranslation():
    '''returns None\n\n
    generateModelQueryItemNameTranslation(final String parentNamespace, final String querySubjectName, final String queryItemName, final String nameTranslation, final int localeIndex)\n
    '''
def generateModelQueryItemDescTranslation():
    '''returns None\n\n
    generateModelQueryItemDescTranslation(final String parentNamespace, final String querySubjectName, final String queryItemName, final String descTranslation, final int localeIndex)\n
    '''
def getQuerySubjectSequence():
    '''returns int\n\n
    getQuerySubjectSequence()\n
    '''
