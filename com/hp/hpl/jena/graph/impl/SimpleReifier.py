def SimpleReifier():
'''public SimpleReifier(final GraphBase parent, final ReificationStyle style)
public SimpleReifier(final GraphBase parent, final ReifierTripleMap tm, final ReifierFragmentsMap fm, final ReificationStyle style)
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
def getTriple():
'''public Triple getTriple(final Node n)
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
def clear():
'''public void clear()
'''
pass
def reifyAs():
'''public Node reifyAs(final Node tag, final Triple toReify)
'''
pass
def remove():
'''public void remove(final Node n, final Triple t)
public void remove(final Triple t)
'''
pass
def handledAdd():
'''public boolean handledAdd(final Triple fragment)
'''
pass
def handledRemove():
'''public boolean handledRemove(final Triple fragment)
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
def graphAddQuad():
'''public static void graphAddQuad(final GraphAdd g, final Node node, final Triple t)
'''
pass
def toString():
'''public String toString()
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
