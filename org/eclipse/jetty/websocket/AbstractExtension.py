def AbstractExtension():
    '''public AbstractExtension(final String name)
    '''
def init():
    '''public boolean init(final Map<String, String> parameters)
    '''
def getInitParameter():
    '''public String getInitParameter(final String name)
    public String getInitParameter(final String name, final String dft)
    public int getInitParameter(final String name, final int dft)
    '''
def bind():
    '''public void bind(final WebSocket.FrameConnection connection, final WebSocketParser.FrameHandler incoming, final WebSocketGenerator outgoing)
    '''
def getName():
    '''public String getName()
    '''
def getParameterizedName():
    '''public String getParameterizedName()
    '''
def onFrame():
    '''public void onFrame(final byte flags, final byte opcode, final Buffer buffer)
    '''
def close():
    '''public void close(final int code, final String message)
    '''
def flush():
    '''public int flush()
    '''
def isBufferEmpty():
    '''public boolean isBufferEmpty()
    '''
def addFrame():
    '''public void addFrame(final byte flags, final byte opcode, final byte[] content, final int offset, final int length)
    '''
def setFlag():
    '''public byte setFlag(final byte flags, final int rsv)
    '''
def clearFlag():
    '''public byte clearFlag(final byte flags, final int rsv)
    '''
def isFlag():
    '''public boolean isFlag(final byte flags, final int rsv)
    '''
def toString():
    '''public String toString()
    '''
