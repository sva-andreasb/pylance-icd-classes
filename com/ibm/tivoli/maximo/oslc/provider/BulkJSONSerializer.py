def BulkJSONSerializer():
    '''public BulkJSONSerializer(final MboSetRemote mboSet, final String osName, final String templateName, final int pageSize)
    public BulkJSONSerializer(final MboSetRemote mboSet, final String osName, final int pageSize, final String selectStatement, final String savedQuery, final boolean fetchmodedelta)
    '''
def serializeNextPage():
    '''public byte[] serializeNextPage()
    '''
def nextPageAsJson():
    '''public JSONArray nextPageAsJson(final boolean includeHref)
    public JSONArray nextPageAsJson(final boolean includeHref, final boolean includeRowStamp)
    '''
def hasNextPage():
    '''public boolean hasNextPage()
    '''
def getMaxRowStamp():
    '''public Long getMaxRowStamp()
    '''
