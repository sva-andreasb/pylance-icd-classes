def ():
    '''returns IloIntSetMap\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final ilog.concert.cppimpl.IloDiscreteDataCollectionArray indexer)\n
    (final IloEnv env, final IloDiscreteDataCollection indexer)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def get():
    '''returns IloIntSet\n\n
    get(final int index)\n
    get(final double index)\n
    get(final String index)\n
    get(final IloTuple index)\n
    '''
def set():
    '''returns None\n\n
    set(final int index, final IloIntSet v)\n
    set(final double index, final IloIntSet v)\n
    set(final String index, final IloIntSet v)\n
    set(final IloTuple index, final IloIntSet v)\n
    set(final String index, final ilog.concert.cppimpl.IloIntSet value)\n
    set(final int index, final ilog.concert.cppimpl.IloIntSet value)\n
    set(final double index, final ilog.concert.cppimpl.IloIntSet value)\n
    set(final ilog.opl_core.cppimpl.IloTuple index, final ilog.concert.cppimpl.IloIntSet value)\n
    set(final IloSymbol index, final ilog.concert.cppimpl.IloIntSet value)\n
    '''
def setAt():
    '''returns None\n\n
    setAt(final IloMapIndexArray indices, final IloIntSet v)\n
    '''
def getAt():
    '''returns IloIntSet\n\n
    getAt(final IloMapIndexArray indices)\n
    '''
def makeMapIndexer():
    '''returns IloDiscreteDataCollectionArray\n\n
    makeMapIndexer()\n
    '''
def getSub_IloIntSetMap():
    '''returns IloIntSetMap\n\n
    getSub_IloIntSetMap(final double index)\n
    getSub_IloIntSetMap(final int index)\n
    getSub_IloIntSetMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    getSub_IloIntSetMap(final String index)\n
    '''
