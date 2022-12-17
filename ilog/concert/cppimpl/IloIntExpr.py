def ():
    '''returns IloIntExpr\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloIntExprArg arg)\n
    (final SWIGTYPE_p_IloIntLinExprTerm term)\n
    (final IloEnv env, final int constant)\n
    (final IloEnv env)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def add():
    '''returns None\n\n
    add(final IloLinearIntExpr arg0)\n
    '''
def addTerm():
    '''returns None\n\n
    addTerm(final int val, final IloIntVar var)\n
    addTerm(final IloIntVar var, final int val)\n
    '''
def addTerms():
    '''returns None\n\n
    addTerms(final int[] arg0, final IloIntVar[] arg1, final int arg2, final int arg3)\n
    addTerms(final int[] arg0, final IloIntVar[] arg1)\n
    addTerms(final IloIntVar[] arg0, final int[] arg1, final int arg2, final int arg3)\n
    addTerms(final IloIntVar[] vars, final int[] vals)\n
    '''
def linearIterator():
    '''returns IloLinearIntExprIterator\n\n
    linearIterator()\n
    '''
def remove():
    '''returns None\n\n
    remove(final IloIntVar var)\n
    remove(final IloIntVar[] vars, final int arg1, final int arg2)\n
    remove(final IloIntVar[] vars)\n
    '''
def getConstant():
    '''returns int\n\n
    getConstant()\n
    '''
def setConstant():
    '''returns None\n\n
    setConstant(final int val)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def operator_sum_equal():
    '''returns IloIntExpr\n\n
    operator_sum_equal(final int val)\n
    operator_sum_equal(final IloIntExprArg expr)\n
    '''
def operator_diff_equal():
    '''returns IloIntExpr\n\n
    operator_diff_equal(final int val)\n
    operator_diff_equal(final IloIntExprArg expr)\n
    '''
def operator_prod_equal():
    '''returns IloIntExpr\n\n
    operator_prod_equal(final int val)\n
    '''
def _getLinearIterator():
    '''returns IloRangeI_LinearIterator\n\n
    _getLinearIterator()\n
    '''
def addTermCpp():
    '''returns None\n\n
    addTermCpp(final int val, final ilog.concert.cppimpl.IloIntVar var)\n
    '''
def setIntConstantCpp():
    '''returns None\n\n
    setIntConstantCpp(final int val)\n
    '''
def removeCpp():
    '''returns None\n\n
    removeCpp(final ilog.concert.cppimpl.IloIntVar val)\n
    '''
