def setMode():
    '''returns MultipartEntityBuilder\n\n
    setMode(final HttpMultipartMode mode)\n
    '''
def setLaxMode():
    '''returns MultipartEntityBuilder\n\n
    setLaxMode()\n
    '''
def setStrictMode():
    '''returns MultipartEntityBuilder\n\n
    setStrictMode()\n
    '''
def setBoundary():
    '''returns MultipartEntityBuilder\n\n
    setBoundary(final String boundary)\n
    '''
def setMimeSubtype():
    '''returns MultipartEntityBuilder\n\n
    setMimeSubtype(final String subType)\n
    '''
def seContentType():
    '''returns MultipartEntityBuilder\n\n
    seContentType(final ContentType contentType)\n
    '''
def setContentType():
    '''returns MultipartEntityBuilder\n\n
    setContentType(final ContentType contentType)\n
    '''
def setCharset():
    '''returns MultipartEntityBuilder\n\n
    setCharset(final Charset charset)\n
    '''
def addPart():
    '''returns MultipartEntityBuilder\n\n
    addPart(final FormBodyPart bodyPart)\n
    addPart(final String name, final ContentBody contentBody)\n
    '''
def addTextBody():
    '''returns MultipartEntityBuilder\n\n
    addTextBody(final String name, final String text, final ContentType contentType)\n
    addTextBody(final String name, final String text)\n
    '''
def addBinaryBody():
    '''returns MultipartEntityBuilder\n\n
    addBinaryBody(final String name, final byte[] b, final ContentType contentType, final String filename)\n
    addBinaryBody(final String name, final byte[] b)\n
    addBinaryBody(final String name, final File file, final ContentType contentType, final String filename)\n
    addBinaryBody(final String name, final File file)\n
    addBinaryBody(final String name, final InputStream stream, final ContentType contentType, final String filename)\n
    addBinaryBody(final String name, final InputStream stream)\n
    '''
def build():
    '''returns HttpEntity\n\n
    build()\n
    '''
