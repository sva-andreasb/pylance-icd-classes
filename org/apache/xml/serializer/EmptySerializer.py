def asContentHandler():
    '''    public ContentHandler asContentHandler()
    '''
def setContentHandler():
    '''    public void setContentHandler(final ContentHandler ch)
    '''
def close():
    '''    public void close()
    '''
def getOutputFormat():
    '''    public Properties getOutputFormat()
    '''
def getOutputStream():
    '''    public OutputStream getOutputStream()
    '''
def getWriter():
    '''    public Writer getWriter()
    '''
def reset():
    '''    public boolean reset()
    '''
def serialize():
    '''    public void serialize(final Node node)
    '''
def setCdataSectionElements():
    '''    public void setCdataSectionElements(final Vector URI_and_localNames)
    public void setCdataSectionElements(final Hashtable h)
    '''
def setEscaping():
    '''    public boolean setEscaping(final boolean escape)
    '''
def setIndent():
    '''    public void setIndent(final boolean indent)
    '''
def setIndentAmount():
    '''    public void setIndentAmount(final int spaces)
    '''
def setOutputFormat():
    '''    public void setOutputFormat(final Properties format)
    '''
def setOutputStream():
    '''    public void setOutputStream(final OutputStream output)
    '''
def setVersion():
    '''    public void setVersion(final String version)
    '''
def setWriter():
    '''    public void setWriter(final Writer writer)
    '''
def setTransformer():
    '''    public void setTransformer(final Transformer transformer)
    '''
def getTransformer():
    '''    public Transformer getTransformer()
    '''
def flushPending():
    '''    public void flushPending()
    '''
def addAttribute():
    '''    public void addAttribute(final String uri, final String localName, final String rawName, final String type, final String value, final boolean XSLAttribute)
    public void addAttribute(final String name, final String value)
    public void addAttribute(final String uri, final String localName, final String rawName, final String type, final String value)
    '''
def addAttributes():
    '''    public void addAttributes(final Attributes atts)
    '''
def characters():
    '''    public void characters(final String chars)
    public void characters(final char[] arg0, final int arg1, final int arg2)
    public void characters(final Node node)
    '''
def endElement():
    '''    public void endElement(final String elemName)
    public void endElement(final String arg0, final String arg1, final String arg2)
    '''
def startDocument():
    '''    public void startDocument()
    '''
def startElement():
    '''    public void startElement(final String uri, final String localName, final String qName)
    public void startElement(final String qName)
    public void startElement(final String arg0, final String arg1, final String arg2, final Attributes arg3)
    '''
def namespaceAfterStartElement():
    '''    public void namespaceAfterStartElement(final String uri, final String prefix)
    '''
def startPrefixMapping():
    '''    public boolean startPrefixMapping(final String prefix, final String uri, final boolean shouldFlush)
    public void startPrefixMapping(final String arg0, final String arg1)
    '''
def entityReference():
    '''    public void entityReference(final String entityName)
    '''
def getNamespaceMappings():
    '''    public NamespaceMappings getNamespaceMappings()
    '''
def getPrefix():
    '''    public String getPrefix(final String uri)
    '''
def getNamespaceURI():
    '''    public String getNamespaceURI(final String name, final boolean isElement)
    '''
def getNamespaceURIFromPrefix():
    '''    public String getNamespaceURIFromPrefix(final String prefix)
    '''
def setDocumentLocator():
    '''    public void setDocumentLocator(final Locator arg0)
    '''
def endDocument():
    '''    public void endDocument()
    '''
def endPrefixMapping():
    '''    public void endPrefixMapping(final String arg0)
    '''
def ignorableWhitespace():
    '''    public void ignorableWhitespace(final char[] arg0, final int arg1, final int arg2)
    '''
def processingInstruction():
    '''    public void processingInstruction(final String arg0, final String arg1)
    '''
def skippedEntity():
    '''    public void skippedEntity(final String arg0)
    '''
def comment():
    '''    public void comment(final String comment)
    public void comment(final char[] arg0, final int arg1, final int arg2)
    '''
def startDTD():
    '''    public void startDTD(final String arg0, final String arg1, final String arg2)
    '''
def endDTD():
    '''    public void endDTD()
    '''
def startEntity():
    '''    public void startEntity(final String arg0)
    '''
def endEntity():
    '''    public void endEntity(final String arg0)
    '''
def startCDATA():
    '''    public void startCDATA()
    '''
def endCDATA():
    '''    public void endCDATA()
    '''
def getDoctypePublic():
    '''    public String getDoctypePublic()
    '''
def getDoctypeSystem():
    '''    public String getDoctypeSystem()
    '''
def getEncoding():
    '''    public String getEncoding()
    '''
def getIndent():
    '''    public boolean getIndent()
    '''
def getIndentAmount():
    '''    public int getIndentAmount()
    '''
def getMediaType():
    '''    public String getMediaType()
    '''
def getOmitXMLDeclaration():
    '''    public boolean getOmitXMLDeclaration()
    '''
def getStandalone():
    '''    public String getStandalone()
    '''
def getVersion():
    '''    public String getVersion()
    '''
def setDoctype():
    '''    public void setDoctype(final String system, final String pub)
    '''
def setDoctypePublic():
    '''    public void setDoctypePublic(final String doctype)
    '''
def setDoctypeSystem():
    '''    public void setDoctypeSystem(final String doctype)
    '''
def setEncoding():
    '''    public void setEncoding(final String encoding)
    '''
def setMediaType():
    '''    public void setMediaType(final String mediatype)
    '''
def setOmitXMLDeclaration():
    '''    public void setOmitXMLDeclaration(final boolean b)
    '''
def setStandalone():
    '''    public void setStandalone(final String standalone)
    '''
def elementDecl():
    '''    public void elementDecl(final String arg0, final String arg1)
    '''
def attributeDecl():
    '''    public void attributeDecl(final String arg0, final String arg1, final String arg2, final String arg3, final String arg4)
    '''
def internalEntityDecl():
    '''    public void internalEntityDecl(final String arg0, final String arg1)
    '''
def externalEntityDecl():
    '''    public void externalEntityDecl(final String arg0, final String arg1, final String arg2)
    '''
def warning():
    '''    public void warning(final SAXParseException arg0)
    '''
def error():
    '''    public void error(final SAXParseException arg0)
    '''
def fatalError():
    '''    public void fatalError(final SAXParseException arg0)
    '''
def asDOMSerializer():
    '''    public DOMSerializer asDOMSerializer()
    '''
def setNamespaceMappings():
    '''    public void setNamespaceMappings(final NamespaceMappings mappings)
    '''
def setSourceLocator():
    '''    public void setSourceLocator(final SourceLocator locator)
    '''
def addUniqueAttribute():
    '''    public void addUniqueAttribute(final String name, final String value, final int flags)
    '''
def addXSLAttribute():
    '''    public void addXSLAttribute(final String qName, final String value, final String uri)
    '''
def notationDecl():
    '''    public void notationDecl(final String arg0, final String arg1, final String arg2)
    '''
def unparsedEntityDecl():
    '''    public void unparsedEntityDecl(final String arg0, final String arg1, final String arg2, final String arg3)
    '''
def setDTDEntityExpansion():
    '''    public void setDTDEntityExpansion(final boolean expand)
    '''
def getOutputProperty():
    '''    public String getOutputProperty(final String name)
    '''
def getOutputPropertyDefault():
    '''    public String getOutputPropertyDefault(final String name)
    '''
def setOutputProperty():
    '''    public void setOutputProperty(final String name, final String val)
    '''
def setOutputPropertyDefault():
    '''    public void setOutputPropertyDefault(final String name, final String val)
    '''
def asDOM3Serializer():
    '''    public Object asDOM3Serializer()
    '''
