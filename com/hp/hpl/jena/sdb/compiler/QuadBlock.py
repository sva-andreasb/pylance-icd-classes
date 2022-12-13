def QuadBlock():
    '''    public QuadBlock()
    public QuadBlock(final QuadBlock other)
    public QuadBlock(final OpQuadPattern quadPattern)
    '''
def clone():
    '''    public QuadBlock clone()
    '''
def asArray():
    '''    public Quad[] asArray()
    '''
def getGraphNode():
    '''    public Node getGraphNode()
    '''
def contains():
    '''    public boolean contains(final Quad pattern)
    public boolean contains(final Node g, final Node s, final Node p, final Node o)
    '''
def findFirst():
    '''    public int findFirst(final Quad pattern)
    public int findFirst(final Node g, final Node s, final Node p, final Node o)
    public int findFirst(final int start, final Quad pattern)
    public int findFirst(final int start, Node g, Node s, Node p, Node o)
    '''
def subBlock():
    '''    public QuadBlock subBlock(final int fromIndex, final int toIndex)
    public QuadBlock subBlock(final int fromIndex)
    '''
def find():
    '''    public Iterable<Quad> find(final Quad pattern)
    public Iterable<Quad> find(Node g, Node s, Node p, Node o)
    '''
def toString():
    '''    public String toString()
    public String toString(final PrefixMapping prefixMapping)
    '''
def output():
    '''    public void output(final IndentedWriter out, final SerializationContext sCxt)
    public void output(final IndentedWriter out)
    '''
def apply():
    '''    public void apply(final Quad quad)
    '''
