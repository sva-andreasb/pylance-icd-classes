def ():
    '''returns IloRange\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final double lb, final double ub, final String name)\n
    (final IloEnv env, final double lb, final double ub)\n
    (final IloEnv env, final double lhs, final IloNumExprArg expr, final double rhs, final String name)\n
    (final IloEnv env, final double lhs, final IloNumExprArg expr, final double rhs)\n
    (final IloEnv env, final double lhs, final IloNumExprArg expr)\n
    (final IloEnv env, final IloNumExprArg expr, final double rhs, final String name)\n
    (final IloEnv env, final IloNumExprArg expr, final double rhs)\n
    (final IloEnv env, final IloNumExprArg expr)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def getExpr():
    '''returns IloNumExpr\n\n
    getExpr()\n
    '''
def setExpr():
    '''returns None\n\n
    setExpr(final IloNumExpr expr)\n
    setExpr(final IloNumExprArg expr)\n
    '''
def clearExpr():
    '''returns None\n\n
    clearExpr()\n
    '''
def getLB():
    '''returns double\n\n
    getLB()\n
    '''
def getUB():
    '''returns double\n\n
    getUB()\n
    '''
def getCppExpr_not_used():
    '''returns IloNumExprArg\n\n
    getCppExpr_not_used()\n
    '''
def operator_func():
    '''returns IloAddValueToRange\n\n
    operator_func(final double value)\n
    '''
def setLinearCoef():
    '''returns None\n\n
    setLinearCoef(final IloNumVar var, final double value)\n
    '''
def setLinearCoefs():
    '''returns None\n\n
    setLinearCoefs(final IloNumVarArray vars, final IloNumArray values)\n
    '''
def setBounds():
    '''returns None\n\n
    setBounds(final double lb, final double ub)\n
    '''
def setUB():
    '''returns None\n\n
    setUB(final double ub)\n
    '''
def setLB():
    '''returns None\n\n
    setLB(final double lb)\n
    '''
def getLinearIterator():
    '''returns SWIGTYPE_p_IloExpr__LinearIterator\n\n
    getLinearIterator()\n
    '''
def getQuadIterator():
    '''returns SWIGTYPE_p_IloExpr__QuadIterator\n\n
    getQuadIterator()\n
    '''
