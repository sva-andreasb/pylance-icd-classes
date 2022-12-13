def WrappedReifier():
    '''    public WrappedReifier(final Reifier base, final Graph parent)
    '''
def getStyle():
    '''    public ReificationStyle getStyle()
    '''
def getParentGraph():
    '''    public Graph getParentGraph()
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
def reifyAs():
    '''    public Node reifyAs(final Node n, final Triple t)
    '''
def hasTriple():
    '''    public boolean hasTriple(final Node n)
    public boolean hasTriple(final Triple t)
    '''
def allNodes():
    '''    public ExtendedIterator<Node> allNodes()
    public ExtendedIterator<Node> allNodes(final Triple t)
    '''
def remove():
    '''    public void remove(final Node n, final Triple t)
    public void remove(final Triple t)
    '''
def handledAdd():
    '''    public boolean handledAdd(final Triple t)
    '''
def handledRemove():
    '''    public boolean handledRemove(final Triple t)
    '''
def getTriple():
    '''    public Triple getTriple(final Node n)
    '''
def close():
    '''    public void close()
    '''
