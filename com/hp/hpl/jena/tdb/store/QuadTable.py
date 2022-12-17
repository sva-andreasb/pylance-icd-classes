def ():
    '''returns QuadTable\n\n
    (final TupleIndex[] indexes, final NodeTable nodeTable)\n
    '''
def add():
    '''returns boolean\n\n
    add(final Quad quad)\n
    add(final Node gn, final Triple triple)\n
    add(final Node g, final Node s, final Node p, final Node o)\n
    '''
def delete():
    '''returns boolean\n\n
    delete(final Quad quad)\n
    delete(final Node gn, final Triple triple)\n
    delete(final Node g, final Node s, final Node p, final Node o)\n
    '''
def find():
    '''returns Iterator<Quad>\n\n
    find(final Node g, final Node s, final Node p, final Node o)\n
    '''
def getNodeTupleTable():
    '''returns NodeTupleTable\n\n
    getNodeTupleTable()\n
    '''
def sync():
    '''returns None\n\n
    sync()\n
    sync(final boolean force)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def clearQuads():
    '''returns None\n\n
    clearQuads()\n
    '''
def convert():
    '''returns Quad\n\n
    convert(final Tuple<Node> item)\n
    '''
