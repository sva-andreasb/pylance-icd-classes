def ():
    '''returns RowRecordsAggregate\n\n
    ()\n
    (final RecordStream rs, final SharedValueManager svm)\n
    '''
def insertRow():
    '''returns None\n\n
    insertRow(final RowRecord row)\n
    '''
def removeRow():
    '''returns None\n\n
    removeRow(final RowRecord row)\n
    '''
def getRow():
    '''returns RowRecord\n\n
    getRow(final int rowIndex)\n
    '''
def getPhysicalNumberOfRows():
    '''returns int\n\n
    getPhysicalNumberOfRows()\n
    '''
def getFirstRowNum():
    '''returns int\n\n
    getFirstRowNum()\n
    '''
def getLastRowNum():
    '''returns int\n\n
    getLastRowNum()\n
    '''
def getRowBlockCount():
    '''returns int\n\n
    getRowBlockCount()\n
    '''
def getRowCountForBlock():
    '''returns int\n\n
    getRowCountForBlock(final int block)\n
    '''
def visitContainedRecords():
    '''returns None\n\n
    visitContainedRecords(final RecordVisitor rv)\n
    '''
def getIterator():
    '''returns Iterator<RowRecord>\n\n
    getIterator()\n
    '''
def findStartOfRowOutlineGroup():
    '''returns int\n\n
    findStartOfRowOutlineGroup(final int row)\n
    '''
def findEndOfRowOutlineGroup():
    '''returns int\n\n
    findEndOfRowOutlineGroup(final int row)\n
    '''
def collapseRow():
    '''returns None\n\n
    collapseRow(final int rowNumber)\n
    '''
def isRowGroupCollapsed():
    '''returns boolean\n\n
    isRowGroupCollapsed(final int row)\n
    '''
def expandRow():
    '''returns None\n\n
    expandRow(final int rowNumber)\n
    '''
def isRowGroupHiddenByParent():
    '''returns boolean\n\n
    isRowGroupHiddenByParent(final int row)\n
    '''
def getCellValueIterator():
    '''returns Iterator<CellValueRecordInterface>\n\n
    getCellValueIterator()\n
    '''
def createIndexRecord():
    '''returns IndexRecord\n\n
    createIndexRecord(final int indexRecordOffset, final int sizeOfInitialSheetRecords)\n
    '''
def insertCell():
    '''returns None\n\n
    insertCell(final CellValueRecordInterface cvRec)\n
    '''
def removeCell():
    '''returns None\n\n
    removeCell(final CellValueRecordInterface cvRec)\n
    '''
def createFormula():
    '''returns FormulaRecordAggregate\n\n
    createFormula(final int row, final int col)\n
    '''
def updateFormulasAfterRowShift():
    '''returns None\n\n
    updateFormulasAfterRowShift(final FormulaShifter formulaShifter, final int currentExternSheetIndex)\n
    '''
def createDimensions():
    '''returns DimensionsRecord\n\n
    createDimensions()\n
    '''
