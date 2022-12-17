def createConditionalFormattingRule():
    '''returns HSSFConditionalFormattingRule\n\n
    createConditionalFormattingRule(final byte comparisonOperation, final String formula1, final String formula2)\n
    createConditionalFormattingRule(final byte comparisonOperation, final String formula1)\n
    createConditionalFormattingRule(final String formula)\n
    createConditionalFormattingRule(final IconMultiStateFormatting.IconSet iconSet)\n
    createConditionalFormattingRule(final HSSFExtendedColor color)\n
    createConditionalFormattingRule(final ExtendedColor color)\n
    '''
def createConditionalFormattingColorScaleRule():
    '''returns HSSFConditionalFormattingRule\n\n
    createConditionalFormattingColorScaleRule()\n
    '''
def addConditionalFormatting():
    '''returns int\n\n
    addConditionalFormatting(final HSSFConditionalFormatting cf)\n
    addConditionalFormatting(final ConditionalFormatting cf)\n
    addConditionalFormatting(final CellRangeAddress[] regions, final HSSFConditionalFormattingRule[] cfRules)\n
    addConditionalFormatting(final CellRangeAddress[] regions, final ConditionalFormattingRule[] cfRules)\n
    addConditionalFormatting(final CellRangeAddress[] regions, final HSSFConditionalFormattingRule rule1)\n
    addConditionalFormatting(final CellRangeAddress[] regions, final ConditionalFormattingRule rule1)\n
    addConditionalFormatting(final CellRangeAddress[] regions, final HSSFConditionalFormattingRule rule1, final HSSFConditionalFormattingRule rule2)\n
    addConditionalFormatting(final CellRangeAddress[] regions, final ConditionalFormattingRule rule1, final ConditionalFormattingRule rule2)\n
    '''
def getConditionalFormattingAt():
    '''returns HSSFConditionalFormatting\n\n
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
