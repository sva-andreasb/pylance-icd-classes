def ():
    '''returns IloIntMapBase\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final IloDiscreteDataCollection indexer)\n
    '''
def setOwn():
    '''returns None\n\n
    setOwn(final boolean cMemoryOwn)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def getNbDim():
    '''returns int\n\n
    getNbDim()\n
    '''
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def getTotalSize():
    '''returns int\n\n
    getTotalSize()\n
    '''
def getNonEmptySlotSize():
    '''returns int\n\n
    getNonEmptySlotSize()\n
    '''
def getIndexer():
    '''returns IloDiscreteDataCollection\n\n
    getIndexer()\n
    getIndexer(final int i)\n
    '''
def cpp_makeMapIndexer():
    '''returns IloDiscreteDataCollectionArray\n\n
    cpp_makeMapIndexer()\n
    '''
def operator_get():
    '''returns IloIntMapBase\n\n
    operator_get(final int i)\n
    operator_get(final double n)\n
    operator_get(final String a)\n
    operator_get(final IloSymbol s)\n
    operator_get(final IloTuple t)\n
    '''
def getSub_IloMap():
    '''returns IloIntMapBase\n\n
    getSub_IloMap(final int i)\n
    getSub_IloMap(final double n)\n
    getSub_IloMap(final String a)\n
    getSub_IloMap(final IloTuple i)\n
    '''
def get_IloMap():
    '''returns int\n\n
    get_IloMap(final int idx)\n
    get_IloMap(final double idx)\n
    get_IloMap(final String idx)\n
    get_IloMap(final IloTuple idx)\n
    get_IloMap(final IloSymbol idx)\n
    '''
def set():
    '''returns None\n\n
    set(final int idx, final int value)\n
    set(final double idx, final int value)\n
    set(final String idx, final int value)\n
    set(final IloTuple idx, final int value)\n
    set(final IloSymbol idx, final int value)\n
    '''
def setAt():
    '''returns None\n\n
    setAt(final IloMapIndexArray indices, final int value)\n
    setAt(final IloMapIndexArray indices, final IloOplObject value)\n
    '''
def getAt_IloMap():
    '''returns int\n\n
    getAt_IloMap(final IloMapIndexArray indices)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getMapImpl():
    '''returns SWIGTYPE_p_IloAbstractMapI\n\n
    getMapImpl()\n
    '''
