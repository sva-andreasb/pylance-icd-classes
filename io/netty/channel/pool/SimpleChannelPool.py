def ():
    '''returns SimpleChannelPool\n\n
    (final Bootstrap bootstrap, final ChannelPoolHandler handler)\n
    (final Bootstrap bootstrap, final ChannelPoolHandler handler, final ChannelHealthChecker healthCheck)\n
    (final Bootstrap bootstrap, final ChannelPoolHandler handler, final ChannelHealthChecker healthCheck, final boolean releaseHealthCheck)\n
    (final Bootstrap bootstrap, final ChannelPoolHandler handler, final ChannelHealthChecker healthCheck, final boolean releaseHealthCheck, final boolean lastRecentUsed)\n
    '''
def acquire():
    '''returns Future<Channel>\n\n
    acquire(final Promise<Channel> promise)\n
    '''
def operationComplete():
    '''returns None\n\n
    operationComplete(final ChannelFuture future)\n
    operationComplete(final Future<Boolean> future)\n
    operationComplete(final Future<Boolean> future)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def release():
    '''returns Future<Void>\n\n
    release(final Channel channel, final Promise<Void> promise)\n
    '''
def fillInStackTrace():
    '''returns Throwable\n\n
    fillInStackTrace()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def closeAsync():
    '''returns Future<Void>\n\n
    closeAsync()\n
    '''
def call():
    '''returns Void\n\n
    call()\n
    '''
