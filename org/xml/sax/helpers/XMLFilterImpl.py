def XMLFilterImpl():
    '''public XMLFilterImpl()
    public XMLFilterImpl(final XMLReader parent)
    '''
def setParent():
    '''public void setParent(final XMLReader parent)
    '''
def getParent():
    '''public XMLReader getParent()
    '''
def setFeature():
    '''public void setFeature(final String str, final boolean b)
    '''
def getFeature():
    '''public boolean getFeature(final String str)
    '''
def setProperty():
    '''public void setProperty(final String str, final Object o)
    '''
def getProperty():
    '''public Object getProperty(final String str)
    '''
def setEntityResolver():
    '''public void setEntityResolver(final EntityResolver entityResolver)
    '''
def getEntityResolver():
    '''public EntityResolver getEntityResolver()
    '''
def setDTDHandler():
    '''public void setDTDHandler(final DTDHandler dtdHandler)
    '''
def getDTDHandler():
    '''public DTDHandler getDTDHandler()
    '''
def setContentHandler():
    '''public void setContentHandler(final ContentHandler contentHandler)
    '''
def getContentHandler():
    '''public ContentHandler getContentHandler()
    '''
def setErrorHandler():
    '''public void setErrorHandler(final ErrorHandler errorHandler)
    '''
def getErrorHandler():
    '''public ErrorHandler getErrorHandler()
    '''
def parse():
    '''public void parse(final InputSource inputSource)
    public void parse(final String s)
    '''
def resolveEntity():
    '''public InputSource resolveEntity(final String s, final String s2)
    '''
def notationDecl():
    '''public void notationDecl(final String s, final String s2, final String s3)
    '''
def unparsedEntityDecl():
    '''public void unparsedEntityDecl(final String s, final String s2, final String s3, final String s4)
    '''
def setDocumentLocator():
    '''public void setDocumentLocator(final Locator locator)
    '''
def startDocument():
    '''public void startDocument()
    '''
def endDocument():
    '''public void endDocument()
    '''
def startPrefixMapping():
    '''public void startPrefixMapping(final String s, final String s2)
    '''
def endPrefixMapping():
    '''public void endPrefixMapping(final String s)
    '''
def startElement():
    '''public void startElement(final String s, final String s2, final String s3, final Attributes attributes)
    '''
def endElement():
    '''public void endElement(final String s, final String s2, final String s3)
    '''
def characters():
    '''public void characters(final char[] array, final int n, final int n2)
    '''
def ignorableWhitespace():
    '''public void ignorableWhitespace(final char[] array, final int n, final int n2)
    '''
def processingInstruction():
    '''public void processingInstruction(final String s, final String s2)
    '''
def skippedEntity():
    '''public void skippedEntity(final String s)
    '''
def warning():
    '''public void warning(final SAXParseException ex)
    '''
def error():
    '''public void error(final SAXParseException ex)
    '''
def fatalError():
    '''public void fatalError(final SAXParseException ex)
    '''
