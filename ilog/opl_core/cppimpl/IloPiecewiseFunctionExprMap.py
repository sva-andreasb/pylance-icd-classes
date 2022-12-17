def ():
    '''returns IloPiecewiseFunctionExprMap\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final ilog.concert.cppimpl.IloDiscreteDataCollectionArray indexer)\n
    (final IloEnv env, final IloDiscreteDataCollection indexer)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def get():
    '''returns IloPiecewiseFunctionExpr\n\n
    get(final int index)\n
    get(final double index)\n
    get(final String index)\n
    get(final IloTuple index)\n
    '''
def set():
    '''returns None\n\n
    set(final int index, final IloPiecewiseFunctionExpr v)\n
    set(final double index, final IloPiecewiseFunctionExpr v)\n
    set(final String index, final IloPiecewiseFunctionExpr v)\n
    set(final IloTuple index, final IloPiecewiseFunctionExpr v)\n
    '''
def setAt():
    '''returns None\n\n
    setAt(final IloMapIndexArray indices, final IloPiecewiseFunctionExpr v)\n
    '''
def getAt():
    '''returns IloPiecewiseFunctionExpr\n\n
    getAt(final IloMapIndexArray indices)\n
    '''
def makeMapIndexer():
    '''returns IloDiscreteDataCollectionArray\n\n
    makeMapIndexer()\n
    '''
def getSub_IloPiecewiseFunctionExprMap():
    '''returns IloPiecewiseFunctionExprMap\n\n
    getSub_IloPiecewiseFunctionExprMap(final double index)\n
    getSub_IloPiecewiseFunctionExprMap(final int index)\n
    getSub_IloPiecewiseFunctionExprMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    getSub_IloPiecewiseFunctionExprMap(final String index)\n
    '''
def operator_get_IloPiecewiseFunctionExprMap():
    '''returns IloPiecewiseFunctionExprMap\n\n
    operator_get_IloPiecewiseFunctionExprMap(final int index)\n
    operator_get_IloPiecewiseFunctionExprMap(final double index)\n
    operator_get_IloPiecewiseFunctionExprMap(final String index)\n
    operator_get_IloPiecewiseFunctionExprMap(final IloSymbol index)\n
    operator_get_IloPiecewiseFunctionExprMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    '''
