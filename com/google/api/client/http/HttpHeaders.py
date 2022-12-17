def ():
    '''returns ParseHeaderState\n\n
    ()\n
    (final HttpHeaders headers, final StringBuilder logger)\n
    '''
def clone():
    '''returns HttpHeaders\n\n
    clone()\n
    '''
def set():
    '''returns HttpHeaders\n\n
    set(final String fieldName, final Object value)\n
    '''
def setAccept():
    '''returns HttpHeaders\n\n
    setAccept(final String accept)\n
    '''
def setAcceptEncoding():
    '''returns HttpHeaders\n\n
    setAcceptEncoding(final String acceptEncoding)\n
    '''
def setAuthorization():
    '''returns HttpHeaders\n\n
    setAuthorization(final String authorization)\n
    setAuthorization(final List<String> authorization)\n
    '''
def setCacheControl():
    '''returns HttpHeaders\n\n
    setCacheControl(final String cacheControl)\n
    '''
def setContentEncoding():
    '''returns HttpHeaders\n\n
    setContentEncoding(final String contentEncoding)\n
    '''
def setContentLength():
    '''returns HttpHeaders\n\n
    setContentLength(final Long contentLength)\n
    '''
def setContentMD5():
    '''returns HttpHeaders\n\n
    setContentMD5(final String contentMD5)\n
    '''
def setContentRange():
    '''returns HttpHeaders\n\n
    setContentRange(final String contentRange)\n
    '''
def setContentType():
    '''returns HttpHeaders\n\n
    setContentType(final String contentType)\n
    '''
def setCookie():
    '''returns HttpHeaders\n\n
    setCookie(final String cookie)\n
    '''
def setDate():
    '''returns HttpHeaders\n\n
    setDate(final String date)\n
    '''
def setETag():
    '''returns HttpHeaders\n\n
    setETag(final String etag)\n
    '''
def setExpires():
    '''returns HttpHeaders\n\n
    setExpires(final String expires)\n
    '''
def setIfModifiedSince():
    '''returns HttpHeaders\n\n
    setIfModifiedSince(final String ifModifiedSince)\n
    '''
def setIfMatch():
    '''returns HttpHeaders\n\n
    setIfMatch(final String ifMatch)\n
    '''
def setIfNoneMatch():
    '''returns HttpHeaders\n\n
    setIfNoneMatch(final String ifNoneMatch)\n
    '''
def setIfUnmodifiedSince():
    '''returns HttpHeaders\n\n
    setIfUnmodifiedSince(final String ifUnmodifiedSince)\n
    '''
def setIfRange():
    '''returns HttpHeaders\n\n
    setIfRange(final String ifRange)\n
    '''
def setLastModified():
    '''returns HttpHeaders\n\n
    setLastModified(final String lastModified)\n
    '''
def setLocation():
    '''returns HttpHeaders\n\n
    setLocation(final String location)\n
    '''
def setMimeVersion():
    '''returns HttpHeaders\n\n
    setMimeVersion(final String mimeVersion)\n
    '''
def setRange():
    '''returns HttpHeaders\n\n
    setRange(final String range)\n
    '''
def setRetryAfter():
    '''returns HttpHeaders\n\n
    setRetryAfter(final String retryAfter)\n
    '''
def setUserAgent():
    '''returns HttpHeaders\n\n
    setUserAgent(final String userAgent)\n
    '''
def setAuthenticate():
    '''returns HttpHeaders\n\n
    setAuthenticate(final String authenticate)\n
    '''
def setAge():
    '''returns HttpHeaders\n\n
    setAge(final Long age)\n
    '''
def setBasicAuthentication():
    '''returns HttpHeaders\n\n
    setBasicAuthentication(final String username, final String password)\n
    '''
def getFirstHeaderStringValue():
    '''returns String\n\n
    getFirstHeaderStringValue(final String name)\n
    '''
def getHeaderStringValues():
    '''returns List<String>\n\n
    getHeaderStringValues(final String name)\n
    '''
def addHeader():
    '''returns None\n\n
    addHeader(final String name, final String value)\n
    '''
def execute():
    '''returns LowLevelHttpResponse\n\n
    execute()\n
    '''
