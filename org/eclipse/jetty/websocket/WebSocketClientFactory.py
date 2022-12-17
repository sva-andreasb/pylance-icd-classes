def ():
    '''returns WebSocketClientConnection\n\n
    ()\n
    (final ThreadPool threadPool)\n
    (final ThreadPool threadPool, final MaskGen maskGen)\n
    (ThreadPool threadPool, final MaskGen maskGen, final int bufferSize)\n
    (final AsyncEndPoint endpoint, final WebSocketClient.WebSocketFuture future)\n
    (final WebSocketClientFactory factory, final WebSocket webSocket, final EndPoint endPoint, final WebSocketBuffers buffers, final long timeStamp, final int maxIdleTime, final String protocol, final List<Extension> extensions, final int draftVersion, final MaskGen maskGen)\n
    '''
def getSslContextFactory():
    '''returns SslContextFactory\n\n
    getSslContextFactory()\n
    '''
def getSelectorManager():
    '''returns SelectorManager\n\n
    getSelectorManager()\n
    '''
def getThreadPool():
    '''returns ThreadPool\n\n
    getThreadPool()\n
    '''
def getMaskGen():
    '''returns MaskGen\n\n
    getMaskGen()\n
    '''
def setMaskGen():
    '''returns None\n\n
    setMaskGen(final MaskGen maskGen)\n
    '''
def setBufferSize():
    '''returns None\n\n
    setBufferSize(final int bufferSize)\n
    '''
def getBufferSize():
    '''returns int\n\n
    getBufferSize()\n
    '''
def newWebSocketClient():
    '''returns WebSocketClient\n\n
    newWebSocketClient()\n
    '''
def dispatch():
    '''returns boolean\n\n
    dispatch(final Runnable task)\n
    '''
def newConnection():
    '''returns AsyncConnection\n\n
    newConnection(final SocketChannel channel, final AsyncEndPoint endpoint, final Object attachment)\n
    '''
def startResponse():
    '''returns None\n\n
    startResponse(final Buffer version, final int status, final Buffer reason)\n
    '''
def parsedHeader():
    '''returns None\n\n
    parsedHeader(final Buffer name, final Buffer value)\n
    '''
def startRequest():
    '''returns None\n\n
    startRequest(final Buffer method, final Buffer url, final Buffer version)\n
    '''
def content():
    '''returns None\n\n
    content(final Buffer ref)\n
    '''
def handle():
    '''returns Connection\n\n
    handle()\n
    '''
def onInputShutdown():
    '''returns None\n\n
    onInputShutdown()\n
    '''
def isIdle():
    '''returns boolean\n\n
    isIdle()\n
    '''
def isSuspended():
    '''returns boolean\n\n
    isSuspended()\n
    '''
def onClose():
    '''returns None\n\n
    onClose()\n
    onClose()\n
    '''
