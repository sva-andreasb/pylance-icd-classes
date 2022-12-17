def ():
    '''returns SOAPEnvelope\n\n
    ()\n
    (final SOAPConstants soapConstants)\n
    (final SOAPConstants soapConstants, final SchemaVersion schemaVersion)\n
    (final boolean registerPrefixes, final SOAPConstants soapConstants)\n
    (final boolean registerPrefixes, SOAPConstants soapConstants, final SchemaVersion schemaVersion)\n
    (final InputStream input)\n
    '''
def getMessageType():
    '''returns String\n\n
    getMessageType()\n
    '''
def setMessageType():
    '''returns None\n\n
    setMessageType(final String messageType)\n
    '''
def getBodyElements():
    '''returns Vector\n\n
    getBodyElements()\n
    '''
def getTrailers():
    '''returns Vector\n\n
    getTrailers()\n
    '''
def getFirstBody():
    '''returns SOAPBodyElement\n\n
    getFirstBody()\n
    '''
def getHeaders():
    '''returns Vector\n\n
    getHeaders()\n
    '''
def getHeadersByActor():
    '''returns Vector\n\n
    getHeadersByActor(final ArrayList actors)\n
    '''
def addHeader():
    '''returns None\n\n
    addHeader(final SOAPHeaderElement hdr)\n
    '''
def addBodyElement():
    '''returns None\n\n
    addBodyElement(final SOAPBodyElement element)\n
    '''
def removeHeaders():
    '''returns None\n\n
    removeHeaders()\n
    '''
def setHeader():
    '''returns None\n\n
    setHeader(final SOAPHeader hdr)\n
    '''
def removeHeader():
    '''returns None\n\n
    removeHeader(final SOAPHeaderElement hdr)\n
    '''
def removeBody():
    '''returns None\n\n
    removeBody()\n
    '''
def setBody():
    '''returns None\n\n
    setBody(final SOAPBody body)\n
    '''
def removeBodyElement():
    '''returns None\n\n
    removeBodyElement(final SOAPBodyElement element)\n
    '''
def removeTrailer():
    '''returns None\n\n
    removeTrailer(final MessageElement element)\n
    '''
def clearBody():
    '''returns None\n\n
    clearBody()\n
    '''
def addTrailer():
    '''returns None\n\n
    addTrailer(final MessageElement element)\n
    '''
def getHeaderByName():
    '''returns SOAPHeaderElement\n\n
    getHeaderByName(final String namespace, final String localPart)\n
    getHeaderByName(final String namespace, final String localPart, final boolean accessAllHeaders)\n
    '''
def getBodyByName():
    '''returns SOAPBodyElement\n\n
    getBodyByName(final String namespace, final String localPart)\n
    '''
def getHeadersByName():
    '''returns Enumeration\n\n
    getHeadersByName(final String namespace, final String localPart)\n
    getHeadersByName(final String namespace, final String localPart, final boolean accessAllHeaders)\n
    '''
def outputImpl():
    '''returns None\n\n
    outputImpl(final SerializationContext context)\n
    '''
def getSOAPConstants():
    '''returns SOAPConstants\n\n
    getSOAPConstants()\n
    '''
def setSoapConstants():
    '''returns None\n\n
    setSoapConstants(final SOAPConstants soapConstants)\n
    '''
def getSchemaVersion():
    '''returns SchemaVersion\n\n
    getSchemaVersion()\n
    '''
def setSchemaVersion():
    '''returns None\n\n
    setSchemaVersion(final SchemaVersion schemaVersion)\n
    '''
def createName():
    '''returns Name\n\n
    createName(final String localName)\n
    createName(final String localName, final String prefix, final String uri)\n
    '''
def setSAAJEncodingCompliance():
    '''returns None\n\n
    setSAAJEncodingCompliance(final boolean comply)\n
    '''
def removeChild():
    '''returns Node\n\n
    removeChild(final Node oldChild)\n
    '''
def cloneNode():
    '''returns Node\n\n
    cloneNode(final boolean deep)\n
    '''
def setOwnerDocument():
    '''returns None\n\n
    setOwnerDocument(final SOAPPart sp)\n
    '''
def setRecorded():
    '''returns None\n\n
    setRecorded(final boolean recorded)\n
    '''
def isRecorded():
    '''returns boolean\n\n
    isRecorded()\n
    '''
def setDirty():
    '''returns None\n\n
    setDirty(final boolean dirty)\n
    '''
