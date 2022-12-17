def ():
    '''returns UnmapProxyTask\n\n
    (final DiscoveryManagement discoveryManagement, final LeaseRenewalManager leaseRenewalManager)\n
    (final DiscoveryManagement discoveryManagement, final LeaseRenewalManager leaseRenewalManager, final Configuration configuration)\n
    (final ProxyReg reg)\n
    (final Lease lease, final long seqNo)\n
    (final ServiceRegistrar serviceRegistrar, final ServiceItem item)\n
    (final ServiceRegistrar proxy)\n
    (final ServiceRegistrar proxy)\n
    (final ServiceTemplate serviceTemplate, final ServiceItemFilter filter, final ServiceDiscoveryListener e, final long leaseDuration)\n
    ()\n
    (final ProxyReg proxyReg)\n
    (final ProxyReg proxyReg)\n
    (final ProxyReg proxyReg)\n
    (final Object service)\n
    (final ProxyReg proxyReg, final ServiceID sid, final ServiceItem item, final int transition, final int n)\n
    (final ServiceID serviceID)\n
    (final ProxyReg proxyReg, final ServiceItem srvcItem, final boolean matchMatchEvent, final int n)\n
    (final ProxyReg proxyReg, final ServiceItemReg itemReg, final ServiceID serviceID, final int n)\n
    '''
def lookup():
    '''returns ServiceItem[]\n\n
    lookup(final ServiceTemplate serviceTemplate, final ServiceItemFilter serviceItemFilter)\n
    lookup(final ServiceTemplate serviceTemplate, final ServiceItemFilter serviceItemFilter, final long n)\n
    lookup(final ServiceTemplate serviceTemplate, final int n, final ServiceItemFilter serviceItemFilter)\n
    lookup(final ServiceTemplate serviceTemplate, final int n, final int n2, final ServiceItemFilter serviceItemFilter, final long n3)\n
    lookup(final ServiceItemFilter serviceItemFilter)\n
    lookup(final ServiceItemFilter serviceItemFilter, final int n)\n
    '''
def createLookupCache():
    '''returns LookupCache\n\n
    createLookupCache(final ServiceTemplate serviceTemplate, final ServiceItemFilter serviceItemFilter, final ServiceDiscoveryListener serviceDiscoveryListener)\n
    '''
def getDiscoveryManager():
    '''returns DiscoveryManagement\n\n
    getDiscoveryManager()\n
    '''
def getLeaseRenewalManager():
    '''returns LeaseRenewalManager\n\n
    getLeaseRenewalManager()\n
    '''
def terminate():
    '''returns None\n\n
    terminate()\n
    terminate()\n
    '''
def isFromProxy():
    '''returns boolean\n\n
    isFromProxy(final ProxyReg proxyReg)\n
    '''
def runAfter():
    '''returns boolean\n\n
    runAfter(final List list, final int n)\n
    runAfter(final List list, final int n)\n
    runAfter(final List list, final int n)\n
    '''
def getServiceID():
    '''returns ServiceID\n\n
    getServiceID()\n
    '''
def getSeqN():
    '''returns int\n\n
    getSeqN()\n
    '''
def serviceRemoved():
    '''returns None\n\n
    serviceRemoved(final ServiceDiscoveryEvent serviceDiscoveryEvent)\n
    '''
def serviceChanged():
    '''returns None\n\n
    serviceChanged(final ServiceDiscoveryEvent serviceDiscoveryEvent)\n
    '''
def addProxy():
    '''returns None\n\n
    addProxy(final ServiceRegistrar serviceRegistrar)\n
    '''
def removeProxy():
    '''returns None\n\n
    removeProxy(final ServiceRegistrar o)\n
    '''
def hasNoProxys():
    '''returns boolean\n\n
    hasNoProxys()\n
    '''
def setDiscarded():
    '''returns None\n\n
    setDiscarded(final boolean bDiscarded)\n
    '''
def isDiscarded():
    '''returns boolean\n\n
    isDiscarded()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def notify():
    '''returns None\n\n
    notify(final LeaseRenewalEvent leaseRenewalEvent)\n
    notify(final RemoteEvent remoteEvent)\n
    notify(final RemoteEvent remoteEvent)\n
    '''
def discard():
    '''returns None\n\n
    discard(final Object obj)\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final ServiceDiscoveryListener e)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final ServiceDiscoveryListener serviceDiscoveryListener)\n
    '''
def addProxyReg():
    '''returns None\n\n
    addProxyReg(final ProxyReg proxyReg)\n
    '''
def removeProxyReg():
    '''returns None\n\n
    removeProxyReg(final ProxyReg key)\n
    '''
def getLeaseDuration():
    '''returns long\n\n
    getLeaseDuration()\n
    '''
def getProxyVerifier():
    '''returns TrustVerifier\n\n
    getProxyVerifier()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def discovered():
    '''returns None\n\n
    discovered(final DiscoveryEvent discoveryEvent)\n
    '''
def discarded():
    '''returns None\n\n
    discarded(final DiscoveryEvent discoveryEvent)\n
    '''
