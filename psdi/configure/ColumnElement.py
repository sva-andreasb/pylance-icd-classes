END_OF_MEDIUM = "char  '\u0019'"
DC3 = "char  '\u0013'"
def ColumnElement():
    '''    public ColumnElement(final String name, final Namespace namespace, final String dir)
    public ColumnElement(final String name, final String dir)
    public ColumnElement(final String name, final String uri, final String dir)
    public ColumnElement(final String name, final String prefix, final String uri, final String dir)
    public ColumnElement(final TableElement tableElement, final String name, final HashMap newCol, final HashMap oldCol)
    '''
def getColumnName():
    '''    public String getColumnName()
    '''
def getTableName():
    '''    public String getTableName()
    '''
def getStatus():
    '''    public String getStatus()
    '''
def getNewChanged():
    '''    public String getNewChanged()
    '''
def setNewChanged():
    '''    public void setNewChanged(final String value)
    '''
def getColumnAttributes():
    '''    public List getColumnAttributes()
    '''
def getColumnAttribute():
    '''    public Element getColumnAttribute(final String attrName)
    '''
def getAddSql():
    '''    public ArrayList getAddSql(final String tbname, final String name, final Connection con, final Util util, final HashMap oldCol, final TableElement tableElement)
    '''
def getUpdateSql():
    '''    public ArrayList getUpdateSql(final String tbname, final String name, final Connection con, final Util util, final HashMap oldCol, final TableElement tableElement)
    '''
def customClassExists():
    '''    public boolean customClassExists(final String className)
    '''
def getColumnMeta():
    '''    public HashMap getColumnMeta(final String tableName, final String columnName)
    '''
def getNewHashmap():
    '''    public HashMap getNewHashmap(HashMap oldMap, final boolean rebuild)
    '''
def toHashmap():
    '''    public HashMap toHashmap(final HashMap oldMap)
    '''
def getGLLength():
    '''    public String getGLLength()
    '''
def getAmountLength():
    '''    public String getAmountLength()
    '''
def getAmountScale():
    '''    public String getAmountScale()
    '''
def isCharType():
    '''    public boolean isCharType(final Element attr)
    public boolean isCharType(final String maxtype)
    '''
def forceDrop():
    '''    public boolean forceDrop()
    '''
def addUserColumn():
    '''    public ArrayList addUserColumn(final String baseTable)
    public ArrayList addUserColumn(final String tableName, final HashMap column)
    '''
def addAutoSelectColumn():
    '''    public ArrayList addAutoSelectColumn(final String tableName, final Util util)
    '''
def addViewColumn():
    '''    public ArrayList addViewColumn(final String tableName, final Util util)
    '''
def adjustViewRequired():
    '''    public ArrayList adjustViewRequired(final Util util)
    '''
def viewColumnExists():
    '''    public boolean viewColumnExists()
    '''
def getUpdateCount():
    '''    public int getUpdateCount()
    '''
