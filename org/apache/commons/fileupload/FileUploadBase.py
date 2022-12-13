CONTENT_TYPE = "String  \"Content-type\""
CONTENT_DISPOSITION = "String  \"Content-disposition\""
CONTENT_LENGTH = "String  \"Content-length\""
FORM_DATA = "String  \"form-data\""
ATTACHMENT = "String  \"attachment\""
MULTIPART = "String  \"multipart/\""
MULTIPART_FORM_DATA = "String  \"multipart/form-data\""
MULTIPART_MIXED = "String  \"multipart/mixed\""
MAX_HEADER_SIZE = "int  1024"
def FileUploadBase():
    '''public FileUploadBase()
    '''
def isMultipartContent():
    '''public static final boolean isMultipartContent(final RequestContext ctx)
    public static boolean isMultipartContent(final HttpServletRequest req)
    '''
def getSizeMax():
    '''public long getSizeMax()
    '''
def setSizeMax():
    '''public void setSizeMax(final long sizeMax)
    '''
def getFileSizeMax():
    '''public long getFileSizeMax()
    '''
def setFileSizeMax():
    '''public void setFileSizeMax(final long fileSizeMax)
    '''
def getHeaderEncoding():
    '''public String getHeaderEncoding()
    '''
def setHeaderEncoding():
    '''public void setHeaderEncoding(final String encoding)
    '''
def parseRequest():
    '''public List<FileItem> parseRequest(final HttpServletRequest req)
    public List<FileItem> parseRequest(final RequestContext ctx)
    '''
def getItemIterator():
    '''public FileItemIterator getItemIterator(final RequestContext ctx)
    '''
def parseParameterMap():
    '''public Map<String, List<FileItem>> parseParameterMap(final RequestContext ctx)
    '''
def getProgressListener():
    '''public ProgressListener getProgressListener()
    '''
def setProgressListener():
    '''public void setProgressListener(final ProgressListener pListener)
    '''
def hasNext():
    '''public boolean hasNext()
    '''
def next():
    '''public FileItemStream next()
    '''
def getContentType():
    '''public String getContentType()
    '''
def getFieldName():
    '''public String getFieldName()
    public String getFieldName()
    '''
def getName():
    '''public String getName()
    '''
def isFormField():
    '''public boolean isFormField()
    '''
def openStream():
    '''public InputStream openStream()
    '''
def getHeaders():
    '''public FileItemHeaders getHeaders()
    '''
def setHeaders():
    '''public void setHeaders(final FileItemHeaders pHeaders)
    '''
def FileUploadIOException():
    '''public FileUploadIOException(final FileUploadException pCause)
    '''
def getCause():
    '''public Throwable getCause()
    public Throwable getCause()
    '''
def InvalidContentTypeException():
    '''public InvalidContentTypeException()
    public InvalidContentTypeException(final String message)
    public InvalidContentTypeException(final String msg, final Throwable cause)
    '''
def IOFileUploadException():
    '''public IOFileUploadException(final String pMsg, final IOException pException)
    '''
def getActualSize():
    '''public long getActualSize()
    '''
def getPermittedSize():
    '''public long getPermittedSize()
    '''
def UnknownSizeException():
    '''public UnknownSizeException()
    public UnknownSizeException(final String message)
    '''
def SizeLimitExceededException():
    '''public SizeLimitExceededException()
    public SizeLimitExceededException(final String message)
    public SizeLimitExceededException(final String message, final long actual, final long permitted)
    '''
def FileSizeLimitExceededException():
    '''public FileSizeLimitExceededException(final String message, final long actual, final long permitted)
    '''
def getFileName():
    '''public String getFileName()
    '''
def setFileName():
    '''public void setFileName(final String pFileName)
    '''
def setFieldName():
    '''public void setFieldName(final String pFieldName)
    '''
