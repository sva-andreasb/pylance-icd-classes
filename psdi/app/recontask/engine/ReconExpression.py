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
    '''    public ReconExpression(final ReconInfo reconInfo)
    '''
def setExpressionTag():
    '''    public void setExpressionTag(final String expressionTag)
    '''
def getExpressionTag():
    '''    public String getExpressionTag()
    '''
def getCompiledExpressionAsString():
    '''    public String getCompiledExpressionAsString()
    '''
def addExpressionToken():
    '''    public void addExpressionToken(final int tokenType, final String tokenValue)
    public void addExpressionToken(final int tokenType, final String tokenValue, final String tokenUnit)
    '''
def prepareAttributeIndexes():
    '''    public void prepareAttributeIndexes(final ReconValueSet leadingSet, final ReconValueSet subordinateSet)
    '''
def readExpression():
    '''    public void readExpression(final MboSetRemote reconLinkSet)
    '''
def reset():
    '''    public void reset()
    '''
def processOperatorToken():
    '''    public static void processOperatorToken(final Stack operatorStack, final Stack nodeStack, final ReconExpressionToken currentToken)
    '''
def processRightParenthesisToken():
    '''    public static void processRightParenthesisToken(final Stack operatorStack, final Stack nodeStack)
    '''
def processInfixExpression():
    '''    public static void processInfixExpression(final Stack operatorStack, final Stack nodeStack, final ReconExpressionToken currentToken)
    '''
def getAttributeSet():
    '''    public Set getAttributeSet(final boolean getLeftSide, final boolean stripPrefixes)
    '''
def getAttributeToUnitMap():
    '''    public Map getAttributeToUnitMap(final boolean getLeftSide, final boolean stripPrefixes)
    '''
