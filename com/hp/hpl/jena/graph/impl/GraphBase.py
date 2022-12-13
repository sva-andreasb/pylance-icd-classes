TOSTRING_TRIPLE_BASE = "int  10"
TOSTRING_TRIPLE_LIMIT = "int  17"
def GraphBase():
'''public GraphBase()
public GraphBase(final ReificationStyle style)
'''
pass
def close():
'''public void close()
'''
pass
def isClosed():
'''public boolean isClosed()
'''
pass
def dependsOn():
'''public boolean dependsOn(final Graph other)
'''
pass
def queryHandler():
'''public QueryHandler queryHandler()
'''
pass
def getStatisticsHandler():
'''public GraphStatisticsHandler getStatisticsHandler()
'''
pass
def getEventManager():
'''public GraphEventManager getEventManager()
'''
pass
def notifyAdd():
'''public void notifyAdd(final Triple t)
'''
pass
def notifyDelete():
'''public void notifyDelete(final Triple t)
'''
pass
def getTransactionHandler():
'''public TransactionHandler getTransactionHandler()
'''
pass
def getBulkUpdateHandler():
'''public BulkUpdateHandler getBulkUpdateHandler()
'''
pass
def getCapabilities():
'''public Capabilities getCapabilities()
'''
pass
def getPrefixMapping():
'''public PrefixMapping getPrefixMapping()
'''
pass
def add():
'''public void add(final Triple t)
'''
pass
def performAdd():
'''public void performAdd(final Triple t)
'''
pass
def delete():
'''public final void delete(final Triple t)
'''
pass
def performDelete():
'''public void performDelete(final Triple t)
'''
pass
def find():
'''public final ExtendedIterator<Triple> find(final TripleMatch m)
public final ExtendedIterator<Triple> find(final Node s, final Node p, final Node o)
'''
pass
def forTestingOnly_graphBaseFind():
'''public ExtendedIterator<Triple> forTestingOnly_graphBaseFind(final TripleMatch tm)
'''
pass
def contains():
'''public final boolean contains(final Triple t)
public final boolean contains(final Node s, final Node p, final Node o)
'''
pass
def getReifier():
'''public Reifier getReifier()
'''
pass
def size():
'''public final int size()
'''
pass
def isEmpty():
'''public boolean isEmpty()
'''
pass
def isIsomorphicWith():
'''public boolean isIsomorphicWith(final Graph g)
'''
pass
def toString():
'''public String toString()
public static String toString(final String prefix, final Graph that)
'''
pass
