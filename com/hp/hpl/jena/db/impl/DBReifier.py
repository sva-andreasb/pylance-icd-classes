def ():
    '''returns DBReifier\n\n
    (final GraphRDB parent, final ReificationStyle style, final List<SpecializedGraphReifier> allReifiers, final List<SpecializedGraphReifier> hiddenReifiers)\n
    '''
def getParentGraph():
    '''returns Graph\n\n
    getParentGraph()\n
    '''
def getStyle():
    '''returns ReificationStyle\n\n
    getStyle()\n
    '''
def find():
    '''returns ExtendedIterator<Triple>\n\n
    find(final TripleMatch m)\n
    '''
def findExposed():
    '''returns ExtendedIterator<Triple>\n\n
    findExposed(final TripleMatch m)\n
    '''
def findEither():
    '''returns ExtendedIterator<Triple>\n\n
    findEither(final TripleMatch m, final boolean showHidden)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def reifyAs():
    '''returns Node\n\n
    reifyAs(final Node n, final Triple t)\n
    '''
def hasTriple():
    '''returns boolean\n\n
    hasTriple(final Node n)\n
    hasTriple(final Triple t)\n
    '''
def allNodes():
    '''returns ExtendedIterator<Node>\n\n
    allNodes()\n
    allNodes(final Triple t)\n
    '''
def remove():
    '''returns None\n\n
    remove(final Node n, final Triple t)\n
    remove(final Triple t)\n
    '''
def handledAdd():
    '''returns boolean\n\n
    handledAdd(final Triple t)\n
    '''
def handledRemove():
    '''returns boolean\n\n
    handledRemove(final Triple t)\n
    '''
def getTriple():
    '''returns Triple\n\n
    getTriple(final Node n)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
