def TripleTable():
    '''public TripleTable(final TupleIndex[] indexes, final NodeTable nodeTable)
    '''
def add():
    '''public boolean add(final Triple triple)
    public boolean add(final Node s, final Node p, final Node o)
    '''
def delete():
    '''public boolean delete(final Triple triple)
    public boolean delete(final Node s, final Node p, final Node o)
    '''
def find():
    '''public Iterator<Triple> find(final Node s, final Node p, final Node o)
    '''
def getNodeTupleTable():
    '''public NodeTupleTable getNodeTupleTable()
    '''
def sync():
    '''public void sync()
    public void sync(final boolean force)
    '''
def close():
    '''public void close()
    '''
def isEmpty():
    '''public boolean isEmpty()
    '''
def clearTriples():
    '''public void clearTriples()
    '''
def convert():
    '''public Triple convert(final Tuple<Node> item)
    '''
