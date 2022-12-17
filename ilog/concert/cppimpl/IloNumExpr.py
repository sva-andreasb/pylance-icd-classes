def ():
    '''returns IloNumExpr\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloNumExprArg expr)\n
    (final IloEnv env, final double arg1)\n
    (final IloEnv env)\n
    (final SWIGTYPE_p_IloNumLinExprTerm term)\n
    (final SWIGTYPE_p_IloIntLinExprTerm term)\n
    (final SWIGTYPE_p_IloNumQuadExprTerm term)\n
    (final SWIGTYPE_p_IloIntQuadExprTerm term)\n
    (final SWIGTYPE_p_IloExpr expr)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def add():
    '''returns None\n\n
    add(final IloLinearNumExpr arg0)\n
    '''
def addTerm():
    '''returns None\n\n
    addTerm(final double val, final IloNumVar var)\n
    addTerm(final IloNumVar var, final double val)\n
    '''
def addTerms():
    '''returns None\n\n
    addTerms(final double[] vals, final IloNumVar[] vars, final int arg2, final int arg3)\n
    addTerms(final double[] vals, final IloNumVar[] vars)\n
    addTerms(final IloNumVar[] vars, final double[] vals, final int arg2, final int arg3)\n
    addTerms(final IloNumVar[] vars, final double[] vals)\n
    '''
def linearIterator():
    '''returns IloLinearNumExprIterator\n\n
    linearIterator()\n
    '''
def remove():
    '''returns None\n\n
    remove(final IloNumVar var)\n
    remove(final IloNumVar[] vars, final int arg1, final int arg2)\n
    remove(final IloNumVar[] vars)\n
    '''
def getConstant():
    '''returns double\n\n
    getConstant()\n
    '''
def setConstant():
    '''returns None\n\n
    setConstant(final double val)\n
    '''
def operator_sum_equal():
    '''returns IloNumExpr\n\n
    operator_sum_equal(final double val)\n
    operator_sum_equal(final IloNumExprArg expr)\n
    '''
def operator_diff_equal():
    '''returns IloNumExpr\n\n
    operator_diff_equal(final double val)\n
    operator_diff_equal(final IloNumExprArg expr)\n
    '''
def operator_prod_equal():
    '''returns IloNumExpr\n\n
    operator_prod_equal(final double val)\n
    '''
def operator_div_equal():
    '''returns IloNumExpr\n\n
    operator_div_equal(final double val)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def _getLinearIterator():
    '''returns IloRangeI_LinearIterator\n\n
    _getLinearIterator()\n
    '''
def addTermCpp():
    '''returns None\n\n
    addTermCpp(final double val, final ilog.concert.cppimpl.IloNumVar var)\n
    '''
def setNumConstantCpp():
    '''returns None\n\n
    setNumConstantCpp(final double val)\n
    '''
def removeCpp():
    '''returns None\n\n
    removeCpp(final ilog.concert.cppimpl.IloNumVar val)\n
    '''
