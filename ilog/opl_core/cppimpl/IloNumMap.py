def ():
    '''returns IloNumMap\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final ilog.concert.cppimpl.IloDiscreteDataCollectionArray indexer)\n
    (final IloEnv env, final IloDiscreteDataCollection indexer)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def get():
    '''returns double\n\n
    get(final int index)\n
    get(final double index)\n
    get(final String index)\n
    get(final IloTuple index)\n
    '''
def set():
    '''returns None\n\n
    set(final IloTuple index, final double v)\n
    set(final String index, final double value)\n
    set(final int index, final double value)\n
    set(final double index, final double value)\n
    set(final ilog.opl_core.cppimpl.IloTuple index, final double value)\n
    set(final IloSymbol index, final double value)\n
    '''
def setAt():
    '''returns None\n\n
    setAt(final IloMapIndexArray indices, final double v)\n
    '''
def getAt():
    '''returns double\n\n
    getAt(final IloMapIndexArray indices)\n
    '''
def makeMapIndexer():
    '''returns IloDiscreteDataCollectionArray\n\n
    makeMapIndexer()\n
    '''
def get_IloNumMap():
    '''returns double\n\n
    get_IloNumMap(final int index)\n
    get_IloNumMap(final double index)\n
    get_IloNumMap(final String index)\n
    get_IloNumMap(final IloSymbol index)\n
    get_IloNumMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    '''
def getSub_IloNumMap():
    '''returns IloNumMap\n\n
    getSub_IloNumMap(final double index)\n
    getSub_IloNumMap(final int index)\n
    getSub_IloNumMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    getSub_IloNumMap(final String index)\n
    '''
def operator_get_IloNumMap():
    '''returns IloNumMap\n\n
    operator_get_IloNumMap(final int index)\n
    operator_get_IloNumMap(final double index)\n
    operator_get_IloNumMap(final String index)\n
    operator_get_IloNumMap(final IloSymbol index)\n
    operator_get_IloNumMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    '''
