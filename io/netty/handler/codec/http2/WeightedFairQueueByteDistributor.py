def WeightedFairQueueByteDistributor():
'''public WeightedFairQueueByteDistributor(final Http2Connection connection)
public WeightedFairQueueByteDistributor(final Http2Connection connection, final int maxStateOnlySize)
'''
pass
def onStreamAdded():
'''public void onStreamAdded(final Http2Stream stream)
'''
pass
def onStreamActive():
'''public void onStreamActive(final Http2Stream stream)
'''
pass
def onStreamClosed():
'''public void onStreamClosed(final Http2Stream stream)
'''
pass
def onStreamRemoved():
'''public void onStreamRemoved(final Http2Stream stream)
'''
pass
def updateStreamableBytes():
'''public void updateStreamableBytes(final StreamState state)
'''
pass
def updateDependencyTree():
'''public void updateDependencyTree(final int childStreamId, final int parentStreamId, final short weight, final boolean exclusive)
'''
pass
def distribute():
'''public boolean distribute(int maxBytes, final Writer writer)
'''
pass
def allocationQuantum():
'''public void allocationQuantum(final int allocationQuantum)
'''
pass
def compare():
'''public int compare(final State o1, final State o2)
public int compare(final State o1, final State o2)
'''
pass
def priorityQueueIndex():
'''public int priorityQueueIndex(final DefaultPriorityQueue<?> queue)
public void priorityQueueIndex(final DefaultPriorityQueue<?> queue, final int i)
'''
pass
def toString():
'''public String toString()
'''
pass
