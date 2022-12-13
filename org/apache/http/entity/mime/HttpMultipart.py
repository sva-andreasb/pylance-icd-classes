def HttpMultipart():
    '''    public HttpMultipart(final String subType, final Charset charset, final String boundary, final HttpMultipartMode mode)
    public HttpMultipart(final String subType, final Charset charset, final String boundary)
    public HttpMultipart(final String subType, final String boundary)
    '''
def getSubType():
    '''    public String getSubType()
    '''
def getCharset():
    '''    public Charset getCharset()
    '''
def getMode():
    '''    public HttpMultipartMode getMode()
    '''
def getBodyParts():
    '''    public List<FormBodyPart> getBodyParts()
    '''
def addBodyPart():
    '''    public void addBodyPart(final FormBodyPart part)
    '''
def getBoundary():
    '''    public String getBoundary()
    '''
def writeTo():
    '''    public void writeTo(final OutputStream out)
    '''
def getTotalLength():
    '''    public long getTotalLength()
    '''
