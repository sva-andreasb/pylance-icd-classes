TOKEN_INVALID = "int  0"
TOKEN_LEFT_PARENTHESIS = "int  1"
TOKEN_RIGHT_PARENTHESIS = "int  2"
TOKEN_OPERATOR = "int  3"
TOKEN_CONSTANT = "int  4"
TOKEN_DATASET1_FIELD = "int  5"
TOKEN_DATASET2_FIELD = "int  6"
TOKEN_VALUE = "int  7"
TOKEN_LOWEST_VALUE = "int  1"
TOKEN_HIGHEST_VALUE = "int  7"
def ():
    '''returns ReconExpression\n\n
    (final ReconInfo reconInfo)\n
    '''
def setExpressionTag():
    '''returns None\n\n
    setExpressionTag(final String expressionTag)\n
    '''
def getExpressionTag():
    '''returns String\n\n
    getExpressionTag()\n
    '''
def getCompiledExpressionAsString():
    '''returns String\n\n
    getCompiledExpressionAsString()\n
    '''
def addExpressionToken():
    '''returns None\n\n
    addExpressionToken(final int tokenType, final String tokenValue)\n
    addExpressionToken(final int tokenType, final String tokenValue, final String tokenUnit)\n
    '''
def prepareAttributeIndexes():
    '''returns None\n\n
    prepareAttributeIndexes(final ReconValueSet leadingSet, final ReconValueSet subordinateSet)\n
    '''
def readExpression():
    '''returns None\n\n
    readExpression(final MboSetRemote reconLinkSet)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def getAttributeSet():
    '''returns Set\n\n
    getAttributeSet(final boolean getLeftSide, final boolean stripPrefixes)\n
    '''
def getAttributeToUnitMap():
    '''returns Map\n\n
    getAttributeToUnitMap(final boolean getLeftSide, final boolean stripPrefixes)\n
    '''
