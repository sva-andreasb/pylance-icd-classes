def SimpleEventManager():
    '''public SimpleEventManager(final Graph graph)
    '''
def register():
    '''public GraphEventManager register(final GraphListener listener)
    '''
def unregister():
    '''public GraphEventManager unregister(final GraphListener listener)
    '''
def listening():
    '''public boolean listening()
    '''
def notifyAddTriple():
    '''public void notifyAddTriple(final Graph g, final Triple t)
    '''
def notifyAddArray():
    '''public void notifyAddArray(final Graph g, final Triple[] ts)
    '''
def notifyAddList():
    '''public void notifyAddList(final Graph g, final List<Triple> L)
    '''
def notifyAddIterator():
    '''public void notifyAddIterator(final Graph g, final List<Triple> it)
    public void notifyAddIterator(final Graph g, final Iterator<Triple> it)
    '''
def notifyAddGraph():
    '''public void notifyAddGraph(final Graph g, final Graph added)
    '''
def notifyDeleteTriple():
    '''public void notifyDeleteTriple(final Graph g, final Triple t)
    '''
def notifyDeleteArray():
    '''public void notifyDeleteArray(final Graph g, final Triple[] ts)
    '''
def notifyDeleteList():
    '''public void notifyDeleteList(final Graph g, final List<Triple> L)
    '''
def notifyDeleteIterator():
    '''public void notifyDeleteIterator(final Graph g, final List<Triple> L)
    public void notifyDeleteIterator(final Graph g, final Iterator<Triple> it)
    '''
def notifyDeleteGraph():
    '''public void notifyDeleteGraph(final Graph g, final Graph removed)
    '''
def notifyEvent():
    '''public void notifyEvent(final Graph source, final Object event)
    '''
def notifyingRemove():
    '''public static ExtendedIterator<Triple> notifyingRemove(final Graph g, final Iterator<Triple> i)
    '''
def remove():
    '''public void remove()
    '''
