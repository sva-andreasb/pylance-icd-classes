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
def ReconExpression():
'''public ReconExpression(final ReconInfo reconInfo)
'''
pass
def setExpressionTag():
'''public void setExpressionTag(final String expressionTag)
'''
pass
def getExpressionTag():
'''public String getExpressionTag()
'''
pass
def getCompiledExpressionAsString():
'''public String getCompiledExpressionAsString()
'''
pass
def addExpressionToken():
'''public void addExpressionToken(final int tokenType, final String tokenValue)
public void addExpressionToken(final int tokenType, final String tokenValue, final String tokenUnit)
'''
pass
def prepareAttributeIndexes():
'''public void prepareAttributeIndexes(final ReconValueSet leadingSet, final ReconValueSet subordinateSet)
'''
pass
def readExpression():
'''public void readExpression(final MboSetRemote reconLinkSet)
'''
pass
def reset():
'''public void reset()
'''
pass
def processOperatorToken():
'''public static void processOperatorToken(final Stack operatorStack, final Stack nodeStack, final ReconExpressionToken currentToken)
'''
pass
def processRightParenthesisToken():
'''public static void processRightParenthesisToken(final Stack operatorStack, final Stack nodeStack)
'''
pass
def processInfixExpression():
'''public static void processInfixExpression(final Stack operatorStack, final Stack nodeStack, final ReconExpressionToken currentToken)
'''
pass
def getAttributeSet():
'''public Set getAttributeSet(final boolean getLeftSide, final boolean stripPrefixes)
'''
pass
def getAttributeToUnitMap():
'''public Map getAttributeToUnitMap(final boolean getLeftSide, final boolean stripPrefixes)
'''
pass
