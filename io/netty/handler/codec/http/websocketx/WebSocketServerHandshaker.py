SUB_PROTOCOL_WILDCARD = "String  \"*\""
def uri():
    '''returns String\n\n
    uri()\n
    '''
def subprotocols():
    '''returns Set<String>\n\n
    subprotocols()\n
    '''
def version():
    '''returns WebSocketVersion\n\n
    version()\n
    '''
def maxFramePayloadLength():
    '''returns int\n\n
    maxFramePayloadLength()\n
    '''
def decoderConfig():
    '''returns WebSocketDecoderConfig\n\n
    decoderConfig()\n
    '''
def handshake():
    '''returns ChannelFuture\n\n
    handshake(final Channel channel, final FullHttpRequest req)\n
    handshake(final Channel channel, final HttpRequest req)\n
    '''
def operationComplete():
    '''returns None\n\n
    operationComplete(final ChannelFuture future)\n
    '''
def exceptionCaught():
    '''returns None\n\n
    exceptionCaught(final ChannelHandlerContext ctx, final Throwable cause)\n
    '''
def channelInactive():
    '''returns None\n\n
    channelInactive(final ChannelHandlerContext ctx)\n
    '''
def close():
    '''returns ChannelFuture\n\n
    close(final Channel channel, final CloseWebSocketFrame frame)\n
    close(final Channel channel, final CloseWebSocketFrame frame, final ChannelPromise promise)\n
    '''
def selectedSubprotocol():
    '''returns String\n\n
    selectedSubprotocol()\n
    '''
