END_OF_MEDIUM = "char  '\u0019'"
DC3 = "char  '\u0013'"
def ():
    '''returns ColumnElement\n\n
    (final String name, final Namespace namespace, final String dir)\n
    (final String name, final String dir)\n
    (final String name, final String uri, final String dir)\n
    (final String name, final String prefix, final String uri, final String dir)\n
    (final TableElement tableElement, final String name, final HashMap newCol, final HashMap oldCol)\n
    '''
def getColumnName():
    '''returns String\n\n
    getColumnName()\n
    '''
def getTableName():
    '''returns String\n\n
    getTableName()\n
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
def getColumnAttributes():
    '''returns List\n\n
    getColumnAttributes()\n
    '''
def getColumnAttribute():
    '''returns Element\n\n
    getColumnAttribute(final String attrName)\n
    '''
def getAddSql():
    '''returns ArrayList\n\n
    getAddSql(final String tbname, final String name, final Connection con, final Util util, final HashMap oldCol, final TableElement tableElement)\n
    '''
def getUpdateSql():
    '''returns ArrayList\n\n
    getUpdateSql(final String tbname, final String name, final Connection con, final Util util, final HashMap oldCol, final TableElement tableElement)\n
    '''
def customClassExists():
    '''returns boolean\n\n
    customClassExists(final String className)\n
    '''
def getColumnMeta():
    '''returns HashMap\n\n
    getColumnMeta(final String tableName, final String columnName)\n
    '''
def getNewHashmap():
    '''returns HashMap\n\n
    getNewHashmap(HashMap oldMap, final boolean rebuild)\n
    '''
def toHashmap():
    '''returns HashMap\n\n
    toHashmap(final HashMap oldMap)\n
    '''
def getGLLength():
    '''returns String\n\n
    getGLLength()\n
    '''
def getAmountLength():
    '''returns String\n\n
    getAmountLength()\n
    '''
def getAmountScale():
    '''returns String\n\n
    getAmountScale()\n
    '''
def isCharType():
    '''returns boolean\n\n
    isCharType(final Element attr)\n
    isCharType(final String maxtype)\n
    '''
def forceDrop():
    '''returns boolean\n\n
    forceDrop()\n
    '''
def addUserColumn():
    '''returns ArrayList\n\n
    addUserColumn(final String baseTable)\n
    addUserColumn(final String tableName, final HashMap column)\n
    '''
def addAutoSelectColumn():
    '''returns ArrayList\n\n
    addAutoSelectColumn(final String tableName, final Util util)\n
    '''
def addViewColumn():
    '''returns ArrayList\n\n
    addViewColumn(final String tableName, final Util util)\n
    '''
def adjustViewRequired():
    '''returns ArrayList\n\n
    adjustViewRequired(final Util util)\n
    '''
def viewColumnExists():
    '''returns boolean\n\n
    viewColumnExists()\n
    '''
def getUpdateCount():
    '''returns int\n\n
    getUpdateCount()\n
    '''
