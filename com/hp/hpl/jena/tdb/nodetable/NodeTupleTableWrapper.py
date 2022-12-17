def ():
    '''returns NodeTupleTableWrapper\n\n
    (final NodeTupleTable ntt)\n
    '''
def addRow():
    '''returns boolean\n\n
    addRow(final Node... nodes)\n
    '''
def deleteRow():
    '''returns boolean\n\n
    deleteRow(final Node... nodes)\n
    '''
def find():
    '''returns Iterator<Tuple<NodeId>>\n\n
    find(final Node... nodes)\n
    find(final NodeId... ids)\n
    '''
def findAsNodeIds():
    '''returns Iterator<Tuple<NodeId>>\n\n
    findAsNodeIds(final Node... nodes)\n
    '''
def getNodeTable():
    '''returns NodeTable\n\n
    getNodeTable()\n
    '''
def getTupleTable():
    '''returns TupleTable\n\n
    getTupleTable()\n
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
def sync():
    '''returns None\n\n
    sync()\n
    sync(final boolean force)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
