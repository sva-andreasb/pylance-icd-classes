def ():
    '''returns ConditionalFormattingEvaluator\n\n
    (final Workbook wb, final WorkbookEvaluatorProvider provider)\n
    '''
def clearAllCachedFormats():
    '''returns None\n\n
    clearAllCachedFormats()\n
    '''
def clearAllCachedValues():
    '''returns None\n\n
    clearAllCachedValues()\n
    '''
def getConditionalFormattingForCell():
    '''returns List<EvaluationConditionalFormatRule>\n\n
    getConditionalFormattingForCell(final CellReference cellRef)\n
    getConditionalFormattingForCell(final Cell cell)\n
    '''
def getFormatRulesForSheet():
    '''returns List<EvaluationConditionalFormatRule>\n\n
    getFormatRulesForSheet(final String sheetName)\n
    getFormatRulesForSheet(final Sheet sheet)\n
    '''
def getMatchingCells():
    '''returns List<Cell>\n\n
    getMatchingCells(final Sheet sheet, final int conditionalFormattingIndex, final int ruleIndex)\n
    getMatchingCells(final EvaluationConditionalFormatRule rule)\n
    '''
