def SimpleChannelPool():
'''public SimpleChannelPool(final Bootstrap bootstrap, final ChannelPoolHandler handler)
public SimpleChannelPool(final Bootstrap bootstrap, final ChannelPoolHandler handler, final ChannelHealthChecker healthCheck)
public SimpleChannelPool(final Bootstrap bootstrap, final ChannelPoolHandler handler, final ChannelHealthChecker healthCheck, final boolean releaseHealthCheck)
public SimpleChannelPool(final Bootstrap bootstrap, final ChannelPoolHandler handler, final ChannelHealthChecker healthCheck, final boolean releaseHealthCheck, final boolean lastRecentUsed)
'''
pass
def acquire():
'''public final Future<Channel> acquire()
public Future<Channel> acquire(final Promise<Channel> promise)
'''
pass
def operationComplete():
'''public void operationComplete(final ChannelFuture future)
public void operationComplete(final Future<Boolean> future)
public void operationComplete(final Future<Boolean> future)
'''
pass
def run():
'''public void run()
public void run()
'''
pass
def release():
'''public final Future<Void> release(final Channel channel)
public Future<Void> release(final Channel channel, final Promise<Void> promise)
'''
pass
def fillInStackTrace():
'''public Throwable fillInStackTrace()
'''
pass
def close():
'''public void close()
'''
pass
def closeAsync():
'''public Future<Void> closeAsync()
'''
pass
def call():
'''public Void call()
'''
pass
