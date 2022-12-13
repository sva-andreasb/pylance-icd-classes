DEFAULT = "String  DEFAULT""
OPTIMIZE_ALL_REIFICATIONS_AND_HIDE_NOTHING = "int  1"
OPTIMIZE_AND_HIDE_FULL_AND_PARTIAL_REIFICATIONS = "int  2"
OPTIMIZE_AND_HIDE_ONLY_FULL_REIFICATIONS = "int  3"
def styleRDB():
'''public static int styleRDB(final ReificationStyle style)
public static ReificationStyle styleRDB(final int behaviour)
'''
pass
def GraphRDB():
'''public GraphRDB(final IDBConnection con, String graphID, final Graph requestedProperties, final int reificationBehaviour, final boolean isNew)
'''
pass
def getCapabilities():
'''public Capabilities getCapabilities()
'''
pass
def handlesLiteralTyping():
'''public boolean handlesLiteralTyping()
'''
pass
def getNode():
'''public Node getNode()
'''
pass
def getPropertyTriples():
'''public ExtendedIterator<Triple> getPropertyTriples()
'''
pass
def isClosed():
'''public boolean isClosed()
'''
pass
def performAdd():
'''public void performAdd(final Triple t)
'''
pass
def add():
'''public void add(final List<Triple> triples)
'''
pass
def performDelete():
'''public void performDelete(final Triple t)
'''
pass
def delete():
'''public void delete(final List<Triple> triples)
'''
pass
def graphBaseSize():
'''public int graphBaseSize()
'''
pass
def graphBaseContains():
'''public boolean graphBaseContains(final Triple t)
'''
pass
def graphBaseFind():
'''public ExtendedIterator<Triple> graphBaseFind(final TripleMatch m)
'''
pass
def reifierTriples():
'''public ExtendedIterator<Triple> reifierTriples(final TripleMatch m)
'''
pass
def reifierSize():
'''public int reifierSize()
'''
pass
def getBulkUpdateHandler():
'''public BulkUpdateHandler getBulkUpdateHandler()
'''
pass
def getReifier():
'''public Reifier getReifier()
'''
pass
def getPrefixMapping():
'''public PrefixMapping getPrefixMapping()
'''
pass
def getTransactionHandler():
'''public TransactionHandler getTransactionHandler()
'''
pass
def close():
'''public synchronized void close()
'''
pass
def remove():
'''public synchronized void remove()
'''
pass
def clear():
'''public synchronized void clear()
'''
pass
def getConnection():
'''public IDBConnection getConnection()
'''
pass
def reificationBehavior():
'''public int reificationBehavior()
'''
pass
def getSpecializedGraphs():
'''public Iterator<SpecializedGraph> getSpecializedGraphs()
'''
pass
def queryHandler():
'''public QueryHandler queryHandler()
'''
pass
def DBqueryHandler():
'''public DBQueryHandler DBqueryHandler()
'''
pass
def getDoDuplicateCheck():
'''public boolean getDoDuplicateCheck()
'''
pass
def setDoDuplicateCheck():
'''public void setDoDuplicateCheck(final boolean bool)
'''
pass
def setDoFastpath():
'''public void setDoFastpath(final boolean val)
'''
pass
def getDoFastpath():
'''public boolean getDoFastpath()
'''
pass
def setQueryOnlyAsserted():
'''public void setQueryOnlyAsserted(final boolean opt)
'''
pass
def getQueryOnlyAsserted():
'''public boolean getQueryOnlyAsserted()
'''
pass
def setQueryOnlyReified():
'''public void setQueryOnlyReified(final boolean opt)
'''
pass
def getQueryOnlyReified():
'''public boolean getQueryOnlyReified()
'''
pass
def setQueryFullReified():
'''public void setQueryFullReified(final boolean opt)
'''
pass
def getQueryFullReified():
'''public boolean getQueryFullReified()
'''
pass
def setDoImplicitJoin():
'''public void setDoImplicitJoin(final boolean val)
'''
pass
