def WrappedReifier():
'''public WrappedReifier(final Reifier base, final Graph parent)
'''
pass
def getStyle():
'''public ReificationStyle getStyle()
'''
pass
def getParentGraph():
'''public Graph getParentGraph()
'''
pass
def find():
'''public ExtendedIterator<Triple> find(final TripleMatch m)
'''
pass
def findExposed():
'''public ExtendedIterator<Triple> findExposed(final TripleMatch m)
'''
pass
def findEither():
'''public ExtendedIterator<Triple> findEither(final TripleMatch m, final boolean showHidden)
'''
pass
def size():
'''public int size()
'''
pass
def reifyAs():
'''public Node reifyAs(final Node n, final Triple t)
'''
pass
def hasTriple():
'''public boolean hasTriple(final Node n)
public boolean hasTriple(final Triple t)
'''
pass
def allNodes():
'''public ExtendedIterator<Node> allNodes()
public ExtendedIterator<Node> allNodes(final Triple t)
'''
pass
def remove():
'''public void remove(final Node n, final Triple t)
public void remove(final Triple t)
'''
pass
def handledAdd():
'''public boolean handledAdd(final Triple t)
'''
pass
def handledRemove():
'''public boolean handledRemove(final Triple t)
'''
pass
def getTriple():
'''public Triple getTriple(final Node n)
'''
pass
def close():
'''public void close()
'''
pass
