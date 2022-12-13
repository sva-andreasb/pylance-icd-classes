def SimpleEventManager():
'''public SimpleEventManager(final Graph graph)
'''
pass
def register():
'''public GraphEventManager register(final GraphListener listener)
'''
pass
def unregister():
'''public GraphEventManager unregister(final GraphListener listener)
'''
pass
def listening():
'''public boolean listening()
'''
pass
def notifyAddTriple():
'''public void notifyAddTriple(final Graph g, final Triple t)
'''
pass
def notifyAddArray():
'''public void notifyAddArray(final Graph g, final Triple[] ts)
'''
pass
def notifyAddList():
'''public void notifyAddList(final Graph g, final List<Triple> L)
'''
pass
def notifyAddIterator():
'''public void notifyAddIterator(final Graph g, final List<Triple> it)
public void notifyAddIterator(final Graph g, final Iterator<Triple> it)
'''
pass
def notifyAddGraph():
'''public void notifyAddGraph(final Graph g, final Graph added)
'''
pass
def notifyDeleteTriple():
'''public void notifyDeleteTriple(final Graph g, final Triple t)
'''
pass
def notifyDeleteArray():
'''public void notifyDeleteArray(final Graph g, final Triple[] ts)
'''
pass
def notifyDeleteList():
'''public void notifyDeleteList(final Graph g, final List<Triple> L)
'''
pass
def notifyDeleteIterator():
'''public void notifyDeleteIterator(final Graph g, final List<Triple> L)
public void notifyDeleteIterator(final Graph g, final Iterator<Triple> it)
'''
pass
def notifyDeleteGraph():
'''public void notifyDeleteGraph(final Graph g, final Graph removed)
'''
pass
def notifyEvent():
'''public void notifyEvent(final Graph source, final Object event)
'''
pass
def notifyingRemove():
'''public static ExtendedIterator<Triple> notifyingRemove(final Graph g, final Iterator<Triple> i)
'''
pass
def remove():
'''public void remove()
'''
pass
