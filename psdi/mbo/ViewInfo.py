CACHE_NAME = "String  \"BMX.MAXIMODD.VI\""
def getViewColumns():
    '''    public HashMap<String, ViewColumnInfo> getViewColumns()
    '''
def getViewFetchAttributeName():
    '''    public String getViewFetchAttributeName(final String tbName, final String tbColName)
    public String getViewFetchAttributeName(final String viewColName)
    '''
def clearColumnInfo():
    '''    public void clearColumnInfo()
    '''
def addColumnInfo():
    '''    public void addColumnInfo(final ViewColumnInfo viewColumnInfo)
    '''
def addTableInfo():
    '''    public void addTableInfo(final String tableName, final TableInfo tableInfo)
    '''
def getTables():
    '''    public Iterator getTables()
    '''
def getTableInfos():
    '''    public Iterator getTableInfos()
    '''
def getTableCount():
    '''    public int getTableCount()
    '''
def getEntityColumns():
    '''    public Iterator getEntityColumns()
    '''
def getColumns():
    '''    public Iterator getColumns(final String tableName)
    '''
def getTableName():
    '''    public String getTableName(final String entityColumnName)
    '''
def getColumnName():
    '''    public String getColumnName(final String entityColumnName)
    public String getColumnName(final String entityColumnName, final String tableName)
    '''
def getEntityColumnName():
    '''    public String getEntityColumnName(final String tableColumnName, final String tableName)
    '''
def getKeyColumns():
    '''    public Iterator getKeyColumns(final String tableName)
    '''
def getAuditTable():
    '''    public String getAuditTable(final String tableName)
    '''
def getLangColumnName():
    '''    public String getLangColumnName(final String tableName)
    '''
def getOrphans():
    '''    public HashMap<String, String> getOrphans(String tableName)
    '''
def getRowStampInfo():
    '''    public RowStampInfo getRowStampInfo()
    '''
def getTenantIdInfo():
    '''    public TenantIdInfo getTenantIdInfo()
    '''
def getViewName():
    '''    public String getViewName()
    '''
def getAutoSelect():
    '''    public boolean getAutoSelect()
    '''
def getViewSelect():
    '''    public String getViewSelect()
    '''
def setTablesInHierarchyOrder():
    '''    public void setTablesInHierarchyOrder(final ArrayList<String> tableNames)
    '''
def getTablesInHierarchyOrder():
    '''    public Iterator getTablesInHierarchyOrder()
    '''
def getTablesInReverseHierarchyOrder():
    '''    public Iterator getTablesInReverseHierarchyOrder()
    '''
def setTenantIdInfo():
    '''    public synchronized void setTenantIdInfo(final TenantIdInfo tenantIdInfo)
    '''
def setRowStampInfo():
    '''    public synchronized void setRowStampInfo(final RowStampInfo rowStampInfo)
    '''
def hasRowStamp():
    '''    public boolean hasRowStamp()
    '''
def hasImplicitTenantId():
    '''    public boolean hasImplicitTenantId(final String tableName)
    public boolean hasImplicitTenantId()
    '''
def getTypedReference():
    '''    public ViewInfoBase getTypedReference()
    '''
def getTypedReferenceForSet():
    '''    public ViewInfoBase getTypedReferenceForSet()
    '''
def isTenantOwned():
    '''    public boolean isTenantOwned()
    '''
def getCacheName():
    '''    public String getCacheName()
    '''
def TableIterator():
    '''    public TableIterator(final Iterator iterator)
    '''
def remove():
    '''    public void remove()
    public void remove()
    '''
def ColumnIterator():
    '''    public ColumnIterator(final Iterator iterator)
    '''
