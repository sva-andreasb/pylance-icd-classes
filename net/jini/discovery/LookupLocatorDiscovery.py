def ():
    '''returns DiscoveryTask\n\n
    (final LookupLocator[] array)\n
    (final LookupLocator[] array, final Configuration configuration)\n
    (final LookupLocator l)\n
    (final ArrayList listeners, final Map groupsMap, final boolean discard)\n
    ()\n
    (final LocatorReg reg, final TaskManager taskManager, final WakeupManager wakeupManager)\n
    '''
def addDiscoveryListener():
    '''returns None\n\n
    addDiscoveryListener(final DiscoveryListener e)\n
    '''
def getRegistrars():
    '''returns ServiceRegistrar[]\n\n
    getRegistrars()\n
    '''
def discard():
    '''returns None\n\n
    discard(final ServiceRegistrar serviceRegistrar)\n
    '''
def setLocators():
    '''returns None\n\n
    setLocators(final LookupLocator[] array)\n
    '''
def removeLocators():
    '''returns None\n\n
    removeLocators(final LookupLocator[] array)\n
    '''
def calcNextTryTime():
    '''returns None\n\n
    calcNextTryTime()\n
    '''
def fixupNextTryTime():
    '''returns None\n\n
    fixupNextTryTime()\n
    '''
def tryGetProxy():
    '''returns boolean\n\n
    tryGetProxy()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def run():
    '''returns None\n\n
    run()\n
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
