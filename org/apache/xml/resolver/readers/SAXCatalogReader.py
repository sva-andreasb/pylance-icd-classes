def setParserFactory():
    '''returns None\n\n
    setParserFactory(final SAXParserFactory parserFactory)\n
    '''
def setParserClass():
    '''returns None\n\n
    setParserClass(final String parserClass)\n
    '''
def getParserFactory():
    '''returns SAXParserFactory\n\n
    getParserFactory()\n
    '''
def getParserClass():
    '''returns String\n\n
    getParserClass()\n
    '''
def setClassLoader():
    '''returns None\n\n
    setClassLoader(final ClassLoader loader)\n
    '''
def ():
    '''returns SAXCatalogReader\n\n
    ()\n
    (final SAXParserFactory parserFactory)\n
    (final String parserClass)\n
    '''
def setCatalogParser():
    '''returns None\n\n
    setCatalogParser(String namespaceURI, final String rootElement, final String parserClass)\n
    '''
def getCatalogParser():
    '''returns String\n\n
    getCatalogParser(String namespaceURI, final String rootElement)\n
    '''
def readCatalog():
    '''returns None\n\n
    readCatalog(final Catalog catalog, final String fileUrl)\n
    readCatalog(final Catalog catalog, final InputStream is)\n
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
def startElement():
    '''returns None\n\n
    startElement(final String name, final AttributeList atts)\n
    startElement(final String namespaceURI, final String localName, final String qName, final Attributes atts)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String name)\n
    endElement(final String namespaceURI, final String localName, final String qName)\n
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
def startPrefixMapping():
    '''returns None\n\n
    startPrefixMapping(final String prefix, final String uri)\n
    '''
def endPrefixMapping():
    '''returns None\n\n
    endPrefixMapping(final String prefix)\n
    '''
def skippedEntity():
    '''returns None\n\n
    skippedEntity(final String name)\n
    '''
