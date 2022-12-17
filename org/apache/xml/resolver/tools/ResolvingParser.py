def ():
    '''returns ResolvingParser\n\n
    ()\n
    (final CatalogManager manager)\n
    '''
def getCatalog():
    '''returns Catalog\n\n
    getCatalog()\n
    '''
def parse():
    '''returns None\n\n
    parse(final InputSource input)\n
    parse(final String systemId)\n
    '''
def setDocumentHandler():
    '''returns None\n\n
    setDocumentHandler(final DocumentHandler handler)\n
    '''
def setDTDHandler():
    '''returns None\n\n
    setDTDHandler(final DTDHandler handler)\n
    '''
def setEntityResolver():
    '''returns None\n\n
    setEntityResolver(final EntityResolver resolver)\n
    '''
def setErrorHandler():
    '''returns None\n\n
    setErrorHandler(final ErrorHandler handler)\n
    '''
def setLocale():
    '''returns None\n\n
    setLocale(final Locale locale)\n
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
    endElement(final String name)\n
    '''
def ignorableWhitespace():
    '''returns None\n\n
    ignorableWhitespace(final char[] ch, final int start, final int length)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String target, final String pidata)\n
    '''
def setDocumentLocator():
    '''returns None\n\n
    setDocumentLocator(final Locator locator)\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument()\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String name, final AttributeList atts)\n
    '''
def notationDecl():
    '''returns None\n\n
    notationDecl(final String name, final String publicId, final String systemId)\n
    '''
def unparsedEntityDecl():
    '''returns None\n\n
    unparsedEntityDecl(final String name, final String publicId, final String systemId, final String notationName)\n
    '''
def resolveEntity():
    '''returns InputSource\n\n
    resolveEntity(final String publicId, final String systemId)\n
    '''
