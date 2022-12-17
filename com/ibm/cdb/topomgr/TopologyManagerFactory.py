def getTopologyManager():
    '''returns TopologyManager\n\n
    getTopologyManager(final SessionContext sessionCtx)\n
    getTopologyManager(final SessionContext sessionCtx, final boolean enableCache)\n
    getTopologyManager()\n
    getTopologyManager(final boolean enableCache)\n
    getTopologyManager(final long version, final SessionContext sessionCtx)\n
    getTopologyManager(final long version, final SessionContext sessionCtx, final long token)\n
    getTopologyManager(final long version)\n
    getTopologyManager(final long version, final boolean enableCache)\n
    getTopologyManager(final long version, final SessionContext sessionCtx, final boolean enableCache)\n
    getTopologyManager(final long version, final SessionContext sessionCtx, final boolean enableCache, final long token)\n
    '''
def getDomainTopologyManager():
    '''returns TopologyManager\n\n
    getDomainTopologyManager(final long version, final boolean enableCache, final String hostname, final int port)\n
    '''
def registerForTopologyManager():
    '''returns None\n\n
    registerForTopologyManager(final TopologyManagerFactoryListener listener, final SessionContext sessionCtx)\n
    registerForTopologyManager(final TopologyManagerFactoryListener listener, final SessionContext sessionCtx, final boolean enableCache)\n
    registerForTopologyManager(final TopologyManagerFactoryListener listener)\n
    registerForTopologyManager(final TopologyManagerFactoryListener listener, final boolean enableCache)\n
    registerForTopologyManager(final TopologyManagerFactoryListener listener, final long version, final SessionContext sessionCtx)\n
    registerForTopologyManager(final TopologyManagerFactoryListener listener, final long version)\n
    registerForTopologyManager(final TopologyManagerFactoryListener listener, final long version, final boolean enableCache)\n
    registerForTopologyManager(final TopologyManagerFactoryListener listener, final long version, final SessionContext sessionCtx, final boolean enableCache)\n
    '''
