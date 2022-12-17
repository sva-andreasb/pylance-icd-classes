def ():
    '''returns IloConstraintMap\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final ilog.concert.cppimpl.IloDiscreteDataCollectionArray indexer)\n
    (final IloEnv env, final IloDiscreteDataCollection indexer)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def get():
    '''returns IloConstraint\n\n
    get(final int index)\n
    get(final double index)\n
    get(final String index)\n
    get(final IloTuple index)\n
    '''
def set():
    '''returns None\n\n
    set(final int index, final IloConstraint v)\n
    set(final double index, final IloConstraint v)\n
    set(final String index, final IloConstraint v)\n
    set(final IloTuple index, final IloConstraint v)\n
    '''
def setAt():
    '''returns None\n\n
    setAt(final IloMapIndexArray indices, final IloConstraint v)\n
    '''
def getAt():
    '''returns IloConstraint\n\n
    getAt(final IloMapIndexArray indices)\n
    '''
def makeMapIndexer():
    '''returns IloDiscreteDataCollectionArray\n\n
    makeMapIndexer()\n
    '''
def getSub_IloConstraintMap():
    '''returns IloConstraintMap\n\n
    getSub_IloConstraintMap(final double index)\n
    getSub_IloConstraintMap(final int index)\n
    getSub_IloConstraintMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    getSub_IloConstraintMap(final String index)\n
    '''
def operator_get_IloConstraintMap():
    '''returns IloConstraintMap\n\n
    operator_get_IloConstraintMap(final int index)\n
    operator_get_IloConstraintMap(final double index)\n
    operator_get_IloConstraintMap(final String index)\n
    operator_get_IloConstraintMap(final IloSymbol index)\n
    operator_get_IloConstraintMap(final ilog.opl_core.cppimpl.IloTuple index)\n
    '''
def asNewConstraintArray():
    '''returns IloConstraintArray\n\n
    asNewConstraintArray()\n
    '''
