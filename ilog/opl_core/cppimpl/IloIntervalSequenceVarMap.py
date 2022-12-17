def ():
    '''returns IloIntervalSequenceVarMap\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final ilog.concert.cppimpl.IloDiscreteDataCollectionArray indexer)\n
    (final IloEnv env, final IloDiscreteDataCollection indexer)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def get():
    '''returns IloIntervalSequenceVar\n\n
    get(final int index)\n
    get(final double index)\n
    get(final String index)\n
    get(final IloTuple index)\n
    '''
def set():
    '''returns None\n\n
    set(final int index, final IloIntervalSequenceVar v)\n
    set(final double index, final IloIntervalSequenceVar v)\n
    set(final String index, final IloIntervalSequenceVar v)\n
    set(final IloTuple index, final IloIntervalSequenceVar v)\n
    '''
def setAt():
    '''returns None\n\n
    setAt(final IloMapIndexArray indices, final IloIntervalSequenceVar v)\n
    '''
def getAt():
    '''returns IloIntervalSequenceVar\n\n
    getAt(final IloMapIndexArray indices)\n
    '''
def makeMapIndexer():
    '''returns IloDiscreteDataCollectionArray\n\n
    makeMapIndexer()\n
    '''
def getSub_IloIntervalSequenceVarMap():
    '''returns IloIntervalSequenceVarMap\n\n
    getSub_IloIntervalSequenceVarMap(final double index)\n
    getSub_IloIntervalSequenceVarMap(final int index)\n
    getSub_IloIntervalSequenceVarMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    getSub_IloIntervalSequenceVarMap(final String index)\n
    '''
def operator_get_IloIntervalSequenceVarMap():
    '''returns IloIntervalSequenceVarMap\n\n
    operator_get_IloIntervalSequenceVarMap(final int index)\n
    operator_get_IloIntervalSequenceVarMap(final double index)\n
    operator_get_IloIntervalSequenceVarMap(final String index)\n
    operator_get_IloIntervalSequenceVarMap(final IloSymbol index)\n
    operator_get_IloIntervalSequenceVarMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    '''
def asNewIntervalSequenceVarArray():
    '''returns IloIntervalSequenceVarArray\n\n
    asNewIntervalSequenceVarArray()\n
    '''
