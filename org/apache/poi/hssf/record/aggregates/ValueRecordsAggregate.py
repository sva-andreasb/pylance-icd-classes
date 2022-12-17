def ():
    '''returns ValueIterator\n\n
    ()\n
    ()\n
    '''
def insertCell():
    '''returns None\n\n
    insertCell(final CellValueRecordInterface cell)\n
    '''
def removeCell():
    '''returns None\n\n
    removeCell(final CellValueRecordInterface cell)\n
    '''
def removeAllCellsValuesForRow():
    '''returns None\n\n
    removeAllCellsValuesForRow(final int rowIndex)\n
    '''
def getPhysicalNumberOfCells():
    '''returns int\n\n
    getPhysicalNumberOfCells()\n
    '''
def getFirstCellNum():
    '''returns int\n\n
    getFirstCellNum()\n
    '''
def getLastCellNum():
    '''returns int\n\n
    getLastCellNum()\n
    '''
def addMultipleBlanks():
    '''returns None\n\n
    addMultipleBlanks(final MulBlankRecord mbr)\n
    '''
def construct():
    '''returns None\n\n
    construct(final CellValueRecordInterface rec, final RecordStream rs, final SharedValueManager sfh)\n
    '''
def getRowCellBlockSize():
    '''returns int\n\n
    getRowCellBlockSize(final int startRow, final int endRow)\n
    '''
def rowHasCells():
    '''returns boolean\n\n
    rowHasCells(final int row)\n
    '''
def visitCellsForRow():
    '''returns None\n\n
    visitCellsForRow(final int rowIndex, final RecordAggregate.RecordVisitor rv)\n
    '''
def updateFormulasAfterRowShift():
    '''returns None\n\n
    updateFormulasAfterRowShift(final FormulaShifter shifter, final int currentExternSheetIndex)\n
    '''
def iterator():
    '''returns Iterator<CellValueRecordInterface>\n\n
    iterator()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns CellValueRecordInterface\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
