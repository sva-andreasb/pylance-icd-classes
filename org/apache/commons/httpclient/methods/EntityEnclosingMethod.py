CONTENT_LENGTH_AUTO = "long  -2L"
CONTENT_LENGTH_CHUNKED = "long  -1L"
def ():
    '''returns EntityEnclosingMethod\n\n
    ()\n
    (final String uri)\n
    '''
def getFollowRedirects():
    '''returns boolean\n\n
    getFollowRedirects()\n
    '''
def setFollowRedirects():
    '''returns None\n\n
    setFollowRedirects(final boolean followRedirects)\n
    '''
def setRequestContentLength():
    '''returns None\n\n
    setRequestContentLength(final int length)\n
    setRequestContentLength(final long length)\n
    '''
def getRequestCharSet():
    '''returns String\n\n
    getRequestCharSet()\n
    '''
def setContentChunked():
    '''returns None\n\n
    setContentChunked(final boolean chunked)\n
    '''
def setRequestBody():
    '''returns None\n\n
    setRequestBody(final InputStream body)\n
    setRequestBody(final String body)\n
    '''
def recycle():
    '''returns None\n\n
    recycle()\n
    '''
def getRequestEntity():
    '''returns RequestEntity\n\n
    getRequestEntity()\n
    '''
def setRequestEntity():
    '''returns None\n\n
    setRequestEntity(final RequestEntity requestEntity)\n
    '''
