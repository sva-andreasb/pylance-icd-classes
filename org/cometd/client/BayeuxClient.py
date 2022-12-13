BACKOFF_INCREMENT_OPTION = "String  backoffIncrement""
MAX_BACKOFF_OPTION = "String  maxBackoff""
BAYEUX_VERSION = "String  1.0""
def BayeuxClient():
'''public BayeuxClient(final String url, final ClientTransport transport, final ClientTransport... transports)
public BayeuxClient(final String url, final ScheduledExecutorService scheduler, final ClientTransport transport, final ClientTransport... transports)
'''
pass
def getBackoffIncrement():
'''public long getBackoffIncrement()
'''
pass
def getMaxBackoff():
'''public long getMaxBackoff()
'''
pass
def getCookie():
'''public String getCookie(final String name)
'''
pass
def setCookie():
'''public void setCookie(final String name, final String value)
public void setCookie(final String name, final String value, final int maxAge)
'''
pass
def getId():
'''public String getId()
'''
pass
def isHandshook():
'''public boolean isHandshook()
'''
pass
def isConnected():
'''public boolean isConnected()
'''
pass
def isDisconnected():
'''public boolean isDisconnected()
'''
pass
def handshake():
'''public void handshake()
public void handshake(final Map<String, Object> handshakeFields)
public State handshake(final long waitMs)
public State handshake(final Map<String, Object> template, final long waitMs)
'''
pass
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
pass
def waitFor():
'''public boolean waitFor(final long waitMs, final State state, final State... states)
'''
pass
def disconnect():
'''public void disconnect()
public boolean disconnect(final long timeout)
'''
pass
def onMessage():
'''public void onMessage(final ClientSessionChannel channel, final Message message)
'''
pass
def abort():
'''public void abort()
'''
pass
def postCreate():
'''public void postCreate()
public void postCreate()
public void postCreate()
public void postCreate()
public void postCreate()
public void postCreate()
'''
pass
def run():
'''public void run()
public void run()
'''
pass
def getAllowedTransports():
'''public List<String> getAllowedTransports()
'''
pass
def getKnownTransportNames():
'''public Set<String> getKnownTransportNames()
'''
pass
def getTransport():
'''public ClientTransport getTransport(final String transport)
public ClientTransport getTransport()
'''
pass
def setDebugEnabled():
'''public void setDebugEnabled(final boolean debug)
'''
pass
def isDebugEnabled():
'''public boolean isDebugEnabled()
'''
pass
def getOption():
'''public Object getOption(final String qualifiedName)
'''
pass
def setOption():
'''public void setOption(final String qualifiedName, final Object value)
'''
pass
def getOptionNames():
'''public Set<String> getOptionNames()
'''
pass
def getOptions():
'''public Map<String, Object> getOptions()
'''
pass
def onSending():
'''public void onSending(final Message[] messages)
public void onSending(final Message[] messages)
'''
pass
def onMessages():
'''public void onMessages(final List<Message.Mutable> messages)
public void onMessages(final List<Message.Mutable> messages)
'''
pass
def onFailure():
'''public void onFailure(final Throwable x, final Message[] messages)
'''
pass
def dump():
'''public String dump()
'''
pass
def onConnectException():
'''public void onConnectException(final Throwable x, final Message[] messages)
'''
pass
def onException():
'''public void onException(final Throwable x, final Message[] messages)
'''
pass
def onExpire():
'''public void onExpire(final Message[] messages)
'''
pass
def onProtocolError():
'''public void onProtocolError(final String info, final Message[] messages)
'''
pass
def getSession():
'''public ClientSession getSession()
'''
pass
def publish():
'''public void publish(final Object data)
public void publish(final Object data, final String messageId)
'''
pass
def getType():
'''public State getType()
'''
pass
def toString():
'''public String toString()
'''
pass
def RehandshakingState():
'''public RehandshakingState(final Map<String, Object> handshakeFields, final ClientTransport transport, final long backoff)
'''
pass
