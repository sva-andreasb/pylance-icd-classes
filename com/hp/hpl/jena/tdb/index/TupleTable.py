def ():
    '''returns TupleTable\n\n
    (final int tupleLen, final TupleIndex[] indexes)\n
    '''
def add():
    '''returns boolean\n\n
    add(final Tuple<NodeId> t)\n
    '''
def delete():
    '''returns boolean\n\n
    delete(final Tuple<NodeId> t)\n
    '''
def find():
    '''returns Iterator<Tuple<NodeId>>\n\n
    find(final Tuple<NodeId> pattern)\n
    '''
def sync():
    '''returns None\n\n
    sync()\n
    sync(final boolean force)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def size():
    '''returns long\n\n
    size()\n
    '''
def getIndex():
    '''returns TupleIndex\n\n
    getIndex(final int i)\n
    '''
def getIndexes():
    '''returns TupleIndex[]\n\n
    getIndexes()\n
    '''
def getTupleLen():
    '''returns int\n\n
    getTupleLen()\n
    '''
def setTupleIndex():
    '''returns None\n\n
    setTupleIndex(final int i, final TupleIndex index)\n
    '''
def numIndexes():
    '''returns int\n\n
    numIndexes()\n
    '''
