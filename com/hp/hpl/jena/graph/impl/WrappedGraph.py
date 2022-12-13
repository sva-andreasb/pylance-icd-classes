def WrappedGraph():
    '''    public WrappedGraph(final Graph base)
    '''
def dependsOn():
    '''    public boolean dependsOn(final Graph other)
    '''
def queryHandler():
    '''    public QueryHandler queryHandler()
    '''
def getTransactionHandler():
    '''    public TransactionHandler getTransactionHandler()
    '''
def getBulkUpdateHandler():
    '''    public BulkUpdateHandler getBulkUpdateHandler()
    '''
def getStatisticsHandler():
    '''    public GraphStatisticsHandler getStatisticsHandler()
    '''
def getCapabilities():
    '''    public Capabilities getCapabilities()
    '''
def getEventManager():
    '''    public GraphEventManager getEventManager()
    '''
def getReifier():
    '''    public Reifier getReifier()
    '''
def getPrefixMapping():
    '''    public PrefixMapping getPrefixMapping()
    '''
def add():
    '''    public void add(final Triple t)
    '''
def delete():
    '''    public void delete(final Triple t)
    '''
def find():
    '''    public ExtendedIterator<Triple> find(final TripleMatch m)
    public ExtendedIterator<Triple> find(final Node s, final Node p, final Node o)
    '''
def isIsomorphicWith():
    '''    public boolean isIsomorphicWith(final Graph g)
    '''
def contains():
    '''    public boolean contains(final Node s, final Node p, final Node o)
    public boolean contains(final Triple t)
    '''
def close():
    '''    public void close()
    '''
def isClosed():
    '''    public boolean isClosed()
    '''
def isEmpty():
    '''    public boolean isEmpty()
    '''
def size():
    '''    public int size()
    '''
def performAdd():
    '''    public void performAdd(final Triple t)
    '''
def performDelete():
    '''    public void performDelete(final Triple t)
    '''
