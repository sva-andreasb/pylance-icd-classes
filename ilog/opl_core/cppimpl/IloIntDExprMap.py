def ():
    '''returns IloIntDExprMap\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final IloIntExprArg expr, final IloDiscreteDataCollectionArray indexer, final IloMapIndexArray indexes)\n
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
    '''returns IloIntExpr\n\n
    get(final int index)\n
    get(final double index)\n
    get(final String index)\n
    get(final IloTuple index)\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def get_IloIntDExprMap():
    '''returns IloIntExprArg\n\n
    get_IloIntDExprMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    get_IloIntDExprMap(final String index)\n
    get_IloIntDExprMap(final IloSymbol index)\n
    get_IloIntDExprMap(final double index)\n
    get_IloIntDExprMap(final int index)\n
    '''
