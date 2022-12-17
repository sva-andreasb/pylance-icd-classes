def ():
    '''returns SpdyFrameCodec\n\n
    (final SpdyVersion version)\n
    (final SpdyVersion version, final boolean validateHeaders)\n
    (final SpdyVersion version, final int maxChunkSize, final int maxHeaderSize, final int compressionLevel, final int windowBits, final int memLevel)\n
    (final SpdyVersion version, final int maxChunkSize, final int maxHeaderSize, final int compressionLevel, final int windowBits, final int memLevel, final boolean validateHeaders)\n
    '''
def handlerAdded():
    '''returns None\n\n
    handlerAdded(final ChannelHandlerContext ctx)\n
    '''
def operationComplete():
    '''returns None\n\n
    operationComplete(final ChannelFuture future)\n
    '''
def channelReadComplete():
    '''returns None\n\n
    channelReadComplete(final ChannelHandlerContext ctx)\n
    '''
def bind():
    '''returns None\n\n
    bind(final ChannelHandlerContext ctx, final SocketAddress localAddress, final ChannelPromise promise)\n
    '''
def connect():
    '''returns None\n\n
    connect(final ChannelHandlerContext ctx, final SocketAddress remoteAddress, final SocketAddress localAddress, final ChannelPromise promise)\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect(final ChannelHandlerContext ctx, final ChannelPromise promise)\n
    '''
def close():
    '''returns None\n\n
    close(final ChannelHandlerContext ctx, final ChannelPromise promise)\n
    '''
def deregister():
    '''returns None\n\n
    deregister(final ChannelHandlerContext ctx, final ChannelPromise promise)\n
    '''
def read():
    '''returns None\n\n
    read(final ChannelHandlerContext ctx)\n
    '''
def flush():
    '''returns None\n\n
    flush(final ChannelHandlerContext ctx)\n
    '''
def write():
    '''returns None\n\n
    write(final ChannelHandlerContext ctx, final Object msg, final ChannelPromise promise)\n
    '''
def readDataFrame():
    '''returns None\n\n
    readDataFrame(final int streamId, final boolean last, final ByteBuf data)\n
    '''
def readSynStreamFrame():
    '''returns None\n\n
    readSynStreamFrame(final int streamId, final int associatedToStreamId, final byte priority, final boolean last, final boolean unidirectional)\n
    '''
def readSynReplyFrame():
    '''returns None\n\n
    readSynReplyFrame(final int streamId, final boolean last)\n
    '''
def readRstStreamFrame():
    '''returns None\n\n
    readRstStreamFrame(final int streamId, final int statusCode)\n
    '''
def readSettingsFrame():
    '''returns None\n\n
    readSettingsFrame(final boolean clearPersisted)\n
    '''
def readSetting():
    '''returns None\n\n
    readSetting(final int id, final int value, final boolean persistValue, final boolean persisted)\n
    '''
def readSettingsEnd():
    '''returns None\n\n
    readSettingsEnd()\n
    '''
def readPingFrame():
    '''returns None\n\n
    readPingFrame(final int id)\n
    '''
def readGoAwayFrame():
    '''returns None\n\n
    readGoAwayFrame(final int lastGoodStreamId, final int statusCode)\n
    '''
def readHeadersFrame():
    '''returns None\n\n
    readHeadersFrame(final int streamId, final boolean last)\n
    '''
def readWindowUpdateFrame():
    '''returns None\n\n
    readWindowUpdateFrame(final int streamId, final int deltaWindowSize)\n
    '''
def readHeaderBlock():
    '''returns None\n\n
    readHeaderBlock(final ByteBuf headerBlock)\n
    '''
def readHeaderBlockEnd():
    '''returns None\n\n
    readHeaderBlockEnd()\n
    '''
def readFrameError():
    '''returns None\n\n
    readFrameError(final String message)\n
    '''
