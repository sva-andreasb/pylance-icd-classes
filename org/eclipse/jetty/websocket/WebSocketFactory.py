def WebSocketFactory():
    '''    public WebSocketFactory(final Acceptor acceptor)
    public WebSocketFactory(final Acceptor acceptor, final int bufferSize)
    '''
def getMaxIdleTime():
    '''    public long getMaxIdleTime()
    '''
def setMaxIdleTime():
    '''    public void setMaxIdleTime(final int maxIdleTime)
    '''
def getBufferSize():
    '''    public int getBufferSize()
    '''
def setBufferSize():
    '''    public void setBufferSize(final int bufferSize)
    '''
def getMaxTextMessageSize():
    '''    public int getMaxTextMessageSize()
    '''
def setMaxTextMessageSize():
    '''    public void setMaxTextMessageSize(final int maxTextMessageSize)
    '''
def getMaxBinaryMessageSize():
    '''    public int getMaxBinaryMessageSize()
    '''
def setMaxBinaryMessageSize():
    '''    public void setMaxBinaryMessageSize(final int maxBinaryMessageSize)
    '''
def upgrade():
    '''    public void upgrade(final HttpServletRequest request, final HttpServletResponse response, final WebSocket websocket, final String protocol)
    '''
def acceptWebSocket():
    '''    public boolean acceptWebSocket(final HttpServletRequest request, final HttpServletResponse response)
    '''
def initExtensions():
    '''    public List<Extension> initExtensions(final List<String> requested, final int maxDataOpcodes, final int maxControlOpcodes, final int maxReservedBits)
    '''
