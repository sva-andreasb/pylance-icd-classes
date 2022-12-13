def ToXMLSAXHandler():
    '''    public ToXMLSAXHandler()
    public ToXMLSAXHandler(final ContentHandler handler, final String encoding)
    public ToXMLSAXHandler(final ContentHandler handler, final LexicalHandler lex, final String encoding)
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
def indent():
    '''    public void indent(final int n)
    '''
def serialize():
    '''    public void serialize(final Node node)
    '''
def setEscaping():
    '''    public boolean setEscaping(final boolean escape)
    '''
def setOutputFormat():
    '''    public void setOutputFormat(final Properties format)
    '''
def setOutputStream():
    '''    public void setOutputStream(final OutputStream output)
    '''
def setWriter():
    '''    public void setWriter(final Writer writer)
    '''
def attributeDecl():
    '''    public void attributeDecl(final String arg0, final String arg1, final String arg2, final String arg3, final String arg4)
    '''
def elementDecl():
    '''    public void elementDecl(final String arg0, final String arg1)
    '''
def externalEntityDecl():
    '''    public void externalEntityDecl(final String arg0, final String arg1, final String arg2)
    '''
def internalEntityDecl():
    '''    public void internalEntityDecl(final String arg0, final String arg1)
    '''
def endDocument():
    '''    public void endDocument()
    '''
def closeCDATA():
    '''    public void closeCDATA()
    '''
def endElement():
    '''    public void endElement(String namespaceURI, String localName, final String qName)
    public void endElement(final String elemName)
    '''
def endPrefixMapping():
    '''    public void endPrefixMapping(final String prefix)
    '''
def ignorableWhitespace():
    '''    public void ignorableWhitespace(final char[] arg0, final int arg1, final int arg2)
    '''
def setDocumentLocator():
    '''    public void setDocumentLocator(final Locator arg0)
    '''
def skippedEntity():
    '''    public void skippedEntity(final String arg0)
    '''
def startPrefixMapping():
    '''    public void startPrefixMapping(final String prefix, final String uri)
    public boolean startPrefixMapping(final String prefix, final String uri, final boolean shouldFlush)
    '''
def comment():
    '''    public void comment(final char[] arg0, final int arg1, final int arg2)
    '''
def endCDATA():
    '''    public void endCDATA()
    '''
def endDTD():
    '''    public void endDTD()
    '''
def startEntity():
    '''    public void startEntity(final String arg0)
    '''
def characters():
    '''    public void characters(final String chars)
    public void characters(final char[] ch, final int off, final int len)
    '''
def startElement():
    '''    public void startElement(final String elementNamespaceURI, final String elementLocalName, final String elementName)
    public void startElement(final String elementName)
    public void startElement(final String namespaceURI, final String localName, final String name, final Attributes atts)
    '''
def namespaceAfterStartElement():
    '''    public void namespaceAfterStartElement(final String prefix, final String uri)
    '''
def processingInstruction():
    '''    public void processingInstruction(final String target, final String data)
    '''
def startCDATA():
    '''    public void startCDATA()
    '''
def addAttribute():
    '''    public void addAttribute(final String uri, final String localName, final String rawName, final String type, final String value, final boolean XSLAttribute)
    '''
def reset():
    '''    public boolean reset()
    '''
