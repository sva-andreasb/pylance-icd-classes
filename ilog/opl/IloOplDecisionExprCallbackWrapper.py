def ():
    '''returns IloOplDecisionExprCallbackWrapper\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final boolean enableScripting)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def startDecisionExpr():
    '''returns boolean\n\n
    startDecisionExpr(final String dexprName, final double coef, final IloNumExprArg expr)\n
    '''
def startSum():
    '''returns boolean\n\n
    startSum(final double coef, final IloNumExprArg expr)\n
    '''
def addTerm():
    '''returns None\n\n
    addTerm(final double coef, final IloNumExprArg expr)\n
    '''
def endSum():
    '''returns None\n\n
    endSum()\n
    '''
def endDecisionExpr():
    '''returns None\n\n
    endDecisionExpr(final String dexprName)\n
    '''
