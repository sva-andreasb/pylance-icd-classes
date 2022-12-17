def ():
    '''returns SAXOMBuilder\n\n
    (final OMFactory factory)\n
    ()\n
    '''
def setDocumentLocator():
    '''returns None\n\n
    setDocumentLocator(final Locator arg0)\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument()\n
    '''
def endDocument():
    '''returns None\n\n
    endDocument()\n
    '''
def startDTD():
    '''returns None\n\n
    startDTD(final String name, final String publicId, final String systemId)\n
    '''
def endDTD():
    '''returns None\n\n
    endDTD()\n
    '''
def startPrefixMapping():
    '''returns None\n\n
    startPrefixMapping(final String prefix, final String uri)\n
    '''
def endPrefixMapping():
    '''returns None\n\n
    endPrefixMapping(final String arg0)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String namespaceURI, String localName, final String qName, final Attributes atts)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String arg0, final String arg1, final String arg2)\n
    '''
def startCDATA():
    '''returns None\n\n
    startCDATA()\n
    '''
def endCDATA():
    '''returns None\n\n
    endCDATA()\n
    '''
def characterData():
    '''returns None\n\n
    characterData(final char[] ch, final int start, final int length, final int nodeType)\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] ch, final int start, final int length)\n
    '''
def ignorableWhitespace():
    '''returns None\n\n
    ignorableWhitespace(final char[] ch, final int start, final int length)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String target, final String data)\n
    '''
def comment():
    '''returns None\n\n
    comment(final char[] ch, final int start, final int length)\n
    '''
def skippedEntity():
    '''returns None\n\n
    skippedEntity(final String arg0)\n
    '''
def startEntity():
    '''returns None\n\n
    startEntity(final String name)\n
    '''
def endEntity():
    '''returns None\n\n
    endEntity(final String name)\n
    '''
def getDocument():
    '''returns OMDocument\n\n
    getDocument()\n
    '''
def getRootElement():
    '''returns OMElement\n\n
    getRootElement()\n
    '''
