def WebSocketClientFactory():
    '''public WebSocketClientFactory()
    public WebSocketClientFactory(final ThreadPool threadPool)
    public WebSocketClientFactory(final ThreadPool threadPool, final MaskGen maskGen)
    public WebSocketClientFactory(ThreadPool threadPool, final MaskGen maskGen, final int bufferSize)
    '''
def getSslContextFactory():
    '''public SslContextFactory getSslContextFactory()
    '''
def getSelectorManager():
    '''public SelectorManager getSelectorManager()
    '''
def getThreadPool():
    '''public ThreadPool getThreadPool()
    '''
def getMaskGen():
    '''public MaskGen getMaskGen()
    '''
def setMaskGen():
    '''public void setMaskGen(final MaskGen maskGen)
    '''
def setBufferSize():
    '''public void setBufferSize(final int bufferSize)
    '''
def getBufferSize():
    '''public int getBufferSize()
    '''
def newWebSocketClient():
    '''public WebSocketClient newWebSocketClient()
    '''
def dispatch():
    '''public boolean dispatch(final Runnable task)
    '''
def newConnection():
    '''public AsyncConnection newConnection(final SocketChannel channel, final AsyncEndPoint endpoint, final Object attachment)
    '''
def HandshakeConnection():
    '''public HandshakeConnection(final AsyncEndPoint endpoint, final WebSocketClient.WebSocketFuture future)
    '''
def startResponse():
    '''public void startResponse(final Buffer version, final int status, final Buffer reason)
    '''
def parsedHeader():
    '''public void parsedHeader(final Buffer name, final Buffer value)
    '''
def startRequest():
    '''public void startRequest(final Buffer method, final Buffer url, final Buffer version)
    '''
def content():
    '''public void content(final Buffer ref)
    '''
def handle():
    '''public Connection handle()
    '''
def onInputShutdown():
    '''public void onInputShutdown()
    '''
def isIdle():
    '''public boolean isIdle()
    '''
def isSuspended():
    '''public boolean isSuspended()
    '''
def onClose():
    '''public void onClose()
    public void onClose()
    '''
def WebSocketClientConnection():
    '''public WebSocketClientConnection(final WebSocketClientFactory factory, final WebSocket webSocket, final EndPoint endPoint, final WebSocketBuffers buffers, final long timeStamp, final int maxIdleTime, final String protocol, final List<Extension> extensions, final int draftVersion, final MaskGen maskGen)
    '''
