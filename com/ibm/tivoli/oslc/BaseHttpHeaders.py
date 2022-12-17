def ():
    '''returns BaseHttpHeaders\n\n
    (final Map<String, List<String>> headers)\n
    '''
def addBulkRequestHeaders():
    '''returns None\n\n
    addBulkRequestHeaders(final Map<String, List<String>> bulkHeaders)\n
    '''
def getSingleHeader():
    '''returns String\n\n
    getSingleHeader(final String headerName)\n
    '''
def getHeader():
    '''returns List<String>\n\n
    getHeader(final String headerName)\n
    '''
def setIfModifiedSince():
    '''returns None\n\n
    setIfModifiedSince(final Date ifModifiedSince)\n
    '''
def getIfModifiedSince():
    '''returns Date\n\n
    getIfModifiedSince()\n
    '''
def containsHeader():
    '''returns boolean\n\n
    containsHeader(final String headerName)\n
    '''
def isNoCache():
    '''returns boolean\n\n
    isNoCache()\n
    '''
def matchesEtagToNoneMatchHeader():
    '''returns boolean\n\n
    matchesEtagToNoneMatchHeader(final String etag)\n
    '''
def matchesEtagToMatchHeader():
    '''returns boolean\n\n
    matchesEtagToMatchHeader(final String etag)\n
    '''
def isEtagToMatchHeaderWildCard():
    '''returns boolean\n\n
    isEtagToMatchHeaderWildCard()\n
    '''
def isEtagNoneMatchHeaderWildCard():
    '''returns boolean\n\n
    isEtagNoneMatchHeaderWildCard()\n
    '''
