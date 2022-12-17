def ():
    '''returns SAX2EventRecorder\n\n
    ()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def getLength():
    '''returns int\n\n
    getLength()\n
    getLength()\n
    '''
def setDocumentLocator():
    '''returns int\n\n
    setDocumentLocator(final Locator p1)\n
    '''
def startDocument():
    '''returns int\n\n
    startDocument()\n
    '''
def endDocument():
    '''returns int\n\n
    endDocument()\n
    '''
def startPrefixMapping():
    '''returns int\n\n
    startPrefixMapping(final String p1, final String p2)\n
    '''
def endPrefixMapping():
    '''returns int\n\n
    endPrefixMapping(final String p1)\n
    '''
def startElement():
    '''returns int\n\n
    startElement(final String p1, final String p2, final String p3, final Attributes p4)\n
    '''
def endElement():
    '''returns int\n\n
    endElement(final String p1, final String p2, final String p3)\n
    '''
def characters():
    '''returns int\n\n
    characters(final char[] p1, final int p2, final int p3)\n
    '''
def ignorableWhitespace():
    '''returns int\n\n
    ignorableWhitespace(final char[] p1, final int p2, final int p3)\n
    '''
def processingInstruction():
    '''returns int\n\n
    processingInstruction(final String p1, final String p2)\n
    '''
def skippedEntity():
    '''returns int\n\n
    skippedEntity(final String p1)\n
    '''
def startDTD():
    '''returns None\n\n
    startDTD(final String name, final String publicId, final String systemId)\n
    '''
def endDTD():
    '''returns None\n\n
    endDTD()\n
    '''
def startEntity():
    '''returns None\n\n
    startEntity(final String name)\n
    '''
def endEntity():
    '''returns None\n\n
    endEntity(final String name)\n
    '''
def startCDATA():
    '''returns None\n\n
    startCDATA()\n
    '''
def endCDATA():
    '''returns None\n\n
    endCDATA()\n
    '''
def comment():
    '''returns None\n\n
    comment(final char[] ch, final int start, final int length)\n
    '''
def newElement():
    '''returns int\n\n
    newElement(final MessageElement elem)\n
    '''
def replay():
    '''returns None\n\n
    replay(final ContentHandler handler)\n
    replay(final int start, final int stop, final ContentHandler handler)\n
    '''
def add():
    '''returns int\n\n
    add(final Object p1, final Object p2, final Object p3, final Object p4, final Object p5)\n
    '''
def get():
    '''returns Object\n\n
    get(final int pos, final int fld)\n
    '''
