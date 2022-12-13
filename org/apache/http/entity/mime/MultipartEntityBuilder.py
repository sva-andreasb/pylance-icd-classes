def create():
    '''    public static MultipartEntityBuilder create()
    '''
def setMode():
    '''    public MultipartEntityBuilder setMode(final HttpMultipartMode mode)
    '''
def setLaxMode():
    '''    public MultipartEntityBuilder setLaxMode()
    '''
def setStrictMode():
    '''    public MultipartEntityBuilder setStrictMode()
    '''
def setBoundary():
    '''    public MultipartEntityBuilder setBoundary(final String boundary)
    '''
def setMimeSubtype():
    '''    public MultipartEntityBuilder setMimeSubtype(final String subType)
    '''
def seContentType():
    '''    public MultipartEntityBuilder seContentType(final ContentType contentType)
    '''
def setContentType():
    '''    public MultipartEntityBuilder setContentType(final ContentType contentType)
    '''
def setCharset():
    '''    public MultipartEntityBuilder setCharset(final Charset charset)
    '''
def addPart():
    '''    public MultipartEntityBuilder addPart(final FormBodyPart bodyPart)
    public MultipartEntityBuilder addPart(final String name, final ContentBody contentBody)
    '''
def addTextBody():
    '''    public MultipartEntityBuilder addTextBody(final String name, final String text, final ContentType contentType)
    public MultipartEntityBuilder addTextBody(final String name, final String text)
    '''
def addBinaryBody():
    '''    public MultipartEntityBuilder addBinaryBody(final String name, final byte[] b, final ContentType contentType, final String filename)
    public MultipartEntityBuilder addBinaryBody(final String name, final byte[] b)
    public MultipartEntityBuilder addBinaryBody(final String name, final File file, final ContentType contentType, final String filename)
    public MultipartEntityBuilder addBinaryBody(final String name, final File file)
    public MultipartEntityBuilder addBinaryBody(final String name, final InputStream stream, final ContentType contentType, final String filename)
    public MultipartEntityBuilder addBinaryBody(final String name, final InputStream stream)
    '''
def build():
    '''    public HttpEntity build()
    '''
