def ():
    '''returns AbstractExtension\n\n
    (final String name)\n
    '''
def init():
    '''returns boolean\n\n
    init(final Map<String, String> parameters)\n
    '''
def getInitParameter():
    '''returns int\n\n
    getInitParameter(final String name)\n
    getInitParameter(final String name, final String dft)\n
    getInitParameter(final String name, final int dft)\n
    '''
def bind():
    '''returns None\n\n
    bind(final WebSocket.FrameConnection connection, final WebSocketParser.FrameHandler incoming, final WebSocketGenerator outgoing)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getParameterizedName():
    '''returns String\n\n
    getParameterizedName()\n
    '''
def onFrame():
    '''returns None\n\n
    onFrame(final byte flags, final byte opcode, final Buffer buffer)\n
    '''
def close():
    '''returns None\n\n
    close(final int code, final String message)\n
    '''
def flush():
    '''returns int\n\n
    flush()\n
    '''
def isBufferEmpty():
    '''returns boolean\n\n
    isBufferEmpty()\n
    '''
def addFrame():
    '''returns None\n\n
    addFrame(final byte flags, final byte opcode, final byte[] content, final int offset, final int length)\n
    '''
def setFlag():
    '''returns byte\n\n
    setFlag(final byte flags, final int rsv)\n
    '''
def clearFlag():
    '''returns byte\n\n
    clearFlag(final byte flags, final int rsv)\n
    '''
def isFlag():
    '''returns boolean\n\n
    isFlag(final byte flags, final int rsv)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
