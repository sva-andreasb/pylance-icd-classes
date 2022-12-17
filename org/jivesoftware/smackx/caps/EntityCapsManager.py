NAMESPACE = "String  \"http://jabber.org/protocol/caps\""
ELEMENT = "String  \"c\""
def connected():
    '''returns None\n\n
    connected(final XMPPConnection connection)\n
    '''
def authenticated():
    '''returns None\n\n
    authenticated(final XMPPConnection connection, final boolean resumed)\n
    '''
def processStanza():
    '''returns None\n\n
    processStanza(final Stanza packet)\n
    processStanza(final Stanza packet)\n
    processStanza(final Stanza packet)\n
    '''
def presenceUnavailable():
    '''returns None\n\n
    presenceUnavailable(final FullJid from, final Presence presence)\n
    '''
def onEntityCapailitiesChanged():
    '''returns None\n\n
    onEntityCapailitiesChanged()\n
    '''
def entityCapsEnabled():
    '''returns boolean\n\n
    entityCapsEnabled()\n
    '''
def setEntityNode():
    '''returns None\n\n
    setEntityNode(final String entityNode)\n
    '''
def getCapsVersionAndHash():
    '''returns CapsVersionAndHash\n\n
    getCapsVersionAndHash()\n
    '''
def getLocalNodeVer():
    '''returns String\n\n
    getLocalNodeVer()\n
    '''
def areEntityCapsSupported():
    '''returns boolean\n\n
    areEntityCapsSupported(final Jid jid)\n
    '''
def areEntityCapsSupportedByServer():
    '''returns boolean\n\n
    areEntityCapsSupportedByServer()\n
    '''
def getNodeFeatures():
    '''returns List<String>\n\n
    getNodeFeatures()\n
    '''
def getNodePacketExtensions():
    '''returns List<ExtensionElement>\n\n
    getNodePacketExtensions()\n
    '''
def compare():
    '''returns int\n\n
    compare(final FormField f1, final FormField f2)\n
    '''
def connectionCreated():
    '''returns None\n\n
    connectionCreated(final XMPPConnection connection)\n
    '''
def getDiscoverInfoByUser():
    '''returns DiscoverInfo\n\n
    getDiscoverInfoByUser(final ServiceDiscoveryManager serviceDiscoveryManager, final Jid jid)\n
    '''
def getNodeVer():
    '''returns String\n\n
    getNodeVer()\n
    '''
def getNode():
    '''returns String\n\n
    getNode()\n
    '''
def getHash():
    '''returns String\n\n
    getHash()\n
    '''
def getVer():
    '''returns String\n\n
    getVer()\n
    '''
