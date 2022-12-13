PREFIX = "String  ws""
NAME = "String  websocket""
PROTOCOL_OPTION = "String  protocol""
MESSAGES_PER_FRAME_OPTION = "String  messagesPerFrame""
BUFFER_SIZE_OPTION = "String  bufferSize""
MAX_MESSAGE_SIZE_OPTION = "String  maxMessageSize""
THREAD_POOL_MAX_SIZE = "String  threadPoolMaxSize""
def WebSocketTransport():
'''public WebSocketTransport(final BayeuxServerImpl bayeux)
'''
pass
def init():
'''public void init()
'''
pass
def accept():
'''public boolean accept(final HttpServletRequest request)
'''
pass
def handle():
'''public void handle(final HttpServletRequest request, final HttpServletResponse response)
'''
pass
def doWebSocketConnect():
'''public WebSocket doWebSocketConnect(final HttpServletRequest request, final String protocol)
'''
pass
def checkOrigin():
'''public boolean checkOrigin(final HttpServletRequest request, final String origin)
'''
pass
def getContext():
'''public BayeuxContext getContext()
'''
pass
def WebSocketScheduler():
'''public WebSocketScheduler(final WebSocketContext context, final String userAgent)
'''
pass
def onOpen():
'''public void onOpen(final WebSocket.Connection connection)
'''
pass
def onClose():
'''public void onClose(final int code, final String reason)
'''
pass
def onMessage():
'''public void onMessage(final String data)
'''
pass
def cancel():
'''public void cancel()
'''
pass
def schedule():
'''public void schedule()
'''
pass
def run():
'''public void run()
public void run()
'''
pass
def WebSocketContext():
'''public WebSocketContext(final HttpServletRequest request)
'''
pass
def getUserPrincipal():
'''public Principal getUserPrincipal()
'''
pass
def isUserInRole():
'''public boolean isUserInRole(final String role)
'''
pass
def getRemoteAddress():
'''public InetSocketAddress getRemoteAddress()
'''
pass
def getLocalAddress():
'''public InetSocketAddress getLocalAddress()
'''
pass
def getHeader():
'''public String getHeader(final String name)
'''
pass
def getHeaderValues():
'''public List<String> getHeaderValues(final String name)
'''
pass
def getParameter():
'''public String getParameter(final String name)
'''
pass
def getParameterValues():
'''public List<String> getParameterValues(final String name)
'''
pass
def getCookie():
'''public String getCookie(final String name)
'''
pass
def getHttpSessionId():
'''public String getHttpSessionId()
'''
pass
def getHttpSessionAttribute():
'''public Object getHttpSessionAttribute(final String name)
'''
pass
def setHttpSessionAttribute():
'''public void setHttpSessionAttribute(final String name, final Object value)
'''
pass
def invalidateHttpSession():
'''public void invalidateHttpSession()
'''
pass
def getRequestAttribute():
'''public Object getRequestAttribute(final String name)
'''
pass
def getContextAttribute():
'''public Object getContextAttribute(final String name)
'''
pass
def getContextInitParameter():
'''public String getContextInitParameter(final String name)
'''
pass
def getURL():
'''public String getURL()
'''
pass
