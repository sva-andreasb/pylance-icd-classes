def SimpleChannelPool():
    '''public SimpleChannelPool(final Bootstrap bootstrap, final ChannelPoolHandler handler)
    public SimpleChannelPool(final Bootstrap bootstrap, final ChannelPoolHandler handler, final ChannelHealthChecker healthCheck)
    public SimpleChannelPool(final Bootstrap bootstrap, final ChannelPoolHandler handler, final ChannelHealthChecker healthCheck, final boolean releaseHealthCheck)
    public SimpleChannelPool(final Bootstrap bootstrap, final ChannelPoolHandler handler, final ChannelHealthChecker healthCheck, final boolean releaseHealthCheck, final boolean lastRecentUsed)
    '''
def acquire():
    '''public final Future<Channel> acquire()
    public Future<Channel> acquire(final Promise<Channel> promise)
    '''
def operationComplete():
    '''public void operationComplete(final ChannelFuture future)
    public void operationComplete(final Future<Boolean> future)
    public void operationComplete(final Future<Boolean> future)
    '''
def run():
    '''public void run()
    public void run()
    '''
def release():
    '''public final Future<Void> release(final Channel channel)
    public Future<Void> release(final Channel channel, final Promise<Void> promise)
    '''
def fillInStackTrace():
    '''public Throwable fillInStackTrace()
    '''
def close():
    '''public void close()
    '''
def closeAsync():
    '''public Future<Void> closeAsync()
    '''
def call():
    '''public Void call()
    '''
