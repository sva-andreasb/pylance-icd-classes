def ():
    '''returns IloTupleMap\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final ilog.concert.cppimpl.IloDiscreteDataCollectionArray indexer, final ilog.opl_core.cppimpl.IloTupleSchema schema)\n
    '''
def setOwn():
    '''returns None\n\n
    setOwn(final boolean cMemoryOwn)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def setAt():
    '''returns None\n\n
    setAt(final IloMapIndexArray indices, final IloTuple v)\n
    setAt(final IloMapIndexArray indices, final IloTupleBuffer v)\n
    setAt(final ilog.opl_core.cppimpl.IloMapIndexArray indices, final ilog.opl_core.cppimpl.IloTuple value)\n
    setAt(final ilog.opl_core.cppimpl.IloMapIndexArray indices, final ilog.opl_core.cppimpl.IloTupleBuffer value)\n
    setAt(final ilog.opl_core.cppimpl.IloMapIndexArray indices, final IloOplObject value)\n
    '''
def getAt():
    '''returns None\n\n
    getAt(final IloMapIndexArray indices, final IloTuple v)\n
    getAt(final IloMapIndexArray indices, final IloTupleBuffer v)\n
    '''
def makeMapIndexer():
    '''returns IloDiscreteDataCollectionArray\n\n
    makeMapIndexer()\n
    '''
def getSchema():
    '''returns IloTupleSchema\n\n
    getSchema()\n
    '''
def makeTuple():
    '''returns IloTuple\n\n
    makeTuple()\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def getIndexer():
    '''returns IloDiscreteDataCollection\n\n
    getIndexer()\n
    getIndexer(final int i)\n
    '''
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def getNbDim():
    '''returns int\n\n
    getNbDim()\n
    '''
def getTotalSize():
    '''returns int\n\n
    getTotalSize()\n
    '''
def getNonEmptySlotSize():
    '''returns int\n\n
    getNonEmptySlotSize()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getAt_IloTupleMap():
    '''returns None\n\n
    getAt_IloTupleMap(final ilog.opl_core.cppimpl.IloMapIndexArray indices)\n
    getAt_IloTupleMap(final ilog.opl_core.cppimpl.IloMapIndexArray indices, final ilog.opl_core.cppimpl.IloTuple tuple)\n
    getAt_IloTupleMap(final ilog.opl_core.cppimpl.IloMapIndexArray indices, final ilog.opl_core.cppimpl.IloTupleBuffer buffer)\n
    '''
def isDefaultValue():
    '''returns boolean\n\n
    isDefaultValue(final ilog.opl_core.cppimpl.IloTuple tuple)\n
    '''
def getMapImpl():
    '''returns SWIGTYPE_p_IloAbstractMapI\n\n
    getMapImpl()\n
    '''
