def MultipartEntity():
    '''    public MultipartEntity(HttpMultipartMode mode, String boundary, final Charset charset)
    public MultipartEntity(final HttpMultipartMode mode)
    public MultipartEntity()
    '''
def addPart():
    '''    public void addPart(final FormBodyPart bodyPart)
    public void addPart(final String name, final ContentBody contentBody)
    '''
def isRepeatable():
    '''    public boolean isRepeatable()
    '''
def isChunked():
    '''    public boolean isChunked()
    '''
def isStreaming():
    '''    public boolean isStreaming()
    '''
def getContentLength():
    '''    public long getContentLength()
    '''
def getContentType():
    '''    public Header getContentType()
    '''
def getContentEncoding():
    '''    public Header getContentEncoding()
    '''
def consumeContent():
    '''    public void consumeContent()
    '''
def getContent():
    '''    public InputStream getContent()
    '''
def writeTo():
    '''    public void writeTo(final OutputStream outstream)
    '''
