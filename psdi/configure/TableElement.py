def TableElement():
    '''public TableElement(final String name, final Namespace namespace, final String dir)
    public TableElement(final String name, final String dir)
    public TableElement(final String name, final String uri, final String dir)
    public TableElement(final String name, final String prefix, final String uri, final String dir)
    public TableElement(final String tbname, final HashMap newTable, final HashMap oldTable)
    '''
def isView():
    '''public boolean isView(final HashMap objMap)
    public boolean isView()
    '''
def addView():
    '''public boolean addView()
    '''
def getTableName():
    '''public String getTableName()
    '''
def setTableName():
    '''public void setTableName(final String tableName)
    '''
def getStatus():
    '''public String getStatus()
    '''
def getNewChanged():
    '''public String getNewChanged()
    '''
def setNewChanged():
    '''public void setNewChanged(final String value)
    '''
def forceDrop():
    '''public boolean forceDrop()
    '''
def forceRebuild():
    '''public boolean forceRebuild()
    '''
def getColumnsFromTable():
    '''public TreeMap getColumnsFromTable(final HashMap table)
    '''
def getTableAttributes():
    '''public List getTableAttributes()
    '''
def getTableAttribute():
    '''public Element getTableAttribute(final String attrName)
    '''
def getColumns():
    '''public List getColumns()
    '''
def getColumn():
    '''public ColumnElement getColumn(final String colName)
    '''
def getAddSql():
    '''public ArrayList getAddSql(final String tbname, final Connection con, final Util util, final HashMap oldTable)
    '''
def getUpdateSql():
    '''public ArrayList getUpdateSql(final String tbname, final Connection con, final Util util, final HashMap oldTable)
    '''
def getPreDropSql():
    '''public ArrayList getPreDropSql()
    '''
def getDropIndexesSql():
    '''public String getDropIndexesSql(final String tableName)
    '''
def getNewHashmap():
    '''public HashMap getNewHashmap(HashMap oldMap, final boolean rebuild)
    '''
def toHashmap():
    '''public HashMap toHashmap(final HashMap oldMap)
    '''
def getNextVal():
    '''public int getNextVal(final String tableName, final String columnName)
    '''
def adjustView():
    '''public ArrayList adjustView(final HashMap baseTable, final Util util)
    '''
def getUpdateCount():
    '''public int getUpdateCount()
    '''
