def DBReifierGraph():
    '''    public DBReifierGraph(final GraphRDB parent, final List<SpecializedGraphReifier> reifiers)
    '''
def add():
    '''    public void add(final Triple t)
    '''
def delete():
    '''    public void delete(final Triple t)
    '''
def size():
    '''    public int size()
    '''
def isEmpty():
    '''    public boolean isEmpty()
    '''
def contains():
    '''    public boolean contains(final Triple t)
    public boolean contains(final Node s, final Node p, final Node o)
    '''
def getStatisticsHandler():
    '''    public GraphStatisticsHandler getStatisticsHandler()
    '''
def find():
    '''    public ExtendedIterator<Triple> find(final TripleMatch m)
    public ExtendedIterator<Triple> find(final Node s, final Node p, final Node o)
    '''
def getPrefixMapping():
    '''    public PrefixMapping getPrefixMapping()
    '''
def getTransactionHandler():
    '''    public TransactionHandler getTransactionHandler()
    '''
def close():
    '''    public void close()
    '''
def isClosed():
    '''    public boolean isClosed()
    '''
def getEventManager():
    '''    public GraphEventManager getEventManager()
    '''
def dependsOn():
    '''    public boolean dependsOn(final Graph other)
    '''
def queryHandler():
    '''    public QueryHandler queryHandler()
    '''
def getBulkUpdateHandler():
    '''    public BulkUpdateHandler getBulkUpdateHandler()
    '''
def getCapabilities():
    '''    public Capabilities getCapabilities()
    '''
def getReifier():
    '''    public Reifier getReifier()
    '''
def isIsomorphicWith():
    '''    public boolean isIsomorphicWith(final Graph g)
    '''
def capabilities():
    '''    public int capabilities()
    '''
def toString():
    '''    public String toString()
    '''
