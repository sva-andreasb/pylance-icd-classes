NAMESPACE = "String  \"http://jabber.org/protocol/commands\""
def getAddHocCommandsManager():
    '''    public static synchronized AdHocCommandManager getAddHocCommandsManager(final XMPPConnection connection)
    '''
def handleIQRequest():
    '''    public IQ handleIQRequest(final IQ iqRequest)
    '''
def registerCommand():
    '''    public void registerCommand(final String node, final String name, final Class<? extends LocalCommand> clazz)
    public void registerCommand(final String node, final String name, final LocalCommandFactory factory)
    '''
def getInstance():
    '''    public LocalCommand getInstance()
    '''
def getNodeFeatures():
    '''    public List<String> getNodeFeatures()
    '''
def discoverCommands():
    '''    public DiscoverItems discoverCommands(final Jid jid)
    '''
def publishCommands():
    '''    public void publishCommands(final Jid jid)
    '''
def getRemoteCommand():
    '''    public RemoteCommand getRemoteCommand(final Jid jid, final String node)
    '''
def run():
    '''    public void run()
    '''
def connectionCreated():
    '''    public void connectionCreated(final XMPPConnection connection)
    '''
def getCommandInstance():
    '''    public LocalCommand getCommandInstance()
    '''
def getName():
    '''    public String getName()
    '''
def getNode():
    '''    public String getNode()
    '''
def getOwnerJID():
    '''    public Jid getOwnerJID()
    '''
