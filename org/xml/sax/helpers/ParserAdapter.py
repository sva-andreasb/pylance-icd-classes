def ():
    '''returns ParserAdapter\n\n
    ()\n
    (final Parser parser)\n
    '''
def setFeature():
    '''returns None\n\n
    setFeature(final String str, final boolean uris)\n
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
    parse(final String s)\n
    parse(final InputSource inputSource)\n
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
    startElement(final String s, final AttributeList attributeList)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String s)\n
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
def getLength():
    '''returns int\n\n
    getLength()\n
    '''
def getURI():
    '''returns String\n\n
    getURI(final int n)\n
    '''
def getLocalName():
    '''returns String\n\n
    getLocalName(final int n)\n
    '''
def getQName():
    '''returns String\n\n
    getQName(final int n)\n
    '''
def getType():
    '''returns String\n\n
    getType(final int n)\n
    getType(final String s, final String s2)\n
    getType(final String s)\n
    '''
def getValue():
    '''returns String\n\n
    getValue(final int n)\n
    getValue(final String s, final String s2)\n
    getValue(final String s)\n
    '''
def getIndex():
    '''returns int\n\n
    getIndex(final String s, final String s2)\n
    getIndex(final String anObject)\n
    '''
