def ():
    '''returns SAXWrapper\n\n
    (final XMLHandler handler)\n
    '''
def setDocumentLocator():
    '''returns None\n\n
    setDocumentLocator(final Locator locator)\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument()\n
    '''
def endDocument():
    '''returns None\n\n
    endDocument()\n
    '''
def startPrefixMapping():
    '''returns None\n\n
    startPrefixMapping(final String prefix, final String uri)\n
    '''
def endPrefixMapping():
    '''returns None\n\n
    endPrefixMapping(final String prefix)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String uri, final String localName, final String qName, final Attributes attributes)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String uri, final String localName, final String qName)\n
    '''
def warning():
    '''returns None\n\n
    warning(final SAXParseException e)\n
    '''
def error():
    '''returns None\n\n
    error(final SAXParseException e)\n
    '''
def fatalError():
    '''returns None\n\n
    fatalError(final SAXParseException e)\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] ch, final int start, final int length)\n
    '''
def ignorableWhitespace():
    '''returns None\n\n
    ignorableWhitespace(final char[] ch, final int start, final int length)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String target, final String data)\n
    '''
def skippedEntity():
    '''returns None\n\n
    skippedEntity(final String name)\n
    '''
def resolveEntity():
    '''returns InputSource\n\n
    resolveEntity(final String publicId, final String systemId)\n
    '''
def notationDecl():
    '''returns None\n\n
    notationDecl(final String name, final String publicId, final String systemId)\n
    '''
def unparsedEntityDecl():
    '''returns None\n\n
    unparsedEntityDecl(final String name, final String publicId, final String systemId, final String notationName)\n
    '''
def startDTD():
    '''returns None\n\n
    startDTD(final String name, final String publicId, final String systemId)\n
    '''
def endDTD():
    '''returns None\n\n
    endDTD()\n
    '''
def startEntity():
    '''returns None\n\n
    startEntity(final String name)\n
    '''
def endEntity():
    '''returns None\n\n
    endEntity(final String name)\n
    '''
def startCDATA():
    '''returns None\n\n
    startCDATA()\n
    '''
def endCDATA():
    '''returns None\n\n
    endCDATA()\n
    '''
def comment():
    '''returns None\n\n
    comment(final char[] characters, final int start, final int length)\n
    '''
