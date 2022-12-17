def ():
    '''returns ResolvingXMLFilter\n\n
    ()\n
    (final XMLReader parent)\n
    (final CatalogManager manager)\n
    (final XMLReader parent, final CatalogManager manager)\n
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
def startElement():
    '''returns None\n\n
    startElement(final String uri, final String localName, final String qName, final Attributes atts)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String target, final String pidata)\n
    '''
