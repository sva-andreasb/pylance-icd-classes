def MultipartContent():
'''public MultipartContent()
'''
pass
def writeTo():
'''public void writeTo(final OutputStream out)
'''
pass
def retrySupported():
'''public boolean retrySupported()
'''
pass
def setMediaType():
'''public MultipartContent setMediaType(final HttpMediaType mediaType)
'''
pass
def getParts():
'''public final Collection<Part> getParts()
'''
pass
def addPart():
'''public MultipartContent addPart(final Part part)
'''
pass
def setParts():
'''public MultipartContent setParts(final Collection<Part> parts)
'''
pass
def setContentParts():
'''public MultipartContent setContentParts(final Collection<? extends HttpContent> contentParts)
'''
pass
def getBoundary():
'''public final String getBoundary()
'''
pass
def setBoundary():
'''public MultipartContent setBoundary(final String boundary)
'''
pass
def Part():
'''public Part()
public Part(final HttpContent content)
public Part(final HttpHeaders headers, final HttpContent content)
'''
pass
def setContent():
'''public Part setContent(final HttpContent content)
'''
pass
def getContent():
'''public HttpContent getContent()
'''
pass
def setHeaders():
'''public Part setHeaders(final HttpHeaders headers)
'''
pass
def getHeaders():
'''public HttpHeaders getHeaders()
'''
pass
def setEncoding():
'''public Part setEncoding(final HttpEncoding encoding)
'''
pass
def getEncoding():
'''public HttpEncoding getEncoding()
'''
pass
