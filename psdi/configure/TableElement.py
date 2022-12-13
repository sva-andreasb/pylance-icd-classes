def TableElement():
'''public TableElement(final String name, final Namespace namespace, final String dir)
public TableElement(final String name, final String dir)
public TableElement(final String name, final String uri, final String dir)
public TableElement(final String name, final String prefix, final String uri, final String dir)
public TableElement(final String tbname, final HashMap newTable, final HashMap oldTable)
'''
pass
def isView():
'''public boolean isView(final HashMap objMap)
public boolean isView()
'''
pass
def addView():
'''public boolean addView()
'''
pass
def getTableName():
'''public String getTableName()
'''
pass
def setTableName():
'''public void setTableName(final String tableName)
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
def forceDrop():
'''public boolean forceDrop()
'''
pass
def forceRebuild():
'''public boolean forceRebuild()
'''
pass
def getColumnsFromTable():
'''public TreeMap getColumnsFromTable(final HashMap table)
'''
pass
def getTableAttributes():
'''public List getTableAttributes()
'''
pass
def getTableAttribute():
'''public Element getTableAttribute(final String attrName)
'''
pass
def getColumns():
'''public List getColumns()
'''
pass
def getColumn():
'''public ColumnElement getColumn(final String colName)
'''
pass
def getAddSql():
'''public ArrayList getAddSql(final String tbname, final Connection con, final Util util, final HashMap oldTable)
'''
pass
def getUpdateSql():
'''public ArrayList getUpdateSql(final String tbname, final Connection con, final Util util, final HashMap oldTable)
'''
pass
def getPreDropSql():
'''public ArrayList getPreDropSql()
'''
pass
def getDropIndexesSql():
'''public String getDropIndexesSql(final String tableName)
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
def getNextVal():
'''public int getNextVal(final String tableName, final String columnName)
'''
pass
def adjustView():
'''public ArrayList adjustView(final HashMap baseTable, final Util util)
'''
pass
def getUpdateCount():
'''public int getUpdateCount()
'''
pass
