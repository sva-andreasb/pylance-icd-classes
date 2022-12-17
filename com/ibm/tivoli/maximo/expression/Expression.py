GLOBAL_VARS = "String  \"globalvars\""
LOCAL_VARS = "String  \"localvars\""
def getVariables():
    '''returns ExpressionContext\n\n
    getVariables()\n
    '''
def setLineNum():
    '''returns None\n\n
    setLineNum(final int lineNum)\n
    '''
def getLineNum():
    '''returns Integer\n\n
    getLineNum()\n
    '''
def isMBRMode():
    '''returns boolean\n\n
    isMBRMode()\n
    '''
def setScriptContext():
    '''returns None\n\n
    setScriptContext(final Map<String, Object> context)\n
    '''
def setGlobalVar():
    '''returns None\n\n
    setGlobalVar(final String varName, final Object value)\n
    '''
def getGlobalVar():
    '''returns Object\n\n
    getGlobalVar(final String varName)\n
    '''
def hasGlobalVar():
    '''returns boolean\n\n
    hasGlobalVar(final String varName)\n
    '''
def setLocalVar():
    '''returns None\n\n
    setLocalVar(final String varName, final Object value)\n
    '''
def getLocalVar():
    '''returns Object\n\n
    getLocalVar(final String varName)\n
    '''
def hasLocalVar():
    '''returns boolean\n\n
    hasLocalVar(final String varName)\n
    '''
def resolveVar():
    '''returns Object\n\n
    resolveVar(final String varName)\n
    '''
def ():
    '''returns Tokenizer\n\n
    (final String expression, final ExpressionContext context)\n
    (final String oper, final int precedence, final boolean leftAssoc)\n
    (final String input)\n
    '''
def eval():
    '''returns BigDecimal\n\n
    eval(final BigDecimal v1, final BigDecimal v2)\n
    eval(final BigDecimal v1, final BigDecimal v2)\n
    eval(final BigDecimal v1, final BigDecimal v2)\n
    eval(final BigDecimal v1, final BigDecimal v2)\n
    eval(final BigDecimal v1, final BigDecimal v2)\n
    eval(final BigDecimal v1, BigDecimal v2)\n
    eval(final BigDecimal v1, final BigDecimal v2)\n
    eval(final BigDecimal v1, final BigDecimal v2)\n
    eval(BigDecimal v1, final BigDecimal v2)\n
    eval(BigDecimal v1, final BigDecimal v2)\n
    eval(BigDecimal v1, final BigDecimal v2)\n
    eval(BigDecimal v1, final BigDecimal v2)\n
    eval(final BigDecimal v1, final BigDecimal v2)\n
    eval(final BigDecimal v1, final BigDecimal v2)\n
    eval(final BigDecimal v1, final BigDecimal v2)\n
    eval(final BigDecimal v1, final BigDecimal v2)\n
    eval(final List<BigDecimal> parameters)\n
    eval()\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval(final List<BigDecimal> parameters)\n
    eval()\n
    eval()\n
    eval()\n
    eval()\n
    eval()\n
    eval()\n
    eval()\n
    eval()\n
    eval()\n
    '''
def lazyEval():
    '''returns LazyNumber\n\n
    lazyEval(final List<LazyNumber> lazyParams)\n
    '''
def getError():
    '''returns Exception\n\n
    getError()\n
    getError()\n
    getError()\n
    getError()\n
    getError()\n
    getError()\n
    getError()\n
    getError()\n
    getError()\n
    '''
def findAttributesInExpression():
    '''returns Set<String>\n\n
    findAttributesInExpression()\n
    '''
def validateAttributesInExpression():
    '''returns None\n\n
    validateAttributesInExpression()\n
    '''
def validateEval():
    '''returns BigDecimal\n\n
    validateEval()\n
    '''
def evalObjectValue():
    '''returns Object\n\n
    evalObjectValue()\n
    '''
def setPrecision():
    '''returns Expression\n\n
    setPrecision(final int precision)\n
    '''
def setRoundingMode():
    '''returns Expression\n\n
    setRoundingMode(final RoundingMode roundingMode)\n
    '''
def getMathContext():
    '''returns MathContext\n\n
    getMathContext()\n
    '''
def addOperator():
    '''returns Operator\n\n
    addOperator(final Operator operator)\n
    '''
def addFunction():
    '''returns Function\n\n
    addFunction(final Function function)\n
    '''
def addLazyFunction():
    '''returns LazyFunction\n\n
    addLazyFunction(final LazyFunction function)\n
    '''
def setVariable():
    '''returns Expression\n\n
    setVariable(final String variable, final BigDecimal value)\n
    setVariable(final String variable, final String value)\n
    '''
def with():
    '''returns Expression\n\n
    with(final String variable, final BigDecimal value)\n
    with(final String variable, final String value)\n
    '''
def and():
    '''returns Expression\n\n
    and(final String variable, final String value)\n
    and(final String variable, final BigDecimal value)\n
    '''
def getExpressionTokenizer():
    '''returns Iterator<String>\n\n
    getExpressionTokenizer()\n
    '''
def toRPN():
    '''returns String\n\n
    toRPN()\n
    '''
def getCalculatedValue():
    '''returns Object\n\n
    getCalculatedValue(final Object key)\n
    '''
def cacheValue():
    '''returns None\n\n
    cacheValue(final String key, final Double value)\n
    '''
def getCachedValue():
    '''returns Double\n\n
    getCachedValue(final String key)\n
    '''
def hasCachedValue():
    '''returns boolean\n\n
    hasCachedValue(final String key)\n
    '''
def setAttrFormulaAttrName():
    '''returns None\n\n
    setAttrFormulaAttrName(final String attrName)\n
    '''
def getAttrFormulaAttrName():
    '''returns String\n\n
    getAttrFormulaAttrName()\n
    '''
def getObjectFormulaInfo():
    '''returns ObjectFormulaInfo\n\n
    getObjectFormulaInfo()\n
    '''
def setObjectFormulaInfo():
    '''returns None\n\n
    setObjectFormulaInfo(final ObjectFormulaInfo objectFormulaInfo)\n
    '''
def setExpValue():
    '''returns None\n\n
    setExpValue(final String key, final Double value)\n
    '''
def getMetaData():
    '''returns Object\n\n
    getMetaData(final String key)\n
    '''
def setMetaData():
    '''returns None\n\n
    setMetaData(final String key, final Object value)\n
    '''
def setErrorData():
    '''returns None\n\n
    setErrorData(final String key, final Exception value)\n
    '''
def isVar():
    '''returns boolean\n\n
    isVar(final String key)\n
    '''
def shouldEval():
    '''returns boolean\n\n
    shouldEval()\n
    '''
def getOper():
    '''returns String\n\n
    getOper()\n
    '''
def getPrecedence():
    '''returns int\n\n
    getPrecedence()\n
    '''
def isLeftAssoc():
    '''returns boolean\n\n
    isLeftAssoc()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns String\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def getPos():
    '''returns int\n\n
    getPos()\n
    '''
