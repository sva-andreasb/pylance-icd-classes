def ():
    '''returns WebSocketConnectionRFC6455\n\n
    (final WebSocket websocket, final EndPoint endpoint, final WebSocketBuffers buffers, final long timestamp, final int maxIdleTime, final String protocol, final List<Extension> extensions, final int draft)\n
    (final WebSocket websocket, final EndPoint endpoint, final WebSocketBuffers buffers, final long timestamp, final int maxIdleTime, final String protocol, final List<Extension> extensions, final int draft, final MaskGen maskgen)\n
    '''
def getExtensions():
    '''returns List<Extension>\n\n
    getExtensions()\n
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
def onIdleExpired():
    '''returns None\n\n
    onIdleExpired(final long idleForMs)\n
    '''
def isSuspended():
    '''returns boolean\n\n
    isSuspended()\n
    '''
def onClose():
    '''returns None\n\n
    onClose()\n
    '''
def closeIn():
    '''returns None\n\n
    closeIn(final int code, final String message)\n
    '''
def closeOut():
    '''returns None\n\n
    closeOut(int code, final String message)\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def fillBuffersFrom():
    '''returns None\n\n
    fillBuffersFrom(final Buffer buffer)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    toString()\n
    '''
def sendMessage():
    '''returns None\n\n
    sendMessage(final String content)\n
    sendMessage(final byte[] content, final int offset, final int length)\n
    '''
def sendFrame():
    '''returns None\n\n
    sendFrame(final byte flags, final byte opcode, final byte[] content, final int offset, final int length)\n
    '''
def sendControl():
    '''returns None\n\n
    sendControl(final byte ctrl, final byte[] data, final int offset, final int length)\n
    '''
def isMessageComplete():
    '''returns boolean\n\n
    isMessageComplete(final byte flags)\n
    '''
def isOpen():
    '''returns boolean\n\n
    isOpen()\n
    '''
def close():
    '''returns None\n\n
    close(final int code, final String message)\n
    close()\n
    close(final int code, final String message)\n
    '''
def setMaxIdleTime():
    '''returns None\n\n
    setMaxIdleTime(final int ms)\n
    '''
def setMaxTextMessageSize():
    '''returns None\n\n
    setMaxTextMessageSize(final int size)\n
    '''
def setMaxBinaryMessageSize():
    '''returns None\n\n
    setMaxBinaryMessageSize(final int size)\n
    '''
def getMaxIdleTime():
    '''returns int\n\n
    getMaxIdleTime()\n
    '''
def getMaxTextMessageSize():
    '''returns int\n\n
    getMaxTextMessageSize()\n
    '''
def getMaxBinaryMessageSize():
    '''returns int\n\n
    getMaxBinaryMessageSize()\n
    '''
def getProtocol():
    '''returns String\n\n
    getProtocol()\n
    '''
def binaryOpcode():
    '''returns byte\n\n
    binaryOpcode()\n
    '''
def textOpcode():
    '''returns byte\n\n
    textOpcode()\n
    '''
def continuationOpcode():
    '''returns byte\n\n
    continuationOpcode()\n
    '''
def finMask():
    '''returns byte\n\n
    finMask()\n
    '''
def isControl():
    '''returns boolean\n\n
    isControl(final byte opcode)\n
    '''
def isText():
    '''returns boolean\n\n
    isText(final byte opcode)\n
    '''
def isBinary():
    '''returns boolean\n\n
    isBinary(final byte opcode)\n
    '''
def isContinuation():
    '''returns boolean\n\n
    isContinuation(final byte opcode)\n
    '''
def isClose():
    '''returns boolean\n\n
    isClose(final byte opcode)\n
    '''
def isPing():
    '''returns boolean\n\n
    isPing(final byte opcode)\n
    '''
def isPong():
    '''returns boolean\n\n
    isPong(final byte opcode)\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect()\n
    '''
def setAllowFrameFragmentation():
    '''returns None\n\n
    setAllowFrameFragmentation(final boolean allowFragmentation)\n
    '''
def isAllowFrameFragmentation():
    '''returns boolean\n\n
    isAllowFrameFragmentation()\n
    '''
def onFrame():
    '''returns None\n\n
    onFrame(final byte flags, final byte opcode, final Buffer buffer)\n
    '''
