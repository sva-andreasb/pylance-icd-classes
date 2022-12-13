def ToXMLSAXHandler():
'''public ToXMLSAXHandler()
public ToXMLSAXHandler(final ContentHandler handler, final String encoding)
public ToXMLSAXHandler(final ContentHandler handler, final LexicalHandler lex, final String encoding)
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
def indent():
'''public void indent(final int n)
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
def attributeDecl():
'''public void attributeDecl(final String arg0, final String arg1, final String arg2, final String arg3, final String arg4)
'''
pass
def elementDecl():
'''public void elementDecl(final String arg0, final String arg1)
'''
pass
def externalEntityDecl():
'''public void externalEntityDecl(final String arg0, final String arg1, final String arg2)
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
def closeCDATA():
'''public void closeCDATA()
'''
pass
def endElement():
'''public void endElement(String namespaceURI, String localName, final String qName)
public void endElement(final String elemName)
'''
pass
def endPrefixMapping():
'''public void endPrefixMapping(final String prefix)
'''
pass
def ignorableWhitespace():
'''public void ignorableWhitespace(final char[] arg0, final int arg1, final int arg2)
'''
pass
def setDocumentLocator():
'''public void setDocumentLocator(final Locator arg0)
'''
pass
def skippedEntity():
'''public void skippedEntity(final String arg0)
'''
pass
def startPrefixMapping():
'''public void startPrefixMapping(final String prefix, final String uri)
public boolean startPrefixMapping(final String prefix, final String uri, final boolean shouldFlush)
'''
pass
def comment():
'''public void comment(final char[] arg0, final int arg1, final int arg2)
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
def startEntity():
'''public void startEntity(final String arg0)
'''
pass
def characters():
'''public void characters(final String chars)
public void characters(final char[] ch, final int off, final int len)
'''
pass
def startElement():
'''public void startElement(final String elementNamespaceURI, final String elementLocalName, final String elementName)
public void startElement(final String elementName)
public void startElement(final String namespaceURI, final String localName, final String name, final Attributes atts)
'''
pass
def namespaceAfterStartElement():
'''public void namespaceAfterStartElement(final String prefix, final String uri)
'''
pass
def processingInstruction():
'''public void processingInstruction(final String target, final String data)
'''
pass
def startCDATA():
'''public void startCDATA()
'''
pass
def addAttribute():
'''public void addAttribute(final String uri, final String localName, final String rawName, final String type, final String value, final boolean XSLAttribute)
'''
pass
def reset():
'''public boolean reset()
'''
pass
