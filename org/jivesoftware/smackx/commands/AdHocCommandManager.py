NAMESPACE = "String  http://jabber.org/protocol/commands""
def getAddHocCommandsManager():
'''public static synchronized AdHocCommandManager getAddHocCommandsManager(final XMPPConnection connection)
'''
pass
def handleIQRequest():
'''public IQ handleIQRequest(final IQ iqRequest)
'''
pass
def registerCommand():
'''public void registerCommand(final String node, final String name, final Class<? extends LocalCommand> clazz)
public void registerCommand(final String node, final String name, final LocalCommandFactory factory)
'''
pass
def getInstance():
'''public LocalCommand getInstance()
'''
pass
def getNodeFeatures():
'''public List<String> getNodeFeatures()
'''
pass
def discoverCommands():
'''public DiscoverItems discoverCommands(final Jid jid)
'''
pass
def publishCommands():
'''public void publishCommands(final Jid jid)
'''
pass
def getRemoteCommand():
'''public RemoteCommand getRemoteCommand(final Jid jid, final String node)
'''
pass
def run():
'''public void run()
'''
pass
def connectionCreated():
'''public void connectionCreated(final XMPPConnection connection)
'''
pass
def getCommandInstance():
'''public LocalCommand getCommandInstance()
'''
pass
def getName():
'''public String getName()
'''
pass
def getNode():
'''public String getNode()
'''
pass
def getOwnerJID():
'''public Jid getOwnerJID()
'''
pass
