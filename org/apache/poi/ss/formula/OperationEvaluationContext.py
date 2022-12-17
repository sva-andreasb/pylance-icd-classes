def ():
    '''returns OperationEvaluationContext\n\n
    (final WorkbookEvaluator bookEvaluator, final EvaluationWorkbook workbook, final int sheetIndex, final int srcRowNum, final int srcColNum, final EvaluationTracker tracker)\n
    (final WorkbookEvaluator bookEvaluator, final EvaluationWorkbook workbook, final int sheetIndex, final int srcRowNum, final int srcColNum, final EvaluationTracker tracker, final boolean isSingleValue)\n
    '''
def getWorkbook():
    '''returns EvaluationWorkbook\n\n
    getWorkbook()\n
    '''
def getRowIndex():
    '''returns int\n\n
    getRowIndex()\n
    '''
def getColumnIndex():
    '''returns int\n\n
    getColumnIndex()\n
    '''
def getRefEvaluatorForCurrentSheet():
    '''returns SheetRangeEvaluator\n\n
    getRefEvaluatorForCurrentSheet()\n
    '''
def getDynamicReference():
    '''returns ValueEval\n\n
    getDynamicReference(final String workbookName, final String sheetName, final String refStrPart1, final String refStrPart2, final boolean isA1Style)\n
    '''
def findUserDefinedFunction():
    '''returns FreeRefFunction\n\n
    findUserDefinedFunction(final String functionName)\n
    '''
def getRefEval():
    '''returns ValueEval\n\n
    getRefEval(final int rowIndex, final int columnIndex)\n
    '''
def getRef3DEval():
    '''returns ValueEval\n\n
    getRef3DEval(final Ref3DPtg rptg)\n
    getRef3DEval(final Ref3DPxg rptg)\n
    '''
def getAreaEval():
    '''returns ValueEval\n\n
    getAreaEval(final int firstRowIndex, final int firstColumnIndex, final int lastRowIndex, final int lastColumnIndex)\n
    '''
def getArea3DEval():
    '''returns ValueEval\n\n
    getArea3DEval(final Area3DPtg aptg)\n
    getArea3DEval(final Area3DPxg aptg)\n
    '''
def getNameXEval():
    '''returns ValueEval\n\n
    getNameXEval(final NameXPtg nameXPtg)\n
    getNameXEval(final NameXPxg nameXPxg)\n
    '''
def getSheetIndex():
    '''returns int\n\n
    getSheetIndex()\n
    '''
def isSingleValue():
    '''returns boolean\n\n
    isSingleValue()\n
    '''
