FROM_GROUP = "int  1"
FROM_LOCATOR = "int  2"
def ():
    '''returns ProxyReg\n\n
    (final String[] array, final LookupLocator[] array2, final DiscoveryListener discoveryListener)\n
    (final String[] array, final LookupLocator[] array2, final DiscoveryListener discoveryListener, final Configuration configuration)\n
    (final ServiceRegistrar proxy, final String[] memberGroups, final int from)\n
    '''
def getLocators():
    '''returns LookupLocator[]\n\n
    getLocators()\n
    '''
def addLocators():
    '''returns None\n\n
    addLocators(final LookupLocator[] array)\n
    '''
def removeLocators():
    '''returns None\n\n
    removeLocators(final LookupLocator[] array)\n
    '''
def setLocators():
    '''returns None\n\n
    setLocators(final LookupLocator[] locators)\n
    '''
def getGroups():
    '''returns String[]\n\n
    getGroups()\n
    '''
def addGroups():
    '''returns None\n\n
    addGroups(final String[] array)\n
    '''
def removeGroups():
    '''returns None\n\n
    removeGroups(final String[] array)\n
    '''
def setGroups():
    '''returns None\n\n
    setGroups(final String[] groups)\n
    '''
def addDiscoveryListener():
    '''returns None\n\n
    addDiscoveryListener(final DiscoveryListener discoveryListener)\n
    '''
def removeDiscoveryListener():
    '''returns None\n\n
    removeDiscoveryListener(final DiscoveryListener o)\n
    '''
def getRegistrars():
    '''returns ServiceRegistrar[]\n\n
    getRegistrars()\n
    '''
def discard():
    '''returns None\n\n
    discard(final ServiceRegistrar serviceRegistrar)\n
    discard()\n
    '''
def terminate():
    '''returns None\n\n
    terminate()\n
    '''
def getFrom():
    '''returns int\n\n
    getFrom(final ServiceRegistrar serviceRegistrar)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def discovered():
    '''returns None\n\n
    discovered(final DiscoveryEvent discoveryEvent)\n
    discovered(final DiscoveryEvent discoveryEvent)\n
    '''
def discarded():
    '''returns None\n\n
    discarded(final DiscoveryEvent discoveryEvent)\n
    discarded(final DiscoveryEvent discoveryEvent)\n
    '''
def changed():
    '''returns None\n\n
    changed(final DiscoveryEvent discoveryEvent)\n
    '''
