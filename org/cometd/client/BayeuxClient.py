BACKOFF_INCREMENT_OPTION = "String  \"backoffIncrement\""
MAX_BACKOFF_OPTION = "String  \"maxBackoff\""
BAYEUX_VERSION = "String  \"1.0\""
def ():
    '''returns RehandshakingState\n\n
    (final String url, final ClientTransport transport, final ClientTransport... transports)\n
    (final String url, final ScheduledExecutorService scheduler, final ClientTransport transport, final ClientTransport... transports)\n
    (final Map<String, Object> handshakeFields, final ClientTransport transport, final long backoff)\n
    '''
def getBackoffIncrement():
    '''returns long\n\n
    getBackoffIncrement()\n
    '''
def getMaxBackoff():
    '''returns long\n\n
    getMaxBackoff()\n
    '''
def getCookie():
    '''returns String\n\n
    getCookie(final String name)\n
    '''
def setCookie():
    '''returns None\n\n
    setCookie(final String name, final String value)\n
    setCookie(final String name, final String value, final int maxAge)\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def isHandshook():
    '''returns boolean\n\n
    isHandshook()\n
    '''
def isConnected():
    '''returns boolean\n\n
    isConnected()\n
    '''
def isDisconnected():
    '''returns boolean\n\n
    isDisconnected()\n
    '''
def handshake():
    '''returns State\n\n
    handshake()\n
    handshake(final Map<String, Object> handshakeFields)\n
    handshake(final long waitMs)\n
    handshake(final Map<String, Object> template, final long waitMs)\n
    '''
def create():
    '''returns BayeuxClientState\n\n
    create(final BayeuxClientState oldState)\n
    create(final BayeuxClientState oldState)\n
    create(final BayeuxClientState oldState)\n
    create(final BayeuxClientState oldState)\n
    create(final BayeuxClientState oldState)\n
    create(final BayeuxClientState oldState)\n
    create(final BayeuxClientState oldState)\n
    create(final BayeuxClientState oldState)\n
    create(final BayeuxClientState oldState)\n
    create(final BayeuxClientState oldState)\n
    create(final BayeuxClientState oldState)\n
    '''
def waitFor():
    '''returns boolean\n\n
    waitFor(final long waitMs, final State state, final State... states)\n
    '''
def disconnect():
    '''returns boolean\n\n
    disconnect()\n
    disconnect(final long timeout)\n
    '''
def onMessage():
    '''returns None\n\n
    onMessage(final ClientSessionChannel channel, final Message message)\n
    '''
def abort():
    '''returns None\n\n
    abort()\n
    '''
def postCreate():
    '''returns None\n\n
    postCreate()\n
    postCreate()\n
    postCreate()\n
    postCreate()\n
    postCreate()\n
    postCreate()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def getAllowedTransports():
    '''returns List<String>\n\n
    getAllowedTransports()\n
    '''
def getKnownTransportNames():
    '''returns Set<String>\n\n
    getKnownTransportNames()\n
    '''
def getTransport():
    '''returns ClientTransport\n\n
    getTransport(final String transport)\n
    getTransport()\n
    '''
def setDebugEnabled():
    '''returns None\n\n
    setDebugEnabled(final boolean debug)\n
    '''
def isDebugEnabled():
    '''returns boolean\n\n
    isDebugEnabled()\n
    '''
def getOption():
    '''returns Object\n\n
    getOption(final String qualifiedName)\n
    '''
def setOption():
    '''returns None\n\n
    setOption(final String qualifiedName, final Object value)\n
    '''
def getOptionNames():
    '''returns Set<String>\n\n
    getOptionNames()\n
    '''
def onSending():
    '''returns None\n\n
    onSending(final Message[] messages)\n
    onSending(final Message[] messages)\n
    '''
def onMessages():
    '''returns None\n\n
    onMessages(final List<Message.Mutable> messages)\n
    onMessages(final List<Message.Mutable> messages)\n
    '''
def onFailure():
    '''returns None\n\n
    onFailure(final Throwable x, final Message[] messages)\n
    '''
def dump():
    '''returns String\n\n
    dump()\n
    '''
def onConnectException():
    '''returns None\n\n
    onConnectException(final Throwable x, final Message[] messages)\n
    '''
def onException():
    '''returns None\n\n
    onException(final Throwable x, final Message[] messages)\n
    '''
def onExpire():
    '''returns None\n\n
    onExpire(final Message[] messages)\n
    '''
def onProtocolError():
    '''returns None\n\n
    onProtocolError(final String info, final Message[] messages)\n
    '''
def getSession():
    '''returns ClientSession\n\n
    getSession()\n
    '''
def publish():
    '''returns None\n\n
    publish(final Object data)\n
    publish(final Object data, final String messageId)\n
    '''
def getType():
    '''returns State\n\n
    getType()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
