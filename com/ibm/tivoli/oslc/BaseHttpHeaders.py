def BaseHttpHeaders():
    '''public BaseHttpHeaders(final Map<String, List<String>> headers)
    '''
def getHeaders():
    '''public Map<String, List<String>> getHeaders()
    '''
def addBulkRequestHeaders():
    '''public void addBulkRequestHeaders(final Map<String, List<String>> bulkHeaders)
    '''
def getSingleHeader():
    '''public String getSingleHeader(final String headerName)
    '''
def getHeader():
    '''public List<String> getHeader(final String headerName)
    '''
def setIfModifiedSince():
    '''public void setIfModifiedSince(final Date ifModifiedSince)
    '''
def getIfModifiedSince():
    '''public Date getIfModifiedSince()
    '''
def containsHeader():
    '''public boolean containsHeader(final String headerName)
    '''
def isNoCache():
    '''public boolean isNoCache()
    '''
def matchesEtagToNoneMatchHeader():
    '''public boolean matchesEtagToNoneMatchHeader(final String etag)
    '''
def matchesEtagToMatchHeader():
    '''public boolean matchesEtagToMatchHeader(final String etag)
    '''
def isEtagToMatchHeaderWildCard():
    '''public boolean isEtagToMatchHeaderWildCard()
    '''
def isEtagNoneMatchHeaderWildCard():
    '''public boolean isEtagNoneMatchHeaderWildCard()
    '''
