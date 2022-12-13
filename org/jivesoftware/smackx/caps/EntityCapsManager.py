NAMESPACE = "String  http://jabber.org/protocol/caps""
ELEMENT = "String  c""
def setDefaultEntityNode():
'''public static void setDefaultEntityNode(final String entityNode)
'''
pass
def getNodeVersionByJid():
'''public static String getNodeVersionByJid(final Jid jid)
'''
pass
def getNodeVerHashByJid():
'''public static NodeVerHash getNodeVerHashByJid(final Jid jid)
'''
pass
def getDiscoverInfoByUser():
'''public static DiscoverInfo getDiscoverInfoByUser(final Jid user)
public DiscoverInfo getDiscoverInfoByUser(final ServiceDiscoveryManager serviceDiscoveryManager, final Jid jid)
'''
pass
def getDiscoveryInfoByNodeVer():
'''public static DiscoverInfo getDiscoveryInfoByNodeVer(final String nodeVer)
'''
pass
def setPersistentCache():
'''public static void setPersistentCache(final EntityCapsPersistentCache cache)
'''
pass
def setMaxsCacheSizes():
'''public static void setMaxsCacheSizes(final int maxJidToNodeVerSize, final int maxCapsCacheSize)
'''
pass
def clearMemoryCache():
'''public static void clearMemoryCache()
'''
pass
def connected():
'''public void connected(final XMPPConnection connection)
'''
pass
def authenticated():
'''public void authenticated(final XMPPConnection connection, final boolean resumed)
'''
pass
def processStanza():
'''public void processStanza(final Stanza packet)
public void processStanza(final Stanza packet)
public void processStanza(final Stanza packet)
'''
pass
def presenceUnavailable():
'''public void presenceUnavailable(final FullJid from, final Presence presence)
'''
pass
def onEntityCapailitiesChanged():
'''public void onEntityCapailitiesChanged()
'''
pass
def getInstanceFor():
'''public static synchronized EntityCapsManager getInstanceFor(final XMPPConnection connection)
'''
pass
def enableEntityCaps():
'''public synchronized void enableEntityCaps()
'''
pass
def disableEntityCaps():
'''public synchronized void disableEntityCaps()
'''
pass
def entityCapsEnabled():
'''public boolean entityCapsEnabled()
'''
pass
def setEntityNode():
'''public void setEntityNode(final String entityNode)
'''
pass
def removeUserCapsNode():
'''public static void removeUserCapsNode(final Jid user)
'''
pass
def getCapsVersionAndHash():
'''public CapsVersionAndHash getCapsVersionAndHash()
'''
pass
def getLocalNodeVer():
'''public String getLocalNodeVer()
'''
pass
def areEntityCapsSupported():
'''public boolean areEntityCapsSupported(final Jid jid)
'''
pass
def areEntityCapsSupportedByServer():
'''public boolean areEntityCapsSupportedByServer()
'''
pass
def getNodeFeatures():
'''public List<String> getNodeFeatures()
'''
pass
def getNodePacketExtensions():
'''public List<ExtensionElement> getNodePacketExtensions()
'''
pass
def verifyDiscoverInfoVersion():
'''public static boolean verifyDiscoverInfoVersion(final String ver, final String hash, final DiscoverInfo info)
'''
pass
def compare():
'''public int compare(final FormField f1, final FormField f2)
'''
pass
def connectionCreated():
'''public void connectionCreated(final XMPPConnection connection)
'''
pass
def getNodeVer():
'''public String getNodeVer()
'''
pass
def getNode():
'''public String getNode()
'''
pass
def getHash():
'''public String getHash()
'''
pass
def getVer():
'''public String getVer()
'''
pass
