def ():
    '''returns SAXParserHandler\n\n
    ()\n
    '''
def setEntityResolver():
    '''returns None\n\n
    setEntityResolver(final EntityResolver er)\n
    '''
def setContentHandler():
    '''returns None\n\n
    setContentHandler(final ContentHandler ch)\n
    '''
def resolveEntity():
    '''returns InputSource\n\n
    resolveEntity(final String publicId, final String systemId)\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] ch, final int start, final int length)\n
    '''
def endDocument():
    '''returns None\n\n
    endDocument()\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String namespaceURI, final String localName, final String qName)\n
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
    setDocumentLocator(final Locator locator)\n
    '''
def skippedEntity():
    '''returns None\n\n
    skippedEntity(final String name)\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument()\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String namespaceURI, final String localName, final String qName, final Attributes atts)\n
    '''
def startPrefixMapping():
    '''returns None\n\n
    startPrefixMapping(final String prefix, final String uri)\n
    '''
