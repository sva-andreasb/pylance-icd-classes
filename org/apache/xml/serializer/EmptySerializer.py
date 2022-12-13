def asContentHandler():
'''public ContentHandler asContentHandler()
'''
pass
def setContentHandler():
'''public void setContentHandler(final ContentHandler ch)
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
def setCdataSectionElements():
'''public void setCdataSectionElements(final Vector URI_and_localNames)
public void setCdataSectionElements(final Hashtable h)
'''
pass
def setEscaping():
'''public boolean setEscaping(final boolean escape)
'''
pass
def setIndent():
'''public void setIndent(final boolean indent)
'''
pass
def setIndentAmount():
'''public void setIndentAmount(final int spaces)
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
def setVersion():
'''public void setVersion(final String version)
'''
pass
def setWriter():
'''public void setWriter(final Writer writer)
'''
pass
def setTransformer():
'''public void setTransformer(final Transformer transformer)
'''
pass
def getTransformer():
'''public Transformer getTransformer()
'''
pass
def flushPending():
'''public void flushPending()
'''
pass
def addAttribute():
'''public void addAttribute(final String uri, final String localName, final String rawName, final String type, final String value, final boolean XSLAttribute)
public void addAttribute(final String name, final String value)
public void addAttribute(final String uri, final String localName, final String rawName, final String type, final String value)
'''
pass
def addAttributes():
'''public void addAttributes(final Attributes atts)
'''
pass
def characters():
'''public void characters(final String chars)
public void characters(final char[] arg0, final int arg1, final int arg2)
public void characters(final Node node)
'''
pass
def endElement():
'''public void endElement(final String elemName)
public void endElement(final String arg0, final String arg1, final String arg2)
'''
pass
def startDocument():
'''public void startDocument()
'''
pass
def startElement():
'''public void startElement(final String uri, final String localName, final String qName)
public void startElement(final String qName)
public void startElement(final String arg0, final String arg1, final String arg2, final Attributes arg3)
'''
pass
def namespaceAfterStartElement():
'''public void namespaceAfterStartElement(final String uri, final String prefix)
'''
pass
def startPrefixMapping():
'''public boolean startPrefixMapping(final String prefix, final String uri, final boolean shouldFlush)
public void startPrefixMapping(final String arg0, final String arg1)
'''
pass
def entityReference():
'''public void entityReference(final String entityName)
'''
pass
def getNamespaceMappings():
'''public NamespaceMappings getNamespaceMappings()
'''
pass
def getPrefix():
'''public String getPrefix(final String uri)
'''
pass
def getNamespaceURI():
'''public String getNamespaceURI(final String name, final boolean isElement)
'''
pass
def getNamespaceURIFromPrefix():
'''public String getNamespaceURIFromPrefix(final String prefix)
'''
pass
def setDocumentLocator():
'''public void setDocumentLocator(final Locator arg0)
'''
pass
def endDocument():
'''public void endDocument()
'''
pass
def endPrefixMapping():
'''public void endPrefixMapping(final String arg0)
'''
pass
def ignorableWhitespace():
'''public void ignorableWhitespace(final char[] arg0, final int arg1, final int arg2)
'''
pass
def processingInstruction():
'''public void processingInstruction(final String arg0, final String arg1)
'''
pass
def skippedEntity():
'''public void skippedEntity(final String arg0)
'''
pass
def comment():
'''public void comment(final String comment)
public void comment(final char[] arg0, final int arg1, final int arg2)
'''
pass
def startDTD():
'''public void startDTD(final String arg0, final String arg1, final String arg2)
'''
pass
def endDTD():
'''public void endDTD()
'''
pass
def startEntity():
'''public void startEntity(final String arg0)
'''
pass
def endEntity():
'''public void endEntity(final String arg0)
'''
pass
def startCDATA():
'''public void startCDATA()
'''
pass
def endCDATA():
'''public void endCDATA()
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
def setMediaType():
'''public void setMediaType(final String mediatype)
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
def elementDecl():
'''public void elementDecl(final String arg0, final String arg1)
'''
pass
def attributeDecl():
'''public void attributeDecl(final String arg0, final String arg1, final String arg2, final String arg3, final String arg4)
'''
pass
def internalEntityDecl():
'''public void internalEntityDecl(final String arg0, final String arg1)
'''
pass
def externalEntityDecl():
'''public void externalEntityDecl(final String arg0, final String arg1, final String arg2)
'''
pass
def warning():
'''public void warning(final SAXParseException arg0)
'''
pass
def error():
'''public void error(final SAXParseException arg0)
'''
pass
def fatalError():
'''public void fatalError(final SAXParseException arg0)
'''
pass
def asDOMSerializer():
'''public DOMSerializer asDOMSerializer()
'''
pass
def setNamespaceMappings():
'''public void setNamespaceMappings(final NamespaceMappings mappings)
'''
pass
def setSourceLocator():
'''public void setSourceLocator(final SourceLocator locator)
'''
pass
def addUniqueAttribute():
'''public void addUniqueAttribute(final String name, final String value, final int flags)
'''
pass
def addXSLAttribute():
'''public void addXSLAttribute(final String qName, final String value, final String uri)
'''
pass
def notationDecl():
'''public void notationDecl(final String arg0, final String arg1, final String arg2)
'''
pass
def unparsedEntityDecl():
'''public void unparsedEntityDecl(final String arg0, final String arg1, final String arg2, final String arg3)
'''
pass
def setDTDEntityExpansion():
'''public void setDTDEntityExpansion(final boolean expand)
'''
pass
def getOutputProperty():
'''public String getOutputProperty(final String name)
'''
pass
def getOutputPropertyDefault():
'''public String getOutputPropertyDefault(final String name)
'''
pass
def setOutputProperty():
'''public void setOutputProperty(final String name, final String val)
'''
pass
def setOutputPropertyDefault():
'''public void setOutputPropertyDefault(final String name, final String val)
'''
pass
def asDOM3Serializer():
'''public Object asDOM3Serializer()
'''
pass
