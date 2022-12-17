def ():
    '''returns WebSocketFactory\n\n
    (final Acceptor acceptor)\n
    (final Acceptor acceptor, final int bufferSize)\n
    '''
def getMaxIdleTime():
    '''returns long\n\n
    getMaxIdleTime()\n
    '''
def setMaxIdleTime():
    '''returns None\n\n
    setMaxIdleTime(final int maxIdleTime)\n
    '''
def getBufferSize():
    '''returns int\n\n
    getBufferSize()\n
    '''
def setBufferSize():
    '''returns None\n\n
    setBufferSize(final int bufferSize)\n
    '''
def getMaxTextMessageSize():
    '''returns int\n\n
    getMaxTextMessageSize()\n
    '''
def setMaxTextMessageSize():
    '''returns None\n\n
    setMaxTextMessageSize(final int maxTextMessageSize)\n
    '''
def getMaxBinaryMessageSize():
    '''returns int\n\n
    getMaxBinaryMessageSize()\n
    '''
def setMaxBinaryMessageSize():
    '''returns None\n\n
    setMaxBinaryMessageSize(final int maxBinaryMessageSize)\n
    '''
def upgrade():
    '''returns None\n\n
    upgrade(final HttpServletRequest request, final HttpServletResponse response, final WebSocket websocket, final String protocol)\n
    '''
def acceptWebSocket():
    '''returns boolean\n\n
    acceptWebSocket(final HttpServletRequest request, final HttpServletResponse response)\n
    '''
def initExtensions():
    '''returns List<Extension>\n\n
    initExtensions(final List<String> requested, final int maxDataOpcodes, final int maxControlOpcodes, final int maxReservedBits)\n
    '''
