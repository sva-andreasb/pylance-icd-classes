def ():
    '''returns IloNumSetMap\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final ilog.concert.cppimpl.IloDiscreteDataCollectionArray indexer)\n
    (final IloEnv env, final IloDiscreteDataCollection indexer)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def get():
    '''returns IloNumSet\n\n
    get(final int index)\n
    get(final double index)\n
    get(final String index)\n
    get(final IloTuple index)\n
    '''
def set():
    '''returns None\n\n
    set(final int index, final IloNumSet v)\n
    set(final double index, final IloNumSet v)\n
    set(final String index, final IloNumSet v)\n
    set(final IloTuple index, final IloNumSet v)\n
    set(final String index, final ilog.concert.cppimpl.IloNumSet value)\n
    set(final int index, final ilog.concert.cppimpl.IloNumSet value)\n
    set(final double index, final ilog.concert.cppimpl.IloNumSet value)\n
    set(final ilog.opl_core.cppimpl.IloTuple index, final ilog.concert.cppimpl.IloNumSet value)\n
    set(final IloSymbol index, final ilog.concert.cppimpl.IloNumSet value)\n
    '''
def setAt():
    '''returns None\n\n
    setAt(final IloMapIndexArray indices, final IloNumSet v)\n
    '''
def getAt():
    '''returns IloNumSet\n\n
    getAt(final IloMapIndexArray indices)\n
    '''
def makeMapIndexer():
    '''returns IloDiscreteDataCollectionArray\n\n
    makeMapIndexer()\n
    '''
def getSub_IloNumSetMap():
    '''returns IloNumSetMap\n\n
    getSub_IloNumSetMap(final double index)\n
    getSub_IloNumSetMap(final int index)\n
    getSub_IloNumSetMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    getSub_IloNumSetMap(final String index)\n
    '''
def operator_get_IloNumSetMap():
    '''returns IloNumSetMap\n\n
    operator_get_IloNumSetMap(final int index)\n
    operator_get_IloNumSetMap(final double index)\n
    operator_get_IloNumSetMap(final String index)\n
    operator_get_IloNumSetMap(final IloSymbol index)\n
    operator_get_IloNumSetMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    '''
