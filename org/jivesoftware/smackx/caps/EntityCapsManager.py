NAMESPACE = "String  \"http://jabber.org/protocol/caps\""
ELEMENT = "String  \"c\""
def setDefaultEntityNode():
    '''    public static void setDefaultEntityNode(final String entityNode)
    '''
def getNodeVersionByJid():
    '''    public static String getNodeVersionByJid(final Jid jid)
    '''
def getNodeVerHashByJid():
    '''    public static NodeVerHash getNodeVerHashByJid(final Jid jid)
    '''
def getDiscoverInfoByUser():
    '''    public static DiscoverInfo getDiscoverInfoByUser(final Jid user)
    public DiscoverInfo getDiscoverInfoByUser(final ServiceDiscoveryManager serviceDiscoveryManager, final Jid jid)
    '''
def getDiscoveryInfoByNodeVer():
    '''    public static DiscoverInfo getDiscoveryInfoByNodeVer(final String nodeVer)
    '''
def setPersistentCache():
    '''    public static void setPersistentCache(final EntityCapsPersistentCache cache)
    '''
def setMaxsCacheSizes():
    '''    public static void setMaxsCacheSizes(final int maxJidToNodeVerSize, final int maxCapsCacheSize)
    '''
def clearMemoryCache():
    '''    public static void clearMemoryCache()
    '''
def connected():
    '''    public void connected(final XMPPConnection connection)
    '''
def authenticated():
    '''    public void authenticated(final XMPPConnection connection, final boolean resumed)
    '''
def processStanza():
    '''    public void processStanza(final Stanza packet)
    public void processStanza(final Stanza packet)
    public void processStanza(final Stanza packet)
    '''
def presenceUnavailable():
    '''    public void presenceUnavailable(final FullJid from, final Presence presence)
    '''
def onEntityCapailitiesChanged():
    '''    public void onEntityCapailitiesChanged()
    '''
def getInstanceFor():
    '''    public static synchronized EntityCapsManager getInstanceFor(final XMPPConnection connection)
    '''
def enableEntityCaps():
    '''    public synchronized void enableEntityCaps()
    '''
def disableEntityCaps():
    '''    public synchronized void disableEntityCaps()
    '''
def entityCapsEnabled():
    '''    public boolean entityCapsEnabled()
    '''
def setEntityNode():
    '''    public void setEntityNode(final String entityNode)
    '''
def removeUserCapsNode():
    '''    public static void removeUserCapsNode(final Jid user)
    '''
def getCapsVersionAndHash():
    '''    public CapsVersionAndHash getCapsVersionAndHash()
    '''
def getLocalNodeVer():
    '''    public String getLocalNodeVer()
    '''
def areEntityCapsSupported():
    '''    public boolean areEntityCapsSupported(final Jid jid)
    '''
def areEntityCapsSupportedByServer():
    '''    public boolean areEntityCapsSupportedByServer()
    '''
def getNodeFeatures():
    '''    public List<String> getNodeFeatures()
    '''
def getNodePacketExtensions():
    '''    public List<ExtensionElement> getNodePacketExtensions()
    '''
def verifyDiscoverInfoVersion():
    '''    public static boolean verifyDiscoverInfoVersion(final String ver, final String hash, final DiscoverInfo info)
    '''
def compare():
    '''    public int compare(final FormField f1, final FormField f2)
    '''
def connectionCreated():
    '''    public void connectionCreated(final XMPPConnection connection)
    '''
def getNodeVer():
    '''    public String getNodeVer()
    '''
def getNode():
    '''    public String getNode()
    '''
def getHash():
    '''    public String getHash()
    '''
def getVer():
    '''    public String getVer()
    '''
