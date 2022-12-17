def ():
    '''returns SpecializedGraph_TripleStore\n\n
    (final IPSet pSet, final Integer dbGraphID)\n
    '''
def add():
    '''returns None\n\n
    add(final Graph g, final SpecializedGraph.CompletionFlag complete)\n
    add(final Triple t, final SpecializedGraph.CompletionFlag complete)\n
    add(final List<Triple> triples, final SpecializedGraph.CompletionFlag complete)\n
    '''
def delete():
    '''returns None\n\n
    delete(final Triple t, final SpecializedGraph.CompletionFlag complete)\n
    delete(final List<Triple> triples, final SpecializedGraph.CompletionFlag complete)\n
    '''
def tripleCount():
    '''returns int\n\n
    tripleCount()\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final Triple t, final SpecializedGraph.CompletionFlag complete)\n
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
