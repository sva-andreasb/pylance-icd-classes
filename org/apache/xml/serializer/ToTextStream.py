def endDocument():
    '''returns None\n\n
    endDocument()\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String namespaceURI, final String localName, final String name, final Attributes atts)\n
    startElement(final String elementNamespaceURI, final String elementLocalName, final String elementName)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String namespaceURI, final String localName, final String name)\n
    endElement(final String elemName)\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] ch, final int start, final int length)\n
    characters(final String characters)\n
    '''
def charactersRaw():
    '''returns None\n\n
    charactersRaw(final char[] ch, final int start, final int length)\n
    '''
def cdata():
    '''returns None\n\n
    cdata(final char[] ch, final int start, final int length)\n
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
    comment(final String data)\n
    comment(final char[] ch, final int start, final int length)\n
    '''
def entityReference():
    '''returns None\n\n
    entityReference(final String name)\n
    '''
def addAttribute():
    '''returns None\n\n
    addAttribute(final String uri, final String localName, final String rawName, final String type, final String value, final boolean XSLAttribute)\n
    addAttribute(final String name, final String value)\n
    '''
def endCDATA():
    '''returns None\n\n
    endCDATA()\n
    '''
def addUniqueAttribute():
    '''returns None\n\n
    addUniqueAttribute(final String qName, final String value, final int flags)\n
    '''
def startPrefixMapping():
    '''returns None\n\n
    startPrefixMapping(final String prefix, final String uri, final boolean shouldFlush)\n
    startPrefixMapping(final String prefix, final String uri)\n
    '''
def namespaceAfterStartElement():
    '''returns None\n\n
    namespaceAfterStartElement(final String prefix, final String uri)\n
    '''
def flushPending():
    '''returns None\n\n
    flushPending()\n
    '''
