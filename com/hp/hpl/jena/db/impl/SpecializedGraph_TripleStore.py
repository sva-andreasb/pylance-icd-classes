def SpecializedGraph_TripleStore():
    '''    public SpecializedGraph_TripleStore(final IPSet pSet, final Integer dbGraphID)
    '''
def add():
    '''    public void add(final Graph g, final SpecializedGraph.CompletionFlag complete)
    public void add(final Triple t, final SpecializedGraph.CompletionFlag complete)
    public void add(final List<Triple> triples, final SpecializedGraph.CompletionFlag complete)
    '''
def delete():
    '''    public void delete(final Triple t, final SpecializedGraph.CompletionFlag complete)
    public void delete(final List<Triple> triples, final SpecializedGraph.CompletionFlag complete)
    '''
def tripleCount():
    '''    public int tripleCount()
    '''
def contains():
    '''    public boolean contains(final Triple t, final SpecializedGraph.CompletionFlag complete)
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
