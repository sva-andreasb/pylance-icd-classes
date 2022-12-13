def WebSocketServerHandshakerFactory():
    '''public WebSocketServerHandshakerFactory(final String webSocketURL, final String subprotocols, final boolean allowExtensions)
    public WebSocketServerHandshakerFactory(final String webSocketURL, final String subprotocols, final boolean allowExtensions, final int maxFramePayloadLength)
    public WebSocketServerHandshakerFactory(final String webSocketURL, final String subprotocols, final boolean allowExtensions, final int maxFramePayloadLength, final boolean allowMaskMismatch)
    public WebSocketServerHandshakerFactory(final String webSocketURL, final String subprotocols, final WebSocketDecoderConfig decoderConfig)
    '''
def newHandshaker():
    '''public WebSocketServerHandshaker newHandshaker(final HttpRequest req)
    '''
def sendUnsupportedWebSocketVersionResponse():
    '''public static void sendUnsupportedWebSocketVersionResponse(final Channel channel)
    '''
def sendUnsupportedVersionResponse():
    '''public static ChannelFuture sendUnsupportedVersionResponse(final Channel channel)
    public static ChannelFuture sendUnsupportedVersionResponse(final Channel channel, final ChannelPromise promise)
    '''
