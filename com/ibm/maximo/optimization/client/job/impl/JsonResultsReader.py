def ():
    '''returns TableDescriptorImpl\n\n
    (final File jsonResultsFile)\n
    (final JsonResultsReader reader)\n
    (final TableDescriptor tableDesc)\n
    (final int index, final String name, final Class<T> type)\n
    (final String name)\n
    '''
def getTablesName():
    '''returns List<String>\n\n
    getTablesName()\n
    '''
def getTablesDescriptor():
    '''returns List<TableDescriptor>\n\n
    getTablesDescriptor()\n
    '''
def getTableDescriptor():
    '''returns TableDescriptor\n\n
    getTableDescriptor(final String tableName)\n
    '''
def getAllTablesRowsIterator():
    '''returns TableRowIterator\n\n
    getAllTablesRowsIterator()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns TableRow\n\n
    next()\n
    '''
def getTableDesc():
    '''returns TableDescriptor\n\n
    getTableDesc()\n
    '''
def setColumnValue():
    '''returns None\n\n
    setColumnValue(final String columnName, final Object value)\n
    '''
def getColumnValue():
    '''returns Object\n\n
    getColumnValue(final int index)\n
    getColumnValue(final String columnName)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    getName()\n
    '''
def getIndex():
    '''returns int\n\n
    getIndex()\n
    '''
def addColumnDescriptor():
    '''returns None\n\n
    addColumnDescriptor(final ColumnDescriptor<?> desc)\n
    '''
def getColumnsName():
    '''returns List<String>\n\n
    getColumnsName()\n
    '''
