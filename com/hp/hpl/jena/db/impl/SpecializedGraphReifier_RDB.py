def SpecializedGraphReifier_RDB():
    '''    public SpecializedGraphReifier_RDB(final IPSet pSet, final Integer dbGraphID)
    '''
def add():
    '''    public void add(final Node n, final Triple t, final SpecializedGraph.CompletionFlag complete)
    public void add(final Graph g, final SpecializedGraph.CompletionFlag complete)
    public void add(final Triple frag, final SpecializedGraph.CompletionFlag complete)
    public void add(final List<Triple> triples, final SpecializedGraph.CompletionFlag complete)
    '''
def delete():
    '''    public void delete(final Node n, final Triple t, final SpecializedGraph.CompletionFlag complete)
    public void delete(final Triple frag, final SpecializedGraph.CompletionFlag complete)
    public void delete(final List<Triple> triples, final SpecializedGraph.CompletionFlag complete)
    '''
def contains():
    '''    public boolean contains(final Node n, final Triple t, final SpecializedGraph.CompletionFlag complete)
    public boolean contains(final Triple t, final SpecializedGraph.CompletionFlag complete)
    '''
def findReifiedNodes():
    '''    public ExtendedIterator<Node> findReifiedNodes(final Triple t, final SpecializedGraph.CompletionFlag complete)
    '''
def findReifiedTriple():
    '''    public Triple findReifiedTriple(final Node n, final SpecializedGraph.CompletionFlag complete)
    '''
def findReifiedTriples():
    '''    public ExtendedIterator<Triple> findReifiedTriples(final Node n, final SpecializedGraph.CompletionFlag complete)
    '''
def tripleCount():
    '''    public int tripleCount()
    '''
def find():
    '''    public ExtendedIterator<Triple> find(final TripleMatch t, final SpecializedGraph.CompletionFlag complete)
    '''
def close():
    '''    public void close()
    '''
def clear():
    '''    public void clear()
    '''
def getGraphId():
    '''    public int getGraphId()
    '''
def getPSet():
    '''    public IPSet getPSet()
    '''
def getDBPropLSet():
    '''    public DBPropLSet getDBPropLSet()
    '''
def subsumes():
    '''    public char subsumes(final Triple pattern, final int reifBehavior)
    '''
