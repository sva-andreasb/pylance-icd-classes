def getOutputFormat():
    '''returns Properties\n\n
    getOutputFormat()\n
    '''
def getOutputStream():
    '''returns OutputStream\n\n
    getOutputStream()\n
    '''
def getWriter():
    '''returns Writer\n\n
    getWriter()\n
    '''
def indent():
    '''returns None\n\n
    indent(final int n)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final Node node)\n
    '''
def setEscaping():
    '''returns boolean\n\n
    setEscaping(final boolean escape)\n
    '''
def setIndent():
    '''returns None\n\n
    setIndent(final boolean indent)\n
    '''
def setOutputFormat():
    '''returns None\n\n
    setOutputFormat(final Properties format)\n
    '''
def setOutputStream():
    '''returns None\n\n
    setOutputStream(final OutputStream output)\n
    '''
def setWriter():
    '''returns None\n\n
    setWriter(final Writer writer)\n
    '''
def attributeDecl():
    '''returns None\n\n
    attributeDecl(final String eName, final String aName, final String type, final String valueDefault, final String value)\n
    '''
def elementDecl():
    '''returns None\n\n
    elementDecl(final String name, final String model)\n
    '''
def externalEntityDecl():
    '''returns None\n\n
    externalEntityDecl(final String arg0, final String arg1, final String arg2)\n
    '''
def internalEntityDecl():
    '''returns None\n\n
    internalEntityDecl(final String name, final String value)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String uri, final String localName, final String qName)\n
    endElement(final String elementName)\n
    '''
def endPrefixMapping():
    '''returns None\n\n
    endPrefixMapping(final String prefix)\n
    '''
def ignorableWhitespace():
    '''returns None\n\n
    ignorableWhitespace(final char[] ch, final int start, final int length)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String target, final String data)\n
    '''
def setDocumentLocator():
    '''returns None\n\n
    setDocumentLocator(final Locator arg0)\n
    '''
def skippedEntity():
    '''returns None\n\n
    skippedEntity(final String arg0)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String namespaceURI, final String localName, final String qName, final Attributes atts)\n
    startElement(final String elementNamespaceURI, final String elementLocalName, final String elementName)\n
    startElement(final String elementName)\n
    '''
def comment():
    '''returns None\n\n
    comment(final char[] ch, final int start, final int length)\n
    '''
def endCDATA():
    '''returns None\n\n
    endCDATA()\n
    '''
def endDTD():
    '''returns None\n\n
    endDTD()\n
    '''
def startCDATA():
    '''returns None\n\n
    startCDATA()\n
    '''
def startEntity():
    '''returns None\n\n
    startEntity(final String arg0)\n
    '''
def endDocument():
    '''returns None\n\n
    endDocument()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def characters():
    '''returns None\n\n
    characters(final String chars)\n
    characters(final char[] ch, final int off, final int len)\n
    '''
def ():
    '''returns ToHTMLSAXHandler\n\n
    (final ContentHandler handler, final String encoding)\n
    (final ContentHandler handler, final LexicalHandler lex, final String encoding)\n
    '''
def flushPending():
    '''returns None\n\n
    flushPending()\n
    '''
def startPrefixMapping():
    '''returns None\n\n
    startPrefixMapping(final String prefix, final String uri, final boolean shouldFlush)\n
    startPrefixMapping(final String prefix, final String uri)\n
    '''
def namespaceAfterStartElement():
    '''returns None\n\n
    namespaceAfterStartElement(final String prefix, final String uri)\n
    '''
def reset():
    '''returns boolean\n\n
    reset()\n
    '''
