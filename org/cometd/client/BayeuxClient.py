BACKOFF_INCREMENT_OPTION = "String  \"backoffIncrement\""
MAX_BACKOFF_OPTION = "String  \"maxBackoff\""
BAYEUX_VERSION = "String  \"1.0\""
def BayeuxClient():
    '''public BayeuxClient(final String url, final ClientTransport transport, final ClientTransport... transports)
    public BayeuxClient(final String url, final ScheduledExecutorService scheduler, final ClientTransport transport, final ClientTransport... transports)
    '''
def getBackoffIncrement():
    '''public long getBackoffIncrement()
    '''
def getMaxBackoff():
    '''public long getMaxBackoff()
    '''
def getCookie():
    '''public String getCookie(final String name)
    '''
def setCookie():
    '''public void setCookie(final String name, final String value)
    public void setCookie(final String name, final String value, final int maxAge)
    '''
def getId():
    '''public String getId()
    '''
def isHandshook():
    '''public boolean isHandshook()
    '''
def isConnected():
    '''public boolean isConnected()
    '''
def isDisconnected():
    '''public boolean isDisconnected()
    '''
def handshake():
    '''public void handshake()
    public void handshake(final Map<String, Object> handshakeFields)
    public State handshake(final long waitMs)
    public State handshake(final Map<String, Object> template, final long waitMs)
    '''
def create():
    '''public BayeuxClientState create(final BayeuxClientState oldState)
    public BayeuxClientState create(final BayeuxClientState oldState)
    public BayeuxClientState create(final BayeuxClientState oldState)
    public BayeuxClientState create(final BayeuxClientState oldState)
    public BayeuxClientState create(final BayeuxClientState oldState)
    public BayeuxClientState create(final BayeuxClientState oldState)
    public BayeuxClientState create(final BayeuxClientState oldState)
    public BayeuxClientState create(final BayeuxClientState oldState)
    public BayeuxClientState create(final BayeuxClientState oldState)
    public BayeuxClientState create(final BayeuxClientState oldState)
    public BayeuxClientState create(final BayeuxClientState oldState)
    '''
def waitFor():
    '''public boolean waitFor(final long waitMs, final State state, final State... states)
    '''
def disconnect():
    '''public void disconnect()
    public boolean disconnect(final long timeout)
    '''
def onMessage():
    '''public void onMessage(final ClientSessionChannel channel, final Message message)
    '''
def abort():
    '''public void abort()
    '''
def postCreate():
    '''public void postCreate()
    public void postCreate()
    public void postCreate()
    public void postCreate()
    public void postCreate()
    public void postCreate()
    '''
def run():
    '''public void run()
    public void run()
    '''
def getAllowedTransports():
    '''public List<String> getAllowedTransports()
    '''
def getKnownTransportNames():
    '''public Set<String> getKnownTransportNames()
    '''
def getTransport():
    '''public ClientTransport getTransport(final String transport)
    public ClientTransport getTransport()
    '''
def setDebugEnabled():
    '''public void setDebugEnabled(final boolean debug)
    '''
def isDebugEnabled():
    '''public boolean isDebugEnabled()
    '''
def getOption():
    '''public Object getOption(final String qualifiedName)
    '''
def setOption():
    '''public void setOption(final String qualifiedName, final Object value)
    '''
def getOptionNames():
    '''public Set<String> getOptionNames()
    '''
def getOptions():
    '''public Map<String, Object> getOptions()
    '''
def onSending():
    '''public void onSending(final Message[] messages)
    public void onSending(final Message[] messages)
    '''
def onMessages():
    '''public void onMessages(final List<Message.Mutable> messages)
    public void onMessages(final List<Message.Mutable> messages)
    '''
def onFailure():
    '''public void onFailure(final Throwable x, final Message[] messages)
    '''
def dump():
    '''public String dump()
    '''
def onConnectException():
    '''public void onConnectException(final Throwable x, final Message[] messages)
    '''
def onException():
    '''public void onException(final Throwable x, final Message[] messages)
    '''
def onExpire():
    '''public void onExpire(final Message[] messages)
    '''
def onProtocolError():
    '''public void onProtocolError(final String info, final Message[] messages)
    '''
def getSession():
    '''public ClientSession getSession()
    '''
def publish():
    '''public void publish(final Object data)
    public void publish(final Object data, final String messageId)
    '''
def getType():
    '''public State getType()
    '''
def toString():
    '''public String toString()
    '''
def RehandshakingState():
    '''public RehandshakingState(final Map<String, Object> handshakeFields, final ClientTransport transport, final long backoff)
    '''
