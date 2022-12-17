def visit():
    '''returns boolean\n\n
    visit(final Http2Stream stream)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def write():
    '''returns None\n\n
    write(final ChannelHandlerContext ctx, final Object msg, final ChannelPromise promise)\n
    '''
def operationComplete():
    '''returns None\n\n
    operationComplete(final ChannelFuture channelFuture)\n
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
def onUnknownFrame():
    '''returns None\n\n
    onUnknownFrame(final ChannelHandlerContext ctx, final byte frameType, final int streamId, final Http2Flags flags, final ByteBuf payload)\n
    '''
def onSettingsRead():
    '''returns None\n\n
    onSettingsRead(final ChannelHandlerContext ctx, final Http2Settings settings)\n
    '''
def onPingRead():
    '''returns None\n\n
    onPingRead(final ChannelHandlerContext ctx, final long data)\n
    '''
def onPingAckRead():
    '''returns None\n\n
    onPingAckRead(final ChannelHandlerContext ctx, final long data)\n
    '''
def onRstStreamRead():
    '''returns None\n\n
    onRstStreamRead(final ChannelHandlerContext ctx, final int streamId, final long errorCode)\n
    '''
def onWindowUpdateRead():
    '''returns None\n\n
    onWindowUpdateRead(final ChannelHandlerContext ctx, final int streamId, final int windowSizeIncrement)\n
    '''
def onHeadersRead():
    '''returns None\n\n
    onHeadersRead(final ChannelHandlerContext ctx, final int streamId, final Http2Headers headers, final int streamDependency, final short weight, final boolean exclusive, final int padding, final boolean endStream)\n
    onHeadersRead(final ChannelHandlerContext ctx, final int streamId, final Http2Headers headers, final int padding, final boolean endOfStream)\n
    '''
def onDataRead():
    '''returns int\n\n
    onDataRead(final ChannelHandlerContext ctx, final int streamId, final ByteBuf data, final int padding, final boolean endOfStream)\n
    '''
def onGoAwayRead():
    '''returns None\n\n
    onGoAwayRead(final ChannelHandlerContext ctx, final int lastStreamId, final long errorCode, final ByteBuf debugData)\n
    '''
def onPriorityRead():
    '''returns None\n\n
    onPriorityRead(final ChannelHandlerContext ctx, final int streamId, final int streamDependency, final short weight, final boolean exclusive)\n
    '''
def onSettingsAckRead():
    '''returns None\n\n
    onSettingsAckRead(final ChannelHandlerContext ctx)\n
    '''
def onPushPromiseRead():
    '''returns None\n\n
    onPushPromiseRead(final ChannelHandlerContext ctx, final int streamId, final int promisedStreamId, final Http2Headers headers, final int padding)\n
    '''
def writabilityChanged():
    '''returns None\n\n
    writabilityChanged(final Http2Stream stream)\n
    '''
def id():
    '''returns int\n\n
    id()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
