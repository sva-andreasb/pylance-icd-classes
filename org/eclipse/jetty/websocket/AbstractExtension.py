def AbstractExtension():
'''public AbstractExtension(final String name)
'''
pass
def init():
'''public boolean init(final Map<String, String> parameters)
'''
pass
def getInitParameter():
'''public String getInitParameter(final String name)
public String getInitParameter(final String name, final String dft)
public int getInitParameter(final String name, final int dft)
'''
pass
def bind():
'''public void bind(final WebSocket.FrameConnection connection, final WebSocketParser.FrameHandler incoming, final WebSocketGenerator outgoing)
'''
pass
def getName():
'''public String getName()
'''
pass
def getParameterizedName():
'''public String getParameterizedName()
'''
pass
def onFrame():
'''public void onFrame(final byte flags, final byte opcode, final Buffer buffer)
'''
pass
def close():
'''public void close(final int code, final String message)
'''
pass
def flush():
'''public int flush()
'''
pass
def isBufferEmpty():
'''public boolean isBufferEmpty()
'''
pass
def addFrame():
'''public void addFrame(final byte flags, final byte opcode, final byte[] content, final int offset, final int length)
'''
pass
def setFlag():
'''public byte setFlag(final byte flags, final int rsv)
'''
pass
def clearFlag():
'''public byte clearFlag(final byte flags, final int rsv)
'''
pass
def isFlag():
'''public boolean isFlag(final byte flags, final int rsv)
'''
pass
def toString():
'''public String toString()
'''
pass
