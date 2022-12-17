def ():
    '''returns IloIntMap\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final ilog.concert.cppimpl.IloDiscreteDataCollectionArray indexer)\n
    (final IloEnv env, final IloDiscreteDataCollection indexer)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def get():
    '''returns int\n\n
    get(final int index)\n
    get(final double index)\n
    get(final String index)\n
    get(final IloTuple index)\n
    '''
def set():
    '''returns None\n\n
    set(final IloTuple index, final int v)\n
    set(final String index, final int value)\n
    set(final int index, final int value)\n
    set(final double index, final int value)\n
    set(final ilog.opl_core.cppimpl.IloTuple index, final int value)\n
    set(final IloSymbol index, final int value)\n
    '''
def setAt():
    '''returns None\n\n
    setAt(final IloMapIndexArray indices, final int v)\n
    '''
def getAt():
    '''returns int\n\n
    getAt(final IloMapIndexArray indices)\n
    '''
def makeMapIndexer():
    '''returns IloDiscreteDataCollectionArray\n\n
    makeMapIndexer()\n
    '''
def get_IloIntMap():
    '''returns int\n\n
    get_IloIntMap(final int index)\n
    get_IloIntMap(final double index)\n
    get_IloIntMap(final String index)\n
    get_IloIntMap(final IloSymbol index)\n
    get_IloIntMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    '''
def getSub_IloIntMap():
    '''returns IloIntMap\n\n
    getSub_IloIntMap(final double index)\n
    getSub_IloIntMap(final int index)\n
    getSub_IloIntMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    getSub_IloIntMap(final String index)\n
    '''
def operator_get_IloIntMap():
    '''returns IloIntMap\n\n
    operator_get_IloIntMap(final int index)\n
    operator_get_IloIntMap(final double index)\n
    operator_get_IloIntMap(final String index)\n
    operator_get_IloIntMap(final IloSymbol index)\n
    operator_get_IloIntMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    '''
