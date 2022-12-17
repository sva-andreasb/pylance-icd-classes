def asDocumentHandler():
    '''returns DocumentHandler\n\n
    asDocumentHandler()\n
    '''
def asContentHandler():
    '''returns ContentHandler\n\n
    asContentHandler()\n
    '''
def asDOMSerializer():
    '''returns DOMSerializer\n\n
    asDOMSerializer()\n
    '''
def setOutputByteStream():
    '''returns None\n\n
    setOutputByteStream(final OutputStream output)\n
    '''
def setOutputCharStream():
    '''returns None\n\n
    setOutputCharStream(final Writer writer)\n
    '''
def setOutputFormat():
    '''returns None\n\n
    setOutputFormat(final OutputFormat format)\n
    '''
def reset():
    '''returns boolean\n\n
    reset()\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final Element element)\n
    serialize(final DocumentFragment documentFragment)\n
    serialize(final Document document)\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument()\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] array, final int n, final int n2)\n
    '''
def ignorableWhitespace():
    '''returns None\n\n
    ignorableWhitespace(final char[] array, final int n, int n2)\n
    '''
def processingInstructionIO():
    '''returns None\n\n
    processingInstructionIO(final String str, final String str2)\n
    '''
def comment():
    '''returns None\n\n
    comment(final char[] value, final int offset, final int count)\n
    comment(final String str)\n
    '''
def startCDATA():
    '''returns None\n\n
    startCDATA()\n
    '''
def endCDATA():
    '''returns None\n\n
    endCDATA()\n
    '''
def startNonEscaping():
    '''returns None\n\n
    startNonEscaping()\n
    '''
def endNonEscaping():
    '''returns None\n\n
    endNonEscaping()\n
    '''
def startPreserving():
    '''returns None\n\n
    startPreserving()\n
    '''
def endPreserving():
    '''returns None\n\n
    endPreserving()\n
    '''
def endDocument():
    '''returns None\n\n
    endDocument()\n
    '''
def startEntity():
    '''returns None\n\n
    startEntity(final String s)\n
    '''
def endEntity():
    '''returns None\n\n
    endEntity(final String s)\n
    '''
def setDocumentLocator():
    '''returns None\n\n
    setDocumentLocator(final Locator locator)\n
    '''
def skippedEntity():
    '''returns None\n\n
    skippedEntity(final String s)\n
    '''
def startPrefixMapping():
    '''returns None\n\n
    startPrefixMapping(final String s, final String key)\n
    '''
def endPrefixMapping():
    '''returns None\n\n
    endPrefixMapping(final String s)\n
    '''
def endDTD():
    '''returns None\n\n
    endDTD()\n
    '''
def elementDecl():
    '''returns None\n\n
    elementDecl(final String s, final String s2)\n
    '''
def attributeDecl():
    '''returns None\n\n
    attributeDecl(final String s, final String s2, final String s3, final String s4, final String s5)\n
    '''
def internalEntityDecl():
    '''returns None\n\n
    internalEntityDecl(final String s, final String s2)\n
    '''
def externalEntityDecl():
    '''returns None\n\n
    externalEntityDecl(final String s, final String s2, final String s3)\n
    '''
def unparsedEntityDecl():
    '''returns None\n\n
    unparsedEntityDecl(final String s, final String s2, final String s3, final String s4)\n
    '''
def notationDecl():
    '''returns None\n\n
    notationDecl(final String s, final String s2, final String s3)\n
    '''
