def ():
    '''returns XMLFilterImpl\n\n
    ()\n
    (final XMLReader parent)\n
    '''
def setParent():
    '''returns None\n\n
    setParent(final XMLReader parent)\n
    '''
def getParent():
    '''returns XMLReader\n\n
    getParent()\n
    '''
def setFeature():
    '''returns None\n\n
    setFeature(final String str, final boolean b)\n
    '''
def getFeature():
    '''returns boolean\n\n
    getFeature(final String str)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String str, final Object o)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String str)\n
    '''
def setEntityResolver():
    '''returns None\n\n
    setEntityResolver(final EntityResolver entityResolver)\n
    '''
def getEntityResolver():
    '''returns EntityResolver\n\n
    getEntityResolver()\n
    '''
def setDTDHandler():
    '''returns None\n\n
    setDTDHandler(final DTDHandler dtdHandler)\n
    '''
def getDTDHandler():
    '''returns DTDHandler\n\n
    getDTDHandler()\n
    '''
def setContentHandler():
    '''returns None\n\n
    setContentHandler(final ContentHandler contentHandler)\n
    '''
def getContentHandler():
    '''returns ContentHandler\n\n
    getContentHandler()\n
    '''
def setErrorHandler():
    '''returns None\n\n
    setErrorHandler(final ErrorHandler errorHandler)\n
    '''
def getErrorHandler():
    '''returns ErrorHandler\n\n
    getErrorHandler()\n
    '''
def parse():
    '''returns None\n\n
    parse(final InputSource inputSource)\n
    parse(final String s)\n
    '''
def resolveEntity():
    '''returns InputSource\n\n
    resolveEntity(final String s, final String s2)\n
    '''
def notationDecl():
    '''returns None\n\n
    notationDecl(final String s, final String s2, final String s3)\n
    '''
def unparsedEntityDecl():
    '''returns None\n\n
    unparsedEntityDecl(final String s, final String s2, final String s3, final String s4)\n
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
    startPrefixMapping(final String s, final String s2)\n
    '''
def endPrefixMapping():
    '''returns None\n\n
    endPrefixMapping(final String s)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String s, final String s2, final String s3, final Attributes attributes)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String s, final String s2, final String s3)\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] array, final int n, final int n2)\n
    '''
def ignorableWhitespace():
    '''returns None\n\n
    ignorableWhitespace(final char[] array, final int n, final int n2)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String s, final String s2)\n
    '''
def skippedEntity():
    '''returns None\n\n
    skippedEntity(final String s)\n
    '''
def warning():
    '''returns None\n\n
    warning(final SAXParseException ex)\n
    '''
def error():
    '''returns None\n\n
    error(final SAXParseException ex)\n
    '''
def fatalError():
    '''returns None\n\n
    fatalError(final SAXParseException ex)\n
    '''
