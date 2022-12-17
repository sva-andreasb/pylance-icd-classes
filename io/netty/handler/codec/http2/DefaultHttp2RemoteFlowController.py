def ():
    '''returns DefaultHttp2RemoteFlowController\n\n
    (final Http2Connection connection)\n
    (final Http2Connection connection, final StreamByteDistributor streamByteDistributor)\n
    (final Http2Connection connection, final Listener listener)\n
    (final Http2Connection connection, final StreamByteDistributor streamByteDistributor, final Listener listener)\n
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
def onStreamHalfClosed():
    '''returns None\n\n
    onStreamHalfClosed(final Http2Stream stream)\n
    '''
def channelHandlerContext():
    '''returns ChannelHandlerContext\n\n
    channelHandlerContext(final ChannelHandlerContext ctx)\n
    channelHandlerContext()\n
    '''
def initialWindowSize():
    '''returns int\n\n
    initialWindowSize(final int newWindowSize)\n
    initialWindowSize()\n
    '''
def windowSize():
    '''returns int\n\n
    windowSize(final Http2Stream stream)\n
    windowSize()\n
    '''
def isWritable():
    '''returns boolean\n\n
    isWritable(final Http2Stream stream)\n
    '''
def channelWritabilityChanged():
    '''returns None\n\n
    channelWritabilityChanged()\n
    '''
def updateDependencyTree():
    '''returns None\n\n
    updateDependencyTree(final int childStreamId, final int parentStreamId, final short weight, final boolean exclusive)\n
    '''
def listener():
    '''returns None\n\n
    listener(final Listener listener)\n
    '''
def incrementWindowSize():
    '''returns None\n\n
    incrementWindowSize(final Http2Stream stream, final int delta)\n
    '''
def addFlowControlled():
    '''returns None\n\n
    addFlowControlled(final Http2Stream stream, final FlowControlled frame)\n
    '''
def hasFlowControlled():
    '''returns boolean\n\n
    hasFlowControlled(final Http2Stream stream)\n
    '''
def writePendingBytes():
    '''returns None\n\n
    writePendingBytes()\n
    '''
def stream():
    '''returns Http2Stream\n\n
    stream()\n
    '''
def pendingBytes():
    '''returns long\n\n
    pendingBytes()\n
    '''
def hasFrame():
    '''returns boolean\n\n
    hasFrame()\n
    '''
def visit():
    '''returns boolean\n\n
    visit(final Http2Stream stream)\n
    visit(final Http2Stream stream)\n
    '''
