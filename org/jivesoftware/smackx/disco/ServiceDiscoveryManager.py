def setDefaultIdentity():
    '''    public static void setDefaultIdentity(final DiscoverInfo.Identity identity)
    '''
def handleIQRequest():
    '''    public IQ handleIQRequest(final IQ iqRequest)
    public IQ handleIQRequest(final IQ iqRequest)
    '''
def getIdentityName():
    '''    public String getIdentityName()
    '''
def setIdentity():
    '''    public synchronized void setIdentity(final DiscoverInfo.Identity identity)
    '''
def getIdentityType():
    '''    public String getIdentityType()
    '''
def addIdentity():
    '''    public synchronized void addIdentity(final DiscoverInfo.Identity identity)
    '''
def removeIdentity():
    '''    public synchronized boolean removeIdentity(final DiscoverInfo.Identity identity)
    '''
def getInstanceFor():
    '''    public static synchronized ServiceDiscoveryManager getInstanceFor(final XMPPConnection connection)
    '''
def addDiscoverInfoTo():
    '''    public synchronized void addDiscoverInfoTo(final DiscoverInfo response)
    '''
def setNodeInformationProvider():
    '''    public void setNodeInformationProvider(final String node, final NodeInformationProvider listener)
    '''
def removeNodeInformationProvider():
    '''    public void removeNodeInformationProvider(final String node)
    '''
def getFeatures():
    '''    public synchronized List<String> getFeatures()
    '''
def addFeature():
    '''    public synchronized void addFeature(final String feature)
    '''
def removeFeature():
    '''    public synchronized void removeFeature(final String feature)
    '''
def includesFeature():
    '''    public synchronized boolean includesFeature(final String feature)
    '''
def setExtendedInfo():
    '''    public synchronized void setExtendedInfo(final DataForm info)
    '''
def getExtendedInfo():
    '''    public DataForm getExtendedInfo()
    '''
def getExtendedInfoAsList():
    '''    public List<ExtensionElement> getExtendedInfoAsList()
    '''
def removeExtendedInfo():
    '''    public synchronized void removeExtendedInfo()
    '''
def discoverInfo():
    '''    public DiscoverInfo discoverInfo(final Jid entityID)
    public DiscoverInfo discoverInfo(final Jid entityID, final String node)
    '''
def discoverItems():
    '''    public DiscoverItems discoverItems(final Jid entityID)
    public DiscoverItems discoverItems(final Jid entityID, final String node)
    '''
def canPublishItems():
    '''    public boolean canPublishItems(final Jid entityID)
    public static boolean canPublishItems(final DiscoverInfo info)
    '''
def publishItems():
    '''    public void publishItems(final Jid entityID, final DiscoverItems discoverItems)
    public void publishItems(final Jid entityID, final String node, final DiscoverItems discoverItems)
    '''
def serverSupportsFeature():
    '''    public boolean serverSupportsFeature(final CharSequence feature)
    '''
def serverSupportsFeatures():
    '''    public boolean serverSupportsFeatures(final CharSequence... features)
    public boolean serverSupportsFeatures(final Collection<? extends CharSequence> features)
    '''
def accountSupportsFeatures():
    '''    public boolean accountSupportsFeatures(final CharSequence... features)
    public boolean accountSupportsFeatures(final Collection<? extends CharSequence> features)
    '''
def supportsFeature():
    '''    public boolean supportsFeature(final Jid jid, final CharSequence feature)
    '''
def supportsFeatures():
    '''    public boolean supportsFeatures(final Jid jid, final CharSequence... features)
    public boolean supportsFeatures(final Jid jid, final Collection<? extends CharSequence> features)
    '''
def findServicesDiscoverInfo():
    '''    public List<DiscoverInfo> findServicesDiscoverInfo(final String feature, final boolean stopOnFirst, final boolean useCache)
    public List<DiscoverInfo> findServicesDiscoverInfo(final String feature, final boolean stopOnFirst, final boolean useCache, final Map<? super Jid, Exception> encounteredExceptions)
    public List<DiscoverInfo> findServicesDiscoverInfo(final DomainBareJid serviceName, final String feature, final boolean stopOnFirst, final boolean useCache, final Map<? super Jid, Exception> encounteredExceptions)
    '''
def findServices():
    '''    public List<DomainBareJid> findServices(final String feature, final boolean stopOnFirst, final boolean useCache)
    '''
def findService():
    '''    public DomainBareJid findService(final String feature, final boolean useCache, final String category, final String type)
    public DomainBareJid findService(final String feature, final boolean useCache)
    '''
def addEntityCapabilitiesChangedListener():
    '''    public boolean addEntityCapabilitiesChangedListener(final EntityCapabilitiesChangedListener entityCapabilitiesChangedListener)
    '''
def addDiscoInfoLookupShortcutMechanism():
    '''    public static void addDiscoInfoLookupShortcutMechanism(final DiscoInfoLookupShortcutMechanism discoInfoLookupShortcutMechanism)
    '''
def removeDiscoInfoLookupShortcutMechanism():
    '''    public static void removeDiscoInfoLookupShortcutMechanism(final DiscoInfoLookupShortcutMechanism discoInfoLookupShortcutMechanism)
    '''
def connectionCreated():
    '''    public void connectionCreated(final XMPPConnection connection)
    '''
