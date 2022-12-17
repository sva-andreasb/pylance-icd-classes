def ():
    '''returns FormulaRecordAggregate\n\n
    (final FormulaRecord formulaRec, final StringRecord stringRec, final SharedValueManager svm)\n
    '''
def getFormulaRecord():
    '''returns FormulaRecord\n\n
    getFormulaRecord()\n
    '''
def getStringRecord():
    '''returns StringRecord\n\n
    getStringRecord()\n
    '''
def getXFIndex():
    '''returns short\n\n
    getXFIndex()\n
    '''
def setXFIndex():
    '''returns None\n\n
    setXFIndex(final short xf)\n
    '''
def setColumn():
    '''returns None\n\n
    setColumn(final short col)\n
    '''
def setRow():
    '''returns None\n\n
    setRow(final int row)\n
    '''
def getColumn():
    '''returns short\n\n
    getColumn()\n
    '''
def getRow():
    '''returns int\n\n
    getRow()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def visitContainedRecords():
    '''returns None\n\n
    visitContainedRecords(final RecordVisitor rv)\n
    '''
def getStringValue():
    '''returns String\n\n
    getStringValue()\n
    '''
def setCachedStringResult():
    '''returns None\n\n
    setCachedStringResult(final String value)\n
    '''
def setCachedBooleanResult():
    '''returns None\n\n
    setCachedBooleanResult(final boolean value)\n
    '''
def setCachedErrorResult():
    '''returns None\n\n
    setCachedErrorResult(final int errorCode)\n
    setCachedErrorResult(final FormulaError error)\n
    '''
def setCachedDoubleResult():
    '''returns None\n\n
    setCachedDoubleResult(final double value)\n
    '''
def getFormulaTokens():
    '''returns Ptg[]\n\n
    getFormulaTokens()\n
    '''
def setParsedExpression():
    '''returns None\n\n
    setParsedExpression(final Ptg[] ptgs)\n
    '''
def unlinkSharedFormula():
    '''returns None\n\n
    unlinkSharedFormula()\n
    '''
def notifyFormulaChanging():
    '''returns None\n\n
    notifyFormulaChanging()\n
    '''
def isPartOfArrayFormula():
    '''returns boolean\n\n
    isPartOfArrayFormula()\n
    '''
def getArrayFormulaRange():
    '''returns CellRangeAddress\n\n
    getArrayFormulaRange()\n
    '''
def setArrayFormula():
    '''returns None\n\n
    setArrayFormula(final CellRangeAddress r, final Ptg[] ptgs)\n
    '''
def removeArrayFormula():
    '''returns CellRangeAddress\n\n
    removeArrayFormula(final int rowIndex, final int columnIndex)\n
    '''
