def ():
    '''returns MockLowLevelHttpResponse\n\n
    ()\n
    '''
def addHeader():
    '''returns MockLowLevelHttpResponse\n\n
    addHeader(final String name, final String value)\n
    '''
def setContent():
    '''returns MockLowLevelHttpResponse\n\n
    setContent(final String stringContent)\n
    setContent(final byte[] byteContent)\n
    setContent(final InputStream content)\n
    '''
def setZeroContent():
    '''returns MockLowLevelHttpResponse\n\n
    setZeroContent()\n
    '''
def getContent():
    '''returns InputStream\n\n
    getContent()\n
    '''
def getContentEncoding():
    '''returns String\n\n
    getContentEncoding()\n
    '''
def getContentLength():
    '''returns long\n\n
    getContentLength()\n
    '''
def getHeaderCount():
    '''returns int\n\n
    getHeaderCount()\n
    '''
def getHeaderName():
    '''returns String\n\n
    getHeaderName(final int index)\n
    '''
def getHeaderValue():
    '''returns String\n\n
    getHeaderValue(final int index)\n
    '''
def getReasonPhrase():
    '''returns String\n\n
    getReasonPhrase()\n
    '''
def getStatusCode():
    '''returns int\n\n
    getStatusCode()\n
    '''
def getStatusLine():
    '''returns String\n\n
    getStatusLine()\n
    '''
def setHeaderNames():
    '''returns MockLowLevelHttpResponse\n\n
    setHeaderNames(final List<String> headerNames)\n
    '''
def setHeaderValues():
    '''returns MockLowLevelHttpResponse\n\n
    setHeaderValues(final List<String> headerValues)\n
    '''
def setContentType():
    '''returns MockLowLevelHttpResponse\n\n
    setContentType(final String contentType)\n
    '''
def setContentEncoding():
    '''returns MockLowLevelHttpResponse\n\n
    setContentEncoding(final String contentEncoding)\n
    '''
def setContentLength():
    '''returns MockLowLevelHttpResponse\n\n
    setContentLength(final long contentLength)\n
    '''
def setStatusCode():
    '''returns MockLowLevelHttpResponse\n\n
    setStatusCode(final int statusCode)\n
    '''
def setReasonPhrase():
    '''returns MockLowLevelHttpResponse\n\n
    setReasonPhrase(final String reasonPhrase)\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect()\n
    '''
def isDisconnected():
    '''returns boolean\n\n
    isDisconnected()\n
    '''
