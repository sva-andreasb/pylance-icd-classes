def create():
'''public static MultipartEntityBuilder create()
'''
pass
def setMode():
'''public MultipartEntityBuilder setMode(final HttpMultipartMode mode)
'''
pass
def setLaxMode():
'''public MultipartEntityBuilder setLaxMode()
'''
pass
def setStrictMode():
'''public MultipartEntityBuilder setStrictMode()
'''
pass
def setBoundary():
'''public MultipartEntityBuilder setBoundary(final String boundary)
'''
pass
def setMimeSubtype():
'''public MultipartEntityBuilder setMimeSubtype(final String subType)
'''
pass
def seContentType():
'''public MultipartEntityBuilder seContentType(final ContentType contentType)
'''
pass
def setContentType():
'''public MultipartEntityBuilder setContentType(final ContentType contentType)
'''
pass
def setCharset():
'''public MultipartEntityBuilder setCharset(final Charset charset)
'''
pass
def addPart():
'''public MultipartEntityBuilder addPart(final FormBodyPart bodyPart)
public MultipartEntityBuilder addPart(final String name, final ContentBody contentBody)
'''
pass
def addTextBody():
'''public MultipartEntityBuilder addTextBody(final String name, final String text, final ContentType contentType)
public MultipartEntityBuilder addTextBody(final String name, final String text)
'''
pass
def addBinaryBody():
'''public MultipartEntityBuilder addBinaryBody(final String name, final byte[] b, final ContentType contentType, final String filename)
public MultipartEntityBuilder addBinaryBody(final String name, final byte[] b)
public MultipartEntityBuilder addBinaryBody(final String name, final File file, final ContentType contentType, final String filename)
public MultipartEntityBuilder addBinaryBody(final String name, final File file)
public MultipartEntityBuilder addBinaryBody(final String name, final InputStream stream, final ContentType contentType, final String filename)
public MultipartEntityBuilder addBinaryBody(final String name, final InputStream stream)
'''
pass
def build():
'''public HttpEntity build()
'''
pass
