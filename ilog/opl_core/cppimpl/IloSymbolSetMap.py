def ():
    '''returns IloSymbolSetMap\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final ilog.concert.cppimpl.IloDiscreteDataCollectionArray indexer)\n
    (final IloEnv env, final IloDiscreteDataCollection indexer)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def get():
    '''returns IloSymbolSet\n\n
    get(final int index)\n
    get(final double index)\n
    get(final String index)\n
    get(final IloTuple index)\n
    '''
def set():
    '''returns None\n\n
    set(final int index, final IloSymbolSet v)\n
    set(final double index, final IloSymbolSet v)\n
    set(final String index, final IloSymbolSet v)\n
    set(final IloTuple index, final IloSymbolSet v)\n
    set(final String index, final ilog.opl_core.cppimpl.IloSymbolSet value)\n
    set(final int index, final ilog.opl_core.cppimpl.IloSymbolSet value)\n
    set(final double index, final ilog.opl_core.cppimpl.IloSymbolSet value)\n
    set(final ilog.opl_core.cppimpl.IloTuple index, final ilog.opl_core.cppimpl.IloSymbolSet value)\n
    set(final IloSymbol index, final ilog.opl_core.cppimpl.IloSymbolSet value)\n
    '''
def setAt():
    '''returns None\n\n
    setAt(final IloMapIndexArray indices, final IloSymbolSet v)\n
    '''
def getAt():
    '''returns IloSymbolSet\n\n
    getAt(final IloMapIndexArray indices)\n
    '''
def makeMapIndexer():
    '''returns IloDiscreteDataCollectionArray\n\n
    makeMapIndexer()\n
    '''
def getSub_IloSymbolSetMap():
    '''returns IloSymbolSetMap\n\n
    getSub_IloSymbolSetMap(final double index)\n
    getSub_IloSymbolSetMap(final int index)\n
    getSub_IloSymbolSetMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    getSub_IloSymbolSetMap(final String index)\n
    '''
def operator_get_IloSymbolSetMap():
    '''returns IloSymbolSetMap\n\n
    operator_get_IloSymbolSetMap(final int index)\n
    operator_get_IloSymbolSetMap(final double index)\n
    operator_get_IloSymbolSetMap(final String index)\n
    operator_get_IloSymbolSetMap(final IloSymbol index)\n
    operator_get_IloSymbolSetMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    '''
