LOG_LEVEL = "String  logLevel""
OFF_LOG_LEVEL = "int  0"
CONFIG_LOG_LEVEL = "int  1"
INFO_LOG_LEVEL = "int  2"
DEBUG_LOG_LEVEL = "int  3"
JSON_CONTEXT = "String  jsonContext""
def BayeuxServerImpl():
'''public BayeuxServerImpl()
'''
pass
def getLogger():
'''public Logger getLogger()
'''
pass
def run():
'''public void run()
public void run()
'''
pass
def startTimeout():
'''public void startTimeout(final Timeout.Task task, final long interval)
'''
pass
def cancelTimeout():
'''public void cancelTimeout(final Timeout.Task task)
'''
pass
def newChannelId():
'''public ChannelId newChannelId(final String id)
'''
pass
def getOptions():
'''public Map<String, Object> getOptions()
'''
pass
def getOption():
'''public Object getOption(final String qualifiedName)
'''
pass
def getOptionNames():
'''public Set<String> getOptionNames()
'''
pass
def setOption():
'''public void setOption(final String qualifiedName, final Object value)
'''
pass
def setOptions():
'''public void setOptions(final Map<String, Object> options)
'''
pass
def randomLong():
'''public long randomLong()
'''
pass
def setCurrentTransport():
'''public void setCurrentTransport(final AbstractServerTransport transport)
'''
pass
def getCurrentTransport():
'''public ServerTransport getCurrentTransport()
'''
pass
def getContext():
'''public BayeuxContext getContext()
'''
pass
def getSecurityPolicy():
'''public SecurityPolicy getSecurityPolicy()
'''
pass
def createIfAbsent():
'''public boolean createIfAbsent(final String channelName, final ConfigurableServerChannel.Initializer... initializers)
'''
pass
def getSessions():
'''public List<ServerSession> getSessions()
'''
pass
def getSession():
'''public ServerSession getSession(final String clientId)
'''
pass
def removeServerSession():
'''public boolean removeServerSession(final ServerSession session, final boolean timedout)
'''
pass
def newLocalSession():
'''public LocalSession newLocalSession(final String idHint)
'''
pass
def setSecurityPolicy():
'''public void setSecurityPolicy(final SecurityPolicy securityPolicy)
'''
pass
def addExtension():
'''public void addExtension(final BayeuxServer.Extension extension)
'''
pass
def removeExtension():
'''public void removeExtension(final BayeuxServer.Extension extension)
'''
pass
def addListener():
'''public void addListener(final BayeuxServer.BayeuxServerListener listener)
'''
pass
def getChannel():
'''public ServerChannel getChannel(final String channelId)
'''
pass
def getChannels():
'''public List<ServerChannel> getChannels()
'''
pass
def getChannelChildren():
'''public List<ServerChannelImpl> getChannelChildren(final ChannelId channelId)
'''
pass
def removeListener():
'''public void removeListener(final BayeuxServer.BayeuxServerListener listener)
'''
pass
def freeze():
'''public void freeze(final ServerMessage.Mutable mutable)
'''
pass
def getKnownTransportNames():
'''public Set<String> getKnownTransportNames()
'''
pass
def getTransport():
'''public ServerTransport getTransport(final String transport)
'''
pass
def addTransport():
'''public void addTransport(final ServerTransport transport)
'''
pass
def setTransports():
'''public void setTransports(final ServerTransport... transports)
public void setTransports(final List<ServerTransport> transports)
'''
pass
def getAllowedTransports():
'''public List<String> getAllowedTransports()
'''
pass
def setAllowedTransports():
'''public void setAllowedTransports(final String... allowed)
public void setAllowedTransports(final List<String> allowed)
'''
pass
def sweep():
'''public void sweep()
'''
pass
def dump():
'''public String dump()
'''
pass
def onMessage():
'''public void onMessage(ServerSessionImpl session, final ServerMessage.Mutable message)
public void onMessage(final ServerSessionImpl session, final ServerMessage.Mutable message)
public void onMessage(final ServerSessionImpl from, final ServerMessage.Mutable message)
public void onMessage(final ServerSessionImpl from, final ServerMessage.Mutable message)
public void onMessage(final ServerSessionImpl session, final ServerMessage.Mutable message)
'''
pass
