def DefaultHttp2FrameWriter():
    '''public DefaultHttp2FrameWriter()
    public DefaultHttp2FrameWriter(final Http2HeadersEncoder.SensitivityDetector headersSensitivityDetector)
    public DefaultHttp2FrameWriter(final Http2HeadersEncoder.SensitivityDetector headersSensitivityDetector, final boolean ignoreMaxHeaderListSize)
    public DefaultHttp2FrameWriter(final Http2HeadersEncoder headersEncoder)
    '''
def configuration():
    '''public Configuration configuration()
    '''
def frameSizePolicy():
    '''public Http2FrameSizePolicy frameSizePolicy()
    '''
def maxFrameSize():
    '''public void maxFrameSize(final int max)
    public int maxFrameSize()
    '''
def close():
    '''public void close()
    '''
def writeData():
    '''public ChannelFuture writeData(final ChannelHandlerContext ctx, final int streamId, ByteBuf data, int padding, final boolean endStream, final ChannelPromise promise)
    '''
def writeHeaders():
    '''public ChannelFuture writeHeaders(final ChannelHandlerContext ctx, final int streamId, final Http2Headers headers, final int padding, final boolean endStream, final ChannelPromise promise)
    public ChannelFuture writeHeaders(final ChannelHandlerContext ctx, final int streamId, final Http2Headers headers, final int streamDependency, final short weight, final boolean exclusive, final int padding, final boolean endStream, final ChannelPromise promise)
    '''
def writePriority():
    '''public ChannelFuture writePriority(final ChannelHandlerContext ctx, final int streamId, final int streamDependency, final short weight, final boolean exclusive, final ChannelPromise promise)
    '''
def writeRstStream():
    '''public ChannelFuture writeRstStream(final ChannelHandlerContext ctx, final int streamId, final long errorCode, final ChannelPromise promise)
    '''
def writeSettings():
    '''public ChannelFuture writeSettings(final ChannelHandlerContext ctx, final Http2Settings settings, final ChannelPromise promise)
    '''
def writeSettingsAck():
    '''public ChannelFuture writeSettingsAck(final ChannelHandlerContext ctx, final ChannelPromise promise)
    '''
def writePing():
    '''public ChannelFuture writePing(final ChannelHandlerContext ctx, final boolean ack, final long data, final ChannelPromise promise)
    '''
def writePushPromise():
    '''public ChannelFuture writePushPromise(final ChannelHandlerContext ctx, final int streamId, final int promisedStreamId, final Http2Headers headers, final int padding, final ChannelPromise promise)
    '''
def writeGoAway():
    '''public ChannelFuture writeGoAway(final ChannelHandlerContext ctx, final int lastStreamId, final long errorCode, final ByteBuf debugData, final ChannelPromise promise)
    '''
def writeWindowUpdate():
    '''public ChannelFuture writeWindowUpdate(final ChannelHandlerContext ctx, final int streamId, final int windowSizeIncrement, final ChannelPromise promise)
    '''
def writeFrame():
    '''public ChannelFuture writeFrame(final ChannelHandlerContext ctx, final byte frameType, final int streamId, final Http2Flags flags, final ByteBuf payload, final ChannelPromise promise)
    '''
