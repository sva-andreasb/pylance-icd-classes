def ():
    '''returns IndexElement\n\n
    (final String name, final Namespace namespace)\n
    (final String name)\n
    (final String name, final String uri)\n
    (final String name, final String prefix, final String uri)\n
    (final String tbname, final String ixname, final HashMap newIndex, final HashMap oldIndex)\n
    '''
def getIndexName():
    '''returns String\n\n
    getIndexName()\n
    '''
def getIndexAttributes():
    '''returns List\n\n
    getIndexAttributes()\n
    '''
def getKeys():
    '''returns List\n\n
    getKeys()\n
    '''
def getColNames():
    '''returns String[]\n\n
    getColNames()\n
    '''
def getAddSql():
    '''returns ArrayList\n\n
    getAddSql(final String tbname, final String ixname, final Connection con, final Util util, HashMap oldIndex)\n
    '''
def getDropSql():
    '''returns ArrayList\n\n
    getDropSql(final String tbname, final String ixname, final Connection con, final Util util, final HashMap oldIndex)\n
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
    setNewChanged(final String in)\n
    '''
def getSequenceName():
    '''returns String\n\n
    getSequenceName(final String table, final String column)\n
    '''
def toHashmap():
    '''returns HashMap\n\n
    toHashmap(final HashMap oldMap)\n
    '''
