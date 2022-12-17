COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloOPLSolutionExpCallback\n\n
    (final IloGoalBreakdownFactory goalFactory)\n
    '''
def processOplDecisionExpr():
    '''returns IloBreakdownVariable\n\n
    processOplDecisionExpr(final String variableName)\n
    '''
def customStartDecisionExpr():
    '''returns boolean\n\n
    customStartDecisionExpr(final String exprName, final double value)\n
    '''
def customEndDecisionExpr():
    '''returns None\n\n
    customEndDecisionExpr(final String arg0)\n
    '''
def customStartSum():
    '''returns boolean\n\n
    customStartSum(final double arg0)\n
    '''
def customEndSum():
    '''returns None\n\n
    customEndSum()\n
    '''
def customAddTerm():
    '''returns None\n\n
    customAddTerm(final double value)\n
    '''
def evaluate():
    '''returns Object\n\n
    evaluate(final IloOplScriptExpression expr, final Parameter elts, final ilog.concert.IloStringArray array, final boolean keyOnly, final boolean canReturnTuple)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
