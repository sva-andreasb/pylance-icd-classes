def setParserFactory():
'''public void setParserFactory(final SAXParserFactory parserFactory)
'''
pass
def setParserClass():
'''public void setParserClass(final String parserClass)
'''
pass
def getParserFactory():
'''public SAXParserFactory getParserFactory()
'''
pass
def getParserClass():
'''public String getParserClass()
'''
pass
def setClassLoader():
'''public void setClassLoader(final ClassLoader loader)
'''
pass
def SAXCatalogReader():
'''public SAXCatalogReader()
public SAXCatalogReader(final SAXParserFactory parserFactory)
public SAXCatalogReader(final String parserClass)
'''
pass
def setCatalogParser():
'''public void setCatalogParser(String namespaceURI, final String rootElement, final String parserClass)
'''
pass
def getCatalogParser():
'''public String getCatalogParser(String namespaceURI, final String rootElement)
'''
pass
def readCatalog():
'''public void readCatalog(final Catalog catalog, final String fileUrl)
public void readCatalog(final Catalog catalog, final InputStream is)
'''
pass
def setDocumentLocator():
'''public void setDocumentLocator(final Locator locator)
'''
pass
def startDocument():
'''public void startDocument()
'''
pass
def endDocument():
'''public void endDocument()
'''
pass
def startElement():
'''public void startElement(final String name, final AttributeList atts)
public void startElement(final String namespaceURI, final String localName, final String qName, final Attributes atts)
'''
pass
def endElement():
'''public void endElement(final String name)
public void endElement(final String namespaceURI, final String localName, final String qName)
'''
pass
def characters():
'''public void characters(final char[] ch, final int start, final int length)
'''
pass
def ignorableWhitespace():
'''public void ignorableWhitespace(final char[] ch, final int start, final int length)
'''
pass
def processingInstruction():
'''public void processingInstruction(final String target, final String data)
'''
pass
def startPrefixMapping():
'''public void startPrefixMapping(final String prefix, final String uri)
'''
pass
def endPrefixMapping():
'''public void endPrefixMapping(final String prefix)
'''
pass
def skippedEntity():
'''public void skippedEntity(final String name)
'''
pass
