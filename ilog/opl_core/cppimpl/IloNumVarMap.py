def ():
    '''returns IloNumVarMap\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final ilog.concert.cppimpl.IloDiscreteDataCollectionArray indexer)\n
    (final IloEnv env, final IloDiscreteDataCollection indexer)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def get():
    '''returns IloNumVar\n\n
    get(final int index)\n
    get(final double index)\n
    get(final String index)\n
    get(final IloTuple index)\n
    '''
def set():
    '''returns None\n\n
    set(final int index, final IloNumVar v)\n
    set(final double index, final IloNumVar v)\n
    set(final String index, final IloNumVar v)\n
    set(final IloTuple index, final IloNumVar v)\n
    set(final String index, final ilog.concert.cppimpl.IloNumVar value)\n
    set(final int index, final ilog.concert.cppimpl.IloNumVar value)\n
    set(final double index, final ilog.concert.cppimpl.IloNumVar value)\n
    set(final ilog.opl_core.cppimpl.IloTuple index, final ilog.concert.cppimpl.IloNumVar value)\n
    set(final IloSymbol index, final ilog.concert.cppimpl.IloNumVar value)\n
    '''
def setAt():
    '''returns None\n\n
    setAt(final IloMapIndexArray indices, final IloNumVar v)\n
    '''
def getAt():
    '''returns IloNumVar\n\n
    getAt(final IloMapIndexArray indices)\n
    '''
def makeMapIndexer():
    '''returns IloDiscreteDataCollectionArray\n\n
    makeMapIndexer()\n
    '''
def getSub_IloNumVarMap():
    '''returns IloNumVarMap\n\n
    getSub_IloNumVarMap(final double index)\n
    getSub_IloNumVarMap(final int index)\n
    getSub_IloNumVarMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    getSub_IloNumVarMap(final String index)\n
    '''
def operator_get_IloNumVarMap():
    '''returns IloNumVarMap\n\n
    operator_get_IloNumVarMap(final int index)\n
    operator_get_IloNumVarMap(final double index)\n
    operator_get_IloNumVarMap(final String index)\n
    operator_get_IloNumVarMap(final IloSymbol index)\n
    operator_get_IloNumVarMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    '''
def asNewNumVarArray():
    '''returns IloNumVarArray\n\n
    asNewNumVarArray()\n
    '''
