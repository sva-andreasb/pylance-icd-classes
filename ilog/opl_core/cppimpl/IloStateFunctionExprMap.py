def ():
    '''returns IloStateFunctionExprMap\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final ilog.concert.cppimpl.IloDiscreteDataCollectionArray indexer)\n
    (final IloEnv env, final IloDiscreteDataCollection indexer)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def get():
    '''returns IloStateFunctionExpr\n\n
    get(final int index)\n
    get(final double index)\n
    get(final String index)\n
    get(final IloTuple index)\n
    '''
def set():
    '''returns None\n\n
    set(final int index, final IloStateFunctionExpr v)\n
    set(final double index, final IloStateFunctionExpr v)\n
    set(final String index, final IloStateFunctionExpr v)\n
    set(final IloTuple index, final IloStateFunctionExpr v)\n
    '''
def setAt():
    '''returns None\n\n
    setAt(final IloMapIndexArray indices, final IloStateFunctionExpr v)\n
    '''
def getAt():
    '''returns IloStateFunctionExpr\n\n
    getAt(final IloMapIndexArray indices)\n
    '''
def makeMapIndexer():
    '''returns IloDiscreteDataCollectionArray\n\n
    makeMapIndexer()\n
    '''
def getSub_IloStateFunctionExprMap():
    '''returns IloStateFunctionExprMap\n\n
    getSub_IloStateFunctionExprMap(final double index)\n
    getSub_IloStateFunctionExprMap(final int index)\n
    getSub_IloStateFunctionExprMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    getSub_IloStateFunctionExprMap(final String index)\n
    '''
def operator_get_IloStateFunctionExprMap():
    '''returns IloStateFunctionExprMap\n\n
    operator_get_IloStateFunctionExprMap(final int index)\n
    operator_get_IloStateFunctionExprMap(final double index)\n
    operator_get_IloStateFunctionExprMap(final String index)\n
    operator_get_IloStateFunctionExprMap(final IloSymbol index)\n
    operator_get_IloStateFunctionExprMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    '''
