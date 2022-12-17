def ():
    '''returns IdleStateHandler\n\n
    (final int readerIdleTimeSeconds, final int writerIdleTimeSeconds, final int allIdleTimeSeconds)\n
    (final long readerIdleTime, final long writerIdleTime, final long allIdleTime, final TimeUnit unit)\n
    (final boolean observeOutput, final long readerIdleTime, final long writerIdleTime, final long allIdleTime, final TimeUnit unit)\n
    '''
def operationComplete():
    '''returns None\n\n
    operationComplete(final ChannelFuture future)\n
    '''
def getReaderIdleTimeInMillis():
    '''returns long\n\n
    getReaderIdleTimeInMillis()\n
    '''
def getWriterIdleTimeInMillis():
    '''returns long\n\n
    getWriterIdleTimeInMillis()\n
    '''
def getAllIdleTimeInMillis():
    '''returns long\n\n
    getAllIdleTimeInMillis()\n
    '''
def handlerAdded():
    '''returns None\n\n
    handlerAdded(final ChannelHandlerContext ctx)\n
    '''
def handlerRemoved():
    '''returns None\n\n
    handlerRemoved(final ChannelHandlerContext ctx)\n
    '''
def channelRegistered():
    '''returns None\n\n
    channelRegistered(final ChannelHandlerContext ctx)\n
    '''
def channelActive():
    '''returns None\n\n
    channelActive(final ChannelHandlerContext ctx)\n
    '''
def channelInactive():
    '''returns None\n\n
    channelInactive(final ChannelHandlerContext ctx)\n
    '''
def channelRead():
    '''returns None\n\n
    channelRead(final ChannelHandlerContext ctx, final Object msg)\n
    '''
def channelReadComplete():
    '''returns None\n\n
    channelReadComplete(final ChannelHandlerContext ctx)\n
    '''
def write():
    '''returns None\n\n
    write(final ChannelHandlerContext ctx, final Object msg, final ChannelPromise promise)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
