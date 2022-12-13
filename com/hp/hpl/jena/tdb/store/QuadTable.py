def QuadTable():
    '''public QuadTable(final TupleIndex[] indexes, final NodeTable nodeTable)
    '''
def add():
    '''public boolean add(final Quad quad)
    public boolean add(final Node gn, final Triple triple)
    public boolean add(final Node g, final Node s, final Node p, final Node o)
    '''
def delete():
    '''public boolean delete(final Quad quad)
    public boolean delete(final Node gn, final Triple triple)
    public boolean delete(final Node g, final Node s, final Node p, final Node o)
    '''
def find():
    '''public Iterator<Quad> find(final Node g, final Node s, final Node p, final Node o)
    '''
def getNodeTupleTable():
    '''public NodeTupleTable getNodeTupleTable()
    '''
def sync():
    '''public void sync()
    public void sync(final boolean force)
    '''
def isEmpty():
    '''public boolean isEmpty()
    '''
def close():
    '''public void close()
    '''
def clearQuads():
    '''public void clearQuads()
    '''
def convert():
    '''public Quad convert(final Tuple<Node> item)
    '''
