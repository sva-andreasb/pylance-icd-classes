def deserializing():
    '''public void deserializing(final boolean isDeserializing)
    '''
def DeserializationContext():
    '''public DeserializationContext(final MessageContext ctx, final SOAPHandler initialHandler)
    public DeserializationContext(final InputSource is, final MessageContext ctx, final String messageType)
    public DeserializationContext(final InputSource is, final MessageContext ctx, final String messageType, final SOAPEnvelope env)
    '''
def getSOAPConstants():
    '''public SOAPConstants getSOAPConstants()
    '''
def parse():
    '''public void parse()
    '''
def getCurElement():
    '''public MessageElement getCurElement()
    '''
def setCurElement():
    '''public void setCurElement(final MessageElement el)
    '''
def getMessageContext():
    '''public MessageContext getMessageContext()
    '''
def getEncodingStyle():
    '''public String getEncodingStyle()
    '''
def getEnvelope():
    '''public SOAPEnvelope getEnvelope()
    '''
def getRecorder():
    '''public SAX2EventRecorder getRecorder()
    '''
def setRecorder():
    '''public void setRecorder(final SAX2EventRecorder recorder)
    '''
def getCurrentNSMappings():
    '''public ArrayList getCurrentNSMappings()
    '''
def getNamespaceURI():
    '''public String getNamespaceURI(final String prefix)
    '''
def getQNameFromString():
    '''public QName getQNameFromString(final String qNameStr)
    '''
def getTypeFromXSITypeAttr():
    '''public QName getTypeFromXSITypeAttr(final String namespace, final String localName, final Attributes attrs)
    '''
def getTypeFromAttributes():
    '''public QName getTypeFromAttributes(final String namespace, final String localName, final Attributes attrs)
    '''
def isNil():
    '''public boolean isNil(final Attributes attrs)
    '''
def getDeserializer():
    '''public final Deserializer getDeserializer(final Class cls, final QName xmlType)
    '''
def getDeserializerForClass():
    '''public Deserializer getDeserializerForClass(Class cls)
    '''
def setDestinationClass():
    '''public void setDestinationClass(final Class destClass)
    '''
def getDestinationClass():
    '''public Class getDestinationClass()
    '''
def getDeserializerForType():
    '''public final Deserializer getDeserializerForType(final QName xmlType)
    '''
def getTypeMapping():
    '''public TypeMapping getTypeMapping()
    '''
def getTypeMappingRegistry():
    '''public TypeMappingRegistry getTypeMappingRegistry()
    '''
def getElementByID():
    '''public MessageElement getElementByID(final String id)
    '''
def getObjectByRef():
    '''public Object getObjectByRef(final String href)
    '''
def addObjectById():
    '''public void addObjectById(final String id, final Object obj)
    '''
def registerFixup():
    '''public void registerFixup(final String href, final Deserializer dser)
    '''
def registerElementByID():
    '''public void registerElementByID(final String id, final MessageElement elem)
    '''
def registerResolverForID():
    '''public void registerResolverForID(final String id, final IDResolver resolver)
    '''
def hasElementsByID():
    '''public boolean hasElementsByID()
    '''
def getCurrentRecordPos():
    '''public int getCurrentRecordPos()
    '''
def getStartOfMappingsPos():
    '''public int getStartOfMappingsPos()
    '''
def pushNewElement():
    '''public void pushNewElement(final MessageElement elem)
    '''
def pushElementHandler():
    '''public void pushElementHandler(final SOAPHandler handler)
    '''
def replaceElementHandler():
    '''public void replaceElementHandler(final SOAPHandler handler)
    '''
def popElementHandler():
    '''public SOAPHandler popElementHandler()
    '''
def setProcessingRef():
    '''public void setProcessingRef(final boolean ref)
    '''
def isProcessingRef():
    '''public boolean isProcessingRef()
    '''
def startDocument():
    '''public void startDocument()
    '''
def endDocument():
    '''public void endDocument()
    '''
def isDoneParsing():
    '''public boolean isDoneParsing()
    '''
def startPrefixMapping():
    '''public void startPrefixMapping(final String prefix, final String uri)
    '''
def endPrefixMapping():
    '''public void endPrefixMapping(final String prefix)
    '''
def setDocumentLocator():
    '''public void setDocumentLocator(final Locator locator)
    '''
def getDocumentLocator():
    '''public Locator getDocumentLocator()
    '''
def characters():
    '''public void characters(final char[] p1, final int p2, final int p3)
    '''
def ignorableWhitespace():
    '''public void ignorableWhitespace(final char[] p1, final int p2, final int p3)
    '''
def processingInstruction():
    '''public void processingInstruction(final String p1, final String p2)
    '''
def skippedEntity():
    '''public void skippedEntity(final String p1)
    '''
def startElement():
    '''public void startElement(final String namespace, final String localName, final String qName, Attributes attributes)
    '''
def endElement():
    '''public void endElement(final String namespace, final String localName, final String qName)
    '''
def startDTD():
    '''public void startDTD(final String name, final String publicId, final String systemId)
    public void startDTD(final String arg0, final String arg1, final String arg2)
    '''
def endDTD():
    '''public void endDTD()
    public void endDTD()
    '''
def startEntity():
    '''public void startEntity(final String name)
    public void startEntity(final String arg0)
    '''
def endEntity():
    '''public void endEntity(final String name)
    public void endEntity(final String arg0)
    '''
def startCDATA():
    '''public void startCDATA()
    public void startCDATA()
    '''
def endCDATA():
    '''public void endCDATA()
    public void endCDATA()
    '''
def comment():
    '''public void comment(final char[] ch, final int start, final int length)
    public void comment(final char[] arg0, final int arg1, final int arg2)
    '''
def resolveEntity():
    '''public InputSource resolveEntity(final String publicId, final String systemId)
    '''
def addReferencedObject():
    '''public void addReferencedObject(final String id, final Object referent)
    '''
def getReferencedObject():
    '''public Object getReferencedObject(final String href)
    '''
