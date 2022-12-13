def MultipartEntity():
'''public MultipartEntity(HttpMultipartMode mode, String boundary, final Charset charset)
public MultipartEntity(final HttpMultipartMode mode)
public MultipartEntity()
'''
pass
def addPart():
'''public void addPart(final FormBodyPart bodyPart)
public void addPart(final String name, final ContentBody contentBody)
'''
pass
def isRepeatable():
'''public boolean isRepeatable()
'''
pass
def isChunked():
'''public boolean isChunked()
'''
pass
def isStreaming():
'''public boolean isStreaming()
'''
pass
def getContentLength():
'''public long getContentLength()
'''
pass
def getContentType():
'''public Header getContentType()
'''
pass
def getContentEncoding():
'''public Header getContentEncoding()
'''
pass
def consumeContent():
'''public void consumeContent()
'''
pass
def getContent():
'''public InputStream getContent()
'''
pass
def writeTo():
'''public void writeTo(final OutputStream outstream)
'''
pass
