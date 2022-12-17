def ():
    '''returns IloTupleSet\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final ilog.opl_core.cppimpl.IloTupleSchema schema)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def getSchema():
    '''returns IloTupleSchema\n\n
    getSchema()\n
    '''
def makeTuple():
    '''returns IloTuple\n\n
    makeTuple(final int index)\n
    '''
def makeTupleBuffer():
    '''returns IloTupleBuffer\n\n
    makeTupleBuffer(final int index)\n
    '''
def makeNext():
    '''returns IloTuple\n\n
    makeNext(final IloTuple value, final int n)\n
    makeNext(final IloTuple value)\n
    '''
def makePrevious():
    '''returns IloTuple\n\n
    makePrevious(final IloTuple value, final int n)\n
    makePrevious(final IloTuple value)\n
    '''
def makeNextC():
    '''returns IloTuple\n\n
    makeNextC(final IloTuple value, final int n)\n
    makeNextC(final IloTuple value)\n
    '''
def makePreviousC():
    '''returns IloTuple\n\n
    makePreviousC(final IloTuple value, final int n)\n
    makePreviousC(final IloTuple value)\n
    '''
def makeFirst():
    '''returns IloTuple\n\n
    makeFirst()\n
    '''
def makeLast():
    '''returns IloTuple\n\n
    makeLast()\n
    '''
def find():
    '''returns IloTuple\n\n
    find(final IloTupleBuffer buffer)\n
    '''
def getIndex():
    '''returns int\n\n
    getIndex(final IloTuple tuple)\n
    '''
def isIn():
    '''returns boolean\n\n
    isIn(final IloTupleBuffer buffer)\n
    '''
def iterator():
    '''returns IloTupleIterator\n\n
    iterator()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getColumnName():
    '''returns String\n\n
    getColumnName(final int index)\n
    getColumnName(final IloIntArray path)\n
    '''
def setColumnName():
    '''returns None\n\n
    setColumnName(final int index, final String name)\n
    setColumnName(final IloIntArray path, final String name)\n
    '''
def commit():
    '''returns int\n\n
    commit(final ilog.opl_core.cppimpl.IloTupleBuffer line, final boolean check)\n
    commit(final ilog.opl_core.cppimpl.IloTupleBuffer line)\n
    commit(final IloTupleCellArray line, final boolean check)\n
    '''
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def isIn_cpp():
    '''returns boolean\n\n
    isIn_cpp(final ilog.opl_core.cppimpl.IloTupleBuffer buffer)\n
    '''
def getIndex_cpp():
    '''returns int\n\n
    getIndex_cpp(final ilog.opl_core.cppimpl.IloTuple tuple)\n
    '''
def commit2HashTable():
    '''returns int\n\n
    commit2HashTable(final IloTupleCellArray array, final boolean check)\n
    '''
def fillColumns():
    '''returns None\n\n
    fillColumns()\n
    '''
def getOrMakeSharedKeyCells():
    '''returns IloTupleCellArray\n\n
    getOrMakeSharedKeyCells(final int line)\n
    '''
def getOrMakeSharedTupleCells():
    '''returns IloTupleCellArray\n\n
    getOrMakeSharedTupleCells(final int line)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
