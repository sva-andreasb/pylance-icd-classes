LENGTH_FRAME = "byte  Byte.MIN_VALUE"
SENTINEL_FRAME = "byte  0"
def WebSocketConnectionD00():
    '''    public WebSocketConnectionD00(final WebSocket websocket, final EndPoint endpoint, final WebSocketBuffers buffers, final long timestamp, final int maxIdleTime, final String protocol)
    '''
def setHixieKeys():
    '''    public void setHixieKeys(final String key1, final String key2)
    '''
def onInputShutdown():
    '''    public void onInputShutdown()
    '''
def isOpen():
    '''    public boolean isOpen()
    '''
def isIdle():
    '''    public boolean isIdle()
    '''
def isSuspended():
    '''    public boolean isSuspended()
    '''
def onClose():
    '''    public void onClose()
    '''
def sendMessage():
    '''    public void sendMessage(final String content)
    public void sendMessage(final byte[] data, final int offset, final int length)
    '''
def isMore():
    '''    public boolean isMore(final byte flags)
    '''
def sendControl():
    '''    public void sendControl(final byte code, final byte[] content, final int offset, final int length)
    '''
def sendFrame():
    '''    public void sendFrame(final byte flags, final byte opcode, final byte[] content, final int offset, final int length)
    '''
def close():
    '''    public void close(final int code, final String message)
    public void close()
    public void close(final int code, final String message)
    '''
def disconnect():
    '''    public void disconnect()
    '''
def shutdown():
    '''    public void shutdown()
    '''
def fillBuffersFrom():
    '''    public void fillBuffersFrom(final Buffer buffer)
    '''
def doTheHixieHixieShake():
    '''    public static byte[] doTheHixieHixieShake(final long key1, final long key2, final byte[] key3)
    '''
def setMaxTextMessageSize():
    '''    public void setMaxTextMessageSize(final int size)
    '''
def setMaxIdleTime():
    '''    public void setMaxIdleTime(final int ms)
    '''
def setMaxBinaryMessageSize():
    '''    public void setMaxBinaryMessageSize(final int size)
    '''
def getMaxTextMessageSize():
    '''    public int getMaxTextMessageSize()
    '''
def getMaxIdleTime():
    '''    public int getMaxIdleTime()
    '''
def getMaxBinaryMessageSize():
    '''    public int getMaxBinaryMessageSize()
    '''
def getProtocol():
    '''    public String getProtocol()
    '''
def isMessageComplete():
    '''    public boolean isMessageComplete(final byte flags)
    '''
def binaryOpcode():
    '''    public byte binaryOpcode()
    '''
def textOpcode():
    '''    public byte textOpcode()
    '''
def isControl():
    '''    public boolean isControl(final byte opcode)
    '''
def isText():
    '''    public boolean isText(final byte opcode)
    '''
def isBinary():
    '''    public boolean isBinary(final byte opcode)
    '''
def isContinuation():
    '''    public boolean isContinuation(final byte opcode)
    '''
def isClose():
    '''    public boolean isClose(final byte opcode)
    '''
def isPing():
    '''    public boolean isPing(final byte opcode)
    '''
def isPong():
    '''    public boolean isPong(final byte opcode)
    '''
def getExtensions():
    '''    public List<Extension> getExtensions()
    '''
def continuationOpcode():
    '''    public byte continuationOpcode()
    '''
def finMask():
    '''    public byte finMask()
    '''
def setAllowFrameFragmentation():
    '''    public void setAllowFrameFragmentation(final boolean allowFragmentation)
    '''
def isAllowFrameFragmentation():
    '''    public boolean isAllowFrameFragmentation()
    '''
def onFrame():
    '''    public void onFrame(final byte flags, final byte opcode, final Buffer buffer)
    '''
