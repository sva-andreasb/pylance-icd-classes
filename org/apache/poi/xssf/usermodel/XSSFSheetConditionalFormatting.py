def createConditionalFormattingRule():
    '''returns XSSFConditionalFormattingRule\n\n
    createConditionalFormattingRule(final byte comparisonOperation, final String formula1, final String formula2)\n
    createConditionalFormattingRule(final byte comparisonOperation, final String formula)\n
    createConditionalFormattingRule(final String formula)\n
    createConditionalFormattingRule(final XSSFColor color)\n
    createConditionalFormattingRule(final ExtendedColor color)\n
    createConditionalFormattingRule(final IconMultiStateFormatting.IconSet iconSet)\n
    '''
def createConditionalFormattingColorScaleRule():
    '''returns XSSFConditionalFormattingRule\n\n
    createConditionalFormattingColorScaleRule()\n
    '''
def addConditionalFormatting():
    '''returns int\n\n
    addConditionalFormatting(final CellRangeAddress[] regions, final ConditionalFormattingRule[] cfRules)\n
    addConditionalFormatting(final CellRangeAddress[] regions, final ConditionalFormattingRule rule1)\n
    addConditionalFormatting(final CellRangeAddress[] regions, final ConditionalFormattingRule rule1, final ConditionalFormattingRule rule2)\n
    addConditionalFormatting(final ConditionalFormatting cf)\n
    '''
def getConditionalFormattingAt():
    '''returns XSSFConditionalFormatting\n\n
    getConditionalFormattingAt(final int index)\n
    '''
def getNumConditionalFormattings():
    '''returns int\n\n
    getNumConditionalFormattings()\n
    '''
def removeConditionalFormatting():
    '''returns None\n\n
    removeConditionalFormatting(final int index)\n
    '''
