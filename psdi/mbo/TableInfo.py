CACHE_NAME = "String  \"BMX.MAXIMODD.TI\""
MT_TENANT_TABLE = "int  0"
MT_DELTA_TABLE = "int  1"
MT_SYSTEM_TABLE = "int  2"
MT_TEMPLATE_TABLE = "int  3"
MT_LANDLORDONLY_TABLE = "int  4"
MT_TEMPLATE2_TABLE = "int  6"
MT_DELTA2_TABLE = "int  5"
def getEAuditTableName():
    '''    public String getEAuditTableName()
    '''
def isUsedForAuditing():
    '''    public boolean isUsedForAuditing()
    '''
def isUsedForMLang():
    '''    public boolean isUsedForMLang()
    '''
def isRowStampColumnExists():
    '''    public boolean isRowStampColumnExists()
    '''
def getTableName():
    '''    public String getTableName()
    public String getTableName(final String entityColumnName)
    '''
def getExtTableName():
    '''    public String getExtTableName()
    '''
def isTextSearchEnabled():
    '''    public boolean isTextSearchEnabled()
    '''
def getTables():
    '''    public Iterator getTables()
    '''
def getTableCount():
    '''    public int getTableCount()
    '''
def getTablesInHierarchyOrder():
    '''    public Iterator getTablesInHierarchyOrder()
    '''
def getTablesInReverseHierarchyOrder():
    '''    public Iterator getTablesInReverseHierarchyOrder()
    '''
def getColumnName():
    '''    public String getColumnName(final String entityColumnName)
    public String getColumnName(final String entityColumnName, final String tableName)
    '''
def getEntityColumnName():
    '''    public String getEntityColumnName(final String tableColumnName, final String tableName)
    '''
def getRowStampInfo():
    '''    public RowStampInfo getRowStampInfo()
    '''
def getTenantIdInfo():
    '''    public TenantIdInfo getTenantIdInfo()
    '''
def hasRowStamp():
    '''    public boolean hasRowStamp()
    '''
def getAuditTable():
    '''    public String getAuditTable(final String tableName)
    '''
def getLangTBName():
    '''    public String getLangTBName()
    '''
def addMLInUseColumn():
    '''    public void addMLInUseColumn()
    '''
def removeMLInUseColumn():
    '''    public void removeMLInUseColumn()
    '''
def isMLInUse():
    '''    public boolean isMLInUse()
    '''
def getUniqueColumnName():
    '''    public String getUniqueColumnName()
    '''
def getContentAttrName():
    '''    public String getContentAttrName()
    '''
def getAltIxName():
    '''    public String getAltIxName()
    '''
def getLangColumnName():
    '''    public String getLangColumnName()
    public String getLangColumnName(final String tableName)
    '''
def getStorageType():
    '''    public int getStorageType()
    '''
def getMLParent():
    '''    public String getMLParent()
    '''
def hasImplicitTenantId():
    '''    public boolean hasImplicitTenantId(final String tableName)
    public boolean hasImplicitTenantId()
    '''
def addColumnInfo():
    '''    public void addColumnInfo(final TableColumnInfo columnInfo)
    '''
def getColumnInfo():
    '''    public TableColumnInfo getColumnInfo(final String columnName)
    '''
def getKeyColumns():
    '''    public Iterator getKeyColumns()
    public Iterator getKeyColumns(final String tableName)
    '''
def getColumns():
    '''    public Iterator getColumns()
    public Iterator getColumns(final String tableName)
    '''
def getEntityColumns():
    '''    public Iterator getEntityColumns()
    '''
def getTypedReference():
    '''    public TableInfoBase getTypedReference()
    '''
def getTypedReferenceForSet():
    '''    public TableInfoBase getTypedReferenceForSet()
    '''
def isTenantOwned():
    '''    public boolean isTenantOwned()
    '''
def getCacheName():
    '''    public String getCacheName()
    '''
def compare():
    '''    public int compare(final Object o1, final Object o2)
    '''
def TableIterator():
    '''    public TableIterator(final Iterator iterator)
    '''
def remove():
    '''    public void remove()
    public void remove()
    public void remove()
    '''
def ColumnIterator():
    '''    public ColumnIterator(final Iterator iterator)
    '''
def KeyColumnIterator():
    '''    public KeyColumnIterator(final Iterator iterator)
    '''
def hasNext():
    '''    public boolean hasNext()
    '''
def next():
    '''    public Object next()
    '''
