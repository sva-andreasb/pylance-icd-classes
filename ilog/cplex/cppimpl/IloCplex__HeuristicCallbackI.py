def ():
    '''returns IloCplex__HeuristicCallbackI\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def setBounds():
    '''returns None\n\n
    setBounds(final IloNumVar var, final double lb, final double ub)\n
    setBounds(final IloIntVar var, final double lb, final double ub)\n
    setBounds(final IloNumVarArray var, final IloNumArray lb, final IloNumArray ub)\n
    setBounds(final IloIntVarArray var, final IloNumArray lb, final IloNumArray ub)\n
    '''
def solve():
    '''returns boolean\n\n
    solve(final SWIGTYPE_p_IloCplex__Algorithm alg)\n
    solve()\n
    '''
def isPrimalFeasible():
    '''returns boolean\n\n
    isPrimalFeasible()\n
    '''
def isDualFeasible():
    '''returns boolean\n\n
    isDualFeasible()\n
    '''
def setSolution():
    '''returns None\n\n
    setSolution(final IloNumVarArray vars, final IloNumArray vals)\n
    setSolution(final IloNumVarArray vars, final IloNumArray vals, final double obj)\n
    setSolution(final IloIntVarArray vars, final IloNumArray vals)\n
    setSolution(final IloIntVarArray vars, final IloNumArray vals, final double obj)\n
    '''
