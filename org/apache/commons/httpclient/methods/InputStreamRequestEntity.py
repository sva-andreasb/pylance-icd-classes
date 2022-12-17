CONTENT_LENGTH_AUTO = "int  -2"
def ():
    '''returns InputStreamRequestEntity\n\n
    (final InputStream content)\n
    (final InputStream content, final String contentType)\n
    (final InputStream content, final long contentLength)\n
    (final InputStream content, final long contentLength, final String contentType)\n
    '''
def getContentType():
    '''returns String\n\n
    getContentType()\n
    '''
def isRepeatable():
    '''returns boolean\n\n
    isRepeatable()\n
    '''
def writeRequest():
    '''returns None\n\n
    writeRequest(final OutputStream out)\n
    '''
def getContentLength():
    '''returns long\n\n
    getContentLength()\n
    '''
def getContent():
    '''returns InputStream\n\n
    getContent()\n
    '''
