def CloseWebSocketFrame():
    '''    public CloseWebSocketFrame()
    public CloseWebSocketFrame(final WebSocketCloseStatus status)
    public CloseWebSocketFrame(final WebSocketCloseStatus status, final String reasonText)
    public CloseWebSocketFrame(final int statusCode, final String reasonText)
    public CloseWebSocketFrame(final boolean finalFragment, final int rsv)
    public CloseWebSocketFrame(final boolean finalFragment, final int rsv, final int statusCode, final String reasonText)
    public CloseWebSocketFrame(final boolean finalFragment, final int rsv, final ByteBuf binaryData)
    '''
def statusCode():
    '''    public int statusCode()
    '''
def reasonText():
    '''    public String reasonText()
    '''
def copy():
    '''    public CloseWebSocketFrame copy()
    '''
def duplicate():
    '''    public CloseWebSocketFrame duplicate()
    '''
def retainedDuplicate():
    '''    public CloseWebSocketFrame retainedDuplicate()
    '''
def replace():
    '''    public CloseWebSocketFrame replace(final ByteBuf content)
    '''
def retain():
    '''    public CloseWebSocketFrame retain()
    public CloseWebSocketFrame retain(final int increment)
    '''
def touch():
    '''    public CloseWebSocketFrame touch()
    public CloseWebSocketFrame touch(final Object hint)
    '''
