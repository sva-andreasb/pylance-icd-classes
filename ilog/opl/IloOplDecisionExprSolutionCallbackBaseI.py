def ():
    '''returns IloOplDecisionExprSolutionCallbackBaseI\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    '''
def setOwn():
    '''returns None\n\n
    setOwn(final boolean cMemoryOwn)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def startDecisionExpr():
    '''returns boolean\n\n
    startDecisionExpr(final String dexprName, final double value)\n
    '''
def startSum():
    '''returns boolean\n\n
    startSum(final double coef)\n
    '''
def addTerm():
    '''returns None\n\n
    addTerm(final double value)\n
    '''
def endSum():
    '''returns None\n\n
    endSum()\n
    '''
def endDecisionExpr():
    '''returns None\n\n
    endDecisionExpr(final String dexprName)\n
    '''
def currentIndexArray():
    '''returns IloMapIndexArray\n\n
    currentIndexArray()\n
    '''
def evaluate():
    '''returns String\n\n
    evaluate(final IloOplObject index)\n
    evaluate(final IloOplScriptExpression expr)\n
    '''
def hasChangedIndexNameArray():
    '''returns boolean\n\n
    hasChangedIndexNameArray()\n
    '''
def currentIndexNameArray():
    '''returns IloStringArray\n\n
    currentIndexNameArray()\n
    '''
def hasChangedIndexValueArray():
    '''returns boolean\n\n
    hasChangedIndexValueArray()\n
    '''
def currentIndexValueArray():
    '''returns IloMapIndexArray\n\n
    currentIndexValueArray()\n
    '''
def evaluateNum():
    '''returns double\n\n
    evaluateNum(final IloOplScriptExpression expr)\n
    '''
def evaluateInt():
    '''returns int\n\n
    evaluateInt(final IloOplScriptExpression expr)\n
    '''
def evaluateObject():
    '''returns IloOplObject\n\n
    evaluateObject(final IloOplScriptExpression expr)\n
    '''
