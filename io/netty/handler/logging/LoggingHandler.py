def ():
    '''returns LoggingHandler\n\n
    ()\n
    (final LogLevel level)\n
    (final LogLevel level, final ByteBufFormat byteBufFormat)\n
    (final Class<?> clazz)\n
    (final Class<?> clazz, final LogLevel level)\n
    (final Class<?> clazz, final LogLevel level, final ByteBufFormat byteBufFormat)\n
    (final String name)\n
    (final String name, final LogLevel level)\n
    (final String name, final LogLevel level, final ByteBufFormat byteBufFormat)\n
    '''
def level():
    '''returns LogLevel\n\n
    level()\n
    '''
def byteBufFormat():
    '''returns ByteBufFormat\n\n
    byteBufFormat()\n
    '''
def channelRegistered():
    '''returns None\n\n
    channelRegistered(final ChannelHandlerContext ctx)\n
    '''
def channelUnregistered():
    '''returns None\n\n
    channelUnregistered(final ChannelHandlerContext ctx)\n
    '''
def channelActive():
    '''returns None\n\n
    channelActive(final ChannelHandlerContext ctx)\n
    '''
def channelInactive():
    '''returns None\n\n
    channelInactive(final ChannelHandlerContext ctx)\n
    '''
def exceptionCaught():
    '''returns None\n\n
    exceptionCaught(final ChannelHandlerContext ctx, final Throwable cause)\n
    '''
def userEventTriggered():
    '''returns None\n\n
    userEventTriggered(final ChannelHandlerContext ctx, final Object evt)\n
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
def channelReadComplete():
    '''returns None\n\n
    channelReadComplete(final ChannelHandlerContext ctx)\n
    '''
def channelRead():
    '''returns None\n\n
    channelRead(final ChannelHandlerContext ctx, final Object msg)\n
    '''
def write():
    '''returns None\n\n
    write(final ChannelHandlerContext ctx, final Object msg, final ChannelPromise promise)\n
    '''
def channelWritabilityChanged():
    '''returns None\n\n
    channelWritabilityChanged(final ChannelHandlerContext ctx)\n
    '''
def flush():
    '''returns None\n\n
    flush(final ChannelHandlerContext ctx)\n
    '''
