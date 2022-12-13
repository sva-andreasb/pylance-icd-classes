def NodeTupleTableWrapper():
    '''public NodeTupleTableWrapper(final NodeTupleTable ntt)
    '''
def addRow():
    '''public boolean addRow(final Node... nodes)
    '''
def deleteRow():
    '''public boolean deleteRow(final Node... nodes)
    '''
def find():
    '''public Iterator<Tuple<Node>> find(final Node... nodes)
    public Iterator<Tuple<NodeId>> find(final NodeId... ids)
    '''
def findAsNodeIds():
    '''public Iterator<Tuple<NodeId>> findAsNodeIds(final Node... nodes)
    '''
def getNodeTable():
    '''public NodeTable getNodeTable()
    '''
def getTupleTable():
    '''public TupleTable getTupleTable()
    '''
def isEmpty():
    '''public boolean isEmpty()
    '''
def clear():
    '''public void clear()
    '''
def size():
    '''public long size()
    '''
def sync():
    '''public void sync()
    public void sync(final boolean force)
    '''
def close():
    '''public void close()
    '''
