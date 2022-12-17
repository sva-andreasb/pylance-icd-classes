def ():
    '''returns DefaultHttp2FrameWriter\n\n
    ()\n
    (final Http2HeadersEncoder.SensitivityDetector headersSensitivityDetector)\n
    (final Http2HeadersEncoder.SensitivityDetector headersSensitivityDetector, final boolean ignoreMaxHeaderListSize)\n
    (final Http2HeadersEncoder headersEncoder)\n
    '''
def configuration():
    '''returns Configuration\n\n
    configuration()\n
    '''
def frameSizePolicy():
    '''returns Http2FrameSizePolicy\n\n
    frameSizePolicy()\n
    '''
def maxFrameSize():
    '''returns int\n\n
    maxFrameSize(final int max)\n
    maxFrameSize()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def writeData():
    '''returns ChannelFuture\n\n
    writeData(final ChannelHandlerContext ctx, final int streamId, ByteBuf data, int padding, final boolean endStream, final ChannelPromise promise)\n
    '''
def writeHeaders():
    '''returns ChannelFuture\n\n
    writeHeaders(final ChannelHandlerContext ctx, final int streamId, final Http2Headers headers, final int padding, final boolean endStream, final ChannelPromise promise)\n
    writeHeaders(final ChannelHandlerContext ctx, final int streamId, final Http2Headers headers, final int streamDependency, final short weight, final boolean exclusive, final int padding, final boolean endStream, final ChannelPromise promise)\n
    '''
def writePriority():
    '''returns ChannelFuture\n\n
    writePriority(final ChannelHandlerContext ctx, final int streamId, final int streamDependency, final short weight, final boolean exclusive, final ChannelPromise promise)\n
    '''
def writeRstStream():
    '''returns ChannelFuture\n\n
    writeRstStream(final ChannelHandlerContext ctx, final int streamId, final long errorCode, final ChannelPromise promise)\n
    '''
def writeSettings():
    '''returns ChannelFuture\n\n
    writeSettings(final ChannelHandlerContext ctx, final Http2Settings settings, final ChannelPromise promise)\n
    '''
def writeSettingsAck():
    '''returns ChannelFuture\n\n
    writeSettingsAck(final ChannelHandlerContext ctx, final ChannelPromise promise)\n
    '''
def writePing():
    '''returns ChannelFuture\n\n
    writePing(final ChannelHandlerContext ctx, final boolean ack, final long data, final ChannelPromise promise)\n
    '''
def writePushPromise():
    '''returns ChannelFuture\n\n
    writePushPromise(final ChannelHandlerContext ctx, final int streamId, final int promisedStreamId, final Http2Headers headers, final int padding, final ChannelPromise promise)\n
    '''
def writeGoAway():
    '''returns ChannelFuture\n\n
    writeGoAway(final ChannelHandlerContext ctx, final int lastStreamId, final long errorCode, final ByteBuf debugData, final ChannelPromise promise)\n
    '''
def writeWindowUpdate():
    '''returns ChannelFuture\n\n
    writeWindowUpdate(final ChannelHandlerContext ctx, final int streamId, final int windowSizeIncrement, final ChannelPromise promise)\n
    '''
def writeFrame():
    '''returns ChannelFuture\n\n
    writeFrame(final ChannelHandlerContext ctx, final byte frameType, final int streamId, final Http2Flags flags, final ByteBuf payload, final ChannelPromise promise)\n
    '''
