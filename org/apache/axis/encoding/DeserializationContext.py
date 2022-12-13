def deserializing():
'''public void deserializing(final boolean isDeserializing)
'''
pass
def DeserializationContext():
'''public DeserializationContext(final MessageContext ctx, final SOAPHandler initialHandler)
public DeserializationContext(final InputSource is, final MessageContext ctx, final String messageType)
public DeserializationContext(final InputSource is, final MessageContext ctx, final String messageType, final SOAPEnvelope env)
'''
pass
def getSOAPConstants():
'''public SOAPConstants getSOAPConstants()
'''
pass
def parse():
'''public void parse()
'''
pass
def getCurElement():
'''public MessageElement getCurElement()
'''
pass
def setCurElement():
'''public void setCurElement(final MessageElement el)
'''
pass
def getMessageContext():
'''public MessageContext getMessageContext()
'''
pass
def getEncodingStyle():
'''public String getEncodingStyle()
'''
pass
def getEnvelope():
'''public SOAPEnvelope getEnvelope()
'''
pass
def getRecorder():
'''public SAX2EventRecorder getRecorder()
'''
pass
def setRecorder():
'''public void setRecorder(final SAX2EventRecorder recorder)
'''
pass
def getCurrentNSMappings():
'''public ArrayList getCurrentNSMappings()
'''
pass
def getNamespaceURI():
'''public String getNamespaceURI(final String prefix)
'''
pass
def getQNameFromString():
'''public QName getQNameFromString(final String qNameStr)
'''
pass
def getTypeFromXSITypeAttr():
'''public QName getTypeFromXSITypeAttr(final String namespace, final String localName, final Attributes attrs)
'''
pass
def getTypeFromAttributes():
'''public QName getTypeFromAttributes(final String namespace, final String localName, final Attributes attrs)
'''
pass
def isNil():
'''public boolean isNil(final Attributes attrs)
'''
pass
def getDeserializer():
'''public final Deserializer getDeserializer(final Class cls, final QName xmlType)
'''
pass
def getDeserializerForClass():
'''public Deserializer getDeserializerForClass(Class cls)
'''
pass
def setDestinationClass():
'''public void setDestinationClass(final Class destClass)
'''
pass
def getDestinationClass():
'''public Class getDestinationClass()
'''
pass
def getDeserializerForType():
'''public final Deserializer getDeserializerForType(final QName xmlType)
'''
pass
def getTypeMapping():
'''public TypeMapping getTypeMapping()
'''
pass
def getTypeMappingRegistry():
'''public TypeMappingRegistry getTypeMappingRegistry()
'''
pass
def getElementByID():
'''public MessageElement getElementByID(final String id)
'''
pass
def getObjectByRef():
'''public Object getObjectByRef(final String href)
'''
pass
def addObjectById():
'''public void addObjectById(final String id, final Object obj)
'''
pass
def registerFixup():
'''public void registerFixup(final String href, final Deserializer dser)
'''
pass
def registerElementByID():
'''public void registerElementByID(final String id, final MessageElement elem)
'''
pass
def registerResolverForID():
'''public void registerResolverForID(final String id, final IDResolver resolver)
'''
pass
def hasElementsByID():
'''public boolean hasElementsByID()
'''
pass
def getCurrentRecordPos():
'''public int getCurrentRecordPos()
'''
pass
def getStartOfMappingsPos():
'''public int getStartOfMappingsPos()
'''
pass
def pushNewElement():
'''public void pushNewElement(final MessageElement elem)
'''
pass
def pushElementHandler():
'''public void pushElementHandler(final SOAPHandler handler)
'''
pass
def replaceElementHandler():
'''public void replaceElementHandler(final SOAPHandler handler)
'''
pass
def popElementHandler():
'''public SOAPHandler popElementHandler()
'''
pass
def setProcessingRef():
'''public void setProcessingRef(final boolean ref)
'''
pass
def isProcessingRef():
'''public boolean isProcessingRef()
'''
pass
def startDocument():
'''public void startDocument()
'''
pass
def endDocument():
'''public void endDocument()
'''
pass
def isDoneParsing():
'''public boolean isDoneParsing()
'''
pass
def startPrefixMapping():
'''public void startPrefixMapping(final String prefix, final String uri)
'''
pass
def endPrefixMapping():
'''public void endPrefixMapping(final String prefix)
'''
pass
def setDocumentLocator():
'''public void setDocumentLocator(final Locator locator)
'''
pass
def getDocumentLocator():
'''public Locator getDocumentLocator()
'''
pass
def characters():
'''public void characters(final char[] p1, final int p2, final int p3)
'''
pass
def ignorableWhitespace():
'''public void ignorableWhitespace(final char[] p1, final int p2, final int p3)
'''
pass
def processingInstruction():
'''public void processingInstruction(final String p1, final String p2)
'''
pass
def skippedEntity():
'''public void skippedEntity(final String p1)
'''
pass
def startElement():
'''public void startElement(final String namespace, final String localName, final String qName, Attributes attributes)
'''
pass
def endElement():
'''public void endElement(final String namespace, final String localName, final String qName)
'''
pass
def startDTD():
'''public void startDTD(final String name, final String publicId, final String systemId)
public void startDTD(final String arg0, final String arg1, final String arg2)
'''
pass
def endDTD():
'''public void endDTD()
public void endDTD()
'''
pass
def startEntity():
'''public void startEntity(final String name)
public void startEntity(final String arg0)
'''
pass
def endEntity():
'''public void endEntity(final String name)
public void endEntity(final String arg0)
'''
pass
def startCDATA():
'''public void startCDATA()
public void startCDATA()
'''
pass
def endCDATA():
'''public void endCDATA()
public void endCDATA()
'''
pass
def comment():
'''public void comment(final char[] ch, final int start, final int length)
public void comment(final char[] arg0, final int arg1, final int arg2)
'''
pass
def resolveEntity():
'''public InputSource resolveEntity(final String publicId, final String systemId)
'''
pass
def addReferencedObject():
'''public void addReferencedObject(final String id, final Object referent)
'''
pass
def getReferencedObject():
'''public Object getReferencedObject(final String href)
'''
pass
