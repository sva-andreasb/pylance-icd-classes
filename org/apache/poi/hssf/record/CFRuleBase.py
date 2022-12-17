CONDITION_TYPE_CELL_VALUE_IS = "byte  1"
CONDITION_TYPE_FORMULA = "byte  2"
CONDITION_TYPE_COLOR_SCALE = "byte  3"
CONDITION_TYPE_DATA_BAR = "byte  4"
CONDITION_TYPE_FILTER = "byte  5"
CONDITION_TYPE_ICON_SET = "byte  6"
TEMPLATE_CELL_VALUE = "int  0"
TEMPLATE_FORMULA = "int  1"
TEMPLATE_COLOR_SCALE_FORMATTING = "int  2"
TEMPLATE_DATA_BAR_FORMATTING = "int  3"
TEMPLATE_ICON_SET_FORMATTING = "int  4"
TEMPLATE_FILTER = "int  5"
TEMPLATE_UNIQUE_VALUES = "int  7"
TEMPLATE_CONTAINS_TEXT = "int  8"
TEMPLATE_CONTAINS_BLANKS = "int  9"
TEMPLATE_CONTAINS_NO_BLANKS = "int  10"
TEMPLATE_CONTAINS_ERRORS = "int  11"
TEMPLATE_CONTAINS_NO_ERRORS = "int  12"
TEMPLATE_TODAY = "int  15"
TEMPLATE_TOMORROW = "int  16"
TEMPLATE_YESTERDAY = "int  17"
TEMPLATE_LAST_7_DAYS = "int  18"
TEMPLATE_LAST_MONTH = "int  19"
TEMPLATE_NEXT_MONTH = "int  20"
TEMPLATE_THIS_WEEK = "int  21"
TEMPLATE_NEXT_WEEK = "int  22"
TEMPLATE_LAST_WEEK = "int  23"
TEMPLATE_THIS_MONTH = "int  24"
TEMPLATE_ABOVE_AVERAGE = "int  25"
TEMPLATE_BELOW_AVERAGE = "int  26"
TEMPLATE_DUPLICATE_VALUES = "int  27"
TEMPLATE_ABOVE_OR_EQUAL_TO_AVERAGE = "int  29"
TEMPLATE_BELOW_OR_EQUAL_TO_AVERAGE = "int  30"
NO_COMPARISON = "byte  0"
BETWEEN = "byte  1"
NOT_BETWEEN = "byte  2"
EQUAL = "byte  3"
NOT_EQUAL = "byte  4"
GT = "byte  5"
LT = "byte  6"
GE = "byte  7"
LE = "byte  8"
def getConditionType():
    '''returns byte\n\n
    getConditionType()\n
    '''
def setComparisonOperation():
    '''returns None\n\n
    setComparisonOperation(final byte operation)\n
    '''
def getComparisonOperation():
    '''returns byte\n\n
    getComparisonOperation()\n
    '''
def containsFontFormattingBlock():
    '''returns boolean\n\n
    containsFontFormattingBlock()\n
    '''
def setFontFormatting():
    '''returns None\n\n
    setFontFormatting(final FontFormatting fontFormatting)\n
    '''
def getFontFormatting():
    '''returns FontFormatting\n\n
    getFontFormatting()\n
    '''
def containsAlignFormattingBlock():
    '''returns boolean\n\n
    containsAlignFormattingBlock()\n
    '''
def setAlignFormattingUnchanged():
    '''returns None\n\n
    setAlignFormattingUnchanged()\n
    '''
def containsBorderFormattingBlock():
    '''returns boolean\n\n
    containsBorderFormattingBlock()\n
    '''
def setBorderFormatting():
    '''returns None\n\n
    setBorderFormatting(final BorderFormatting borderFormatting)\n
    '''
def getBorderFormatting():
    '''returns BorderFormatting\n\n
    getBorderFormatting()\n
    '''
def containsPatternFormattingBlock():
    '''returns boolean\n\n
    containsPatternFormattingBlock()\n
    '''
def setPatternFormatting():
    '''returns None\n\n
    setPatternFormatting(final PatternFormatting patternFormatting)\n
    '''
def getPatternFormatting():
    '''returns PatternFormatting\n\n
    getPatternFormatting()\n
    '''
def containsProtectionFormattingBlock():
    '''returns boolean\n\n
    containsProtectionFormattingBlock()\n
    '''
def setProtectionFormattingUnchanged():
    '''returns None\n\n
    setProtectionFormattingUnchanged()\n
    '''
def getOptions():
    '''returns int\n\n
    getOptions()\n
    '''
def isLeftBorderModified():
    '''returns boolean\n\n
    isLeftBorderModified()\n
    '''
def setLeftBorderModified():
    '''returns None\n\n
    setLeftBorderModified(final boolean modified)\n
    '''
def isRightBorderModified():
    '''returns boolean\n\n
    isRightBorderModified()\n
    '''
def setRightBorderModified():
    '''returns None\n\n
    setRightBorderModified(final boolean modified)\n
    '''
def isTopBorderModified():
    '''returns boolean\n\n
    isTopBorderModified()\n
    '''
def setTopBorderModified():
    '''returns None\n\n
    setTopBorderModified(final boolean modified)\n
    '''
def isBottomBorderModified():
    '''returns boolean\n\n
    isBottomBorderModified()\n
    '''
def setBottomBorderModified():
    '''returns None\n\n
    setBottomBorderModified(final boolean modified)\n
    '''
def isTopLeftBottomRightBorderModified():
    '''returns boolean\n\n
    isTopLeftBottomRightBorderModified()\n
    '''
def setTopLeftBottomRightBorderModified():
    '''returns None\n\n
    setTopLeftBottomRightBorderModified(final boolean modified)\n
    '''
def isBottomLeftTopRightBorderModified():
    '''returns boolean\n\n
    isBottomLeftTopRightBorderModified()\n
    '''
def setBottomLeftTopRightBorderModified():
    '''returns None\n\n
    setBottomLeftTopRightBorderModified(final boolean modified)\n
    '''
def isPatternStyleModified():
    '''returns boolean\n\n
    isPatternStyleModified()\n
    '''
def setPatternStyleModified():
    '''returns None\n\n
    setPatternStyleModified(final boolean modified)\n
    '''
def isPatternColorModified():
    '''returns boolean\n\n
    isPatternColorModified()\n
    '''
def setPatternColorModified():
    '''returns None\n\n
    setPatternColorModified(final boolean modified)\n
    '''
def isPatternBackgroundColorModified():
    '''returns boolean\n\n
    isPatternBackgroundColorModified()\n
    '''
def setPatternBackgroundColorModified():
    '''returns None\n\n
    setPatternBackgroundColorModified(final boolean modified)\n
    '''
def getParsedExpression1():
    '''returns Ptg[]\n\n
    getParsedExpression1()\n
    '''
def setParsedExpression1():
    '''returns None\n\n
    setParsedExpression1(final Ptg[] ptgs)\n
    '''
def getParsedExpression2():
    '''returns Ptg[]\n\n
    getParsedExpression2()\n
    '''
def setParsedExpression2():
    '''returns None\n\n
    setParsedExpression2(final Ptg[] ptgs)\n
    '''
