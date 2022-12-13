PREFIX = "String  \"ws\""
NAME = "String  \"websocket\""
PROTOCOL_OPTION = "String  \"protocol\""
MESSAGES_PER_FRAME_OPTION = "String  \"messagesPerFrame\""
BUFFER_SIZE_OPTION = "String  \"bufferSize\""
MAX_MESSAGE_SIZE_OPTION = "String  \"maxMessageSize\""
THREAD_POOL_MAX_SIZE = "String  \"threadPoolMaxSize\""
def WebSocketTransport():
    '''public WebSocketTransport(final BayeuxServerImpl bayeux)
    '''
def init():
    '''public void init()
    '''
def accept():
    '''public boolean accept(final HttpServletRequest request)
    '''
def handle():
    '''public void handle(final HttpServletRequest request, final HttpServletResponse response)
    '''
def doWebSocketConnect():
    '''public WebSocket doWebSocketConnect(final HttpServletRequest request, final String protocol)
    '''
def checkOrigin():
    '''public boolean checkOrigin(final HttpServletRequest request, final String origin)
    '''
def getContext():
    '''public BayeuxContext getContext()
    '''
def WebSocketScheduler():
    '''public WebSocketScheduler(final WebSocketContext context, final String userAgent)
    '''
def onOpen():
    '''public void onOpen(final WebSocket.Connection connection)
    '''
def onClose():
    '''public void onClose(final int code, final String reason)
    '''
def onMessage():
    '''public void onMessage(final String data)
    '''
def cancel():
    '''public void cancel()
    '''
def schedule():
    '''public void schedule()
    '''
def run():
    '''public void run()
    public void run()
    '''
def WebSocketContext():
    '''public WebSocketContext(final HttpServletRequest request)
    '''
def getUserPrincipal():
    '''public Principal getUserPrincipal()
    '''
def isUserInRole():
    '''public boolean isUserInRole(final String role)
    '''
def getRemoteAddress():
    '''public InetSocketAddress getRemoteAddress()
    '''
def getLocalAddress():
    '''public InetSocketAddress getLocalAddress()
    '''
def getHeader():
    '''public String getHeader(final String name)
    '''
def getHeaderValues():
    '''public List<String> getHeaderValues(final String name)
    '''
def getParameter():
    '''public String getParameter(final String name)
    '''
def getParameterValues():
    '''public List<String> getParameterValues(final String name)
    '''
def getCookie():
    '''public String getCookie(final String name)
    '''
def getHttpSessionId():
    '''public String getHttpSessionId()
    '''
def getHttpSessionAttribute():
    '''public Object getHttpSessionAttribute(final String name)
    '''
def setHttpSessionAttribute():
    '''public void setHttpSessionAttribute(final String name, final Object value)
    '''
def invalidateHttpSession():
    '''public void invalidateHttpSession()
    '''
def getRequestAttribute():
    '''public Object getRequestAttribute(final String name)
    '''
def getContextAttribute():
    '''public Object getContextAttribute(final String name)
    '''
def getContextInitParameter():
    '''public String getContextInitParameter(final String name)
    '''
def getURL():
    '''public String getURL()
    '''
