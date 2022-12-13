def BulkJSONSerializer():
'''public BulkJSONSerializer(final MboSetRemote mboSet, final String osName, final String templateName, final int pageSize)
public BulkJSONSerializer(final MboSetRemote mboSet, final String osName, final int pageSize, final String selectStatement, final String savedQuery, final boolean fetchmodedelta)
'''
pass
def serializeNextPage():
'''public byte[] serializeNextPage()
'''
pass
def nextPageAsJson():
'''public JSONArray nextPageAsJson(final boolean includeHref)
public JSONArray nextPageAsJson(final boolean includeHref, final boolean includeRowStamp)
'''
pass
def hasNextPage():
'''public boolean hasNextPage()
'''
pass
def getMaxRowStamp():
'''public Long getMaxRowStamp()
'''
pass
