def ():
    '''returns WorkbookEvaluator\n\n
    (final EvaluationWorkbook workbook, final IStabilityClassifier stabilityClassifier, final UDFFinder udfFinder)\n
    '''
def clearAllCachedResultValues():
    '''returns None\n\n
    clearAllCachedResultValues()\n
    '''
def notifyUpdateCell():
    '''returns None\n\n
    notifyUpdateCell(final EvaluationCell cell)\n
    '''
def notifyDeleteCell():
    '''returns None\n\n
    notifyDeleteCell(final EvaluationCell cell)\n
    '''
def evaluate():
    '''returns ValueEval\n\n
    evaluate(final EvaluationCell srcCell)\n
    evaluate(final String formula, final CellReference ref)\n
    evaluate(final String formula, final CellReference target, final CellRangeAddressBase region)\n
    '''
def findUserDefinedFunction():
    '''returns FreeRefFunction\n\n
    findUserDefinedFunction(final String functionName)\n
    '''
def evaluateList():
    '''returns ValueEval\n\n
    evaluateList(final String formula, final CellReference target, final CellRangeAddressBase region)\n
    '''
def setIgnoreMissingWorkbooks():
    '''returns None\n\n
    setIgnoreMissingWorkbooks(final boolean ignore)\n
    '''
def isIgnoreMissingWorkbooks():
    '''returns boolean\n\n
    isIgnoreMissingWorkbooks()\n
    '''
def setDebugEvaluationOutputForNextEval():
    '''returns None\n\n
    setDebugEvaluationOutputForNextEval(final boolean value)\n
    '''
def isDebugEvaluationOutputForNextEval():
    '''returns boolean\n\n
    isDebugEvaluationOutputForNextEval()\n
    '''
