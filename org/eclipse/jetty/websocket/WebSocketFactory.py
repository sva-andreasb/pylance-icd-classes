def WebSocketFactory():
'''public WebSocketFactory(final Acceptor acceptor)
public WebSocketFactory(final Acceptor acceptor, final int bufferSize)
'''
pass
def getMaxIdleTime():
'''public long getMaxIdleTime()
'''
pass
def setMaxIdleTime():
'''public void setMaxIdleTime(final int maxIdleTime)
'''
pass
def getBufferSize():
'''public int getBufferSize()
'''
pass
def setBufferSize():
'''public void setBufferSize(final int bufferSize)
'''
pass
def getMaxTextMessageSize():
'''public int getMaxTextMessageSize()
'''
pass
def setMaxTextMessageSize():
'''public void setMaxTextMessageSize(final int maxTextMessageSize)
'''
pass
def getMaxBinaryMessageSize():
'''public int getMaxBinaryMessageSize()
'''
pass
def setMaxBinaryMessageSize():
'''public void setMaxBinaryMessageSize(final int maxBinaryMessageSize)
'''
pass
def upgrade():
'''public void upgrade(final HttpServletRequest request, final HttpServletResponse response, final WebSocket websocket, final String protocol)
'''
pass
def acceptWebSocket():
'''public boolean acceptWebSocket(final HttpServletRequest request, final HttpServletResponse response)
'''
pass
def initExtensions():
'''public List<Extension> initExtensions(final List<String> requested, final int maxDataOpcodes, final int maxControlOpcodes, final int maxReservedBits)
'''
pass
