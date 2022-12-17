CACHE_NAME = "String  \"BMX.MAXIMODD.TI\""
MT_TENANT_TABLE = "int  0"
MT_DELTA_TABLE = "int  1"
MT_SYSTEM_TABLE = "int  2"
MT_TEMPLATE_TABLE = "int  3"
MT_LANDLORDONLY_TABLE = "int  4"
MT_TEMPLATE2_TABLE = "int  6"
MT_DELTA2_TABLE = "int  5"
def getEAuditTableName():
    '''returns String\n\n
    getEAuditTableName()\n
    '''
def isUsedForAuditing():
    '''returns boolean\n\n
    isUsedForAuditing()\n
    '''
def isUsedForMLang():
    '''returns boolean\n\n
    isUsedForMLang()\n
    '''
def isRowStampColumnExists():
    '''returns boolean\n\n
    isRowStampColumnExists()\n
    '''
def getTableName():
    '''returns String\n\n
    getTableName()\n
    getTableName(final String entityColumnName)\n
    '''
def getExtTableName():
    '''returns String\n\n
    getExtTableName()\n
    '''
def isTextSearchEnabled():
    '''returns boolean\n\n
    isTextSearchEnabled()\n
    '''
def getTables():
    '''returns Iterator\n\n
    getTables()\n
    '''
def getTableCount():
    '''returns int\n\n
    getTableCount()\n
    '''
def getTablesInHierarchyOrder():
    '''returns Iterator\n\n
    getTablesInHierarchyOrder()\n
    '''
def getTablesInReverseHierarchyOrder():
    '''returns Iterator\n\n
    getTablesInReverseHierarchyOrder()\n
    '''
def getColumnName():
    '''returns String\n\n
    getColumnName(final String entityColumnName)\n
    getColumnName(final String entityColumnName, final String tableName)\n
    '''
def getEntityColumnName():
    '''returns String\n\n
    getEntityColumnName(final String tableColumnName, final String tableName)\n
    '''
def getRowStampInfo():
    '''returns RowStampInfo\n\n
    getRowStampInfo()\n
    '''
def getTenantIdInfo():
    '''returns TenantIdInfo\n\n
    getTenantIdInfo()\n
    '''
def hasRowStamp():
    '''returns boolean\n\n
    hasRowStamp()\n
    '''
def getAuditTable():
    '''returns String\n\n
    getAuditTable(final String tableName)\n
    '''
def getLangTBName():
    '''returns String\n\n
    getLangTBName()\n
    '''
def addMLInUseColumn():
    '''returns None\n\n
    addMLInUseColumn()\n
    '''
def removeMLInUseColumn():
    '''returns None\n\n
    removeMLInUseColumn()\n
    '''
def isMLInUse():
    '''returns boolean\n\n
    isMLInUse()\n
    '''
def getUniqueColumnName():
    '''returns String\n\n
    getUniqueColumnName()\n
    '''
def getContentAttrName():
    '''returns String\n\n
    getContentAttrName()\n
    '''
def getAltIxName():
    '''returns String\n\n
    getAltIxName()\n
    '''
def getLangColumnName():
    '''returns String\n\n
    getLangColumnName()\n
    getLangColumnName(final String tableName)\n
    '''
def getStorageType():
    '''returns int\n\n
    getStorageType()\n
    '''
def getMLParent():
    '''returns String\n\n
    getMLParent()\n
    '''
def hasImplicitTenantId():
    '''returns boolean\n\n
    hasImplicitTenantId(final String tableName)\n
    hasImplicitTenantId()\n
    '''
def addColumnInfo():
    '''returns None\n\n
    addColumnInfo(final TableColumnInfo columnInfo)\n
    '''
def getColumnInfo():
    '''returns TableColumnInfo\n\n
    getColumnInfo(final String columnName)\n
    '''
def getKeyColumns():
    '''returns Iterator\n\n
    getKeyColumns()\n
    getKeyColumns(final String tableName)\n
    '''
def getColumns():
    '''returns Iterator\n\n
    getColumns()\n
    getColumns(final String tableName)\n
    '''
def getEntityColumns():
    '''returns Iterator\n\n
    getEntityColumns()\n
    '''
def getTypedReference():
    '''returns TableInfoBase\n\n
    getTypedReference()\n
    '''
def getTypedReferenceForSet():
    '''returns TableInfoBase\n\n
    getTypedReferenceForSet()\n
    '''
def isTenantOwned():
    '''returns boolean\n\n
    isTenantOwned()\n
    '''
def getCacheName():
    '''returns String\n\n
    getCacheName()\n
    '''
def compare():
    '''returns int\n\n
    compare(final Object o1, final Object o2)\n
    '''
def ():
    '''returns KeyColumnIterator\n\n
    (final Iterator iterator)\n
    (final Iterator iterator)\n
    (final Iterator iterator)\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    remove()\n
    remove()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns Object\n\n
    next()\n
    '''
