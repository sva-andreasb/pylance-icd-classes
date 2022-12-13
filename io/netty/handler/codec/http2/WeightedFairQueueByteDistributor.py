def WeightedFairQueueByteDistributor():
    '''public WeightedFairQueueByteDistributor(final Http2Connection connection)
    public WeightedFairQueueByteDistributor(final Http2Connection connection, final int maxStateOnlySize)
    '''
def onStreamAdded():
    '''public void onStreamAdded(final Http2Stream stream)
    '''
def onStreamActive():
    '''public void onStreamActive(final Http2Stream stream)
    '''
def onStreamClosed():
    '''public void onStreamClosed(final Http2Stream stream)
    '''
def onStreamRemoved():
    '''public void onStreamRemoved(final Http2Stream stream)
    '''
def updateStreamableBytes():
    '''public void updateStreamableBytes(final StreamState state)
    '''
def updateDependencyTree():
    '''public void updateDependencyTree(final int childStreamId, final int parentStreamId, final short weight, final boolean exclusive)
    '''
def distribute():
    '''public boolean distribute(int maxBytes, final Writer writer)
    '''
def allocationQuantum():
    '''public void allocationQuantum(final int allocationQuantum)
    '''
def compare():
    '''public int compare(final State o1, final State o2)
    public int compare(final State o1, final State o2)
    '''
def priorityQueueIndex():
    '''public int priorityQueueIndex(final DefaultPriorityQueue<?> queue)
    public void priorityQueueIndex(final DefaultPriorityQueue<?> queue, final int i)
    '''
def toString():
    '''public String toString()
    '''
