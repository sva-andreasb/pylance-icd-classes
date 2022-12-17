def decode():
    '''returns None\n\n
    decode(final ChannelHandlerContext ctx, final ByteBuf in, final List<Object> out)\n
    decode(final ChannelHandlerContext ctx, final ByteBuf in, final List<Object> out)\n
    '''
def acceptOutboundMessage():
    '''returns boolean\n\n
    acceptOutboundMessage(final Object msg)\n
    acceptOutboundMessage(final Object msg)\n
    '''
def channelRead():
    '''returns None\n\n
    channelRead(final ChannelHandlerContext ctx, final Object msg)\n
    '''
def write():
    '''returns None\n\n
    write(final ChannelHandlerContext ctx, final Object msg, final ChannelPromise promise)\n
    '''
def channelReadComplete():
    '''returns None\n\n
    channelReadComplete(final ChannelHandlerContext ctx)\n
    '''
def channelInactive():
    '''returns None\n\n
    channelInactive(final ChannelHandlerContext ctx)\n
    '''
def handlerAdded():
    '''returns None\n\n
    handlerAdded(final ChannelHandlerContext ctx)\n
    '''
def handlerRemoved():
    '''returns None\n\n
    handlerRemoved(final ChannelHandlerContext ctx)\n
    '''
