OBJECT_ASSET = "String  \"ASSET\""
OBJECT_ASSETSPEC = "String  \"ASSETSPEC\""
OBJECT_ITEM = "String  \"ITEM\""
OBJECT_ITEMSPEC = "String  \"ITEMSPEC\""
ROOTMAXVAR = "String  \"ITASSET\""
def ():
    '''returns AssetDataSet\n\n
    ()\n
    '''
def getMainObjectName():
    '''returns String\n\n
    getMainObjectName()\n
    '''
def getMainObjectUID():
    '''returns String\n\n
    getMainObjectUID()\n
    '''
def getTaskFilterAttributesDomainID():
    '''returns String\n\n
    getTaskFilterAttributesDomainID()\n
    '''
def getFixedTaskFilterWhereClause():
    '''returns String\n\n
    getFixedTaskFilterWhereClause()\n
    '''
def getObjectNameDomainID():
    '''returns String\n\n
    getObjectNameDomainID()\n
    '''
def getRecordCount():
    '''returns int\n\n
    getRecordCount(final Map uidKeys, final String objectName, final String classStructureID)\n
    '''
def getReconResultAttributeNamesForComparison():
    '''returns ResultTableAttributes\n\n
    getReconResultAttributeNamesForComparison(final boolean isDataSet1)\n
    '''
def getReconLinkAttributeNamesForLink():
    '''returns ResultTableAttributes\n\n
    getReconLinkAttributeNamesForLink(final boolean isDataSet1)\n
    '''
def getReconResultAttributeNamesForLink():
    '''returns ResultTableAttributes\n\n
    getReconResultAttributeNamesForLink(final boolean isDataSet1)\n
    '''
def getTableColumnNameForTaskFilter():
    '''returns String\n\n
    getTableColumnNameForTaskFilter(final String attributeName)\n
    '''
def getTableJoinWhereClauseForTaskFilter():
    '''returns String\n\n
    getTableJoinWhereClauseForTaskFilter(final String tableName)\n
    '''
def getTableNameForTaskFilter():
    '''returns String\n\n
    getTableNameForTaskFilter(final String attributeName)\n
    '''
def getExtraTableNamesForComparison():
    '''returns String[]\n\n
    getExtraTableNamesForComparison(final String tableName)\n
    '''
def getTableJoinWhereClauseForComparison():
    '''returns String\n\n
    getTableJoinWhereClauseForComparison(final String tableName, final Map uidKeys)\n
    '''
def getRootSpecMaxVar():
    '''returns String\n\n
    getRootSpecMaxVar(final String objectname)\n
    '''
def getAttributesExcludeList():
    '''returns String[]\n\n
    getAttributesExcludeList(final String objectname)\n
    '''
def getObjectSpecPairs():
    '''returns String[][]\n\n
    getObjectSpecPairs()\n
    '''
def getObjectNameDomainExcludeList():
    '''returns String[]\n\n
    getObjectNameDomainExcludeList(final String objectName)\n
    '''
def isUnitOfMeasureAllowed():
    '''returns boolean\n\n
    isUnitOfMeasureAllowed(final String objectName)\n
    '''
