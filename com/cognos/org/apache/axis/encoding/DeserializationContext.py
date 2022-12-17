def deserializing():
    '''returns None\n\n
    deserializing(final boolean isDeserializing)\n
    '''
def ():
    '''returns DeserializationContext\n\n
    (final MessageContext ctx, final SOAPHandler initialHandler)\n
    (final InputSource is, final MessageContext ctx, final String messageType)\n
    (final InputSource is, final MessageContext ctx, final String messageType, final SOAPEnvelope env)\n
    '''
def getSOAPConstants():
    '''returns SOAPConstants\n\n
    getSOAPConstants()\n
    '''
def parse():
    '''returns None\n\n
    parse()\n
    '''
def getCurElement():
    '''returns MessageElement\n\n
    getCurElement()\n
    '''
def setCurElement():
    '''returns None\n\n
    setCurElement(final MessageElement el)\n
    '''
def getMessageContext():
    '''returns MessageContext\n\n
    getMessageContext()\n
    '''
def getEncodingStyle():
    '''returns String\n\n
    getEncodingStyle()\n
    '''
def getEnvelope():
    '''returns SOAPEnvelope\n\n
    getEnvelope()\n
    '''
def getRecorder():
    '''returns SAX2EventRecorder\n\n
    getRecorder()\n
    '''
def setRecorder():
    '''returns None\n\n
    setRecorder(final SAX2EventRecorder recorder)\n
    '''
def getCurrentNSMappings():
    '''returns ArrayList\n\n
    getCurrentNSMappings()\n
    '''
def getNamespaceURI():
    '''returns String\n\n
    getNamespaceURI(final String prefix)\n
    '''
def getQNameFromString():
    '''returns QName\n\n
    getQNameFromString(final String qNameStr)\n
    '''
def getTypeFromXSITypeAttr():
    '''returns QName\n\n
    getTypeFromXSITypeAttr(final String namespace, final String localName, final Attributes attrs)\n
    '''
def getTypeFromAttributes():
    '''returns QName\n\n
    getTypeFromAttributes(final String namespace, final String localName, final Attributes attrs)\n
    '''
def isNil():
    '''returns boolean\n\n
    isNil(final Attributes attrs)\n
    '''
def getDeserializerForClass():
    '''returns Deserializer\n\n
    getDeserializerForClass(Class cls)\n
    '''
def setDestinationClass():
    '''returns None\n\n
    setDestinationClass(final Class destClass)\n
    '''
def getDestinationClass():
    '''returns Class\n\n
    getDestinationClass()\n
    '''
def getTypeMapping():
    '''returns TypeMapping\n\n
    getTypeMapping()\n
    '''
def getTypeMappingRegistry():
    '''returns TypeMappingRegistry\n\n
    getTypeMappingRegistry()\n
    '''
def getElementByID():
    '''returns MessageElement\n\n
    getElementByID(final String id)\n
    '''
def getObjectByRef():
    '''returns Object\n\n
    getObjectByRef(final String href)\n
    '''
def addObjectById():
    '''returns None\n\n
    addObjectById(final String id, final Object obj)\n
    '''
def registerFixup():
    '''returns None\n\n
    registerFixup(final String href, final Deserializer dser)\n
    '''
def registerElementByID():
    '''returns None\n\n
    registerElementByID(final String id, final MessageElement elem)\n
    '''
def registerResolverForID():
    '''returns None\n\n
    registerResolverForID(final String id, final IDResolver resolver)\n
    '''
def hasElementsByID():
    '''returns boolean\n\n
    hasElementsByID()\n
    '''
def getCurrentRecordPos():
    '''returns int\n\n
    getCurrentRecordPos()\n
    '''
def getStartOfMappingsPos():
    '''returns int\n\n
    getStartOfMappingsPos()\n
    '''
def pushNewElement():
    '''returns None\n\n
    pushNewElement(final MessageElement elem)\n
    '''
def pushElementHandler():
    '''returns None\n\n
    pushElementHandler(final SOAPHandler handler)\n
    '''
def replaceElementHandler():
    '''returns None\n\n
    replaceElementHandler(final SOAPHandler handler)\n
    '''
def popElementHandler():
    '''returns SOAPHandler\n\n
    popElementHandler()\n
    '''
def setProcessingRef():
    '''returns None\n\n
    setProcessingRef(final boolean ref)\n
    '''
def isProcessingRef():
    '''returns boolean\n\n
    isProcessingRef()\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument()\n
    '''
def endDocument():
    '''returns None\n\n
    endDocument()\n
    '''
def isDoneParsing():
    '''returns boolean\n\n
    isDoneParsing()\n
    '''
def startPrefixMapping():
    '''returns None\n\n
    startPrefixMapping(final String prefix, final String uri)\n
    '''
def endPrefixMapping():
    '''returns None\n\n
    endPrefixMapping(final String prefix)\n
    '''
def setDocumentLocator():
    '''returns None\n\n
    setDocumentLocator(final Locator locator)\n
    '''
def getDocumentLocator():
    '''returns Locator\n\n
    getDocumentLocator()\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] p1, final int p2, final int p3)\n
    '''
def ignorableWhitespace():
    '''returns None\n\n
    ignorableWhitespace(final char[] p1, final int p2, final int p3)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String p1, final String p2)\n
    '''
def skippedEntity():
    '''returns None\n\n
    skippedEntity(final String p1)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String namespace, final String localName, final String qName, Attributes attributes)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String namespace, final String localName, final String qName)\n
    '''
def startDTD():
    '''returns None\n\n
    startDTD(final String name, final String publicId, final String systemId)\n
    startDTD(final String arg0, final String arg1, final String arg2)\n
    '''
def endDTD():
    '''returns None\n\n
    endDTD()\n
    endDTD()\n
    '''
def startEntity():
    '''returns None\n\n
    startEntity(final String name)\n
    startEntity(final String arg0)\n
    '''
def endEntity():
    '''returns None\n\n
    endEntity(final String name)\n
    endEntity(final String arg0)\n
    '''
def startCDATA():
    '''returns None\n\n
    startCDATA()\n
    startCDATA()\n
    '''
def endCDATA():
    '''returns None\n\n
    endCDATA()\n
    endCDATA()\n
    '''
def comment():
    '''returns None\n\n
    comment(final char[] ch, final int start, final int length)\n
    comment(final char[] arg0, final int arg1, final int arg2)\n
    '''
def resolveEntity():
    '''returns InputSource\n\n
    resolveEntity(final String publicId, final String systemId)\n
    '''
def addReferencedObject():
    '''returns None\n\n
    addReferencedObject(final String id, final Object referent)\n
    '''
def getReferencedObject():
    '''returns Object\n\n
    getReferencedObject(final String href)\n
    '''
