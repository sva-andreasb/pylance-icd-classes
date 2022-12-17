def ():
    '''returns HSSFFormulaEvaluator\n\n
    (final HSSFWorkbook workbook)\n
    (final HSSFWorkbook workbook, final IStabilityClassifier stabilityClassifier)\n
    '''
def setupReferencedWorkbooks():
    '''returns None\n\n
    setupReferencedWorkbooks(final Map<String, FormulaEvaluator> evaluators)\n
    '''
def notifyUpdateCell():
    '''returns None\n\n
    notifyUpdateCell(final HSSFCell cell)\n
    notifyUpdateCell(final Cell cell)\n
    '''
def notifyDeleteCell():
    '''returns None\n\n
    notifyDeleteCell(final HSSFCell cell)\n
    notifyDeleteCell(final Cell cell)\n
    '''
def notifySetFormula():
    '''returns None\n\n
    notifySetFormula(final Cell cell)\n
    '''
def evaluateInCell():
    '''returns HSSFCell\n\n
    evaluateInCell(final Cell cell)\n
    '''
def evaluateAll():
    '''returns None\n\n
    evaluateAll()\n
    '''
def setIgnoreMissingWorkbooks():
    '''returns None\n\n
    setIgnoreMissingWorkbooks(final boolean ignore)\n
    '''
def setDebugEvaluationOutputForNextEval():
    '''returns None\n\n
    setDebugEvaluationOutputForNextEval(final boolean value)\n
    '''
