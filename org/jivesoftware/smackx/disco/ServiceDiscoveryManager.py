def handleIQRequest():
    '''returns IQ\n\n
    handleIQRequest(final IQ iqRequest)\n
    handleIQRequest(final IQ iqRequest)\n
    '''
def getIdentityName():
    '''returns String\n\n
    getIdentityName()\n
    '''
def getIdentityType():
    '''returns String\n\n
    getIdentityType()\n
    '''
def setNodeInformationProvider():
    '''returns None\n\n
    setNodeInformationProvider(final String node, final NodeInformationProvider listener)\n
    '''
def removeNodeInformationProvider():
    '''returns None\n\n
    removeNodeInformationProvider(final String node)\n
    '''
def getExtendedInfo():
    '''returns DataForm\n\n
    getExtendedInfo()\n
    '''
def getExtendedInfoAsList():
    '''returns List<ExtensionElement>\n\n
    getExtendedInfoAsList()\n
    '''
def discoverInfo():
    '''returns DiscoverInfo\n\n
    discoverInfo(final Jid entityID)\n
    discoverInfo(final Jid entityID, final String node)\n
    '''
def discoverItems():
    '''returns DiscoverItems\n\n
    discoverItems(final Jid entityID)\n
    discoverItems(final Jid entityID, final String node)\n
    '''
def canPublishItems():
    '''returns boolean\n\n
    canPublishItems(final Jid entityID)\n
    '''
def publishItems():
    '''returns None\n\n
    publishItems(final Jid entityID, final DiscoverItems discoverItems)\n
    publishItems(final Jid entityID, final String node, final DiscoverItems discoverItems)\n
    '''
def serverSupportsFeature():
    '''returns boolean\n\n
    serverSupportsFeature(final CharSequence feature)\n
    '''
def serverSupportsFeatures():
    '''returns boolean\n\n
    serverSupportsFeatures(final CharSequence... features)\n
    serverSupportsFeatures(final Collection<? extends CharSequence> features)\n
    '''
def accountSupportsFeatures():
    '''returns boolean\n\n
    accountSupportsFeatures(final CharSequence... features)\n
    accountSupportsFeatures(final Collection<? extends CharSequence> features)\n
    '''
def supportsFeature():
    '''returns boolean\n\n
    supportsFeature(final Jid jid, final CharSequence feature)\n
    '''
def supportsFeatures():
    '''returns boolean\n\n
    supportsFeatures(final Jid jid, final CharSequence... features)\n
    supportsFeatures(final Jid jid, final Collection<? extends CharSequence> features)\n
    '''
def findServicesDiscoverInfo():
    '''returns List<DiscoverInfo>\n\n
    findServicesDiscoverInfo(final String feature, final boolean stopOnFirst, final boolean useCache)\n
    findServicesDiscoverInfo(final String feature, final boolean stopOnFirst, final boolean useCache, final Map<? super Jid, Exception> encounteredExceptions)\n
    findServicesDiscoverInfo(final DomainBareJid serviceName, final String feature, final boolean stopOnFirst, final boolean useCache, final Map<? super Jid, Exception> encounteredExceptions)\n
    '''
def findServices():
    '''returns List<DomainBareJid>\n\n
    findServices(final String feature, final boolean stopOnFirst, final boolean useCache)\n
    '''
def findService():
    '''returns DomainBareJid\n\n
    findService(final String feature, final boolean useCache, final String category, final String type)\n
    findService(final String feature, final boolean useCache)\n
    '''
def addEntityCapabilitiesChangedListener():
    '''returns boolean\n\n
    addEntityCapabilitiesChangedListener(final EntityCapabilitiesChangedListener entityCapabilitiesChangedListener)\n
    '''
def connectionCreated():
    '''returns None\n\n
    connectionCreated(final XMPPConnection connection)\n
    '''
