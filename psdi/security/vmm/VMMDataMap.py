ALN = "int  1"
UPPER = "int  2"
LOWER = "int  3"
INTEGER = "int  4"
YORN = "int  5"
CRYPTO = "int  6"
def ():
    '''returns VMMDataMap\n\n
    ()\n
    '''
def addDataMap():
    '''returns None\n\n
    addDataMap(final String tableId, String table, String column, final String attribute, final boolean keyColumn, final boolean required, final boolean allowRecDelete, final String type)\n
    '''
def getTableName():
    '''returns String\n\n
    getTableName(final String tableId)\n
    '''
def getTableId():
    '''returns String\n\n
    getTableId(final String objectName)\n
    '''
def getObjectName():
    '''returns String\n\n
    getObjectName(final String tableId, final Connection con)\n
    '''
def allowRecDelete():
    '''returns boolean\n\n
    allowRecDelete(final String tableId)\n
    '''
def getTableIds():
    '''returns Iterator\n\n
    getTableIds()\n
    '''
def isUniqueIdColumn():
    '''returns boolean\n\n
    isUniqueIdColumn(final String tableId, String column)\n
    '''
def isSysDateColumn():
    '''returns boolean\n\n
    isSysDateColumn(final String tableId, String column)\n
    '''
def getColumnNames():
    '''returns Iterator\n\n
    getColumnNames(final String tableId)\n
    '''
def getKeyColumnNames():
    '''returns Iterator\n\n
    getKeyColumnNames(final String tableId)\n
    '''
def getColumnNameForAttribute():
    '''returns String\n\n
    getColumnNameForAttribute(final String tableId, final String attributeName)\n
    '''
def isMappedToVMMAttribute():
    '''returns boolean\n\n
    isMappedToVMMAttribute(final String tableId, final String column)\n
    '''
def getAttribute():
    '''returns String\n\n
    getAttribute(final String tableId, String column)\n
    '''
def isRequired():
    '''returns boolean\n\n
    isRequired(final String tableId, String column)\n
    isRequired()\n
    '''
def getType():
    '''returns String\n\n
    getType(final String tableId, String column)\n
    getType()\n
    '''
def getTypeAsInt():
    '''returns int\n\n
    getTypeAsInt(final String tableId, String column)\n
    getTypeAsInt()\n
    '''
def getVMMAttributes():
    '''returns String[]\n\n
    getVMMAttributes()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getAttributeName():
    '''returns String\n\n
    getAttributeName()\n
    '''
def setAttributeName():
    '''returns None\n\n
    setAttributeName(final String name)\n
    '''
def getColumnName():
    '''returns String\n\n
    getColumnName()\n
    '''
def setColumnName():
    '''returns None\n\n
    setColumnName(final String name)\n
    '''
def setRequired():
    '''returns None\n\n
    setRequired(final boolean req)\n
    '''
def setType():
    '''returns None\n\n
    setType(final String t)\n
    '''
