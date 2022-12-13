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
    '''    public byte getConditionType()
    '''
def setComparisonOperation():
    '''    public void setComparisonOperation(final byte operation)
    '''
def getComparisonOperation():
    '''    public byte getComparisonOperation()
    '''
def containsFontFormattingBlock():
    '''    public boolean containsFontFormattingBlock()
    '''
def setFontFormatting():
    '''    public void setFontFormatting(final FontFormatting fontFormatting)
    '''
def getFontFormatting():
    '''    public FontFormatting getFontFormatting()
    '''
def containsAlignFormattingBlock():
    '''    public boolean containsAlignFormattingBlock()
    '''
def setAlignFormattingUnchanged():
    '''    public void setAlignFormattingUnchanged()
    '''
def containsBorderFormattingBlock():
    '''    public boolean containsBorderFormattingBlock()
    '''
def setBorderFormatting():
    '''    public void setBorderFormatting(final BorderFormatting borderFormatting)
    '''
def getBorderFormatting():
    '''    public BorderFormatting getBorderFormatting()
    '''
def containsPatternFormattingBlock():
    '''    public boolean containsPatternFormattingBlock()
    '''
def setPatternFormatting():
    '''    public void setPatternFormatting(final PatternFormatting patternFormatting)
    '''
def getPatternFormatting():
    '''    public PatternFormatting getPatternFormatting()
    '''
def containsProtectionFormattingBlock():
    '''    public boolean containsProtectionFormattingBlock()
    '''
def setProtectionFormattingUnchanged():
    '''    public void setProtectionFormattingUnchanged()
    '''
def getOptions():
    '''    public int getOptions()
    '''
def isLeftBorderModified():
    '''    public boolean isLeftBorderModified()
    '''
def setLeftBorderModified():
    '''    public void setLeftBorderModified(final boolean modified)
    '''
def isRightBorderModified():
    '''    public boolean isRightBorderModified()
    '''
def setRightBorderModified():
    '''    public void setRightBorderModified(final boolean modified)
    '''
def isTopBorderModified():
    '''    public boolean isTopBorderModified()
    '''
def setTopBorderModified():
    '''    public void setTopBorderModified(final boolean modified)
    '''
def isBottomBorderModified():
    '''    public boolean isBottomBorderModified()
    '''
def setBottomBorderModified():
    '''    public void setBottomBorderModified(final boolean modified)
    '''
def isTopLeftBottomRightBorderModified():
    '''    public boolean isTopLeftBottomRightBorderModified()
    '''
def setTopLeftBottomRightBorderModified():
    '''    public void setTopLeftBottomRightBorderModified(final boolean modified)
    '''
def isBottomLeftTopRightBorderModified():
    '''    public boolean isBottomLeftTopRightBorderModified()
    '''
def setBottomLeftTopRightBorderModified():
    '''    public void setBottomLeftTopRightBorderModified(final boolean modified)
    '''
def isPatternStyleModified():
    '''    public boolean isPatternStyleModified()
    '''
def setPatternStyleModified():
    '''    public void setPatternStyleModified(final boolean modified)
    '''
def isPatternColorModified():
    '''    public boolean isPatternColorModified()
    '''
def setPatternColorModified():
    '''    public void setPatternColorModified(final boolean modified)
    '''
def isPatternBackgroundColorModified():
    '''    public boolean isPatternBackgroundColorModified()
    '''
def setPatternBackgroundColorModified():
    '''    public void setPatternBackgroundColorModified(final boolean modified)
    '''
def getParsedExpression1():
    '''    public Ptg[] getParsedExpression1()
    '''
def setParsedExpression1():
    '''    public void setParsedExpression1(final Ptg[] ptgs)
    '''
def getParsedExpression2():
    '''    public Ptg[] getParsedExpression2()
    '''
def setParsedExpression2():
    '''    public void setParsedExpression2(final Ptg[] ptgs)
    '''
def parseFormula():
    '''    public static Ptg[] parseFormula(final String formula, final HSSFSheet sheet)
    '''
