def ():
    '''returns InMemoryRegionImpl\n\n
    (final String name, final String domain)\n
    '''
def addEndpoint():
    '''returns InMemoryRegionImpl\n\n
    addEndpoint(final String serviceName, final String endpoint)\n
    '''
def addHttps():
    '''returns InMemoryRegionImpl\n\n
    addHttps(final String serviceName)\n
    '''
def addHttp():
    '''returns InMemoryRegionImpl\n\n
    addHttp(final String serviceName)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getDomain():
    '''returns String\n\n
    getDomain()\n
    '''
def getPartition():
    '''returns String\n\n
    getPartition()\n
    '''
def isServiceSupported():
    '''returns boolean\n\n
    isServiceSupported(final String serviceName)\n
    '''
def getServiceEndpoint():
    '''returns String\n\n
    getServiceEndpoint(final String serviceName)\n
    '''
def hasHttpsEndpoint():
    '''returns boolean\n\n
    hasHttpsEndpoint(final String serviceName)\n
    '''
def hasHttpEndpoint():
    '''returns boolean\n\n
    hasHttpEndpoint(final String serviceName)\n
    '''
def getAvailableEndpoints():
    '''returns Collection<String>\n\n
    getAvailableEndpoints()\n
    '''
