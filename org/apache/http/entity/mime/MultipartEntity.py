def ():
    '''returns MultipartEntity\n\n
    (HttpMultipartMode mode, String boundary, final Charset charset)\n
    (final HttpMultipartMode mode)\n
    ()\n
    '''
def addPart():
    '''returns None\n\n
    addPart(final FormBodyPart bodyPart)\n
    addPart(final String name, final ContentBody contentBody)\n
    '''
def isRepeatable():
    '''returns boolean\n\n
    isRepeatable()\n
    '''
def isChunked():
    '''returns boolean\n\n
    isChunked()\n
    '''
def isStreaming():
    '''returns boolean\n\n
    isStreaming()\n
    '''
def getContentLength():
    '''returns long\n\n
    getContentLength()\n
    '''
def getContentType():
    '''returns Header\n\n
    getContentType()\n
    '''
def getContentEncoding():
    '''returns Header\n\n
    getContentEncoding()\n
    '''
def consumeContent():
    '''returns None\n\n
    consumeContent()\n
    '''
def getContent():
    '''returns InputStream\n\n
    getContent()\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final OutputStream outstream)\n
    '''
