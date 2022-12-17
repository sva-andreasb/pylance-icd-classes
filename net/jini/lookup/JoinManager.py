def ():
    '''returns ProxyReg\n\n
    (final Object o, final Entry[] array, final ServiceIDListener serviceIDListener, final DiscoveryManagement discMgr, final LeaseRenewalManager leaseRenewalManager)\n
    (final Object o, final Entry[] array, final ServiceIDListener serviceIDListener, final DiscoveryManagement discMgr, final LeaseRenewalManager leaseRenewalManager, final Configuration configuration)\n
    (final Object o, final Entry[] array, final ServiceID serviceID, final DiscoveryManagement discMgr, final LeaseRenewalManager leaseRenewalManager)\n
    (final Object o, final Entry[] array, final ServiceID serviceID, final DiscoveryManagement discMgr, final LeaseRenewalManager leaseRenewalManager, final Configuration configuration)\n
    (final ServiceRegistrar proxy)\n
    '''
def getDiscoveryManager():
    '''returns DiscoveryManagement\n\n
    getDiscoveryManager()\n
    '''
def getLeaseRenewalManager():
    '''returns LeaseRenewalManager\n\n
    getLeaseRenewalManager()\n
    '''
def getJoinSet():
    '''returns ServiceRegistrar[]\n\n
    getJoinSet()\n
    '''
def getAttributes():
    '''returns Entry[]\n\n
    getAttributes()\n
    '''
def addAttributes():
    '''returns None\n\n
    addAttributes(final Entry[] array)\n
    addAttributes(final Entry[] array, final boolean b)\n
    addAttributes(final Entry[] array)\n
    '''
def setAttributes():
    '''returns None\n\n
    setAttributes(final Entry[] array)\n
    setAttributes(final Entry[] attributes)\n
    '''
def modifyAttributes():
    '''returns None\n\n
    modifyAttributes(final Entry[] array, final Entry[] array2)\n
    modifyAttributes(final Entry[] array, final Entry[] array2, final boolean b)\n
    modifyAttributes(final Entry[] array, final Entry[] array2)\n
    '''
def terminate():
    '''returns None\n\n
    terminate()\n
    '''
def tryOnce():
    '''returns boolean\n\n
    tryOnce()\n
    '''
def retryTime():
    '''returns long\n\n
    retryTime()\n
    '''
def runAfter():
    '''returns boolean\n\n
    runAfter(final List list, final int n)\n
    '''
def getProxyReg():
    '''returns ProxyReg\n\n
    getProxyReg()\n
    '''
def getSeqN():
    '''returns int\n\n
    getSeqN()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def addTask():
    '''returns None\n\n
    addTask(final JoinTask joinTask)\n
    '''
def register():
    '''returns None\n\n
    register(final Entry[] array)\n
    '''
def fail():
    '''returns None\n\n
    fail(final Throwable thrown)\n
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
    '''
def discovered():
    '''returns None\n\n
    discovered(final DiscoveryEvent discoveryEvent)\n
    '''
def discarded():
    '''returns None\n\n
    discarded(final DiscoveryEvent discoveryEvent)\n
    '''
