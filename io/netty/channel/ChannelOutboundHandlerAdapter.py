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
def write():
    '''returns None\n\n
    write(final ChannelHandlerContext ctx, final Object msg, final ChannelPromise promise)\n
    '''
def flush():
    '''returns None\n\n
    flush(final ChannelHandlerContext ctx)\n
    '''
