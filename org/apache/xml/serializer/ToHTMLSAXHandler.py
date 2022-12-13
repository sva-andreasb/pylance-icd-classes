def getOutputFormat():
    '''public Properties getOutputFormat()
    '''
def getOutputStream():
    '''public OutputStream getOutputStream()
    '''
def getWriter():
    '''public Writer getWriter()
    '''
def indent():
    '''public void indent(final int n)
    '''
def serialize():
    '''public void serialize(final Node node)
    '''
def setEscaping():
    '''public boolean setEscaping(final boolean escape)
    '''
def setIndent():
    '''public void setIndent(final boolean indent)
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
def attributeDecl():
    '''public void attributeDecl(final String eName, final String aName, final String type, final String valueDefault, final String value)
    '''
def elementDecl():
    '''public void elementDecl(final String name, final String model)
    '''
def externalEntityDecl():
    '''public void externalEntityDecl(final String arg0, final String arg1, final String arg2)
    '''
def internalEntityDecl():
    '''public void internalEntityDecl(final String name, final String value)
    '''
def endElement():
    '''public void endElement(final String uri, final String localName, final String qName)
    public void endElement(final String elementName)
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
    '''public void setDocumentLocator(final Locator arg0)
    '''
def skippedEntity():
    '''public void skippedEntity(final String arg0)
    '''
def startElement():
    '''public void startElement(final String namespaceURI, final String localName, final String qName, final Attributes atts)
    public void startElement(final String elementNamespaceURI, final String elementLocalName, final String elementName)
    public void startElement(final String elementName)
    '''
def comment():
    '''public void comment(final char[] ch, final int start, final int length)
    '''
def endCDATA():
    '''public void endCDATA()
    '''
def endDTD():
    '''public void endDTD()
    '''
def startCDATA():
    '''public void startCDATA()
    '''
def startEntity():
    '''public void startEntity(final String arg0)
    '''
def endDocument():
    '''public void endDocument()
    '''
def close():
    '''public void close()
    '''
def characters():
    '''public void characters(final String chars)
    public void characters(final char[] ch, final int off, final int len)
    '''
def ToHTMLSAXHandler():
    '''public ToHTMLSAXHandler(final ContentHandler handler, final String encoding)
    public ToHTMLSAXHandler(final ContentHandler handler, final LexicalHandler lex, final String encoding)
    '''
def flushPending():
    '''public void flushPending()
    '''
def startPrefixMapping():
    '''public boolean startPrefixMapping(final String prefix, final String uri, final boolean shouldFlush)
    public void startPrefixMapping(final String prefix, final String uri)
    '''
def namespaceAfterStartElement():
    '''public void namespaceAfterStartElement(final String prefix, final String uri)
    '''
def reset():
    '''public boolean reset()
    '''
