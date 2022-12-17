def ():
    '''returns IloNumDExprMap\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final IloNumExprArg expr, final IloDiscreteDataCollectionArray indexer, final IloMapIndexArray indexes)\n
    '''
def setOwn():
    '''returns None\n\n
    setOwn(final boolean cMemoryOwn)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def get():
    '''returns IloNumExpr\n\n
    get(final int index)\n
    get(final double index)\n
    get(final String index)\n
    get(final IloTuple index)\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def get_IloNumDExprMap():
    '''returns IloNumExprArg\n\n
    get_IloNumDExprMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    get_IloNumDExprMap(final String index)\n
    get_IloNumDExprMap(final IloSymbol index)\n
    get_IloNumDExprMap(final double index)\n
    get_IloNumDExprMap(final int index)\n
    '''
