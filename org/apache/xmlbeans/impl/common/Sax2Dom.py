EMPTYSTRING = "String  \"\""
XML_PREFIX = "String  \"xml\""
XMLNS_PREFIX = "String  \"xmlns\""
XMLNS_STRING = "String  \"xmlns:\""
XMLNS_URI = "String  \"http://www.w3.org/2000/xmlns/\""
def ():
    '''returns Sax2Dom\n\n
    ()\n
    (final Node root)\n
    '''
def getDOM():
    '''returns Node\n\n
    getDOM()\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] ch, final int start, final int length)\n
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
    startElement(final String namespace, final String localName, final String qName, final Attributes attrs)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String namespace, final String localName, final String qName)\n
    '''
def startPrefixMapping():
    '''returns None\n\n
    startPrefixMapping(final String prefix, final String uri)\n
    '''
def endPrefixMapping():
    '''returns None\n\n
    endPrefixMapping(final String prefix)\n
    '''
def ignorableWhitespace():
    '''returns None\n\n
    ignorableWhitespace(final char[] ch, final int start, final int length)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String target, final String data)\n
    '''
def setDocumentLocator():
    '''returns None\n\n
    setDocumentLocator(final Locator locator)\n
    '''
def skippedEntity():
    '''returns None\n\n
    skippedEntity(final String name)\n
    '''
def comment():
    '''returns None\n\n
    comment(final char[] ch, final int start, final int length)\n
    '''
def startCDATA():
    '''returns None\n\n
    startCDATA()\n
    '''
def endCDATA():
    '''returns None\n\n
    endCDATA()\n
    '''
def startEntity():
    '''returns None\n\n
    startEntity(final String name)\n
    '''
def endEntity():
    '''returns None\n\n
    endEntity(final String name)\n
    '''
def startDTD():
    '''returns None\n\n
    startDTD(final String name, final String publicId, final String systemId)\n
    '''
def endDTD():
    '''returns None\n\n
    endDTD()\n
    '''
