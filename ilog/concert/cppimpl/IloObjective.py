def ():
    '''returns CppSense\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final double constant, final CppSense sense, final String name)\n
    (final IloEnv env, final double constant, final CppSense sense)\n
    (final IloEnv env, final double constant)\n
    (final IloEnv env)\n
    (final IloEnv env, final IloNumExprArg expr, final CppSense sense, final String name)\n
    (final IloEnv env, final IloNumExprArg expr, final CppSense sense)\n
    (final IloEnv env, final IloNumExprArg expr)\n
    (final IloEnv env, final IloMultiCriterionExpr moExpr, final CppSense sense, final String name)\n
    (final IloEnv env, final IloMultiCriterionExpr moExpr, final CppSense sense)\n
    (final String swigName, final int swigValue)\n
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
    setExpr(final IloNumExprArg arg0)\n
    '''
def clearExpr():
    '''returns None\n\n
    clearExpr()\n
    '''
def getSense():
    '''returns IloObjectiveSense\n\n
    getSense()\n
    '''
def setSense():
    '''returns None\n\n
    setSense(final IloObjectiveSense sense)\n
    setSense(final CppSense sense)\n
    '''
def getCppSense():
    '''returns CppSense\n\n
    getCppSense()\n
    '''
def operator_func():
    '''returns IloAddValueToObj\n\n
    operator_func()\n
    operator_func(final double value)\n
    '''
def getCppExpr_not_used():
    '''returns IloNumExprArg\n\n
    getCppExpr_not_used()\n
    '''
def setLinearCoef():
    '''returns None\n\n
    setLinearCoef(final IloNumVar var, final double value)\n
    '''
def setLinearCoefs():
    '''returns None\n\n
    setLinearCoefs(final IloNumVarArray vars, final IloNumArray values)\n
    '''
def setQuadCoef():
    '''returns None\n\n
    setQuadCoef(final IloNumVar var1, final IloNumVar var2, final double value)\n
    '''
def getLinearIterator():
    '''returns SWIGTYPE_p_IloExpr__LinearIterator\n\n
    getLinearIterator()\n
    '''
def getQuadIterator():
    '''returns SWIGTYPE_p_IloExpr__QuadIterator\n\n
    getQuadIterator()\n
    '''
def mySwigValue():
    '''returns int\n\n
    mySwigValue()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
