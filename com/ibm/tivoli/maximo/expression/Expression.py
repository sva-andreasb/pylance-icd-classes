GLOBAL_VARS = "String  \"globalvars\""
LOCAL_VARS = "String  \"localvars\""
def getVariables():
    '''    public ExpressionContext getVariables()
    '''
def setLineNum():
    '''    public void setLineNum(final int lineNum)
    '''
def getLineNum():
    '''    public Integer getLineNum()
    '''
def isMBRMode():
    '''    public boolean isMBRMode()
    '''
def setScriptContext():
    '''    public void setScriptContext(final Map<String, Object> context)
    '''
def getScriptContext():
    '''    public Map<String, Object> getScriptContext()
    '''
def setGlobalVar():
    '''    public void setGlobalVar(final String varName, final Object value)
    '''
def getGlobalVar():
    '''    public Object getGlobalVar(final String varName)
    '''
def hasGlobalVar():
    '''    public boolean hasGlobalVar(final String varName)
    '''
def setLocalVar():
    '''    public void setLocalVar(final String varName, final Object value)
    '''
def getLocalVar():
    '''    public Object getLocalVar(final String varName)
    '''
def hasLocalVar():
    '''    public boolean hasLocalVar(final String varName)
    '''
def resolveVar():
    '''    public Object resolveVar(final String varName)
    '''
def Expression():
    '''    public Expression(final String expression, final ExpressionContext context)
    '''
def eval():
    '''    public BigDecimal eval(final BigDecimal v1, final BigDecimal v2)
    public BigDecimal eval(final BigDecimal v1, final BigDecimal v2)
    public BigDecimal eval(final BigDecimal v1, final BigDecimal v2)
    public BigDecimal eval(final BigDecimal v1, final BigDecimal v2)
    public BigDecimal eval(final BigDecimal v1, final BigDecimal v2)
    public BigDecimal eval(final BigDecimal v1, BigDecimal v2)
    public BigDecimal eval(final BigDecimal v1, final BigDecimal v2)
    public BigDecimal eval(final BigDecimal v1, final BigDecimal v2)
    public BigDecimal eval(BigDecimal v1, final BigDecimal v2)
    public BigDecimal eval(BigDecimal v1, final BigDecimal v2)
    public BigDecimal eval(BigDecimal v1, final BigDecimal v2)
    public BigDecimal eval(BigDecimal v1, final BigDecimal v2)
    public BigDecimal eval(final BigDecimal v1, final BigDecimal v2)
    public BigDecimal eval(final BigDecimal v1, final BigDecimal v2)
    public BigDecimal eval(final BigDecimal v1, final BigDecimal v2)
    public BigDecimal eval(final BigDecimal v1, final BigDecimal v2)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval()
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval(final List<BigDecimal> parameters)
    public BigDecimal eval()
    public BigDecimal eval()
    public BigDecimal eval()
    public BigDecimal eval()
    public BigDecimal eval()
    public BigDecimal eval()
    public BigDecimal eval()
    public BigDecimal eval()
    public BigDecimal eval()
    '''
def lazyEval():
    '''    public LazyNumber lazyEval(final List<LazyNumber> lazyParams)
    '''
def getError():
    '''    public Exception getError()
    public Exception getError()
    public Exception getError()
    public Exception getError()
    public Exception getError()
    public Exception getError()
    public Exception getError()
    public Exception getError()
    public Exception getError()
    '''
def findAttributesInExpression():
    '''    public Set<String> findAttributesInExpression()
    '''
def validateAttributesInExpression():
    '''    public void validateAttributesInExpression()
    '''
def validateEval():
    '''    public BigDecimal validateEval()
    '''
def evalObjectValue():
    '''    public Object evalObjectValue()
    '''
def setPrecision():
    '''    public Expression setPrecision(final int precision)
    '''
def setRoundingMode():
    '''    public Expression setRoundingMode(final RoundingMode roundingMode)
    '''
def getMathContext():
    '''    public MathContext getMathContext()
    '''
def addOperator():
    '''    public Operator addOperator(final Operator operator)
    '''
def addFunction():
    '''    public Function addFunction(final Function function)
    '''
def addLazyFunction():
    '''    public LazyFunction addLazyFunction(final LazyFunction function)
    '''
def setVariable():
    '''    public Expression setVariable(final String variable, final BigDecimal value)
    public Expression setVariable(final String variable, final String value)
    '''
def with():
    '''    public Expression with(final String variable, final BigDecimal value)
    public Expression with(final String variable, final String value)
    '''
def and():
    '''    public Expression and(final String variable, final String value)
    public Expression and(final String variable, final BigDecimal value)
    '''
def getExpressionTokenizer():
    '''    public Iterator<String> getExpressionTokenizer()
    '''
def toRPN():
    '''    public String toRPN()
    '''
def getCalculatedValue():
    '''    public Map<String, Object> getCalculatedValue()
    public Object getCalculatedValue(final Object key)
    '''
def getExpValue():
    '''    public Map<String, Double> getExpValue()
    '''
def cacheValue():
    '''    public void cacheValue(final String key, final Double value)
    '''
def getCachedValue():
    '''    public Double getCachedValue(final String key)
    '''
def hasCachedValue():
    '''    public boolean hasCachedValue(final String key)
    '''
def setAttrFormulaAttrName():
    '''    public void setAttrFormulaAttrName(final String attrName)
    '''
def getAttrFormulaAttrName():
    '''    public String getAttrFormulaAttrName()
    '''
def getObjectFormulaInfo():
    '''    public ObjectFormulaInfo getObjectFormulaInfo()
    '''
def setObjectFormulaInfo():
    '''    public void setObjectFormulaInfo(final ObjectFormulaInfo objectFormulaInfo)
    '''
def setExpValue():
    '''    public void setExpValue(final String key, final Double value)
    '''
def getExpValueMap():
    '''    public Map<String, Double> getExpValueMap()
    '''
def getMetaData():
    '''    public Object getMetaData(final String key)
    '''
def getMetaDataMap():
    '''    public Map<String, Object> getMetaDataMap()
    '''
def setMetaData():
    '''    public void setMetaData(final String key, final Object value)
    '''
def getErrorDataMap():
    '''    public Map<String, Exception> getErrorDataMap()
    '''
def setErrorData():
    '''    public void setErrorData(final String key, final Exception value)
    '''
def isVar():
    '''    public boolean isVar(final String key)
    '''
def shouldEval():
    '''    public boolean shouldEval()
    '''
def Operator():
    '''    public Operator(final String oper, final int precedence, final boolean leftAssoc)
    '''
def getOper():
    '''    public String getOper()
    '''
def getPrecedence():
    '''    public int getPrecedence()
    '''
def isLeftAssoc():
    '''    public boolean isLeftAssoc()
    '''
def Tokenizer():
    '''    public Tokenizer(final String input)
    '''
def hasNext():
    '''    public boolean hasNext()
    '''
def next():
    '''    public String next()
    '''
def remove():
    '''    public void remove()
    '''
def getPos():
    '''    public int getPos()
    '''
