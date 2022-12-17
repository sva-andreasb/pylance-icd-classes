def ():
    '''returns IloCustomOplDecisionExprSolutionCallback\n\n
    (final IloOplFactory oplEnv, final boolean enableScripting)\n
    '''
def currentIndexArray():
    '''returns IloMapIndexArray\n\n
    currentIndexArray()\n
    '''
def currentIndexNameArray():
    '''returns IloStringArray\n\n
    currentIndexNameArray()\n
    '''
def currentIndexValueArray():
    '''returns IloMapIndexArray\n\n
    currentIndexValueArray()\n
    '''
def hasChangedIndexNameArray():
    '''returns boolean\n\n
    hasChangedIndexNameArray()\n
    '''
def hasChangedIndexValueArray():
    '''returns boolean\n\n
    hasChangedIndexValueArray()\n
    '''
def evaluate():
    '''returns String\n\n
    evaluate(final IloOplObject index)\n
    evaluate(final IloOplScriptExpression expr)\n
    '''
def evaluateInt():
    '''returns int\n\n
    evaluateInt(final IloOplScriptExpression expr)\n
    '''
def evaluateNum():
    '''returns double\n\n
    evaluateNum(final IloOplScriptExpression expr)\n
    '''
def evaluateObject():
    '''returns IloOplObject\n\n
    evaluateObject(final IloOplScriptExpression expr)\n
    '''
def startDecisionExpr():
    '''returns boolean\n\n
    startDecisionExpr(final String dexprName, final double value)\n
    '''
def startSum():
    '''returns boolean\n\n
    startSum(final double value)\n
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
