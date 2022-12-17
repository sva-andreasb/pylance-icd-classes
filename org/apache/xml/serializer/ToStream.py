def ():
    '''returns BoolStack\n\n
    ()\n
    ()\n
    (final int size)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final Node node)\n
    '''
def getOutputStream():
    '''returns OutputStream\n\n
    getOutputStream()\n
    '''
def elementDecl():
    '''returns None\n\n
    elementDecl(final String name, final String model)\n
    '''
def internalEntityDecl():
    '''returns None\n\n
    internalEntityDecl(final String name, final String value)\n
    '''
def setOutputFormat():
    '''returns None\n\n
    setOutputFormat(final Properties format)\n
    '''
def getOutputFormat():
    '''returns Properties\n\n
    getOutputFormat()\n
    '''
def setWriter():
    '''returns None\n\n
    setWriter(final Writer writer)\n
    '''
def setLineSepUse():
    '''returns boolean\n\n
    setLineSepUse(final boolean use_sytem_line_break)\n
    '''
def setOutputStream():
    '''returns None\n\n
    setOutputStream(final OutputStream output)\n
    '''
def setEscaping():
    '''returns boolean\n\n
    setEscaping(final boolean escape)\n
    '''
def attributeDecl():
    '''returns None\n\n
    attributeDecl(final String eName, final String aName, final String type, final String valueDefault, final String value)\n
    '''
def getWriter():
    '''returns Writer\n\n
    getWriter()\n
    '''
def externalEntityDecl():
    '''returns None\n\n
    externalEntityDecl(final String name, final String publicId, final String systemId)\n
    '''
def endNonEscaping():
    '''returns None\n\n
    endNonEscaping()\n
    '''
def startNonEscaping():
    '''returns None\n\n
    startNonEscaping()\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] chars, final int start, final int length)\n
    characters(final String s)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String namespaceURI, final String localName, final String name, final Attributes atts)\n
    startElement(final String elementNamespaceURI, final String elementLocalName, final String elementName)\n
    startElement(final String elementName)\n
    '''
def processAttributes():
    '''returns None\n\n
    processAttributes(final Writer writer, final int nAttrs)\n
    '''
def writeAttrString():
    '''returns None\n\n
    writeAttrString(final Writer writer, final String string, final String encoding)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String namespaceURI, final String localName, final String name)\n
    endElement(final String name)\n
    '''
def startPrefixMapping():
    '''returns boolean\n\n
    startPrefixMapping(final String prefix, final String uri)\n
    startPrefixMapping(final String prefix, final String uri, final boolean shouldFlush)\n
    '''
def comment():
    '''returns None\n\n
    comment(final char[] ch, int start, final int length)\n
    '''
def endCDATA():
    '''returns None\n\n
    endCDATA()\n
    '''
def endDTD():
    '''returns None\n\n
    endDTD()\n
    '''
def endPrefixMapping():
    '''returns None\n\n
    endPrefixMapping(final String prefix)\n
    '''
def ignorableWhitespace():
    '''returns None\n\n
    ignorableWhitespace(final char[] ch, final int start, final int length)\n
    '''
def skippedEntity():
    '''returns None\n\n
    skippedEntity(final String name)\n
    '''
def startCDATA():
    '''returns None\n\n
    startCDATA()\n
    '''
def startEntity():
    '''returns None\n\n
    startEntity(final String name)\n
    '''
def startDTD():
    '''returns None\n\n
    startDTD(final String name, final String publicId, final String systemId)\n
    '''
def getIndentAmount():
    '''returns int\n\n
    getIndentAmount()\n
    '''
def setIndentAmount():
    '''returns None\n\n
    setIndentAmount(final int m_indentAmount)\n
    '''
def setCdataSectionElements():
    '''returns None\n\n
    setCdataSectionElements(final Vector URI_and_localNames)\n
    '''
def flushPending():
    '''returns None\n\n
    flushPending()\n
    '''
def setContentHandler():
    '''returns None\n\n
    setContentHandler(final ContentHandler ch)\n
    '''
def addAttributeAlways():
    '''returns boolean\n\n
    addAttributeAlways(final String uri, final String localName, String rawName, final String type, final String value, final boolean xslAttribute)\n
    '''
def setTransformer():
    '''returns None\n\n
    setTransformer(final Transformer transformer)\n
    '''
def reset():
    '''returns boolean\n\n
    reset()\n
    '''
def setEncoding():
    '''returns None\n\n
    setEncoding(final String encoding)\n
    '''
def notationDecl():
    '''returns None\n\n
    notationDecl(final String name, final String pubID, final String sysID)\n
    '''
def unparsedEntityDecl():
    '''returns None\n\n
    unparsedEntityDecl(final String name, final String pubID, final String sysID, final String notationName)\n
    '''
def setDTDEntityExpansion():
    '''returns None\n\n
    setDTDEntityExpansion(final boolean expand)\n
    '''
def setNewLine():
    '''returns None\n\n
    setNewLine(final char[] eolChars)\n
    '''
def addCdataSectionElements():
    '''returns None\n\n
    addCdataSectionElements(final String URI_and_localNames)\n
    '''
def write():
    '''returns None\n\n
    write(final char[] arg0, final int arg1, final int arg2)\n
    write(final int i)\n
    write(final String s)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
