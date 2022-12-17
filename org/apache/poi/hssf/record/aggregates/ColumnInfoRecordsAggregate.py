def ():
    '''returns ColumnInfoRecordsAggregate\n\n
    ()\n
    (final RecordStream rs)\n
    '''
def clone():
    '''returns ColumnInfoRecordsAggregate\n\n
    clone()\n
    '''
def insertColumn():
    '''returns None\n\n
    insertColumn(final ColumnInfoRecord col)\n
    '''
def visitContainedRecords():
    '''returns None\n\n
    visitContainedRecords(final RecordVisitor rv)\n
    '''
def collapseColumn():
    '''returns None\n\n
    collapseColumn(final int columnIndex)\n
    '''
def expandColumn():
    '''returns None\n\n
    expandColumn(final int columnIndex)\n
    '''
def setColumn():
    '''returns None\n\n
    setColumn(final int targetColumnIx, final Short xfIndex, final Integer width, final Integer level, final Boolean hidden, final Boolean collapsed)\n
    '''
def groupColumnRange():
    '''returns None\n\n
    groupColumnRange(final int fromColumnIx, final int toColumnIx, final boolean indent)\n
    '''
def findColumnInfo():
    '''returns ColumnInfoRecord\n\n
    findColumnInfo(final int columnIndex)\n
    '''
def getMaxOutlineLevel():
    '''returns int\n\n
    getMaxOutlineLevel()\n
    '''
def getOutlineLevel():
    '''returns int\n\n
    getOutlineLevel(final int columnIndex)\n
    '''
def compare():
    '''returns int\n\n
    compare(final ColumnInfoRecord a, final ColumnInfoRecord b)\n
    '''
