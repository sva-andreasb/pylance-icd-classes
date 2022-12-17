def ():
    '''returns TableElement\n\n
    (final String name, final Namespace namespace, final String dir)\n
    (final String name, final String dir)\n
    (final String name, final String uri, final String dir)\n
    (final String name, final String prefix, final String uri, final String dir)\n
    (final String tbname, final HashMap newTable, final HashMap oldTable)\n
    '''
def isView():
    '''returns boolean\n\n
    isView(final HashMap objMap)\n
    isView()\n
    '''
def addView():
    '''returns boolean\n\n
    addView()\n
    '''
def getTableName():
    '''returns String\n\n
    getTableName()\n
    '''
def setTableName():
    '''returns None\n\n
    setTableName(final String tableName)\n
    '''
def getStatus():
    '''returns String\n\n
    getStatus()\n
    '''
def getNewChanged():
    '''returns String\n\n
    getNewChanged()\n
    '''
def setNewChanged():
    '''returns None\n\n
    setNewChanged(final String value)\n
    '''
def forceDrop():
    '''returns boolean\n\n
    forceDrop()\n
    '''
def forceRebuild():
    '''returns boolean\n\n
    forceRebuild()\n
    '''
def getColumnsFromTable():
    '''returns TreeMap\n\n
    getColumnsFromTable(final HashMap table)\n
    '''
def getTableAttributes():
    '''returns List\n\n
    getTableAttributes()\n
    '''
def getTableAttribute():
    '''returns Element\n\n
    getTableAttribute(final String attrName)\n
    '''
def getColumns():
    '''returns List\n\n
    getColumns()\n
    '''
def getColumn():
    '''returns ColumnElement\n\n
    getColumn(final String colName)\n
    '''
def getAddSql():
    '''returns ArrayList\n\n
    getAddSql(final String tbname, final Connection con, final Util util, final HashMap oldTable)\n
    '''
def getUpdateSql():
    '''returns ArrayList\n\n
    getUpdateSql(final String tbname, final Connection con, final Util util, final HashMap oldTable)\n
    '''
def getPreDropSql():
    '''returns ArrayList\n\n
    getPreDropSql()\n
    '''
def getDropIndexesSql():
    '''returns String\n\n
    getDropIndexesSql(final String tableName)\n
    '''
def getNewHashmap():
    '''returns HashMap\n\n
    getNewHashmap(HashMap oldMap, final boolean rebuild)\n
    '''
def toHashmap():
    '''returns HashMap\n\n
    toHashmap(final HashMap oldMap)\n
    '''
def getNextVal():
    '''returns int\n\n
    getNextVal(final String tableName, final String columnName)\n
    '''
def adjustView():
    '''returns ArrayList\n\n
    adjustView(final HashMap baseTable, final Util util)\n
    '''
def getUpdateCount():
    '''returns int\n\n
    getUpdateCount()\n
    '''
