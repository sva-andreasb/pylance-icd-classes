def StreamManagementException():
'''public StreamManagementException()
public StreamManagementException(final String message)
'''
pass
def StreamIdDoesNotMatchException():
'''public StreamIdDoesNotMatchException(final String expected, final String got)
'''
pass
def StreamManagementCounterError():
'''public StreamManagementCounterError(final long handledCount, final long previousServerHandlerCount, final long ackedStanzaCount, final List<Stanza> ackedStanzas)
'''
pass
def getHandledCount():
'''public long getHandledCount()
'''
pass
def getPreviousServerHandledCount():
'''public long getPreviousServerHandledCount()
'''
pass
def getAckedStanzaCount():
'''public long getAckedStanzaCount()
'''
pass
def getOutstandingStanzasCount():
'''public int getOutstandingStanzasCount()
'''
pass
def getAckedStanzas():
'''public List<Stanza> getAckedStanzas()
'''
pass
def getOverflowElementNum():
'''public int getOverflowElementNum()
'''
pass
def getDroppedElements():
'''public int getDroppedElements()
'''
pass
def getElements():
'''public List<Element> getElements()
'''
pass
def getUnacknowledgesStanzas():
'''public List<Stanza> getUnacknowledgesStanzas()
'''
pass
def newWith():
'''public static UnacknowledgedQueueFullException newWith(final int overflowElementNum, final List<Element> elements, final BlockingQueue<Stanza> unacknowledgedStanzas)
'''
pass
