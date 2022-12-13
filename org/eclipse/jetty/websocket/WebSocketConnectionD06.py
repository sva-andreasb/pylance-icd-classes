def WebSocketConnectionD06():
    '''    public WebSocketConnectionD06(final WebSocket websocket, final EndPoint endpoint, final WebSocketBuffers buffers, final long timestamp, final int maxIdleTime, final String protocol)
    '''
def handle():
    '''    public Connection handle()
    '''
def onInputShutdown():
    '''    public void onInputShutdown()
    '''
def isIdle():
    '''    public boolean isIdle()
    '''
def onIdleExpired():
    '''    public void onIdleExpired(final long idleForMs)
    '''
def isSuspended():
    '''    public boolean isSuspended()
    '''
def onClose():
    '''    public void onClose()
    '''
def closeIn():
    '''    public synchronized void closeIn(final int code, final String message)
    '''
def closeOut():
    '''    public synchronized void closeOut(int code, final String message)
    '''
def shutdown():
    '''    public void shutdown()
    '''
def fillBuffersFrom():
    '''    public void fillBuffersFrom(final Buffer buffer)
    '''
def getExtensions():
    '''    public List<Extension> getExtensions()
    '''
def hashKey():
    '''    public static String hashKey(final String key)
    '''
def sendMessage():
    '''    public synchronized void sendMessage(final String content)
    public synchronized void sendMessage(final byte[] content, final int offset, final int length)
    '''
def sendFrame():
    '''    public void sendFrame(final byte flags, final byte opcode, final byte[] content, final int offset, final int length)
    '''
def sendControl():
    '''    public void sendControl(final byte control, final byte[] data, final int offset, final int length)
    '''
def isMessageComplete():
    '''    public boolean isMessageComplete(final byte flags)
    '''
def isOpen():
    '''    public boolean isOpen()
    '''
def close():
    '''    public void close(final int code, final String message)
    public void close()
    public void close(final int code, final String message)
    '''
def setMaxIdleTime():
    '''    public void setMaxIdleTime(final int ms)
    '''
def setMaxTextMessageSize():
    '''    public void setMaxTextMessageSize(final int size)
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
def binaryOpcode():
    '''    public byte binaryOpcode()
    '''
def textOpcode():
    '''    public byte textOpcode()
    '''
def continuationOpcode():
    '''    public byte continuationOpcode()
    '''
def finMask():
    '''    public byte finMask()
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
def disconnect():
    '''    public void disconnect()
    '''
def toString():
    '''    public String toString()
    public String toString()
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
