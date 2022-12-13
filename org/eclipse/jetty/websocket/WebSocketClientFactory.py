def WebSocketClientFactory():
'''public WebSocketClientFactory()
public WebSocketClientFactory(final ThreadPool threadPool)
public WebSocketClientFactory(final ThreadPool threadPool, final MaskGen maskGen)
public WebSocketClientFactory(ThreadPool threadPool, final MaskGen maskGen, final int bufferSize)
'''
pass
def getSslContextFactory():
'''public SslContextFactory getSslContextFactory()
'''
pass
def getSelectorManager():
'''public SelectorManager getSelectorManager()
'''
pass
def getThreadPool():
'''public ThreadPool getThreadPool()
'''
pass
def getMaskGen():
'''public MaskGen getMaskGen()
'''
pass
def setMaskGen():
'''public void setMaskGen(final MaskGen maskGen)
'''
pass
def setBufferSize():
'''public void setBufferSize(final int bufferSize)
'''
pass
def getBufferSize():
'''public int getBufferSize()
'''
pass
def newWebSocketClient():
'''public WebSocketClient newWebSocketClient()
'''
pass
def dispatch():
'''public boolean dispatch(final Runnable task)
'''
pass
def newConnection():
'''public AsyncConnection newConnection(final SocketChannel channel, final AsyncEndPoint endpoint, final Object attachment)
'''
pass
def HandshakeConnection():
'''public HandshakeConnection(final AsyncEndPoint endpoint, final WebSocketClient.WebSocketFuture future)
'''
pass
def startResponse():
'''public void startResponse(final Buffer version, final int status, final Buffer reason)
'''
pass
def parsedHeader():
'''public void parsedHeader(final Buffer name, final Buffer value)
'''
pass
def startRequest():
'''public void startRequest(final Buffer method, final Buffer url, final Buffer version)
'''
pass
def content():
'''public void content(final Buffer ref)
'''
pass
def handle():
'''public Connection handle()
'''
pass
def onInputShutdown():
'''public void onInputShutdown()
'''
pass
def isIdle():
'''public boolean isIdle()
'''
pass
def isSuspended():
'''public boolean isSuspended()
'''
pass
def onClose():
'''public void onClose()
public void onClose()
'''
pass
def WebSocketClientConnection():
'''public WebSocketClientConnection(final WebSocketClientFactory factory, final WebSocket webSocket, final EndPoint endPoint, final WebSocketBuffers buffers, final long timeStamp, final int maxIdleTime, final String protocol, final List<Extension> extensions, final int draftVersion, final MaskGen maskGen)
'''
pass
