def ():
    '''returns ModelListenerAdapter\n\n
    (final ModelCom m, final ModelChangedListener L)\n
    '''
def notifyAddArray():
    '''returns None\n\n
    notifyAddArray(final Graph graph, final Triple[] triples)\n
    '''
def notifyDeleteArray():
    '''returns None\n\n
    notifyDeleteArray(final Graph g, final Triple[] triples)\n
    '''
def notifyAddTriple():
    '''returns None\n\n
    notifyAddTriple(final Graph g, final Triple t)\n
    '''
def notifyAddList():
    '''returns None\n\n
    notifyAddList(final Graph g, final List<Triple> triples)\n
    '''
def notifyAddIterator():
    '''returns None\n\n
    notifyAddIterator(final Graph g, final Iterator<Triple> it)\n
    notifyAddIterator(final Graph g, final List<Triple> triples)\n
    '''
def notifyAddGraph():
    '''returns None\n\n
    notifyAddGraph(final Graph g, final Graph added)\n
    '''
def notifyDeleteIterator():
    '''returns None\n\n
    notifyDeleteIterator(final Graph g, final Iterator<Triple> it)\n
    '''
def notifyDeleteTriple():
    '''returns None\n\n
    notifyDeleteTriple(final Graph g, final Triple t)\n
    '''
def notifyDeleteList():
    '''returns None\n\n
    notifyDeleteList(final Graph g, final List<Triple> triples)\n
    '''
def notifyDeleteGraph():
    '''returns None\n\n
    notifyDeleteGraph(final Graph g, final Graph removed)\n
    '''
def notifyEvent():
    '''returns None\n\n
    notifyEvent(final Graph g, final Object event)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def sameAs():
    '''returns boolean\n\n
    sameAs(final ModelListenerAdapter other)\n
    '''
