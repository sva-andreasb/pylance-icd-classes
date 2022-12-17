def ():
    '''returns IloTupleSetMap\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final ilog.opl_core.cppimpl.IloTupleSchema schema, final ilog.concert.cppimpl.IloDiscreteDataCollectionArray indexer)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def get():
    '''returns IloTupleSet\n\n
    get(final int index)\n
    get(final double index)\n
    get(final String index)\n
    get(final IloTuple index)\n
    '''
def set():
    '''returns None\n\n
    set(final int index, final IloTupleSet v)\n
    set(final double index, final IloTupleSet v)\n
    set(final String index, final IloTupleSet v)\n
    set(final IloTuple index, final IloTupleSet v)\n
    set(final String index, final ilog.opl_core.cppimpl.IloTupleSet value)\n
    set(final int index, final ilog.opl_core.cppimpl.IloTupleSet value)\n
    set(final double index, final ilog.opl_core.cppimpl.IloTupleSet value)\n
    set(final ilog.opl_core.cppimpl.IloTuple index, final ilog.opl_core.cppimpl.IloTupleSet value)\n
    set(final IloSymbol index, final ilog.opl_core.cppimpl.IloTupleSet value)\n
    '''
def setAt():
    '''returns None\n\n
    setAt(final IloMapIndexArray indices, final IloTupleSet v)\n
    '''
def getAt():
    '''returns IloTupleSet\n\n
    getAt(final IloMapIndexArray indices)\n
    '''
def makeMapIndexer():
    '''returns IloDiscreteDataCollectionArray\n\n
    makeMapIndexer()\n
    '''
def getSchema():
    '''returns IloTupleSchema\n\n
    getSchema()\n
    '''
def getSub_IloTupleSetMap():
    '''returns IloTupleSetMap\n\n
    getSub_IloTupleSetMap(final double index)\n
    getSub_IloTupleSetMap(final int index)\n
    getSub_IloTupleSetMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    getSub_IloTupleSetMap(final String index)\n
    '''
def operator_get_IloTupleSetMap():
    '''returns IloTupleSetMap\n\n
    operator_get_IloTupleSetMap(final int index)\n
    operator_get_IloTupleSetMap(final double index)\n
    operator_get_IloTupleSetMap(final String index)\n
    operator_get_IloTupleSetMap(final IloSymbol index)\n
    operator_get_IloTupleSetMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    '''
