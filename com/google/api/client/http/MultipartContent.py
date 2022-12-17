def ():
    '''returns Part\n\n
    ()\n
    ()\n
    (final HttpContent content)\n
    (final HttpHeaders headers, final HttpContent content)\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final OutputStream out)\n
    '''
def retrySupported():
    '''returns boolean\n\n
    retrySupported()\n
    '''
def setMediaType():
    '''returns MultipartContent\n\n
    setMediaType(final HttpMediaType mediaType)\n
    '''
def addPart():
    '''returns MultipartContent\n\n
    addPart(final Part part)\n
    '''
def setParts():
    '''returns MultipartContent\n\n
    setParts(final Collection<Part> parts)\n
    '''
def setContentParts():
    '''returns MultipartContent\n\n
    setContentParts(final Collection<? extends HttpContent> contentParts)\n
    '''
def setBoundary():
    '''returns MultipartContent\n\n
    setBoundary(final String boundary)\n
    '''
def setContent():
    '''returns Part\n\n
    setContent(final HttpContent content)\n
    '''
def getContent():
    '''returns HttpContent\n\n
    getContent()\n
    '''
def setHeaders():
    '''returns Part\n\n
    setHeaders(final HttpHeaders headers)\n
    '''
def getHeaders():
    '''returns HttpHeaders\n\n
    getHeaders()\n
    '''
def setEncoding():
    '''returns Part\n\n
    setEncoding(final HttpEncoding encoding)\n
    '''
def getEncoding():
    '''returns HttpEncoding\n\n
    getEncoding()\n
    '''
