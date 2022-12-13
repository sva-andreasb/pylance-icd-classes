def SimpleReifier():
    '''    public SimpleReifier(final GraphBase parent, final ReificationStyle style)
    public SimpleReifier(final GraphBase parent, final ReifierTripleMap tm, final ReifierFragmentsMap fm, final ReificationStyle style)
    '''
def getStyle():
    '''    public ReificationStyle getStyle()
    '''
def getParentGraph():
    '''    public Graph getParentGraph()
    '''
def getTriple():
    '''    public Triple getTriple(final Node n)
    '''
def hasTriple():
    '''    public boolean hasTriple(final Node n)
    public boolean hasTriple(final Triple t)
    '''
def allNodes():
    '''    public ExtendedIterator<Node> allNodes()
    public ExtendedIterator<Node> allNodes(final Triple t)
    '''
def clear():
    '''    public void clear()
    '''
def reifyAs():
    '''    public Node reifyAs(final Node tag, final Triple toReify)
    '''
def remove():
    '''    public void remove(final Node n, final Triple t)
    public void remove(final Triple t)
    '''
def handledAdd():
    '''    public boolean handledAdd(final Triple fragment)
    '''
def handledRemove():
    '''    public boolean handledRemove(final Triple fragment)
    '''
def find():
    '''    public ExtendedIterator<Triple> find(final TripleMatch m)
    '''
def findExposed():
    '''    public ExtendedIterator<Triple> findExposed(final TripleMatch m)
    '''
def findEither():
    '''    public ExtendedIterator<Triple> findEither(final TripleMatch m, final boolean showHidden)
    '''
def size():
    '''    public int size()
    '''
def graphAddQuad():
    '''    public static void graphAddQuad(final GraphAdd g, final Node node, final Triple t)
    '''
def toString():
    '''    public String toString()
    '''
def close():
    '''    public void close()
    '''
def isClosed():
    '''    public boolean isClosed()
    '''
