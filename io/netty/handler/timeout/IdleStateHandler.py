def IdleStateHandler():
    '''    public IdleStateHandler(final int readerIdleTimeSeconds, final int writerIdleTimeSeconds, final int allIdleTimeSeconds)
    public IdleStateHandler(final long readerIdleTime, final long writerIdleTime, final long allIdleTime, final TimeUnit unit)
    public IdleStateHandler(final boolean observeOutput, final long readerIdleTime, final long writerIdleTime, final long allIdleTime, final TimeUnit unit)
    '''
def operationComplete():
    '''    public void operationComplete(final ChannelFuture future)
    '''
def getReaderIdleTimeInMillis():
    '''    public long getReaderIdleTimeInMillis()
    '''
def getWriterIdleTimeInMillis():
    '''    public long getWriterIdleTimeInMillis()
    '''
def getAllIdleTimeInMillis():
    '''    public long getAllIdleTimeInMillis()
    '''
def handlerAdded():
    '''    public void handlerAdded(final ChannelHandlerContext ctx)
    '''
def handlerRemoved():
    '''    public void handlerRemoved(final ChannelHandlerContext ctx)
    '''
def channelRegistered():
    '''    public void channelRegistered(final ChannelHandlerContext ctx)
    '''
def channelActive():
    '''    public void channelActive(final ChannelHandlerContext ctx)
    '''
def channelInactive():
    '''    public void channelInactive(final ChannelHandlerContext ctx)
    '''
def channelRead():
    '''    public void channelRead(final ChannelHandlerContext ctx, final Object msg)
    '''
def channelReadComplete():
    '''    public void channelReadComplete(final ChannelHandlerContext ctx)
    '''
def write():
    '''    public void write(final ChannelHandlerContext ctx, final Object msg, final ChannelPromise promise)
    '''
def run():
    '''    public void run()
    '''
