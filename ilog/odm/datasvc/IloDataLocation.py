COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloDataLocation\n\n
    (final String tableId, final int colIndex, final IloRowKey rowKey)\n
    (final String tableId, final int colIndex, final int rowIndex)\n
    (final String tableId, final int colIndex, final Long rowId)\n
    '''
def hasRow():
    '''returns boolean\n\n
    hasRow()\n
    '''
def getColIndex():
    '''returns int\n\n
    getColIndex()\n
    '''
def getRowId():
    '''returns Long\n\n
    getRowId()\n
    '''
def getRowIndex():
    '''returns int\n\n
    getRowIndex()\n
    getRowIndex(final IloTableContainer tableContainer)\n
    '''
def getTable():
    '''returns String\n\n
    getTable()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getRow():
    '''returns IloRow\n\n
    getRow(final IloTableContainer tableContainer)\n
    '''
def getRowKey():
    '''returns IloRowKey\n\n
    getRowKey(final IloTableContainer tableContainer)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def getColumnId():
    '''returns String\n\n
    getColumnId(final IloSchemaCatalog catalog)\n
    '''
