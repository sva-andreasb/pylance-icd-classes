def SpecializedGraphReifier_RDB():
'''public SpecializedGraphReifier_RDB(final IPSet pSet, final Integer dbGraphID)
'''
pass
def add():
'''public void add(final Node n, final Triple t, final SpecializedGraph.CompletionFlag complete)
public void add(final Graph g, final SpecializedGraph.CompletionFlag complete)
public void add(final Triple frag, final SpecializedGraph.CompletionFlag complete)
public void add(final List<Triple> triples, final SpecializedGraph.CompletionFlag complete)
'''
pass
def delete():
'''public void delete(final Node n, final Triple t, final SpecializedGraph.CompletionFlag complete)
public void delete(final Triple frag, final SpecializedGraph.CompletionFlag complete)
public void delete(final List<Triple> triples, final SpecializedGraph.CompletionFlag complete)
'''
pass
def contains():
'''public boolean contains(final Node n, final Triple t, final SpecializedGraph.CompletionFlag complete)
public boolean contains(final Triple t, final SpecializedGraph.CompletionFlag complete)
'''
pass
def findReifiedNodes():
'''public ExtendedIterator<Node> findReifiedNodes(final Triple t, final SpecializedGraph.CompletionFlag complete)
'''
pass
def findReifiedTriple():
'''public Triple findReifiedTriple(final Node n, final SpecializedGraph.CompletionFlag complete)
'''
pass
def findReifiedTriples():
'''public ExtendedIterator<Triple> findReifiedTriples(final Node n, final SpecializedGraph.CompletionFlag complete)
'''
pass
def tripleCount():
'''public int tripleCount()
'''
pass
def find():
'''public ExtendedIterator<Triple> find(final TripleMatch t, final SpecializedGraph.CompletionFlag complete)
'''
pass
def close():
'''public void close()
'''
pass
def clear():
'''public void clear()
'''
pass
def getGraphId():
'''public int getGraphId()
'''
pass
def getPSet():
'''public IPSet getPSet()
'''
pass
def getDBPropLSet():
'''public DBPropLSet getDBPropLSet()
'''
pass
def subsumes():
'''public char subsumes(final Triple pattern, final int reifBehavior)
'''
pass
