def MultipartContent():
    '''    public MultipartContent()
    '''
def writeTo():
    '''    public void writeTo(final OutputStream out)
    '''
def retrySupported():
    '''    public boolean retrySupported()
    '''
def setMediaType():
    '''    public MultipartContent setMediaType(final HttpMediaType mediaType)
    '''
def getParts():
    '''    public final Collection<Part> getParts()
    '''
def addPart():
    '''    public MultipartContent addPart(final Part part)
    '''
def setParts():
    '''    public MultipartContent setParts(final Collection<Part> parts)
    '''
def setContentParts():
    '''    public MultipartContent setContentParts(final Collection<? extends HttpContent> contentParts)
    '''
def getBoundary():
    '''    public final String getBoundary()
    '''
def setBoundary():
    '''    public MultipartContent setBoundary(final String boundary)
    '''
def Part():
    '''    public Part()
    public Part(final HttpContent content)
    public Part(final HttpHeaders headers, final HttpContent content)
    '''
def setContent():
    '''    public Part setContent(final HttpContent content)
    '''
def getContent():
    '''    public HttpContent getContent()
    '''
def setHeaders():
    '''    public Part setHeaders(final HttpHeaders headers)
    '''
def getHeaders():
    '''    public HttpHeaders getHeaders()
    '''
def setEncoding():
    '''    public Part setEncoding(final HttpEncoding encoding)
    '''
def getEncoding():
    '''    public HttpEncoding getEncoding()
    '''
