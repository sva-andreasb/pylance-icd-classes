def DisClient():
    '''public DisClient(final BulkLoaderProperties props)
    '''
def setConnProps():
    '''public void setConnProps(final Properties props)
    '''
def init():
    '''public void init()
    '''
def shutdown():
    '''public void shutdown()
    '''
def close():
    '''public void close()
    '''
def commitWork():
    '''public void commitWork()
    '''
def rollbackWork():
    '''public void rollbackWork()
    '''
def getNamingContext():
    '''public Map getNamingContext(final String[] classTypes)
    '''
def registerMSS():
    '''public Guid registerMSS(final HashMap mss)
    '''
def register():
    '''public Guid[] register(final Guid mssGuid, final HashMap[] attributeMaps)
    '''
def registerAbstractResources():
    '''public Guid[] registerAbstractResources(final Guid mssGuid, final HashMap[] attributeMaps)
    '''
def getNames():
    '''public NrsMasterAliasInfo[] getNames(final Guid[] guids)
    '''
def addRelationship():
    '''public int[] addRelationship(final Guid mssGuid, final HashMap[] attributeMaps)
    '''
def removeStale():
    '''public void removeStale(final Guid mssGuid, final Date date)
    '''
def getParentClassTypes():
    '''public String[] getParentClassTypes(final String className)
    '''
