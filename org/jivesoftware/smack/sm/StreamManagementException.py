def StreamManagementException():
    '''public StreamManagementException()
    public StreamManagementException(final String message)
    '''
def StreamIdDoesNotMatchException():
    '''public StreamIdDoesNotMatchException(final String expected, final String got)
    '''
def StreamManagementCounterError():
    '''public StreamManagementCounterError(final long handledCount, final long previousServerHandlerCount, final long ackedStanzaCount, final List<Stanza> ackedStanzas)
    '''
def getHandledCount():
    '''public long getHandledCount()
    '''
def getPreviousServerHandledCount():
    '''public long getPreviousServerHandledCount()
    '''
def getAckedStanzaCount():
    '''public long getAckedStanzaCount()
    '''
def getOutstandingStanzasCount():
    '''public int getOutstandingStanzasCount()
    '''
def getAckedStanzas():
    '''public List<Stanza> getAckedStanzas()
    '''
def getOverflowElementNum():
    '''public int getOverflowElementNum()
    '''
def getDroppedElements():
    '''public int getDroppedElements()
    '''
def getElements():
    '''public List<Element> getElements()
    '''
def getUnacknowledgesStanzas():
    '''public List<Stanza> getUnacknowledgesStanzas()
    '''
def newWith():
    '''public static UnacknowledgedQueueFullException newWith(final int overflowElementNum, final List<Element> elements, final BlockingQueue<Stanza> unacknowledgedStanzas)
    '''
