def ():
    '''returns IloSymbolMap\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final ilog.concert.cppimpl.IloDiscreteDataCollectionArray indexer)\n
    (final IloEnv env, final IloDiscreteDataCollection indexer)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def get():
    '''returns String\n\n
    get(final int index)\n
    get(final double index)\n
    get(final String index)\n
    get(final IloTuple index)\n
    '''
def set():
    '''returns None\n\n
    set(final IloTuple index, final String v)\n
    set(final int index, final String value)\n
    set(final double index, final String value)\n
    set(final String index, final String value)\n
    set(final ilog.opl_core.cppimpl.IloTuple index, final String value)\n
    set(final IloSymbol idx, final String value)\n
    '''
def setAt():
    '''returns None\n\n
    setAt(final IloMapIndexArray indices, final String v)\n
    '''
def getAt():
    '''returns String\n\n
    getAt(final IloMapIndexArray indices)\n
    '''
def makeMapIndexer():
    '''returns IloDiscreteDataCollectionArray\n\n
    makeMapIndexer()\n
    '''
def getAt_IloSymbolMap():
    '''returns IloSymbol\n\n
    getAt_IloSymbolMap(final ilog.opl_core.cppimpl.IloMapIndexArray indices)\n
    '''
def get_IloSymbolMap():
    '''returns IloSymbol\n\n
    get_IloSymbolMap(final int index)\n
    get_IloSymbolMap(final double index)\n
    get_IloSymbolMap(final String index)\n
    get_IloSymbolMap(final IloSymbol index)\n
    get_IloSymbolMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    '''
def getSub_IloSymbolMap():
    '''returns IloSymbolMap\n\n
    getSub_IloSymbolMap(final double index)\n
    getSub_IloSymbolMap(final int index)\n
    getSub_IloSymbolMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    getSub_IloSymbolMap(final String index)\n
    '''
def operator_get_IloSymbolMap():
    '''returns IloSymbolMap\n\n
    operator_get_IloSymbolMap(final int index)\n
    operator_get_IloSymbolMap(final double index)\n
    operator_get_IloSymbolMap(final String index)\n
    operator_get_IloSymbolMap(final IloSymbol index)\n
    operator_get_IloSymbolMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    '''
def setAt_cpp():
    '''returns None\n\n
    setAt_cpp(final ilog.opl_core.cppimpl.IloMapIndexArray indices, final String v)\n
    '''
