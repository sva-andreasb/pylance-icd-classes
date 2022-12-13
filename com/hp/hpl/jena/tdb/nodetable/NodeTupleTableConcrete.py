def NodeTupleTableConcrete():
    '''    public NodeTupleTableConcrete(final int N, final TupleIndex[] indexes, final NodeTable nodeTable)
    '''
def addRow():
    '''    public boolean addRow(final Node... nodes)
    '''
def deleteRow():
    '''    public boolean deleteRow(final Node... nodes)
    '''
def find():
    '''    public Iterator<Tuple<Node>> find(final Node... nodes)
    public Iterator<Tuple<NodeId>> find(final NodeId... ids)
    '''
def findAsNodeIds():
    '''    public Iterator<Tuple<NodeId>> findAsNodeIds(final Node... nodes)
    '''
def getTupleTable():
    '''    public final TupleTable getTupleTable()
    '''
def getNodeTable():
    '''    public final NodeTable getNodeTable()
    '''
def isEmpty():
    '''    public boolean isEmpty()
    '''
def clear():
    '''    public void clear()
    '''
def size():
    '''    public long size()
    '''
def close():
    '''    public final void close()
    '''
def sync():
    '''    public final void sync()
    public final void sync(final boolean force)
    '''
