DEFAULT_WINDOW_UPDATE_RATIO = "float  0.5f"
def DefaultHttp2LocalFlowController():
    '''public DefaultHttp2LocalFlowController(final Http2Connection connection)
    public DefaultHttp2LocalFlowController(final Http2Connection connection, final float windowUpdateRatio, final boolean autoRefillConnectionWindow)
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
def frameWriter():
    '''public DefaultHttp2LocalFlowController frameWriter(final Http2FrameWriter frameWriter)
    '''
def channelHandlerContext():
    '''public void channelHandlerContext(final ChannelHandlerContext ctx)
    '''
def initialWindowSize():
    '''public void initialWindowSize(final int newWindowSize)
    public int initialWindowSize()
    public int initialWindowSize(final Http2Stream stream)
    public int initialWindowSize()
    public int initialWindowSize()
    '''
def windowSize():
    '''public int windowSize(final Http2Stream stream)
    public int windowSize()
    public int windowSize()
    '''
def incrementWindowSize():
    '''public void incrementWindowSize(final Http2Stream stream, final int delta)
    '''
def consumeBytes():
    '''public boolean consumeBytes(final Http2Stream stream, final int numBytes)
    public boolean consumeBytes(final int numBytes)
    public boolean consumeBytes(final int numBytes)
    public boolean consumeBytes(final int numBytes)
    '''
def unconsumedBytes():
    '''public int unconsumedBytes(final Http2Stream stream)
    public int unconsumedBytes()
    public int unconsumedBytes()
    '''
def windowUpdateRatio():
    '''public void windowUpdateRatio(final float ratio)
    public float windowUpdateRatio()
    public void windowUpdateRatio(final Http2Stream stream, final float ratio)
    public float windowUpdateRatio(final Http2Stream stream)
    public float windowUpdateRatio()
    public void windowUpdateRatio(final float ratio)
    public float windowUpdateRatio()
    public void windowUpdateRatio(final float ratio)
    '''
def receiveFlowControlledFrame():
    '''public void receiveFlowControlledFrame(final Http2Stream stream, final ByteBuf data, final int padding, final boolean endOfStream)
    public void receiveFlowControlledFrame(final int dataLength)
    public void receiveFlowControlledFrame(final int dataLength)
    public void receiveFlowControlledFrame(final int dataLength)
    '''
def window():
    '''public void window(final int initialWindowSize)
    public void window(final int initialWindowSize)
    '''
def incrementInitialStreamWindow():
    '''public void incrementInitialStreamWindow(final int delta)
    public void incrementInitialStreamWindow(int delta)
    '''
def writeWindowUpdateIfNeeded():
    '''public boolean writeWindowUpdateIfNeeded()
    public boolean writeWindowUpdateIfNeeded()
    '''
def incrementFlowControlWindows():
    '''public void incrementFlowControlWindows(final int delta)
    public void incrementFlowControlWindows(final int delta)
    '''
def endOfStream():
    '''public void endOfStream(final boolean endOfStream)
    public void endOfStream(final boolean endOfStream)
    '''
def visit():
    '''public boolean visit(final Http2Stream stream)
    '''
def throwIfError():
    '''public void throwIfError()
    '''
