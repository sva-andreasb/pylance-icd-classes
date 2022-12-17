def ():
    '''returns PDQXmlHandler\n\n
    ()\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String s, final String s2, final String s3)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String s, final String s2, final String s3, final Attributes attributes)\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] str, final int offset, final int len)\n
    '''
def endDocument():
    '''returns None\n\n
    endDocument()\n
    '''
def endPrefixMapping():
    '''returns None\n\n
    endPrefixMapping(final String prefix)\n
    '''
def error():
    '''returns None\n\n
    error(final SAXParseException thrown)\n
    '''
def fatalError():
    '''returns None\n\n
    fatalError(final SAXParseException thrown)\n
    '''
def ignorableWhitespace():
    '''returns None\n\n
    ignorableWhitespace(final char[] ch, final int start, final int length)\n
    '''
def notationDecl():
    '''returns None\n\n
    notationDecl(final String name, final String publicId, final String systemId)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String target, final String data)\n
    '''
def resolveEntity():
    '''returns InputSource\n\n
    resolveEntity(final String publicId, final String systemId)\n
    '''
def setDocumentLocator():
    '''returns None\n\n
    setDocumentLocator(final Locator locator_)\n
    '''
def skippedEntity():
    '''returns None\n\n
    skippedEntity(final String name)\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument()\n
    '''
def startPrefixMapping():
    '''returns None\n\n
    startPrefixMapping(final String prefix, final String uri)\n
    '''
def unparsedEntityDecl():
    '''returns None\n\n
    unparsedEntityDecl(final String name, final String publicId, final String systemId, final String notationName)\n
    '''
def warning():
    '''returns None\n\n
    warning(final SAXParseException e)\n
    '''
def getPdqXml():
    '''returns PDQXml\n\n
    getPdqXml()\n
    '''
def setPdqXml():
    '''returns None\n\n
    setPdqXml(final PDQXml pdqXml_)\n
    '''
