END_OF_MEDIUM = "char  '\u0019'"
DC3 = "char  '\u0013'"
def ColumnElement():
'''public ColumnElement(final String name, final Namespace namespace, final String dir)
public ColumnElement(final String name, final String dir)
public ColumnElement(final String name, final String uri, final String dir)
public ColumnElement(final String name, final String prefix, final String uri, final String dir)
public ColumnElement(final TableElement tableElement, final String name, final HashMap newCol, final HashMap oldCol)
'''
pass
def getColumnName():
'''public String getColumnName()
'''
pass
def getTableName():
'''public String getTableName()
'''
pass
def getStatus():
'''public String getStatus()
'''
pass
def getNewChanged():
'''public String getNewChanged()
'''
pass
def setNewChanged():
'''public void setNewChanged(final String value)
'''
pass
def getColumnAttributes():
'''public List getColumnAttributes()
'''
pass
def getColumnAttribute():
'''public Element getColumnAttribute(final String attrName)
'''
pass
def getAddSql():
'''public ArrayList getAddSql(final String tbname, final String name, final Connection con, final Util util, final HashMap oldCol, final TableElement tableElement)
'''
pass
def getUpdateSql():
'''public ArrayList getUpdateSql(final String tbname, final String name, final Connection con, final Util util, final HashMap oldCol, final TableElement tableElement)
'''
pass
def customClassExists():
'''public boolean customClassExists(final String className)
'''
pass
def getColumnMeta():
'''public HashMap getColumnMeta(final String tableName, final String columnName)
'''
pass
def getNewHashmap():
'''public HashMap getNewHashmap(HashMap oldMap, final boolean rebuild)
'''
pass
def toHashmap():
'''public HashMap toHashmap(final HashMap oldMap)
'''
pass
def getGLLength():
'''public String getGLLength()
'''
pass
def getAmountLength():
'''public String getAmountLength()
'''
pass
def getAmountScale():
'''public String getAmountScale()
'''
pass
def isCharType():
'''public boolean isCharType(final Element attr)
public boolean isCharType(final String maxtype)
'''
pass
def forceDrop():
'''public boolean forceDrop()
'''
pass
def addUserColumn():
'''public ArrayList addUserColumn(final String baseTable)
public ArrayList addUserColumn(final String tableName, final HashMap column)
'''
pass
def addAutoSelectColumn():
'''public ArrayList addAutoSelectColumn(final String tableName, final Util util)
'''
pass
def addViewColumn():
'''public ArrayList addViewColumn(final String tableName, final Util util)
'''
pass
def adjustViewRequired():
'''public ArrayList adjustViewRequired(final Util util)
'''
pass
def viewColumnExists():
'''public boolean viewColumnExists()
'''
pass
def getUpdateCount():
'''public int getUpdateCount()
'''
pass
