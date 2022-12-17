def ():
    '''returns Http2FrameLogger\n\n
    (final LogLevel level)\n
    (final LogLevel level, final String name)\n
    (final LogLevel level, final Class<?> clazz)\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled()\n
    '''
def logData():
    '''returns None\n\n
    logData(final Direction direction, final ChannelHandlerContext ctx, final int streamId, final ByteBuf data, final int padding, final boolean endStream)\n
    '''
def logHeaders():
    '''returns None\n\n
    logHeaders(final Direction direction, final ChannelHandlerContext ctx, final int streamId, final Http2Headers headers, final int padding, final boolean endStream)\n
    logHeaders(final Direction direction, final ChannelHandlerContext ctx, final int streamId, final Http2Headers headers, final int streamDependency, final short weight, final boolean exclusive, final int padding, final boolean endStream)\n
    '''
def logPriority():
    '''returns None\n\n
    logPriority(final Direction direction, final ChannelHandlerContext ctx, final int streamId, final int streamDependency, final short weight, final boolean exclusive)\n
    '''
def logRstStream():
    '''returns None\n\n
    logRstStream(final Direction direction, final ChannelHandlerContext ctx, final int streamId, final long errorCode)\n
    '''
def logSettingsAck():
    '''returns None\n\n
    logSettingsAck(final Direction direction, final ChannelHandlerContext ctx)\n
    '''
def logSettings():
    '''returns None\n\n
    logSettings(final Direction direction, final ChannelHandlerContext ctx, final Http2Settings settings)\n
    '''
def logPing():
    '''returns None\n\n
    logPing(final Direction direction, final ChannelHandlerContext ctx, final long data)\n
    '''
def logPingAck():
    '''returns None\n\n
    logPingAck(final Direction direction, final ChannelHandlerContext ctx, final long data)\n
    '''
def logPushPromise():
    '''returns None\n\n
    logPushPromise(final Direction direction, final ChannelHandlerContext ctx, final int streamId, final int promisedStreamId, final Http2Headers headers, final int padding)\n
    '''
def logGoAway():
    '''returns None\n\n
    logGoAway(final Direction direction, final ChannelHandlerContext ctx, final int lastStreamId, final long errorCode, final ByteBuf debugData)\n
    '''
def logWindowsUpdate():
    '''returns None\n\n
    logWindowsUpdate(final Direction direction, final ChannelHandlerContext ctx, final int streamId, final int windowSizeIncrement)\n
    '''
def logUnknownFrame():
    '''returns None\n\n
    logUnknownFrame(final Direction direction, final ChannelHandlerContext ctx, final byte frameType, final int streamId, final Http2Flags flags, final ByteBuf data)\n
    '''
