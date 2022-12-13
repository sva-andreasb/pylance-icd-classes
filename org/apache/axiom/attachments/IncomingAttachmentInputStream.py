HEADER_CONTENT_DESCRIPTION = "String  \"content-description\""
HEADER_CONTENT_TYPE = "String  \"content-type\""
HEADER_CONTENT_TRANSFER_ENCODING = "String  \"content-transfer-encoding\""
HEADER_CONTENT_TYPE_JMS = "String  \"contentType\""
HEADER_CONTENT_LENGTH = "String  \"content-length\""
HEADER_CONTENT_LOCATION = "String  \"content-location\""
HEADER_CONTENT_ID = "String  \"content-id\""
def IncomingAttachmentInputStream():
    '''    public IncomingAttachmentInputStream(final InputStream in, final IncomingAttachmentStreams parentContainer)
    '''
def getHeaders():
    '''    public Map getHeaders()
    '''
def addHeader():
    '''    public void addHeader(final String name, final String value)
    '''
def getHeader():
    '''    public String getHeader(final String name)
    '''
def getContentId():
    '''    public String getContentId()
    '''
def getContentLocation():
    '''    public String getContentLocation()
    '''
def getContentType():
    '''    public String getContentType()
    '''
def markSupported():
    '''    public boolean markSupported()
    '''
def reset():
    '''    public void reset()
    '''
def mark():
    '''    public void mark(final int readLimit)
    '''
def read():
    '''    public int read()
    public int read(final byte[] b)
    public int read(final byte[] b, final int off, final int len)
    '''
