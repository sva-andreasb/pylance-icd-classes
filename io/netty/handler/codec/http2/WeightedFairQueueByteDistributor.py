def ():
    '''returns WeightedFairQueueByteDistributor\n\n
    (final Http2Connection connection)\n
    (final Http2Connection connection, final int maxStateOnlySize)\n
    '''
def onStreamAdded():
    '''returns None\n\n
    onStreamAdded(final Http2Stream stream)\n
    '''
def onStreamActive():
    '''returns None\n\n
    onStreamActive(final Http2Stream stream)\n
    '''
def onStreamClosed():
    '''returns None\n\n
    onStreamClosed(final Http2Stream stream)\n
    '''
def onStreamRemoved():
    '''returns None\n\n
    onStreamRemoved(final Http2Stream stream)\n
    '''
def updateStreamableBytes():
    '''returns None\n\n
    updateStreamableBytes(final StreamState state)\n
    '''
def updateDependencyTree():
    '''returns None\n\n
    updateDependencyTree(final int childStreamId, final int parentStreamId, final short weight, final boolean exclusive)\n
    '''
def distribute():
    '''returns boolean\n\n
    distribute(int maxBytes, final Writer writer)\n
    '''
def allocationQuantum():
    '''returns None\n\n
    allocationQuantum(final int allocationQuantum)\n
    '''
def compare():
    '''returns int\n\n
    compare(final State o1, final State o2)\n
    compare(final State o1, final State o2)\n
    '''
def priorityQueueIndex():
    '''returns None\n\n
    priorityQueueIndex(final DefaultPriorityQueue<?> queue)\n
    priorityQueueIndex(final DefaultPriorityQueue<?> queue, final int i)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
