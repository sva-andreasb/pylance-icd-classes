def ():
    '''returns IloIntVarMap\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final ilog.concert.cppimpl.IloDiscreteDataCollectionArray indexer)\n
    (final IloEnv env, final IloDiscreteDataCollection indexer)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def get():
    '''returns IloIntVar\n\n
    get(final int index)\n
    get(final double index)\n
    get(final String index)\n
    get(final IloTuple index)\n
    '''
def set():
    '''returns None\n\n
    set(final int index, final IloIntVar v)\n
    set(final double index, final IloIntVar v)\n
    set(final String index, final IloIntVar v)\n
    set(final IloTuple index, final IloIntVar v)\n
    set(final String index, final ilog.concert.cppimpl.IloIntVar value)\n
    set(final int index, final ilog.concert.cppimpl.IloIntVar value)\n
    set(final double index, final ilog.concert.cppimpl.IloIntVar value)\n
    set(final ilog.opl_core.cppimpl.IloTuple index, final ilog.concert.cppimpl.IloIntVar value)\n
    set(final IloSymbol index, final ilog.concert.cppimpl.IloIntVar value)\n
    '''
def setAt():
    '''returns None\n\n
    setAt(final IloMapIndexArray indices, final IloIntVar v)\n
    '''
def getAt():
    '''returns IloIntVar\n\n
    getAt(final IloMapIndexArray indices)\n
    '''
def makeMapIndexer():
    '''returns IloDiscreteDataCollectionArray\n\n
    makeMapIndexer()\n
    '''
def getSub_IloIntVarMap():
    '''returns IloIntVarMap\n\n
    getSub_IloIntVarMap(final double index)\n
    getSub_IloIntVarMap(final int index)\n
    getSub_IloIntVarMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    getSub_IloIntVarMap(final String index)\n
    '''
def operator_get_IloIntVarMap():
    '''returns IloIntVarMap\n\n
    operator_get_IloIntVarMap(final int index)\n
    operator_get_IloIntVarMap(final double index)\n
    operator_get_IloIntVarMap(final String index)\n
    operator_get_IloIntVarMap(final IloSymbol index)\n
    operator_get_IloIntVarMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    '''
def asNewIntVarArray():
    '''returns IloIntVarArray\n\n
    asNewIntVarArray()\n
    '''
