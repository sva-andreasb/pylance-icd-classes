NAMESPACE = "String  \"http://jabber.org/protocol/commands\""
def handleIQRequest():
    '''returns IQ\n\n
    handleIQRequest(final IQ iqRequest)\n
    '''
def registerCommand():
    '''returns None\n\n
    registerCommand(final String node, final String name, final Class<? extends LocalCommand> clazz)\n
    registerCommand(final String node, final String name, final LocalCommandFactory factory)\n
    '''
def getInstance():
    '''returns LocalCommand\n\n
    getInstance()\n
    '''
def getNodeFeatures():
    '''returns List<String>\n\n
    getNodeFeatures()\n
    '''
def discoverCommands():
    '''returns DiscoverItems\n\n
    discoverCommands(final Jid jid)\n
    '''
def publishCommands():
    '''returns None\n\n
    publishCommands(final Jid jid)\n
    '''
def getRemoteCommand():
    '''returns RemoteCommand\n\n
    getRemoteCommand(final Jid jid, final String node)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def connectionCreated():
    '''returns None\n\n
    connectionCreated(final XMPPConnection connection)\n
    '''
def getCommandInstance():
    '''returns LocalCommand\n\n
    getCommandInstance()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getNode():
    '''returns String\n\n
    getNode()\n
    '''
def getOwnerJID():
    '''returns Jid\n\n
    getOwnerJID()\n
    '''
