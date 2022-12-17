def ():
    '''returns SimpleEventManager\n\n
    (final Graph graph)\n
    '''
def register():
    '''returns GraphEventManager\n\n
    register(final GraphListener listener)\n
    '''
def unregister():
    '''returns GraphEventManager\n\n
    unregister(final GraphListener listener)\n
    '''
def listening():
    '''returns boolean\n\n
    listening()\n
    '''
def notifyAddTriple():
    '''returns None\n\n
    notifyAddTriple(final Graph g, final Triple t)\n
    '''
def notifyAddArray():
    '''returns None\n\n
    notifyAddArray(final Graph g, final Triple[] ts)\n
    '''
def notifyAddList():
    '''returns None\n\n
    notifyAddList(final Graph g, final List<Triple> L)\n
    '''
def notifyAddIterator():
    '''returns None\n\n
    notifyAddIterator(final Graph g, final List<Triple> it)\n
    notifyAddIterator(final Graph g, final Iterator<Triple> it)\n
    '''
def notifyAddGraph():
    '''returns None\n\n
    notifyAddGraph(final Graph g, final Graph added)\n
    '''
def notifyDeleteTriple():
    '''returns None\n\n
    notifyDeleteTriple(final Graph g, final Triple t)\n
    '''
def notifyDeleteArray():
    '''returns None\n\n
    notifyDeleteArray(final Graph g, final Triple[] ts)\n
    '''
def notifyDeleteList():
    '''returns None\n\n
    notifyDeleteList(final Graph g, final List<Triple> L)\n
    '''
def notifyDeleteIterator():
    '''returns None\n\n
    notifyDeleteIterator(final Graph g, final List<Triple> L)\n
    notifyDeleteIterator(final Graph g, final Iterator<Triple> it)\n
    '''
def notifyDeleteGraph():
    '''returns None\n\n
    notifyDeleteGraph(final Graph g, final Graph removed)\n
    '''
def notifyEvent():
    '''returns None\n\n
    notifyEvent(final Graph source, final Object event)\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
