def SimpleReifierTripleMap():
    '''public SimpleReifierTripleMap()
    '''
def getTriple():
    '''public Triple getTriple(final Node tag)
    '''
def clear():
    '''public void clear()
    '''
def hasTriple():
    '''public boolean hasTriple(final Triple t)
    '''
def putTriple():
    '''public Triple putTriple(final Node key, final Triple value)
    '''
def removeTriple():
    '''public void removeTriple(final Node key)
    public void removeTriple(final Node key, final Triple value)
    public void removeTriple(final Triple t)
    '''
def tagIterator():
    '''public ExtendedIterator<Node> tagIterator(final Triple t)
    public ExtendedIterator<Node> tagIterator()
    '''
def fill():
    '''public void fill(final GraphAdd ga, final Node n, final Triple t)
    '''
def explodeTriple():
    '''public static ExtendedIterator<Triple> explodeTriple(final Triple pattern, final Node tag, final Triple toExplode)
    '''
def asGraph():
    '''public Graph asGraph()
    '''
def graphBaseFind():
    '''public ExtendedIterator<Triple> graphBaseFind(final TripleMatch tm)
    '''
def find():
    '''public ExtendedIterator<Triple> find(final TripleMatch m)
    '''
def size():
    '''public int size()
    '''
