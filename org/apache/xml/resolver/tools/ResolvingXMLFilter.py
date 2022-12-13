def ResolvingXMLFilter():
    '''public ResolvingXMLFilter()
    public ResolvingXMLFilter(final XMLReader parent)
    public ResolvingXMLFilter(final CatalogManager manager)
    public ResolvingXMLFilter(final XMLReader parent, final CatalogManager manager)
    '''
def getCatalog():
    '''public Catalog getCatalog()
    '''
def parse():
    '''public void parse(final InputSource input)
    public void parse(final String systemId)
    '''
def resolveEntity():
    '''public InputSource resolveEntity(final String publicId, final String systemId)
    '''
def notationDecl():
    '''public void notationDecl(final String name, final String publicId, final String systemId)
    '''
def unparsedEntityDecl():
    '''public void unparsedEntityDecl(final String name, final String publicId, final String systemId, final String notationName)
    '''
def startElement():
    '''public void startElement(final String uri, final String localName, final String qName, final Attributes atts)
    '''
def processingInstruction():
    '''public void processingInstruction(final String target, final String pidata)
    '''
