def ():
    '''returns TripleTable\n\n
    (final TupleIndex[] indexes, final NodeTable nodeTable)\n
    '''
def add():
    '''returns boolean\n\n
    add(final Triple triple)\n
    add(final Node s, final Node p, final Node o)\n
    '''
def delete():
    '''returns boolean\n\n
    delete(final Triple triple)\n
    delete(final Node s, final Node p, final Node o)\n
    '''
def find():
    '''returns Iterator<Triple>\n\n
    find(final Node s, final Node p, final Node o)\n
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
def close():
    '''returns None\n\n
    close()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def clearTriples():
    '''returns None\n\n
    clearTriples()\n
    '''
def convert():
    '''returns Triple\n\n
    convert(final Tuple<Node> item)\n
    '''
