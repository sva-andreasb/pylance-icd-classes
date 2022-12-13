PREFIX = "String  ws""
NAME = "String  websocket""
PROTOCOL_OPTION = "String  protocol""
CONNECT_TIMEOUT_OPTION = "String  connectTimeout""
IDLE_TIMEOUT_OPTION = "String  idleTimeout""
MAX_MESSAGE_SIZE_OPTION = "String  maxMessageSize""
UNIQUE_MESSAGE_ID_GUARANTEED_OPTION = "String  uniqueMessageIdGuaranteed""
def create():
'''public static WebSocketTransport create(final Map<String, Object> options, final WebSocketClientFactory webSocketClientFactory)
public static WebSocketTransport create(final Map<String, Object> options, final WebSocketClientFactory webSocketClientFactory, final ScheduledExecutorService scheduler)
'''
pass
def WebSocketTransport():
'''public WebSocketTransport(final Map<String, Object> options, final WebSocketClientFactory webSocketClientFactory, final ScheduledExecutorService scheduler)
'''
pass
def setMessageTransportListener():
'''public void setMessageTransportListener(final TransportListener listener)
'''
pass
def accept():
'''public boolean accept(final String version)
'''
pass
def init():
'''public void init()
'''
pass
def abort():
'''public void abort()
'''
pass
def reset():
'''public void reset()
'''
pass
def terminate():
'''public void terminate()
'''
pass
def send():
'''public void send(final TransportListener listener, final Message.Mutable... messages)
'''
pass
def run():
'''public void run()
'''
pass
def onOpen():
'''public void onOpen(final WebSocket.Connection connection)
'''
pass
def onClose():
'''public void onClose(final int closeCode, final String message)
'''
pass
def onMessage():
'''public void onMessage(final String data)
'''
pass
def WebSocketExchange():
'''public WebSocketExchange(final Message.Mutable message, final TransportListener listener, final ScheduledFuture<?> task)
'''
pass
def toString():
'''public String toString()
'''
pass
