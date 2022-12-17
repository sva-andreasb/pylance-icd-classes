def ():
    '''returns BulkJSONSerializer\n\n
    (final MboSetRemote mboSet, final String osName, final String templateName, final int pageSize)\n
    (final MboSetRemote mboSet, final String osName, final int pageSize, final String selectStatement, final String savedQuery, final boolean fetchmodedelta)\n
    '''
def serializeNextPage():
    '''returns byte[]\n\n
    serializeNextPage()\n
    '''
def nextPageAsJson():
    '''returns JSONArray\n\n
    nextPageAsJson(final boolean includeHref)\n
    nextPageAsJson(final boolean includeHref, final boolean includeRowStamp)\n
    '''
def hasNextPage():
    '''returns boolean\n\n
    hasNextPage()\n
    '''
def getMaxRowStamp():
    '''returns Long\n\n
    getMaxRowStamp()\n
    '''
