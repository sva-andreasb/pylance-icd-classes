def ():
    '''returns EmbeddedChannel\n\n
    ()\n
    (final ChannelId channelId)\n
    (final ChannelHandler... handlers)\n
    (final boolean hasDisconnect, final ChannelHandler... handlers)\n
    (final boolean register, final boolean hasDisconnect, final ChannelHandler... handlers)\n
    (final ChannelId channelId, final ChannelHandler... handlers)\n
    (final ChannelId channelId, final boolean hasDisconnect, final ChannelHandler... handlers)\n
    (final ChannelId channelId, final boolean register, final boolean hasDisconnect, final ChannelHandler... handlers)\n
    (final Channel parent, final ChannelId channelId, final boolean register, final boolean hasDisconnect, final ChannelHandler... handlers)\n
    (final ChannelId channelId, final boolean hasDisconnect, final ChannelConfig config, final ChannelHandler... handlers)\n
    '''
def operationComplete():
    '''returns None\n\n
    operationComplete(final ChannelFuture future)\n
    operationComplete(final ChannelFuture future)\n
    '''
def register():
    '''returns None\n\n
    register()\n
    register(final EventLoop eventLoop, final ChannelPromise promise)\n
    '''
def metadata():
    '''returns ChannelMetadata\n\n
    metadata()\n
    '''
def config():
    '''returns ChannelConfig\n\n
    config()\n
    '''
def isOpen():
    '''returns boolean\n\n
    isOpen()\n
    '''
def isActive():
    '''returns boolean\n\n
    isActive()\n
    '''
def inboundMessages():
    '''returns Queue<Object>\n\n
    inboundMessages()\n
    '''
def lastInboundBuffer():
    '''returns Queue<Object>\n\n
    lastInboundBuffer()\n
    '''
def outboundMessages():
    '''returns Queue<Object>\n\n
    outboundMessages()\n
    '''
def lastOutboundBuffer():
    '''returns Queue<Object>\n\n
    lastOutboundBuffer()\n
    '''
def writeInbound():
    '''returns boolean\n\n
    writeInbound(final Object... msgs)\n
    '''
def writeOneInbound():
    '''returns ChannelFuture\n\n
    writeOneInbound(final Object msg)\n
    writeOneInbound(final Object msg, final ChannelPromise promise)\n
    '''
def flushInbound():
    '''returns EmbeddedChannel\n\n
    flushInbound()\n
    '''
def writeOutbound():
    '''returns boolean\n\n
    writeOutbound(final Object... msgs)\n
    '''
def writeOneOutbound():
    '''returns ChannelFuture\n\n
    writeOneOutbound(final Object msg)\n
    writeOneOutbound(final Object msg, final ChannelPromise promise)\n
    '''
def flushOutbound():
    '''returns EmbeddedChannel\n\n
    flushOutbound()\n
    '''
def finish():
    '''returns boolean\n\n
    finish()\n
    '''
def finishAndReleaseAll():
    '''returns boolean\n\n
    finishAndReleaseAll()\n
    '''
def releaseInbound():
    '''returns boolean\n\n
    releaseInbound()\n
    '''
def releaseOutbound():
    '''returns boolean\n\n
    releaseOutbound()\n
    '''
def runPendingTasks():
    '''returns None\n\n
    runPendingTasks()\n
    '''
def runScheduledPendingTasks():
    '''returns long\n\n
    runScheduledPendingTasks()\n
    '''
def checkException():
    '''returns None\n\n
    checkException()\n
    '''
def localAddress():
    '''returns SocketAddress\n\n
    localAddress()\n
    '''
def remoteAddress():
    '''returns SocketAddress\n\n
    remoteAddress()\n
    '''
def bind():
    '''returns None\n\n
    bind(final SocketAddress localAddress, final ChannelPromise promise)\n
    '''
def connect():
    '''returns None\n\n
    connect(final SocketAddress remoteAddress, final SocketAddress localAddress, final ChannelPromise promise)\n
    connect(final SocketAddress remoteAddress, final SocketAddress localAddress, final ChannelPromise promise)\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect(final ChannelPromise promise)\n
    '''
def close():
    '''returns None\n\n
    close(final ChannelPromise promise)\n
    '''
def closeForcibly():
    '''returns None\n\n
    closeForcibly()\n
    '''
def deregister():
    '''returns None\n\n
    deregister(final ChannelPromise promise)\n
    '''
def beginRead():
    '''returns None\n\n
    beginRead()\n
    '''
def write():
    '''returns None\n\n
    write(final Object msg, final ChannelPromise promise)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def voidPromise():
    '''returns ChannelPromise\n\n
    voidPromise()\n
    '''
def outboundBuffer():
    '''returns ChannelOutboundBuffer\n\n
    outboundBuffer()\n
    '''
