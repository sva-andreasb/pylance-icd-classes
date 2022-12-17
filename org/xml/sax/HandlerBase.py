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
def startElement():
    '''returns None\n\n
    startElement(final String s, final AttributeList list)\n
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
