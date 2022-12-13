PREFIX = "String  \"ws\""
NAME = "String  \"websocket\""
PROTOCOL_OPTION = "String  \"protocol\""
CONNECT_TIMEOUT_OPTION = "String  \"connectTimeout\""
IDLE_TIMEOUT_OPTION = "String  \"idleTimeout\""
MAX_MESSAGE_SIZE_OPTION = "String  \"maxMessageSize\""
UNIQUE_MESSAGE_ID_GUARANTEED_OPTION = "String  \"uniqueMessageIdGuaranteed\""
def create():
    '''    public static WebSocketTransport create(final Map<String, Object> options, final WebSocketClientFactory webSocketClientFactory)
    public static WebSocketTransport create(final Map<String, Object> options, final WebSocketClientFactory webSocketClientFactory, final ScheduledExecutorService scheduler)
    '''
def WebSocketTransport():
    '''    public WebSocketTransport(final Map<String, Object> options, final WebSocketClientFactory webSocketClientFactory, final ScheduledExecutorService scheduler)
    '''
def setMessageTransportListener():
    '''    public void setMessageTransportListener(final TransportListener listener)
    '''
def accept():
    '''    public boolean accept(final String version)
    '''
def init():
    '''    public void init()
    '''
def abort():
    '''    public void abort()
    '''
def reset():
    '''    public void reset()
    '''
def terminate():
    '''    public void terminate()
    '''
def send():
    '''    public void send(final TransportListener listener, final Message.Mutable... messages)
    '''
def run():
    '''    public void run()
    '''
def onOpen():
    '''    public void onOpen(final WebSocket.Connection connection)
    '''
def onClose():
    '''    public void onClose(final int closeCode, final String message)
    '''
def onMessage():
    '''    public void onMessage(final String data)
    '''
def WebSocketExchange():
    '''    public WebSocketExchange(final Message.Mutable message, final TransportListener listener, final ScheduledFuture<?> task)
    '''
def toString():
    '''    public String toString()
    '''
