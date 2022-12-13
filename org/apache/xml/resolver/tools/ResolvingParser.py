def ResolvingParser():
    '''    public ResolvingParser()
    public ResolvingParser(final CatalogManager manager)
    '''
def getCatalog():
    '''    public Catalog getCatalog()
    '''
def parse():
    '''    public void parse(final InputSource input)
    public void parse(final String systemId)
    '''
def setDocumentHandler():
    '''    public void setDocumentHandler(final DocumentHandler handler)
    '''
def setDTDHandler():
    '''    public void setDTDHandler(final DTDHandler handler)
    '''
def setEntityResolver():
    '''    public void setEntityResolver(final EntityResolver resolver)
    '''
def setErrorHandler():
    '''    public void setErrorHandler(final ErrorHandler handler)
    '''
def setLocale():
    '''    public void setLocale(final Locale locale)
    '''
def characters():
    '''    public void characters(final char[] ch, final int start, final int length)
    '''
def endDocument():
    '''    public void endDocument()
    '''
def endElement():
    '''    public void endElement(final String name)
    '''
def ignorableWhitespace():
    '''    public void ignorableWhitespace(final char[] ch, final int start, final int length)
    '''
def processingInstruction():
    '''    public void processingInstruction(final String target, final String pidata)
    '''
def setDocumentLocator():
    '''    public void setDocumentLocator(final Locator locator)
    '''
def startDocument():
    '''    public void startDocument()
    '''
def startElement():
    '''    public void startElement(final String name, final AttributeList atts)
    '''
def notationDecl():
    '''    public void notationDecl(final String name, final String publicId, final String systemId)
    '''
def unparsedEntityDecl():
    '''    public void unparsedEntityDecl(final String name, final String publicId, final String systemId, final String notationName)
    '''
def resolveEntity():
    '''    public InputSource resolveEntity(final String publicId, final String systemId)
    '''
