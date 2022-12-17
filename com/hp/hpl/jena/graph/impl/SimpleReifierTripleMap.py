def ():
    '''returns SimpleReifierTripleMap\n\n
    ()\n
    '''
def getTriple():
    '''returns Triple\n\n
    getTriple(final Node tag)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def hasTriple():
    '''returns boolean\n\n
    hasTriple(final Triple t)\n
    '''
def putTriple():
    '''returns Triple\n\n
    putTriple(final Node key, final Triple value)\n
    '''
def removeTriple():
    '''returns None\n\n
    removeTriple(final Node key)\n
    removeTriple(final Node key, final Triple value)\n
    removeTriple(final Triple t)\n
    '''
def tagIterator():
    '''returns ExtendedIterator<Node>\n\n
    tagIterator(final Triple t)\n
    tagIterator()\n
    '''
def fill():
    '''returns None\n\n
    fill(final GraphAdd ga, final Node n, final Triple t)\n
    '''
def asGraph():
    '''returns Graph\n\n
    asGraph()\n
    '''
def graphBaseFind():
    '''returns ExtendedIterator<Triple>\n\n
    graphBaseFind(final TripleMatch tm)\n
    '''
def find():
    '''returns ExtendedIterator<Triple>\n\n
    find(final TripleMatch m)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
