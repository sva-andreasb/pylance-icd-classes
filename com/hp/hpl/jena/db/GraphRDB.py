DEFAULT = "String  \"DEFAULT\""
OPTIMIZE_ALL_REIFICATIONS_AND_HIDE_NOTHING = "int  1"
OPTIMIZE_AND_HIDE_FULL_AND_PARTIAL_REIFICATIONS = "int  2"
OPTIMIZE_AND_HIDE_ONLY_FULL_REIFICATIONS = "int  3"
def styleRDB():
    '''    public static int styleRDB(final ReificationStyle style)
    public static ReificationStyle styleRDB(final int behaviour)
    '''
def GraphRDB():
    '''    public GraphRDB(final IDBConnection con, String graphID, final Graph requestedProperties, final int reificationBehaviour, final boolean isNew)
    '''
def getCapabilities():
    '''    public Capabilities getCapabilities()
    '''
def handlesLiteralTyping():
    '''    public boolean handlesLiteralTyping()
    '''
def getNode():
    '''    public Node getNode()
    '''
def getPropertyTriples():
    '''    public ExtendedIterator<Triple> getPropertyTriples()
    '''
def isClosed():
    '''    public boolean isClosed()
    '''
def performAdd():
    '''    public void performAdd(final Triple t)
    '''
def add():
    '''    public void add(final List<Triple> triples)
    '''
def performDelete():
    '''    public void performDelete(final Triple t)
    '''
def delete():
    '''    public void delete(final List<Triple> triples)
    '''
def graphBaseSize():
    '''    public int graphBaseSize()
    '''
def graphBaseContains():
    '''    public boolean graphBaseContains(final Triple t)
    '''
def graphBaseFind():
    '''    public ExtendedIterator<Triple> graphBaseFind(final TripleMatch m)
    '''
def reifierTriples():
    '''    public ExtendedIterator<Triple> reifierTriples(final TripleMatch m)
    '''
def reifierSize():
    '''    public int reifierSize()
    '''
def getBulkUpdateHandler():
    '''    public BulkUpdateHandler getBulkUpdateHandler()
    '''
def getReifier():
    '''    public Reifier getReifier()
    '''
def getPrefixMapping():
    '''    public PrefixMapping getPrefixMapping()
    '''
def getTransactionHandler():
    '''    public TransactionHandler getTransactionHandler()
    '''
def close():
    '''    public synchronized void close()
    '''
def remove():
    '''    public synchronized void remove()
    '''
def clear():
    '''    public synchronized void clear()
    '''
def getConnection():
    '''    public IDBConnection getConnection()
    '''
def reificationBehavior():
    '''    public int reificationBehavior()
    '''
def getSpecializedGraphs():
    '''    public Iterator<SpecializedGraph> getSpecializedGraphs()
    '''
def queryHandler():
    '''    public QueryHandler queryHandler()
    '''
def DBqueryHandler():
    '''    public DBQueryHandler DBqueryHandler()
    '''
def getDoDuplicateCheck():
    '''    public boolean getDoDuplicateCheck()
    '''
def setDoDuplicateCheck():
    '''    public void setDoDuplicateCheck(final boolean bool)
    '''
def setDoFastpath():
    '''    public void setDoFastpath(final boolean val)
    '''
def getDoFastpath():
    '''    public boolean getDoFastpath()
    '''
def setQueryOnlyAsserted():
    '''    public void setQueryOnlyAsserted(final boolean opt)
    '''
def getQueryOnlyAsserted():
    '''    public boolean getQueryOnlyAsserted()
    '''
def setQueryOnlyReified():
    '''    public void setQueryOnlyReified(final boolean opt)
    '''
def getQueryOnlyReified():
    '''    public boolean getQueryOnlyReified()
    '''
def setQueryFullReified():
    '''    public void setQueryFullReified(final boolean opt)
    '''
def getQueryFullReified():
    '''    public boolean getQueryFullReified()
    '''
def setDoImplicitJoin():
    '''    public void setDoImplicitJoin(final boolean val)
    '''
