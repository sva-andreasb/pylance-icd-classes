def ():
    '''returns TransportMessage\n\n
    ()\n
    (final InputStream inputStream, final int i, final String contentType, final SOAPContext ctx, final Hashtable headers)\n
    (final String envelope, final SOAPContext ctx, final Hashtable headers)\n
    '''
def editIncoming():
    '''returns None\n\n
    editIncoming(final EnvelopeEditor envelopeEditor)\n
    '''
def editOutgoing():
    '''returns None\n\n
    editOutgoing(final EnvelopeEditor envelopeEditor)\n
    '''
def getBytes():
    '''returns byte[]\n\n
    getBytes()\n
    '''
def getContentLength():
    '''returns int\n\n
    getContentLength()\n
    '''
def getContentType():
    '''returns String\n\n
    getContentType()\n
    '''
def getEnvelope():
    '''returns String\n\n
    getEnvelope()\n
    '''
def getEnvelopeReader():
    '''returns Reader\n\n
    getEnvelopeReader()\n
    '''
def getHeader():
    '''returns String\n\n
    getHeader(final String key)\n
    '''
def getHeaderNames():
    '''returns Enumeration\n\n
    getHeaderNames()\n
    '''
def getHeaders():
    '''returns Hashtable\n\n
    getHeaders()\n
    '''
def getSOAPContext():
    '''returns SOAPContext\n\n
    getSOAPContext()\n
    '''
def read():
    '''returns String\n\n
    read()\n
    '''
def readFully():
    '''returns None\n\n
    readFully(final InputStream inputStream)\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def setBytes():
    '''returns None\n\n
    setBytes(final byte[] bytes)\n
    '''
def setContentType():
    '''returns None\n\n
    setContentType(final String contentType)\n
    '''
def setEnvelope():
    '''returns None\n\n
    setEnvelope(final String envelope)\n
    '''
def setHeader():
    '''returns None\n\n
    setHeader(final String key, final String value)\n
    '''
def unmarshall():
    '''returns Envelope\n\n
    unmarshall(final DocumentBuilder documentBuilder)\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final OutputStream outputStream)\n
    '''
