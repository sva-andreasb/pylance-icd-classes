def IdleStateHandler():
'''public IdleStateHandler(final int readerIdleTimeSeconds, final int writerIdleTimeSeconds, final int allIdleTimeSeconds)
public IdleStateHandler(final long readerIdleTime, final long writerIdleTime, final long allIdleTime, final TimeUnit unit)
public IdleStateHandler(final boolean observeOutput, final long readerIdleTime, final long writerIdleTime, final long allIdleTime, final TimeUnit unit)
'''
pass
def operationComplete():
'''public void operationComplete(final ChannelFuture future)
'''
pass
def getReaderIdleTimeInMillis():
'''public long getReaderIdleTimeInMillis()
'''
pass
def getWriterIdleTimeInMillis():
'''public long getWriterIdleTimeInMillis()
'''
pass
def getAllIdleTimeInMillis():
'''public long getAllIdleTimeInMillis()
'''
pass
def handlerAdded():
'''public void handlerAdded(final ChannelHandlerContext ctx)
'''
pass
def handlerRemoved():
'''public void handlerRemoved(final ChannelHandlerContext ctx)
'''
pass
def channelRegistered():
'''public void channelRegistered(final ChannelHandlerContext ctx)
'''
pass
def channelActive():
'''public void channelActive(final ChannelHandlerContext ctx)
'''
pass
def channelInactive():
'''public void channelInactive(final ChannelHandlerContext ctx)
'''
pass
def channelRead():
'''public void channelRead(final ChannelHandlerContext ctx, final Object msg)
'''
pass
def channelReadComplete():
'''public void channelReadComplete(final ChannelHandlerContext ctx)
'''
pass
def write():
'''public void write(final ChannelHandlerContext ctx, final Object msg, final ChannelPromise promise)
'''
pass
def run():
'''public void run()
'''
pass
