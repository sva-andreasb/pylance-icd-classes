CONTENT_TYPE = "String  Content-type""
CONTENT_DISPOSITION = "String  Content-disposition""
CONTENT_LENGTH = "String  Content-length""
FORM_DATA = "String  form-data""
ATTACHMENT = "String  attachment""
MULTIPART = "String  multipart/""
MULTIPART_FORM_DATA = "String  multipart/form-data""
MULTIPART_MIXED = "String  multipart/mixed""
MAX_HEADER_SIZE = "int  1024"
def FileUploadBase():
'''public FileUploadBase()
'''
pass
def isMultipartContent():
'''public static final boolean isMultipartContent(final RequestContext ctx)
public static boolean isMultipartContent(final HttpServletRequest req)
'''
pass
def getSizeMax():
'''public long getSizeMax()
'''
pass
def setSizeMax():
'''public void setSizeMax(final long sizeMax)
'''
pass
def getFileSizeMax():
'''public long getFileSizeMax()
'''
pass
def setFileSizeMax():
'''public void setFileSizeMax(final long fileSizeMax)
'''
pass
def getHeaderEncoding():
'''public String getHeaderEncoding()
'''
pass
def setHeaderEncoding():
'''public void setHeaderEncoding(final String encoding)
'''
pass
def parseRequest():
'''public List<FileItem> parseRequest(final HttpServletRequest req)
public List<FileItem> parseRequest(final RequestContext ctx)
'''
pass
def getItemIterator():
'''public FileItemIterator getItemIterator(final RequestContext ctx)
'''
pass
def parseParameterMap():
'''public Map<String, List<FileItem>> parseParameterMap(final RequestContext ctx)
'''
pass
def getProgressListener():
'''public ProgressListener getProgressListener()
'''
pass
def setProgressListener():
'''public void setProgressListener(final ProgressListener pListener)
'''
pass
def hasNext():
'''public boolean hasNext()
'''
pass
def next():
'''public FileItemStream next()
'''
pass
def getContentType():
'''public String getContentType()
'''
pass
def getFieldName():
'''public String getFieldName()
public String getFieldName()
'''
pass
def getName():
'''public String getName()
'''
pass
def isFormField():
'''public boolean isFormField()
'''
pass
def openStream():
'''public InputStream openStream()
'''
pass
def getHeaders():
'''public FileItemHeaders getHeaders()
'''
pass
def setHeaders():
'''public void setHeaders(final FileItemHeaders pHeaders)
'''
pass
def FileUploadIOException():
'''public FileUploadIOException(final FileUploadException pCause)
'''
pass
def getCause():
'''public Throwable getCause()
public Throwable getCause()
'''
pass
def InvalidContentTypeException():
'''public InvalidContentTypeException()
public InvalidContentTypeException(final String message)
public InvalidContentTypeException(final String msg, final Throwable cause)
'''
pass
def IOFileUploadException():
'''public IOFileUploadException(final String pMsg, final IOException pException)
'''
pass
def getActualSize():
'''public long getActualSize()
'''
pass
def getPermittedSize():
'''public long getPermittedSize()
'''
pass
def UnknownSizeException():
'''public UnknownSizeException()
public UnknownSizeException(final String message)
'''
pass
def SizeLimitExceededException():
'''public SizeLimitExceededException()
public SizeLimitExceededException(final String message)
public SizeLimitExceededException(final String message, final long actual, final long permitted)
'''
pass
def FileSizeLimitExceededException():
'''public FileSizeLimitExceededException(final String message, final long actual, final long permitted)
'''
pass
def getFileName():
'''public String getFileName()
'''
pass
def setFileName():
'''public void setFileName(final String pFileName)
'''
pass
def setFieldName():
'''public void setFieldName(final String pFieldName)
'''
pass
