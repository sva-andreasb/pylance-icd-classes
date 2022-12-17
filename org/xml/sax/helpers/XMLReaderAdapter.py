def ():
    '''returns XMLReaderAdapter\n\n
    ()\n
    (final XMLReader xmlReader)\n
    '''
def setLocale():
    '''returns None\n\n
    setLocale(final Locale locale)\n
    '''
def setEntityResolver():
    '''returns None\n\n
    setEntityResolver(final EntityResolver entityResolver)\n
    '''
def setDTDHandler():
    '''returns None\n\n
    setDTDHandler(final DTDHandler dtdHandler)\n
    '''
def setDocumentHandler():
    '''returns None\n\n
    setDocumentHandler(final DocumentHandler documentHandler)\n
    '''
def setErrorHandler():
    '''returns None\n\n
    setErrorHandler(final ErrorHandler errorHandler)\n
    '''
def parse():
    '''returns None\n\n
    parse(final String s)\n
    parse(final InputSource inputSource)\n
    '''
def setDocumentLocator():
    '''returns None\n\n
    setDocumentLocator(final Locator documentLocator)\n
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
def getLength():
    '''returns int\n\n
    getLength()\n
    '''
def getName():
    '''returns String\n\n
    getName(final int n)\n
    '''
def getType():
    '''returns String\n\n
    getType(final int n)\n
    getType(final String s)\n
    '''
def getValue():
    '''returns String\n\n
    getValue(final int n)\n
    getValue(final String s)\n
    '''
