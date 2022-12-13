LENGTH_FRAME = "byte  Byte.MIN_VALUE"
SENTINEL_FRAME = "byte  0"
def WebSocketConnectionD00():
'''public WebSocketConnectionD00(final WebSocket websocket, final EndPoint endpoint, final WebSocketBuffers buffers, final long timestamp, final int maxIdleTime, final String protocol)
'''
pass
def setHixieKeys():
'''public void setHixieKeys(final String key1, final String key2)
'''
pass
def onInputShutdown():
'''public void onInputShutdown()
'''
pass
def isOpen():
'''public boolean isOpen()
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
'''
pass
def sendMessage():
'''public void sendMessage(final String content)
public void sendMessage(final byte[] data, final int offset, final int length)
'''
pass
def isMore():
'''public boolean isMore(final byte flags)
'''
pass
def sendControl():
'''public void sendControl(final byte code, final byte[] content, final int offset, final int length)
'''
pass
def sendFrame():
'''public void sendFrame(final byte flags, final byte opcode, final byte[] content, final int offset, final int length)
'''
pass
def close():
'''public void close(final int code, final String message)
public void close()
public void close(final int code, final String message)
'''
pass
def disconnect():
'''public void disconnect()
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
def doTheHixieHixieShake():
'''public static byte[] doTheHixieHixieShake(final long key1, final long key2, final byte[] key3)
'''
pass
def setMaxTextMessageSize():
'''public void setMaxTextMessageSize(final int size)
'''
pass
def setMaxIdleTime():
'''public void setMaxIdleTime(final int ms)
'''
pass
def setMaxBinaryMessageSize():
'''public void setMaxBinaryMessageSize(final int size)
'''
pass
def getMaxTextMessageSize():
'''public int getMaxTextMessageSize()
'''
pass
def getMaxIdleTime():
'''public int getMaxIdleTime()
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
def isMessageComplete():
'''public boolean isMessageComplete(final byte flags)
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
def getExtensions():
'''public List<Extension> getExtensions()
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
