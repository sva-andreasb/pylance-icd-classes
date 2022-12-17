def ():
    '''returns IloRangeArray\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final SWIGTYPE_p_IloDefaultArrayI i)\n
    (final IloEnv env, final int n)\n
    (final IloEnv env)\n
    (final IloEnv env, final int n, final double lb, final double ub)\n
    (final IloEnv env, final IloNumArray lbs, final IloNumExprArray rows, final IloNumArray ubs)\n
    (final IloEnv env, final double lb, final IloNumExprArray rows, final IloNumArray ubs)\n
    (final IloEnv env, final IloNumArray lbs, final IloNumExprArray rows, final double ub)\n
    (final IloEnv env, final double lb, final IloNumExprArray rows, final double ub)\n
    (final IloEnv env, final IloIntArray lbs, final IloNumExprArray rows, final IloIntArray ubs)\n
    (final IloEnv env, final double lb, final IloNumExprArray rows, final IloIntArray ubs)\n
    (final IloEnv env, final IloIntArray lbs, final IloNumExprArray rows, final double ub)\n
    (final IloEnv env, final IloNumArray lbs, final IloNumArray ubs)\n
    (final IloEnv env, final IloIntArray lbs, final IloIntArray ubs)\n
    (final IloEnv env, final double lb, final IloNumArray ubs)\n
    (final IloEnv env, final IloNumArray lbs, final double ub)\n
    (final IloEnv env, final double lb, final IloIntArray ubs)\n
    (final IloEnv env, final IloIntArray lbs, final double ub)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def add():
    '''returns None\n\n
    add(final IloRange range)\n
    add(final int more, final IloRange range)\n
    '''
def operator_get_IloRangeArray():
    '''returns IloRange\n\n
    operator_get_IloRangeArray(final int i)\n
    '''
def setBounds():
    '''returns None\n\n
    setBounds(final IloNumArray lbs, final IloNumArray ubs)\n
    setBounds(final IloIntArray lbs, final IloIntArray ubs)\n
    '''
