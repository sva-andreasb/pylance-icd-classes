TOSTRING_TRIPLE_BASE = "int  10"
TOSTRING_TRIPLE_LIMIT = "int  17"
def GraphBase():
    '''    public GraphBase()
    public GraphBase(final ReificationStyle style)
    '''
def close():
    '''    public void close()
    '''
def isClosed():
    '''    public boolean isClosed()
    '''
def dependsOn():
    '''    public boolean dependsOn(final Graph other)
    '''
def queryHandler():
    '''    public QueryHandler queryHandler()
    '''
def getStatisticsHandler():
    '''    public GraphStatisticsHandler getStatisticsHandler()
    '''
def getEventManager():
    '''    public GraphEventManager getEventManager()
    '''
def notifyAdd():
    '''    public void notifyAdd(final Triple t)
    '''
def notifyDelete():
    '''    public void notifyDelete(final Triple t)
    '''
def getTransactionHandler():
    '''    public TransactionHandler getTransactionHandler()
    '''
def getBulkUpdateHandler():
    '''    public BulkUpdateHandler getBulkUpdateHandler()
    '''
def getCapabilities():
    '''    public Capabilities getCapabilities()
    '''
def getPrefixMapping():
    '''    public PrefixMapping getPrefixMapping()
    '''
def add():
    '''    public void add(final Triple t)
    '''
def performAdd():
    '''    public void performAdd(final Triple t)
    '''
def delete():
    '''    public final void delete(final Triple t)
    '''
def performDelete():
    '''    public void performDelete(final Triple t)
    '''
def find():
    '''    public final ExtendedIterator<Triple> find(final TripleMatch m)
    public final ExtendedIterator<Triple> find(final Node s, final Node p, final Node o)
    '''
def forTestingOnly_graphBaseFind():
    '''    public ExtendedIterator<Triple> forTestingOnly_graphBaseFind(final TripleMatch tm)
    '''
def contains():
    '''    public final boolean contains(final Triple t)
    public final boolean contains(final Node s, final Node p, final Node o)
    '''
def getReifier():
    '''    public Reifier getReifier()
    '''
def size():
    '''    public final int size()
    '''
def isEmpty():
    '''    public boolean isEmpty()
    '''
def isIsomorphicWith():
    '''    public boolean isIsomorphicWith(final Graph g)
    '''
def toString():
    '''    public String toString()
    public static String toString(final String prefix, final Graph that)
    '''
