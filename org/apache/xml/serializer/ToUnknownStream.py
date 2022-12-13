def ToUnknownStream():
'''public ToUnknownStream()
'''
pass
def asContentHandler():
'''public ContentHandler asContentHandler()
'''
pass
def close():
'''public void close()
'''
pass
def getOutputFormat():
'''public Properties getOutputFormat()
'''
pass
def getOutputStream():
'''public OutputStream getOutputStream()
'''
pass
def getWriter():
'''public Writer getWriter()
'''
pass
def reset():
'''public boolean reset()
'''
pass
def serialize():
'''public void serialize(final Node node)
'''
pass
def setEscaping():
'''public boolean setEscaping(final boolean escape)
'''
pass
def setOutputFormat():
'''public void setOutputFormat(final Properties format)
'''
pass
def setOutputStream():
'''public void setOutputStream(final OutputStream output)
'''
pass
def setWriter():
'''public void setWriter(final Writer writer)
'''
pass
def addAttribute():
'''public void addAttribute(final String uri, final String localName, final String rawName, final String type, final String value, final boolean XSLAttribute)
public void addAttribute(final String rawName, final String value)
'''
pass
def addUniqueAttribute():
'''public void addUniqueAttribute(final String rawName, final String value, final int flags)
'''
pass
def characters():
'''public void characters(final String chars)
public void characters(final char[] characters, final int offset, final int length)
'''
pass
def endElement():
'''public void endElement(final String elementName)
public void endElement(String namespaceURI, String localName, final String qName)
'''
pass
def startPrefixMapping():
'''public void startPrefixMapping(final String prefix, final String uri)
public boolean startPrefixMapping(final String prefix, final String uri, final boolean shouldFlush)
'''
pass
def namespaceAfterStartElement():
'''public void namespaceAfterStartElement(final String prefix, final String uri)
'''
pass
def setVersion():
'''public void setVersion(final String version)
'''
pass
def startDocument():
'''public void startDocument()
'''
pass
def startElement():
'''public void startElement(final String qName)
public void startElement(final String namespaceURI, final String localName, final String qName)
public void startElement(final String namespaceURI, final String localName, final String elementName, final Attributes atts)
'''
pass
def comment():
'''public void comment(final String comment)
public void comment(final char[] ch, final int start, final int length)
'''
pass
def getDoctypePublic():
'''public String getDoctypePublic()
'''
pass
def getDoctypeSystem():
'''public String getDoctypeSystem()
'''
pass
def getEncoding():
'''public String getEncoding()
'''
pass
def getIndent():
'''public boolean getIndent()
'''
pass
def getIndentAmount():
'''public int getIndentAmount()
'''
pass
def getMediaType():
'''public String getMediaType()
'''
pass
def getOmitXMLDeclaration():
'''public boolean getOmitXMLDeclaration()
'''
pass
def getStandalone():
'''public String getStandalone()
'''
pass
def getVersion():
'''public String getVersion()
'''
pass
def setDoctype():
'''public void setDoctype(final String system, final String pub)
'''
pass
def setDoctypePublic():
'''public void setDoctypePublic(final String doctype)
'''
pass
def setDoctypeSystem():
'''public void setDoctypeSystem(final String doctype)
'''
pass
def setEncoding():
'''public void setEncoding(final String encoding)
'''
pass
def setIndent():
'''public void setIndent(final boolean indent)
'''
pass
def setIndentAmount():
'''public void setIndentAmount(final int value)
'''
pass
def setMediaType():
'''public void setMediaType(final String mediaType)
'''
pass
def setOmitXMLDeclaration():
'''public void setOmitXMLDeclaration(final boolean b)
'''
pass
def setStandalone():
'''public void setStandalone(final String standalone)
'''
pass
def attributeDecl():
'''public void attributeDecl(final String arg0, final String arg1, final String arg2, final String arg3, final String arg4)
'''
pass
def elementDecl():
'''public void elementDecl(final String arg0, final String arg1)
'''
pass
def externalEntityDecl():
'''public void externalEntityDecl(final String name, final String publicId, final String systemId)
'''
pass
def internalEntityDecl():
'''public void internalEntityDecl(final String arg0, final String arg1)
'''
pass
def endDocument():
'''public void endDocument()
'''
pass
def endPrefixMapping():
'''public void endPrefixMapping(final String prefix)
'''
pass
def ignorableWhitespace():
'''public void ignorableWhitespace(final char[] ch, final int start, final int length)
'''
pass
def processingInstruction():
'''public void processingInstruction(final String target, final String data)
'''
pass
def setDocumentLocator():
'''public void setDocumentLocator(final Locator locator)
'''
pass
def skippedEntity():
'''public void skippedEntity(final String name)
'''
pass
def endCDATA():
'''public void endCDATA()
'''
pass
def endDTD():
'''public void endDTD()
'''
pass
def endEntity():
'''public void endEntity(final String name)
'''
pass
def startCDATA():
'''public void startCDATA()
'''
pass
def startDTD():
'''public void startDTD(final String name, final String publicId, final String systemId)
'''
pass
def startEntity():
'''public void startEntity(final String name)
'''
pass
def asDOMSerializer():
'''public DOMSerializer asDOMSerializer()
'''
pass
def setCdataSectionElements():
'''public void setCdataSectionElements(final Vector URI_and_localNames)
'''
pass
def addAttributes():
'''public void addAttributes(final Attributes atts)
'''
pass
def getNamespaceMappings():
'''public NamespaceMappings getNamespaceMappings()
'''
pass
def flushPending():
'''public void flushPending()
'''
pass
def getPrefix():
'''public String getPrefix(final String namespaceURI)
'''
pass
def entityReference():
'''public void entityReference(final String entityName)
'''
pass
def getNamespaceURI():
'''public String getNamespaceURI(final String qname, final boolean isElement)
'''
pass
def getNamespaceURIFromPrefix():
'''public String getNamespaceURIFromPrefix(final String prefix)
'''
pass
def setTransformer():
'''public void setTransformer(final Transformer t)
'''
pass
def getTransformer():
'''public Transformer getTransformer()
'''
pass
def setContentHandler():
'''public void setContentHandler(final ContentHandler ch)
'''
pass
def setSourceLocator():
'''public void setSourceLocator(final SourceLocator locator)
'''
pass
def asDOM3Serializer():
'''public Object asDOM3Serializer()
'''
pass
