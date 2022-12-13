def setDefaultIdentity():
'''public static void setDefaultIdentity(final DiscoverInfo.Identity identity)
'''
pass
def handleIQRequest():
'''public IQ handleIQRequest(final IQ iqRequest)
public IQ handleIQRequest(final IQ iqRequest)
'''
pass
def getIdentityName():
'''public String getIdentityName()
'''
pass
def setIdentity():
'''public synchronized void setIdentity(final DiscoverInfo.Identity identity)
'''
pass
def getIdentityType():
'''public String getIdentityType()
'''
pass
def addIdentity():
'''public synchronized void addIdentity(final DiscoverInfo.Identity identity)
'''
pass
def removeIdentity():
'''public synchronized boolean removeIdentity(final DiscoverInfo.Identity identity)
'''
pass
def getInstanceFor():
'''public static synchronized ServiceDiscoveryManager getInstanceFor(final XMPPConnection connection)
'''
pass
def addDiscoverInfoTo():
'''public synchronized void addDiscoverInfoTo(final DiscoverInfo response)
'''
pass
def setNodeInformationProvider():
'''public void setNodeInformationProvider(final String node, final NodeInformationProvider listener)
'''
pass
def removeNodeInformationProvider():
'''public void removeNodeInformationProvider(final String node)
'''
pass
def getFeatures():
'''public synchronized List<String> getFeatures()
'''
pass
def addFeature():
'''public synchronized void addFeature(final String feature)
'''
pass
def removeFeature():
'''public synchronized void removeFeature(final String feature)
'''
pass
def includesFeature():
'''public synchronized boolean includesFeature(final String feature)
'''
pass
def setExtendedInfo():
'''public synchronized void setExtendedInfo(final DataForm info)
'''
pass
def getExtendedInfo():
'''public DataForm getExtendedInfo()
'''
pass
def getExtendedInfoAsList():
'''public List<ExtensionElement> getExtendedInfoAsList()
'''
pass
def removeExtendedInfo():
'''public synchronized void removeExtendedInfo()
'''
pass
def discoverInfo():
'''public DiscoverInfo discoverInfo(final Jid entityID)
public DiscoverInfo discoverInfo(final Jid entityID, final String node)
'''
pass
def discoverItems():
'''public DiscoverItems discoverItems(final Jid entityID)
public DiscoverItems discoverItems(final Jid entityID, final String node)
'''
pass
def canPublishItems():
'''public boolean canPublishItems(final Jid entityID)
public static boolean canPublishItems(final DiscoverInfo info)
'''
pass
def publishItems():
'''public void publishItems(final Jid entityID, final DiscoverItems discoverItems)
public void publishItems(final Jid entityID, final String node, final DiscoverItems discoverItems)
'''
pass
def serverSupportsFeature():
'''public boolean serverSupportsFeature(final CharSequence feature)
'''
pass
def serverSupportsFeatures():
'''public boolean serverSupportsFeatures(final CharSequence... features)
public boolean serverSupportsFeatures(final Collection<? extends CharSequence> features)
'''
pass
def accountSupportsFeatures():
'''public boolean accountSupportsFeatures(final CharSequence... features)
public boolean accountSupportsFeatures(final Collection<? extends CharSequence> features)
'''
pass
def supportsFeature():
'''public boolean supportsFeature(final Jid jid, final CharSequence feature)
'''
pass
def supportsFeatures():
'''public boolean supportsFeatures(final Jid jid, final CharSequence... features)
public boolean supportsFeatures(final Jid jid, final Collection<? extends CharSequence> features)
'''
pass
def findServicesDiscoverInfo():
'''public List<DiscoverInfo> findServicesDiscoverInfo(final String feature, final boolean stopOnFirst, final boolean useCache)
public List<DiscoverInfo> findServicesDiscoverInfo(final String feature, final boolean stopOnFirst, final boolean useCache, final Map<? super Jid, Exception> encounteredExceptions)
public List<DiscoverInfo> findServicesDiscoverInfo(final DomainBareJid serviceName, final String feature, final boolean stopOnFirst, final boolean useCache, final Map<? super Jid, Exception> encounteredExceptions)
'''
pass
def findServices():
'''public List<DomainBareJid> findServices(final String feature, final boolean stopOnFirst, final boolean useCache)
'''
pass
def findService():
'''public DomainBareJid findService(final String feature, final boolean useCache, final String category, final String type)
public DomainBareJid findService(final String feature, final boolean useCache)
'''
pass
def addEntityCapabilitiesChangedListener():
'''public boolean addEntityCapabilitiesChangedListener(final EntityCapabilitiesChangedListener entityCapabilitiesChangedListener)
'''
pass
def addDiscoInfoLookupShortcutMechanism():
'''public static void addDiscoInfoLookupShortcutMechanism(final DiscoInfoLookupShortcutMechanism discoInfoLookupShortcutMechanism)
'''
pass
def removeDiscoInfoLookupShortcutMechanism():
'''public static void removeDiscoInfoLookupShortcutMechanism(final DiscoInfoLookupShortcutMechanism discoInfoLookupShortcutMechanism)
'''
pass
def connectionCreated():
'''public void connectionCreated(final XMPPConnection connection)
'''
pass
