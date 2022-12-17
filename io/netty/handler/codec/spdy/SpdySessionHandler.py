def ():
    '''returns SpdySessionHandler\n\n
    (final SpdyVersion version, final boolean server)\n
    '''
def setSessionReceiveWindowSize():
    '''returns None\n\n
    setSessionReceiveWindowSize(final int sessionReceiveWindowSize)\n
    '''
def channelRead():
    '''returns None\n\n
    channelRead(final ChannelHandlerContext ctx, final Object msg)\n
    '''
def channelInactive():
    '''returns None\n\n
    channelInactive(final ChannelHandlerContext ctx)\n
    '''
def exceptionCaught():
    '''returns None\n\n
    exceptionCaught(final ChannelHandlerContext ctx, final Throwable cause)\n
    '''
def close():
    '''returns None\n\n
    close(final ChannelHandlerContext ctx, final ChannelPromise promise)\n
    '''
def write():
    '''returns None\n\n
    write(final ChannelHandlerContext ctx, final Object msg, final ChannelPromise promise)\n
    '''
def operationComplete():
    '''returns None\n\n
    operationComplete(final ChannelFuture future)\n
    operationComplete(final ChannelFuture future)\n
    operationComplete(final ChannelFuture future)\n
    operationComplete(final ChannelFuture future)\n
    operationComplete(final ChannelFuture sentGoAwayFuture)\n
    '''
