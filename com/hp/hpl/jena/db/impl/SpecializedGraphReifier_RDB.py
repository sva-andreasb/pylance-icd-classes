def ():
    '''returns SpecializedGraphReifier_RDB\n\n
    (final IPSet pSet, final Integer dbGraphID)\n
    '''
def add():
    '''returns None\n\n
    add(final Node n, final Triple t, final SpecializedGraph.CompletionFlag complete)\n
    add(final Graph g, final SpecializedGraph.CompletionFlag complete)\n
    add(final Triple frag, final SpecializedGraph.CompletionFlag complete)\n
    add(final List<Triple> triples, final SpecializedGraph.CompletionFlag complete)\n
    '''
def delete():
    '''returns None\n\n
    delete(final Node n, final Triple t, final SpecializedGraph.CompletionFlag complete)\n
    delete(final Triple frag, final SpecializedGraph.CompletionFlag complete)\n
    delete(final List<Triple> triples, final SpecializedGraph.CompletionFlag complete)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final Node n, final Triple t, final SpecializedGraph.CompletionFlag complete)\n
    contains(final Triple t, final SpecializedGraph.CompletionFlag complete)\n
    '''
def findReifiedNodes():
    '''returns ExtendedIterator<Node>\n\n
    findReifiedNodes(final Triple t, final SpecializedGraph.CompletionFlag complete)\n
    '''
def findReifiedTriple():
    '''returns Triple\n\n
    findReifiedTriple(final Node n, final SpecializedGraph.CompletionFlag complete)\n
    '''
def findReifiedTriples():
    '''returns ExtendedIterator<Triple>\n\n
    findReifiedTriples(final Node n, final SpecializedGraph.CompletionFlag complete)\n
    '''
def tripleCount():
    '''returns int\n\n
    tripleCount()\n
    '''
def find():
    '''returns ExtendedIterator<Triple>\n\n
    find(final TripleMatch t, final SpecializedGraph.CompletionFlag complete)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def getGraphId():
    '''returns int\n\n
    getGraphId()\n
    '''
def getPSet():
    '''returns IPSet\n\n
    getPSet()\n
    '''
def getDBPropLSet():
    '''returns DBPropLSet\n\n
    getDBPropLSet()\n
    '''
def subsumes():
    '''returns char\n\n
    subsumes(final Triple pattern, final int reifBehavior)\n
    '''
