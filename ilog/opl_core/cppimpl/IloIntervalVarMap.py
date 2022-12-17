def ():
    '''returns IloIntervalVarMap\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final ilog.concert.cppimpl.IloDiscreteDataCollectionArray indexer)\n
    (final IloEnv env, final IloDiscreteDataCollection indexer)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def get():
    '''returns IloIntervalVar\n\n
    get(final int index)\n
    get(final double index)\n
    get(final String index)\n
    get(final IloTuple index)\n
    '''
def set():
    '''returns None\n\n
    set(final int index, final IloIntervalVar v)\n
    set(final double index, final IloIntervalVar v)\n
    set(final String index, final IloIntervalVar v)\n
    set(final IloTuple index, final IloIntervalVar v)\n
    '''
def setAt():
    '''returns None\n\n
    setAt(final IloMapIndexArray indices, final IloIntervalVar v)\n
    '''
def getAt():
    '''returns IloIntervalVar\n\n
    getAt(final IloMapIndexArray indices)\n
    '''
def makeMapIndexer():
    '''returns IloDiscreteDataCollectionArray\n\n
    makeMapIndexer()\n
    '''
def getSub_IloIntervalVarMap():
    '''returns IloIntervalVarMap\n\n
    getSub_IloIntervalVarMap(final double index)\n
    getSub_IloIntervalVarMap(final int index)\n
    getSub_IloIntervalVarMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    getSub_IloIntervalVarMap(final String index)\n
    '''
def operator_get_IloIntervalVarMap():
    '''returns IloIntervalVarMap\n\n
    operator_get_IloIntervalVarMap(final int index)\n
    operator_get_IloIntervalVarMap(final double index)\n
    operator_get_IloIntervalVarMap(final String index)\n
    operator_get_IloIntervalVarMap(final IloSymbol index)\n
    operator_get_IloIntervalVarMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    '''
def asNewIntervalVarArray():
    '''returns IloIntervalVarArray\n\n
    asNewIntervalVarArray()\n
    '''
