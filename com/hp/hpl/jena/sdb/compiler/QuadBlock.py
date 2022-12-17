def ():
    '''returns QuadBlock\n\n
    ()\n
    (final QuadBlock other)\n
    (final OpQuadPattern quadPattern)\n
    '''
def clone():
    '''returns QuadBlock\n\n
    clone()\n
    '''
def asArray():
    '''returns Quad[]\n\n
    asArray()\n
    '''
def getGraphNode():
    '''returns Node\n\n
    getGraphNode()\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final Quad pattern)\n
    contains(final Node g, final Node s, final Node p, final Node o)\n
    '''
def findFirst():
    '''returns int\n\n
    findFirst(final Quad pattern)\n
    findFirst(final Node g, final Node s, final Node p, final Node o)\n
    findFirst(final int start, final Quad pattern)\n
    findFirst(final int start, Node g, Node s, Node p, Node o)\n
    '''
def subBlock():
    '''returns QuadBlock\n\n
    subBlock(final int fromIndex, final int toIndex)\n
    subBlock(final int fromIndex)\n
    '''
def find():
    '''returns Iterable<Quad>\n\n
    find(final Quad pattern)\n
    find(Node g, Node s, Node p, Node o)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString(final PrefixMapping prefixMapping)\n
    '''
def output():
    '''returns None\n\n
    output(final IndentedWriter out, final SerializationContext sCxt)\n
    output(final IndentedWriter out)\n
    '''
def apply():
    '''returns None\n\n
    apply(final Quad quad)\n
    '''
