def setParserFactory():
    '''    public void setParserFactory(final SAXParserFactory parserFactory)
    '''
def setParserClass():
    '''    public void setParserClass(final String parserClass)
    '''
def getParserFactory():
    '''    public SAXParserFactory getParserFactory()
    '''
def getParserClass():
    '''    public String getParserClass()
    '''
def setClassLoader():
    '''    public void setClassLoader(final ClassLoader loader)
    '''
def SAXCatalogReader():
    '''    public SAXCatalogReader()
    public SAXCatalogReader(final SAXParserFactory parserFactory)
    public SAXCatalogReader(final String parserClass)
    '''
def setCatalogParser():
    '''    public void setCatalogParser(String namespaceURI, final String rootElement, final String parserClass)
    '''
def getCatalogParser():
    '''    public String getCatalogParser(String namespaceURI, final String rootElement)
    '''
def readCatalog():
    '''    public void readCatalog(final Catalog catalog, final String fileUrl)
    public void readCatalog(final Catalog catalog, final InputStream is)
    '''
def setDocumentLocator():
    '''    public void setDocumentLocator(final Locator locator)
    '''
def startDocument():
    '''    public void startDocument()
    '''
def endDocument():
    '''    public void endDocument()
    '''
def startElement():
    '''    public void startElement(final String name, final AttributeList atts)
    public void startElement(final String namespaceURI, final String localName, final String qName, final Attributes atts)
    '''
def endElement():
    '''    public void endElement(final String name)
    public void endElement(final String namespaceURI, final String localName, final String qName)
    '''
def characters():
    '''    public void characters(final char[] ch, final int start, final int length)
    '''
def ignorableWhitespace():
    '''    public void ignorableWhitespace(final char[] ch, final int start, final int length)
    '''
def processingInstruction():
    '''    public void processingInstruction(final String target, final String data)
    '''
def startPrefixMapping():
    '''    public void startPrefixMapping(final String prefix, final String uri)
    '''
def endPrefixMapping():
    '''    public void endPrefixMapping(final String prefix)
    '''
def skippedEntity():
    '''    public void skippedEntity(final String name)
    '''
