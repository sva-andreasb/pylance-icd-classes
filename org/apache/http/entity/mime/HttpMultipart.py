def HttpMultipart():
'''public HttpMultipart(final String subType, final Charset charset, final String boundary, final HttpMultipartMode mode)
public HttpMultipart(final String subType, final Charset charset, final String boundary)
public HttpMultipart(final String subType, final String boundary)
'''
pass
def getSubType():
'''public String getSubType()
'''
pass
def getCharset():
'''public Charset getCharset()
'''
pass
def getMode():
'''public HttpMultipartMode getMode()
'''
pass
def getBodyParts():
'''public List<FormBodyPart> getBodyParts()
'''
pass
def addBodyPart():
'''public void addBodyPart(final FormBodyPart part)
'''
pass
def getBoundary():
'''public String getBoundary()
'''
pass
def writeTo():
'''public void writeTo(final OutputStream out)
'''
pass
def getTotalLength():
'''public long getTotalLength()
'''
pass
