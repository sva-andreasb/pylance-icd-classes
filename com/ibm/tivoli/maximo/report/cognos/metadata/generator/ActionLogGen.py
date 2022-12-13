ROS_SITEORGTYPE = "String  SITEORGTYPE""
ROS_APP = "String  APP""
def ActionLogGen():
'''public ActionLogGen(final PrintWriter out)
'''
pass
def generateScriptHeader():
'''public void generateScriptHeader()
'''
pass
def generateScriptTail():
'''public void generateScriptTail()
'''
pass
def generateTransactionHeader():
'''public void generateTransactionHeader()
public void generateTransactionHeader(final boolean useSavedAttribute)
'''
pass
def generateTransactionTail():
'''public void generateTransactionTail()
'''
pass
def generateProjectInitialization():
'''public void generateProjectInitialization(final String projectName, final String topLevelNamespace)
public void generateProjectInitialization(final String projectName, final String topLevelNamespace, final String defaultLocale)
public void generateProjectInitialization(final String projectName, final String topLevelNamespace, final String defaultLocale, final String queryMode)
'''
pass
def generateCreateNamespace():
'''public void generateCreateNamespace(final String namespace, final String parentNamespace)
'''
pass
def generateDBImport():
'''public void generateDBImport(final String parentNamespace, final String databaseType, final String dataSourceName, final String schema, final Set<MXObject> tables, final Set<MXObject> views, final String databaseName)
'''
pass
def generateModelQuerySubject():
'''public void generateModelQuerySubject(final String parentNamespace, final String querySubjectName)
public void generateModelQuerySubject(final String parentNamespace, final String querySubjectName, final String defaultLocale)
'''
pass
def generateModelQueryItem():
'''public void generateModelQueryItem(final String parentNamespace, final String querySubjectName, final String queryItemName, final String basedOnNamespace, final String sourceQuerySubjectName, final String queryItemDescription, final String dataSourceQueryItemName)
public void generateModelQueryItem(final String parentNamespace, final String querySubjectName, final String queryItemName, final String basedOnNamespace, final String sourceQuerySubjectName, final String queryItemDescription, final String dataSourceQueryItemName, final String defaultLocale)
'''
pass
def generateHideQueryItem():
'''public void generateHideQueryItem(final String parentNamespace, final String querySubjectName, final String queryItemName)
'''
pass
def generateEvaluateQuerySubject():
'''public void generateEvaluateQuerySubject(final String parentNamespace, final String querySubjectName)
'''
pass
def generateReorderByNameQuerySubject():
'''public void generateReorderByNameQuerySubject(final String parentNamespace, final String querySubjectName)
'''
pass
def generateRelationship():
'''public void generateRelationship(final String topLevelNamespace, final String parentNamespace, final String leftQuerySubjectName, final String leftMinCardinality, final String leftMaxCardinality, final String rightQuerySubjectName, final String rightMinCardinality, final String rightMaxCardinality, final String relationshipName, final List<String> leftQueryItems, final List<String> rightQueryItems)
public void generateRelationship(final String topLevelNamespace, final String parentNamespace, final String leftQuerySubjectName, final String leftMinCardinality, final String leftMaxCardinality, final String rightQuerySubjectName, final String rightMinCardinality, final String rightMaxCardinality, final String relationshipName, final String cognosRelationship)
'''
pass
def generateAllowCrossProductJoin():
'''public void generateAllowCrossProductJoin()
'''
pass
def generateSetQueryProcessingToLocal():
'''public void generateSetQueryProcessingToLocal(final String dataSourceName)
'''
pass
def generateCreatePackage():
'''public void generateCreatePackage(final String packageName, final String excludedNamespace, final String topLevelNamespace)
public void generateCreatePackage(final String packageName, final String excludedNamespace, final String topLevelNamespace, final String defaultLocale, final List<String> languages)
'''
pass
def generatePublishPackage():
'''public void generatePublishPackage(final String packageName, final String contentStorePackageLocation)
'''
pass
def generateAddProjectLocale():
'''public void generateAddProjectLocale(final String locale, final String defaultLocale)
'''
pass
def generatePackageNameTranslations():
'''public void generatePackageNameTranslations(final String packageName, final String nameTranslation, final int localeIndex)
'''
pass
def generateModelNameTranslation():
'''public void generateModelNameTranslation(final String modelName, final String nameTranslation, final int localeIndex)
'''
pass
def generateNamespaceTranslation():
'''public void generateNamespaceTranslation(final String namespace, final String nameTranslation, final int localeIndex)
'''
pass
def generateModelQuerySubjectTranslations():
'''public void generateModelQuerySubjectTranslations(final String parentNamespace, final String querySubjectName, final String nameTranslation, final int localeIndex)
'''
pass
def generateModelQueryItemNameTranslation():
'''public void generateModelQueryItemNameTranslation(final String parentNamespace, final String querySubjectName, final String queryItemName, final String nameTranslation, final int localeIndex)
'''
pass
def generateModelQueryItemDescTranslation():
'''public void generateModelQueryItemDescTranslation(final String parentNamespace, final String querySubjectName, final String queryItemName, final String descTranslation, final int localeIndex)
'''
pass
def getQuerySubjectSequence():
'''public int getQuerySubjectSequence()
'''
pass
