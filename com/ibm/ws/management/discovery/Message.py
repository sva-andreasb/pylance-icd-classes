XMLEncoding = "String  \"<?xml version=\\"1.0\\"  standalone='yes'?>\""
DestinationTagStart = "String  \"<JxtaMessageDest>\""
DestinationTagEnd = "String  \"</JxtaMessageDest>\""
SourceTagStart = "String  \"<JxtaMessageSrc>\""
SourceTagEnd = "String  \"</JxtaMessageSrc>\""
DigestTagStart = "String  \"<JxtaMessageDigest>\""
DigestTagEnd = "String  \"</JxtaMessageDigest>\""
def ():
    '''returns Message\n\n
    (final InputStream data)\n
    (final InputStream data, final EndpointAddress source, final EndpointAddress destination)\n
    (final byte[] array)\n
    (final byte[] array, final int offset, final int len)\n
    '''
def getInputStream():
    '''returns InputStream\n\n
    getInputStream()\n
    '''
def getDataInputStream():
    '''returns InputStream\n\n
    getDataInputStream()\n
    '''
def getDestinationAddress():
    '''returns EndpointAddress\n\n
    getDestinationAddress()\n
    '''
def getSourceAddress():
    '''returns EndpointAddress\n\n
    getSourceAddress()\n
    '''
def setDestinationAddress():
    '''returns None\n\n
    setDestinationAddress(final EndpointAddress destination)\n
    '''
def setSourceAddress():
    '''returns None\n\n
    setSourceAddress(final EndpointAddress source)\n
    '''
