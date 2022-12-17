def ():
    '''returns DisClient\n\n
    (final BulkLoaderProperties props)\n
    '''
def setConnProps():
    '''returns None\n\n
    setConnProps(final Properties props)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def commitWork():
    '''returns None\n\n
    commitWork()\n
    '''
def rollbackWork():
    '''returns None\n\n
    rollbackWork()\n
    '''
def getNamingContext():
    '''returns Map\n\n
    getNamingContext(final String[] classTypes)\n
    '''
def registerMSS():
    '''returns Guid\n\n
    registerMSS(final HashMap mss)\n
    '''
def register():
    '''returns Guid[]\n\n
    register(final Guid mssGuid, final HashMap[] attributeMaps)\n
    '''
def registerAbstractResources():
    '''returns Guid[]\n\n
    registerAbstractResources(final Guid mssGuid, final HashMap[] attributeMaps)\n
    '''
def getNames():
    '''returns NrsMasterAliasInfo[]\n\n
    getNames(final Guid[] guids)\n
    '''
def addRelationship():
    '''returns int[]\n\n
    addRelationship(final Guid mssGuid, final HashMap[] attributeMaps)\n
    '''
def removeStale():
    '''returns None\n\n
    removeStale(final Guid mssGuid, final Date date)\n
    '''
def getParentClassTypes():
    '''returns String[]\n\n
    getParentClassTypes(final String className)\n
    '''
