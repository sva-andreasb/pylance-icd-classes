def ToUnknownStream():
    '''public ToUnknownStream()
    '''
def asContentHandler():
    '''public ContentHandler asContentHandler()
    '''
def close():
    '''public void close()
    '''
def getOutputFormat():
    '''public Properties getOutputFormat()
    '''
def getOutputStream():
    '''public OutputStream getOutputStream()
    '''
def getWriter():
    '''public Writer getWriter()
    '''
def reset():
    '''public boolean reset()
    '''
def serialize():
    '''public void serialize(final Node node)
    '''
def setEscaping():
    '''public boolean setEscaping(final boolean escape)
    '''
def setOutputFormat():
    '''public void setOutputFormat(final Properties format)
    '''
def setOutputStream():
    '''public void setOutputStream(final OutputStream output)
    '''
def setWriter():
    '''public void setWriter(final Writer writer)
    '''
def addAttribute():
    '''public void addAttribute(final String uri, final String localName, final String rawName, final String type, final String value, final boolean XSLAttribute)
    public void addAttribute(final String rawName, final String value)
    '''
def addUniqueAttribute():
    '''public void addUniqueAttribute(final String rawName, final String value, final int flags)
    '''
def characters():
    '''public void characters(final String chars)
    public void characters(final char[] characters, final int offset, final int length)
    '''
def endElement():
    '''public void endElement(final String elementName)
    public void endElement(String namespaceURI, String localName, final String qName)
    '''
def startPrefixMapping():
    '''public void startPrefixMapping(final String prefix, final String uri)
    public boolean startPrefixMapping(final String prefix, final String uri, final boolean shouldFlush)
    '''
def namespaceAfterStartElement():
    '''public void namespaceAfterStartElement(final String prefix, final String uri)
    '''
def setVersion():
    '''public void setVersion(final String version)
    '''
def startDocument():
    '''public void startDocument()
    '''
def startElement():
    '''public void startElement(final String qName)
    public void startElement(final String namespaceURI, final String localName, final String qName)
    public void startElement(final String namespaceURI, final String localName, final String elementName, final Attributes atts)
    '''
def comment():
    '''public void comment(final String comment)
    public void comment(final char[] ch, final int start, final int length)
    '''
def getDoctypePublic():
    '''public String getDoctypePublic()
    '''
def getDoctypeSystem():
    '''public String getDoctypeSystem()
    '''
def getEncoding():
    '''public String getEncoding()
    '''
def getIndent():
    '''public boolean getIndent()
    '''
def getIndentAmount():
    '''public int getIndentAmount()
    '''
def getMediaType():
    '''public String getMediaType()
    '''
def getOmitXMLDeclaration():
    '''public boolean getOmitXMLDeclaration()
    '''
def getStandalone():
    '''public String getStandalone()
    '''
def getVersion():
    '''public String getVersion()
    '''
def setDoctype():
    '''public void setDoctype(final String system, final String pub)
    '''
def setDoctypePublic():
    '''public void setDoctypePublic(final String doctype)
    '''
def setDoctypeSystem():
    '''public void setDoctypeSystem(final String doctype)
    '''
def setEncoding():
    '''public void setEncoding(final String encoding)
    '''
def setIndent():
    '''public void setIndent(final boolean indent)
    '''
def setIndentAmount():
    '''public void setIndentAmount(final int value)
    '''
def setMediaType():
    '''public void setMediaType(final String mediaType)
    '''
def setOmitXMLDeclaration():
    '''public void setOmitXMLDeclaration(final boolean b)
    '''
def setStandalone():
    '''public void setStandalone(final String standalone)
    '''
def attributeDecl():
    '''public void attributeDecl(final String arg0, final String arg1, final String arg2, final String arg3, final String arg4)
    '''
def elementDecl():
    '''public void elementDecl(final String arg0, final String arg1)
    '''
def externalEntityDecl():
    '''public void externalEntityDecl(final String name, final String publicId, final String systemId)
    '''
def internalEntityDecl():
    '''public void internalEntityDecl(final String arg0, final String arg1)
    '''
def endDocument():
    '''public void endDocument()
    '''
def endPrefixMapping():
    '''public void endPrefixMapping(final String prefix)
    '''
def ignorableWhitespace():
    '''public void ignorableWhitespace(final char[] ch, final int start, final int length)
    '''
def processingInstruction():
    '''public void processingInstruction(final String target, final String data)
    '''
def setDocumentLocator():
    '''public void setDocumentLocator(final Locator locator)
    '''
def skippedEntity():
    '''public void skippedEntity(final String name)
    '''
def endCDATA():
    '''public void endCDATA()
    '''
def endDTD():
    '''public void endDTD()
    '''
def endEntity():
    '''public void endEntity(final String name)
    '''
def startCDATA():
    '''public void startCDATA()
    '''
def startDTD():
    '''public void startDTD(final String name, final String publicId, final String systemId)
    '''
def startEntity():
    '''public void startEntity(final String name)
    '''
def asDOMSerializer():
    '''public DOMSerializer asDOMSerializer()
    '''
def setCdataSectionElements():
    '''public void setCdataSectionElements(final Vector URI_and_localNames)
    '''
def addAttributes():
    '''public void addAttributes(final Attributes atts)
    '''
def getNamespaceMappings():
    '''public NamespaceMappings getNamespaceMappings()
    '''
def flushPending():
    '''public void flushPending()
    '''
def getPrefix():
    '''public String getPrefix(final String namespaceURI)
    '''
def entityReference():
    '''public void entityReference(final String entityName)
    '''
def getNamespaceURI():
    '''public String getNamespaceURI(final String qname, final boolean isElement)
    '''
def getNamespaceURIFromPrefix():
    '''public String getNamespaceURIFromPrefix(final String prefix)
    '''
def setTransformer():
    '''public void setTransformer(final Transformer t)
    '''
def getTransformer():
    '''public Transformer getTransformer()
    '''
def setContentHandler():
    '''public void setContentHandler(final ContentHandler ch)
    '''
def setSourceLocator():
    '''public void setSourceLocator(final SourceLocator locator)
    '''
def asDOM3Serializer():
    '''public Object asDOM3Serializer()
    '''
