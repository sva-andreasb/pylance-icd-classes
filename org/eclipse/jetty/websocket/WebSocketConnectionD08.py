def WebSocketConnectionD08():
'''public WebSocketConnectionD08(final WebSocket websocket, final EndPoint endpoint, final WebSocketBuffers buffers, final long timestamp, final int maxIdleTime, final String protocol, final List<Extension> extensions, final int draft)
public WebSocketConnectionD08(final WebSocket websocket, final EndPoint endpoint, final WebSocketBuffers buffers, final long timestamp, final int maxIdleTime, final String protocol, final List<Extension> extensions, final int draft, final MaskGen maskgen)
'''
pass
def getExtensions():
'''public List<Extension> getExtensions()
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
def onIdleExpired():
'''public void onIdleExpired(final long idleForMs)
'''
pass
def isSuspended():
'''public boolean isSuspended()
'''
pass
def onClose():
'''public void onClose()
'''
pass
def closeIn():
'''public void closeIn(final int code, final String message)
'''
pass
def closeOut():
'''public void closeOut(int code, final String message)
'''
pass
def shutdown():
'''public void shutdown()
'''
pass
def fillBuffersFrom():
'''public void fillBuffersFrom(final Buffer buffer)
'''
pass
def hashKey():
'''public static String hashKey(final String key)
'''
pass
def toString():
'''public String toString()
public String toString()
public String toString()
'''
pass
def sendMessage():
'''public void sendMessage(final String content)
public void sendMessage(final byte[] content, final int offset, final int length)
'''
pass
def sendFrame():
'''public void sendFrame(final byte flags, final byte opcode, final byte[] content, final int offset, final int length)
'''
pass
def sendControl():
'''public void sendControl(final byte ctrl, final byte[] data, final int offset, final int length)
'''
pass
def isMessageComplete():
'''public boolean isMessageComplete(final byte flags)
'''
pass
def isOpen():
'''public boolean isOpen()
'''
pass
def close():
'''public void close(final int code, final String message)
public void close()
public void close(final int code, final String message)
'''
pass
def setMaxIdleTime():
'''public void setMaxIdleTime(final int ms)
'''
pass
def setMaxTextMessageSize():
'''public void setMaxTextMessageSize(final int size)
'''
pass
def setMaxBinaryMessageSize():
'''public void setMaxBinaryMessageSize(final int size)
'''
pass
def getMaxIdleTime():
'''public int getMaxIdleTime()
'''
pass
def getMaxTextMessageSize():
'''public int getMaxTextMessageSize()
'''
pass
def getMaxBinaryMessageSize():
'''public int getMaxBinaryMessageSize()
'''
pass
def getProtocol():
'''public String getProtocol()
'''
pass
def binaryOpcode():
'''public byte binaryOpcode()
'''
pass
def textOpcode():
'''public byte textOpcode()
'''
pass
def continuationOpcode():
'''public byte continuationOpcode()
'''
pass
def finMask():
'''public byte finMask()
'''
pass
def isControl():
'''public boolean isControl(final byte opcode)
'''
pass
def isText():
'''public boolean isText(final byte opcode)
'''
pass
def isBinary():
'''public boolean isBinary(final byte opcode)
'''
pass
def isContinuation():
'''public boolean isContinuation(final byte opcode)
'''
pass
def isClose():
'''public boolean isClose(final byte opcode)
'''
pass
def isPing():
'''public boolean isPing(final byte opcode)
'''
pass
def isPong():
'''public boolean isPong(final byte opcode)
'''
pass
def disconnect():
'''public void disconnect()
'''
pass
def setAllowFrameFragmentation():
'''public void setAllowFrameFragmentation(final boolean allowFragmentation)
'''
pass
def isAllowFrameFragmentation():
'''public boolean isAllowFrameFragmentation()
'''
pass
def onFrame():
'''public void onFrame(final byte flags, final byte opcode, final Buffer buffer)
'''
pass
