CONTENT_TYPE = "String  \"Content-type\""
CONTENT_DISPOSITION = "String  \"Content-disposition\""
CONTENT_LENGTH = "String  \"Content-length\""
FORM_DATA = "String  \"form-data\""
ATTACHMENT = "String  \"attachment\""
MULTIPART = "String  \"multipart/\""
MULTIPART_FORM_DATA = "String  \"multipart/form-data\""
MULTIPART_MIXED = "String  \"multipart/mixed\""
MAX_HEADER_SIZE = "int  1024"
def ():
    '''returns FileSizeLimitExceededException\n\n
    ()\n
    (final FileUploadException pCause)\n
    ()\n
    (final String message)\n
    (final String msg, final Throwable cause)\n
    (final String pMsg, final IOException pException)\n
    ()\n
    (final String message)\n
    ()\n
    (final String message)\n
    (final String message, final long actual, final long permitted)\n
    (final String message, final long actual, final long permitted)\n
    '''
def getSizeMax():
    '''returns long\n\n
    getSizeMax()\n
    '''
def setSizeMax():
    '''returns None\n\n
    setSizeMax(final long sizeMax)\n
    '''
def getFileSizeMax():
    '''returns long\n\n
    getFileSizeMax()\n
    '''
def setFileSizeMax():
    '''returns None\n\n
    setFileSizeMax(final long fileSizeMax)\n
    '''
def getHeaderEncoding():
    '''returns String\n\n
    getHeaderEncoding()\n
    '''
def setHeaderEncoding():
    '''returns None\n\n
    setHeaderEncoding(final String encoding)\n
    '''
def parseRequest():
    '''returns List<FileItem>\n\n
    parseRequest(final HttpServletRequest req)\n
    parseRequest(final RequestContext ctx)\n
    '''
def getItemIterator():
    '''returns FileItemIterator\n\n
    getItemIterator(final RequestContext ctx)\n
    '''
def getProgressListener():
    '''returns ProgressListener\n\n
    getProgressListener()\n
    '''
def setProgressListener():
    '''returns None\n\n
    setProgressListener(final ProgressListener pListener)\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns FileItemStream\n\n
    next()\n
    '''
def getContentType():
    '''returns String\n\n
    getContentType()\n
    '''
def getFieldName():
    '''returns String\n\n
    getFieldName()\n
    getFieldName()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def isFormField():
    '''returns boolean\n\n
    isFormField()\n
    '''
def openStream():
    '''returns InputStream\n\n
    openStream()\n
    '''
def getHeaders():
    '''returns FileItemHeaders\n\n
    getHeaders()\n
    '''
def setHeaders():
    '''returns None\n\n
    setHeaders(final FileItemHeaders pHeaders)\n
    '''
def getCause():
    '''returns Throwable\n\n
    getCause()\n
    getCause()\n
    '''
def getActualSize():
    '''returns long\n\n
    getActualSize()\n
    '''
def getPermittedSize():
    '''returns long\n\n
    getPermittedSize()\n
    '''
def getFileName():
    '''returns String\n\n
    getFileName()\n
    '''
def setFileName():
    '''returns None\n\n
    setFileName(final String pFileName)\n
    '''
def setFieldName():
    '''returns None\n\n
    setFieldName(final String pFieldName)\n
    '''
