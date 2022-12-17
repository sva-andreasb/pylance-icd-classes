LOG_LEVEL = "String  \"logLevel\""
OFF_LOG_LEVEL = "int  0"
CONFIG_LOG_LEVEL = "int  1"
INFO_LOG_LEVEL = "int  2"
DEBUG_LOG_LEVEL = "int  3"
JSON_CONTEXT = "String  \"jsonContext\""
def ():
    '''returns BayeuxServerImpl\n\n
    ()\n
    '''
def getLogger():
    '''returns Logger\n\n
    getLogger()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def startTimeout():
    '''returns None\n\n
    startTimeout(final Timeout.Task task, final long interval)\n
    '''
def cancelTimeout():
    '''returns None\n\n
    cancelTimeout(final Timeout.Task task)\n
    '''
def newChannelId():
    '''returns ChannelId\n\n
    newChannelId(final String id)\n
    '''
def getOption():
    '''returns Object\n\n
    getOption(final String qualifiedName)\n
    '''
def getOptionNames():
    '''returns Set<String>\n\n
    getOptionNames()\n
    '''
def setOption():
    '''returns None\n\n
    setOption(final String qualifiedName, final Object value)\n
    '''
def setOptions():
    '''returns None\n\n
    setOptions(final Map<String, Object> options)\n
    '''
def randomLong():
    '''returns long\n\n
    randomLong()\n
    '''
def setCurrentTransport():
    '''returns None\n\n
    setCurrentTransport(final AbstractServerTransport transport)\n
    '''
def getCurrentTransport():
    '''returns ServerTransport\n\n
    getCurrentTransport()\n
    '''
def getContext():
    '''returns BayeuxContext\n\n
    getContext()\n
    '''
def getSecurityPolicy():
    '''returns SecurityPolicy\n\n
    getSecurityPolicy()\n
    '''
def createIfAbsent():
    '''returns boolean\n\n
    createIfAbsent(final String channelName, final ConfigurableServerChannel.Initializer... initializers)\n
    '''
def getSessions():
    '''returns List<ServerSession>\n\n
    getSessions()\n
    '''
def getSession():
    '''returns ServerSession\n\n
    getSession(final String clientId)\n
    '''
def removeServerSession():
    '''returns boolean\n\n
    removeServerSession(final ServerSession session, final boolean timedout)\n
    '''
def newLocalSession():
    '''returns LocalSession\n\n
    newLocalSession(final String idHint)\n
    '''
def setSecurityPolicy():
    '''returns None\n\n
    setSecurityPolicy(final SecurityPolicy securityPolicy)\n
    '''
def addExtension():
    '''returns None\n\n
    addExtension(final BayeuxServer.Extension extension)\n
    '''
def removeExtension():
    '''returns None\n\n
    removeExtension(final BayeuxServer.Extension extension)\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final BayeuxServer.BayeuxServerListener listener)\n
    '''
def getChannel():
    '''returns ServerChannel\n\n
    getChannel(final String channelId)\n
    '''
def getChannels():
    '''returns List<ServerChannel>\n\n
    getChannels()\n
    '''
def getChannelChildren():
    '''returns List<ServerChannelImpl>\n\n
    getChannelChildren(final ChannelId channelId)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final BayeuxServer.BayeuxServerListener listener)\n
    '''
def freeze():
    '''returns None\n\n
    freeze(final ServerMessage.Mutable mutable)\n
    '''
def getKnownTransportNames():
    '''returns Set<String>\n\n
    getKnownTransportNames()\n
    '''
def getTransport():
    '''returns ServerTransport\n\n
    getTransport(final String transport)\n
    '''
def addTransport():
    '''returns None\n\n
    addTransport(final ServerTransport transport)\n
    '''
def setTransports():
    '''returns None\n\n
    setTransports(final ServerTransport... transports)\n
    setTransports(final List<ServerTransport> transports)\n
    '''
def getAllowedTransports():
    '''returns List<String>\n\n
    getAllowedTransports()\n
    '''
def setAllowedTransports():
    '''returns None\n\n
    setAllowedTransports(final String... allowed)\n
    setAllowedTransports(final List<String> allowed)\n
    '''
def sweep():
    '''returns None\n\n
    sweep()\n
    '''
def dump():
    '''returns String\n\n
    dump()\n
    '''
def onMessage():
    '''returns None\n\n
    onMessage(ServerSessionImpl session, final ServerMessage.Mutable message)\n
    onMessage(final ServerSessionImpl session, final ServerMessage.Mutable message)\n
    onMessage(final ServerSessionImpl from, final ServerMessage.Mutable message)\n
    onMessage(final ServerSessionImpl from, final ServerMessage.Mutable message)\n
    onMessage(final ServerSessionImpl session, final ServerMessage.Mutable message)\n
    '''
