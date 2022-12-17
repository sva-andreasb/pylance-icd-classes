PREFIX = "String  \"ws\""
NAME = "String  \"websocket\""
PROTOCOL_OPTION = "String  \"protocol\""
MESSAGES_PER_FRAME_OPTION = "String  \"messagesPerFrame\""
BUFFER_SIZE_OPTION = "String  \"bufferSize\""
MAX_MESSAGE_SIZE_OPTION = "String  \"maxMessageSize\""
THREAD_POOL_MAX_SIZE = "String  \"threadPoolMaxSize\""
def ():
    '''returns WebSocketContext\n\n
    (final BayeuxServerImpl bayeux)\n
    (final WebSocketContext context, final String userAgent)\n
    (final HttpServletRequest request)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final HttpServletRequest request)\n
    '''
def handle():
    '''returns None\n\n
    handle(final HttpServletRequest request, final HttpServletResponse response)\n
    '''
def doWebSocketConnect():
    '''returns WebSocket\n\n
    doWebSocketConnect(final HttpServletRequest request, final String protocol)\n
    '''
def checkOrigin():
    '''returns boolean\n\n
    checkOrigin(final HttpServletRequest request, final String origin)\n
    '''
def getContext():
    '''returns BayeuxContext\n\n
    getContext()\n
    '''
def onOpen():
    '''returns None\n\n
    onOpen(final WebSocket.Connection connection)\n
    '''
def onClose():
    '''returns None\n\n
    onClose(final int code, final String reason)\n
    '''
def onMessage():
    '''returns None\n\n
    onMessage(final String data)\n
    '''
def cancel():
    '''returns None\n\n
    cancel()\n
    '''
def schedule():
    '''returns None\n\n
    schedule()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def getUserPrincipal():
    '''returns Principal\n\n
    getUserPrincipal()\n
    '''
def isUserInRole():
    '''returns boolean\n\n
    isUserInRole(final String role)\n
    '''
def getRemoteAddress():
    '''returns InetSocketAddress\n\n
    getRemoteAddress()\n
    '''
def getLocalAddress():
    '''returns InetSocketAddress\n\n
    getLocalAddress()\n
    '''
def getHeader():
    '''returns String\n\n
    getHeader(final String name)\n
    '''
def getHeaderValues():
    '''returns List<String>\n\n
    getHeaderValues(final String name)\n
    '''
def getParameter():
    '''returns String\n\n
    getParameter(final String name)\n
    '''
def getParameterValues():
    '''returns List<String>\n\n
    getParameterValues(final String name)\n
    '''
def getCookie():
    '''returns String\n\n
    getCookie(final String name)\n
    '''
def getHttpSessionId():
    '''returns String\n\n
    getHttpSessionId()\n
    '''
def getHttpSessionAttribute():
    '''returns Object\n\n
    getHttpSessionAttribute(final String name)\n
    '''
def setHttpSessionAttribute():
    '''returns None\n\n
    setHttpSessionAttribute(final String name, final Object value)\n
    '''
def invalidateHttpSession():
    '''returns None\n\n
    invalidateHttpSession()\n
    '''
def getRequestAttribute():
    '''returns Object\n\n
    getRequestAttribute(final String name)\n
    '''
def getContextAttribute():
    '''returns Object\n\n
    getContextAttribute(final String name)\n
    '''
def getContextInitParameter():
    '''returns String\n\n
    getContextInitParameter(final String name)\n
    '''
def getURL():
    '''returns String\n\n
    getURL()\n
    '''
