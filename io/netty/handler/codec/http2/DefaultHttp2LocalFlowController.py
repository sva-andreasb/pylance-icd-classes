DEFAULT_WINDOW_UPDATE_RATIO = "float  0.5f"
def ():
    '''returns DefaultHttp2LocalFlowController\n\n
    (final Http2Connection connection)\n
    (final Http2Connection connection, final float windowUpdateRatio, final boolean autoRefillConnectionWindow)\n
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
def frameWriter():
    '''returns DefaultHttp2LocalFlowController\n\n
    frameWriter(final Http2FrameWriter frameWriter)\n
    '''
def channelHandlerContext():
    '''returns None\n\n
    channelHandlerContext(final ChannelHandlerContext ctx)\n
    '''
def initialWindowSize():
    '''returns int\n\n
    initialWindowSize(final int newWindowSize)\n
    initialWindowSize()\n
    initialWindowSize(final Http2Stream stream)\n
    initialWindowSize()\n
    initialWindowSize()\n
    '''
def windowSize():
    '''returns int\n\n
    windowSize(final Http2Stream stream)\n
    windowSize()\n
    windowSize()\n
    '''
def incrementWindowSize():
    '''returns None\n\n
    incrementWindowSize(final Http2Stream stream, final int delta)\n
    '''
def consumeBytes():
    '''returns boolean\n\n
    consumeBytes(final Http2Stream stream, final int numBytes)\n
    consumeBytes(final int numBytes)\n
    consumeBytes(final int numBytes)\n
    consumeBytes(final int numBytes)\n
    '''
def unconsumedBytes():
    '''returns int\n\n
    unconsumedBytes(final Http2Stream stream)\n
    unconsumedBytes()\n
    unconsumedBytes()\n
    '''
def windowUpdateRatio():
    '''returns None\n\n
    windowUpdateRatio(final float ratio)\n
    windowUpdateRatio()\n
    windowUpdateRatio(final Http2Stream stream, final float ratio)\n
    windowUpdateRatio(final Http2Stream stream)\n
    windowUpdateRatio()\n
    windowUpdateRatio(final float ratio)\n
    windowUpdateRatio()\n
    windowUpdateRatio(final float ratio)\n
    '''
def receiveFlowControlledFrame():
    '''returns None\n\n
    receiveFlowControlledFrame(final Http2Stream stream, final ByteBuf data, final int padding, final boolean endOfStream)\n
    receiveFlowControlledFrame(final int dataLength)\n
    receiveFlowControlledFrame(final int dataLength)\n
    receiveFlowControlledFrame(final int dataLength)\n
    '''
def window():
    '''returns None\n\n
    window(final int initialWindowSize)\n
    window(final int initialWindowSize)\n
    '''
def incrementInitialStreamWindow():
    '''returns None\n\n
    incrementInitialStreamWindow(final int delta)\n
    incrementInitialStreamWindow(int delta)\n
    '''
def writeWindowUpdateIfNeeded():
    '''returns boolean\n\n
    writeWindowUpdateIfNeeded()\n
    writeWindowUpdateIfNeeded()\n
    '''
def incrementFlowControlWindows():
    '''returns None\n\n
    incrementFlowControlWindows(final int delta)\n
    incrementFlowControlWindows(final int delta)\n
    '''
def endOfStream():
    '''returns None\n\n
    endOfStream(final boolean endOfStream)\n
    endOfStream(final boolean endOfStream)\n
    '''
def visit():
    '''returns boolean\n\n
    visit(final Http2Stream stream)\n
    '''
def throwIfError():
    '''returns None\n\n
    throwIfError()\n
    '''
