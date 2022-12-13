LOG_LEVEL = "String  \"logLevel\""
OFF_LOG_LEVEL = "int  0"
CONFIG_LOG_LEVEL = "int  1"
INFO_LOG_LEVEL = "int  2"
DEBUG_LOG_LEVEL = "int  3"
JSON_CONTEXT = "String  \"jsonContext\""
def BayeuxServerImpl():
    '''    public BayeuxServerImpl()
    '''
def getLogger():
    '''    public Logger getLogger()
    '''
def run():
    '''    public void run()
    public void run()
    '''
def startTimeout():
    '''    public void startTimeout(final Timeout.Task task, final long interval)
    '''
def cancelTimeout():
    '''    public void cancelTimeout(final Timeout.Task task)
    '''
def newChannelId():
    '''    public ChannelId newChannelId(final String id)
    '''
def getOptions():
    '''    public Map<String, Object> getOptions()
    '''
def getOption():
    '''    public Object getOption(final String qualifiedName)
    '''
def getOptionNames():
    '''    public Set<String> getOptionNames()
    '''
def setOption():
    '''    public void setOption(final String qualifiedName, final Object value)
    '''
def setOptions():
    '''    public void setOptions(final Map<String, Object> options)
    '''
def randomLong():
    '''    public long randomLong()
    '''
def setCurrentTransport():
    '''    public void setCurrentTransport(final AbstractServerTransport transport)
    '''
def getCurrentTransport():
    '''    public ServerTransport getCurrentTransport()
    '''
def getContext():
    '''    public BayeuxContext getContext()
    '''
def getSecurityPolicy():
    '''    public SecurityPolicy getSecurityPolicy()
    '''
def createIfAbsent():
    '''    public boolean createIfAbsent(final String channelName, final ConfigurableServerChannel.Initializer... initializers)
    '''
def getSessions():
    '''    public List<ServerSession> getSessions()
    '''
def getSession():
    '''    public ServerSession getSession(final String clientId)
    '''
def removeServerSession():
    '''    public boolean removeServerSession(final ServerSession session, final boolean timedout)
    '''
def newLocalSession():
    '''    public LocalSession newLocalSession(final String idHint)
    '''
def setSecurityPolicy():
    '''    public void setSecurityPolicy(final SecurityPolicy securityPolicy)
    '''
def addExtension():
    '''    public void addExtension(final BayeuxServer.Extension extension)
    '''
def removeExtension():
    '''    public void removeExtension(final BayeuxServer.Extension extension)
    '''
def addListener():
    '''    public void addListener(final BayeuxServer.BayeuxServerListener listener)
    '''
def getChannel():
    '''    public ServerChannel getChannel(final String channelId)
    '''
def getChannels():
    '''    public List<ServerChannel> getChannels()
    '''
def getChannelChildren():
    '''    public List<ServerChannelImpl> getChannelChildren(final ChannelId channelId)
    '''
def removeListener():
    '''    public void removeListener(final BayeuxServer.BayeuxServerListener listener)
    '''
def freeze():
    '''    public void freeze(final ServerMessage.Mutable mutable)
    '''
def getKnownTransportNames():
    '''    public Set<String> getKnownTransportNames()
    '''
def getTransport():
    '''    public ServerTransport getTransport(final String transport)
    '''
def addTransport():
    '''    public void addTransport(final ServerTransport transport)
    '''
def setTransports():
    '''    public void setTransports(final ServerTransport... transports)
    public void setTransports(final List<ServerTransport> transports)
    '''
def getAllowedTransports():
    '''    public List<String> getAllowedTransports()
    '''
def setAllowedTransports():
    '''    public void setAllowedTransports(final String... allowed)
    public void setAllowedTransports(final List<String> allowed)
    '''
def sweep():
    '''    public void sweep()
    '''
def dump():
    '''    public String dump()
    '''
def onMessage():
    '''    public void onMessage(ServerSessionImpl session, final ServerMessage.Mutable message)
    public void onMessage(final ServerSessionImpl session, final ServerMessage.Mutable message)
    public void onMessage(final ServerSessionImpl from, final ServerMessage.Mutable message)
    public void onMessage(final ServerSessionImpl from, final ServerMessage.Mutable message)
    public void onMessage(final ServerSessionImpl session, final ServerMessage.Mutable message)
    '''
