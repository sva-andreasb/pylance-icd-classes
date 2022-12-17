PREFIX = "String  \"ws\""
NAME = "String  \"websocket\""
PROTOCOL_OPTION = "String  \"protocol\""
CONNECT_TIMEOUT_OPTION = "String  \"connectTimeout\""
IDLE_TIMEOUT_OPTION = "String  \"idleTimeout\""
MAX_MESSAGE_SIZE_OPTION = "String  \"maxMessageSize\""
UNIQUE_MESSAGE_ID_GUARANTEED_OPTION = "String  \"uniqueMessageIdGuaranteed\""
def ():
    '''returns WebSocketExchange\n\n
    (final Map<String, Object> options, final WebSocketClientFactory webSocketClientFactory, final ScheduledExecutorService scheduler)\n
    (final Message.Mutable message, final TransportListener listener, final ScheduledFuture<?> task)\n
    '''
def setMessageTransportListener():
    '''returns None\n\n
    setMessageTransportListener(final TransportListener listener)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final String version)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def abort():
    '''returns None\n\n
    abort()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def terminate():
    '''returns None\n\n
    terminate()\n
    '''
def send():
    '''returns None\n\n
    send(final TransportListener listener, final Message.Mutable... messages)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def onOpen():
    '''returns None\n\n
    onOpen(final WebSocket.Connection connection)\n
    '''
def onClose():
    '''returns None\n\n
    onClose(final int closeCode, final String message)\n
    '''
def onMessage():
    '''returns None\n\n
    onMessage(final String data)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
